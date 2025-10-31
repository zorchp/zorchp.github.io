---
categories: [C_C++]
tags: C++ CUDA
---

## 写在前面

> https://leetgpu.com/challenges/reduction

可以说是 CUDA 入门的第一个算子, 对于理解并行编程比较有帮助

## reduction 实现与 性能测试(CPU vs GPU)

```cpp
#include "utils.h"
constexpr int BLOCK_SIZE = 256;

__global__ void block_reduce_v1(const float* input, float* partial, int N) {
    __shared__ float cache[BLOCK_SIZE]; // BLOCK_SIZE must use global variable
    int tid = threadIdx.x + blockIdx.x * blockDim.x;
    float local = 0;
    for (int i = tid; i < N; i += gridDim.x * blockDim.x) local += input[i];
    cache[threadIdx.x] = local;
    __syncthreads();

    for (int i = blockDim.x >> 1; i > 0; i >>= 1) {
        if (threadIdx.x < i) {
            cache[threadIdx.x] += cache[threadIdx.x + i];
        }
        __syncthreads();
    }
    if (threadIdx.x == 0) partial[blockIdx.x] = cache[0];
}

// input, output are device pointers
extern "C" void solve_v1(const float* input, float* output, int N) {
    int blocks = min(65535, (N + BLOCK_SIZE - 1) / BLOCK_SIZE);
    CUDA_CHECK(cudaMemset(output, 0, sizeof(float)));
    float* d_partial;
    CUDA_CHECK(cudaMalloc((void**)&d_partial, blocks * sizeof(float)));
    block_reduce_v1<<<blocks, BLOCK_SIZE>>>(input, d_partial, N);


    while (blocks > 1) {
        int next = (blocks + BLOCK_SIZE - 1) / BLOCK_SIZE;
        block_reduce_v1<<<next, BLOCK_SIZE>>>(d_partial, d_partial, blocks);
        blocks = next;
    }
    CUDA_CHECK(cudaDeviceSynchronize());

    CUDA_CHECK(
        cudaMemcpy(output, d_partial, sizeof(float), cudaMemcpyDeviceToDevice));

    CUDA_CHECK(cudaFree(d_partial));
}

__global__ void block_reduce_v2(const float* input, float* output, int N) {
    __shared__ float cache[BLOCK_SIZE]; // BLOCK_SIZE must use global variable
    int tid = threadIdx.x;
    float local = 0;
    for (int i = tid; i < N; i += blockDim.x) local += input[i];
    cache[threadIdx.x] = local;
    __syncthreads();

    for (int i = blockDim.x >> 1; i > 0; i >>= 1) {
        if (threadIdx.x < i) {
            cache[threadIdx.x] += cache[threadIdx.x + i];
        }
        __syncthreads();
    }
    output[0] = cache[0];
}

// input, output are device pointers
extern "C" void solve_v2(const float* input, float* output, int N) {
    int blocks = min(65535, (N + BLOCK_SIZE - 1) / BLOCK_SIZE);
    CUDA_CHECK(cudaMemset(output, 0, sizeof(float)));
    block_reduce_v2<<<blocks, BLOCK_SIZE>>>(input, output, N);
    CUDA_CHECK(cudaDeviceSynchronize());
}

extern "C" void solve_v3(const float* input, float* output, int N) {
    int blocks = min(65535, (N + BLOCK_SIZE - 1) / BLOCK_SIZE);
    CUDA_CHECK(cudaMemset(output, 0, sizeof(float)));
    float* d_partial;
    CUDA_CHECK(cudaMalloc((void**)&d_partial, blocks * sizeof(float)));
    block_reduce_v1<<<blocks, BLOCK_SIZE>>>(input, d_partial, N);
    block_reduce_v2<<<1, BLOCK_SIZE>>>(d_partial, output, blocks);

    CUDA_CHECK(cudaDeviceSynchronize());

    CUDA_CHECK(cudaFree(d_partial));
}

void cpu_reduction_2_N(const float* input, float* output, int N) {
    N >>= 1;
    size_t size = N * sizeof(float);
    float* partial = (float*)malloc(size);
    memcpy(partial, input, size);
    for (int i = 0; i < N; ++i) {
        partial[i] += input[i + N];
    }
    for (int i = N >> 1; i >= 1; i >>= 1) {
        for (int j = 0; j < i; ++j) {
            partial[j] += partial[i + j];
        }
    }
    output[0] = partial[0];
    free(partial);
}

void cpu_reduction(const float* input, float* output, int N) {

    float* partial = (float*)malloc(N * sizeof(float));
    memcpy(partial, input, N * sizeof(float));


    int len = N;
    while (len > 1) {
        int half = len / 2;
        for (int i = 0; i < half; ++i) {
            partial[i] += partial[i + half];
        }
        if (len & 1) {
            partial[0] += partial[len - 1];
        }
        len = half;
    }

    output[0] = partial[0];
    free(partial);
}

int main(int argc, char** argv) {
    // suppose N is even number
    if (argc != 2) {
        fprintf(stderr, "Usage: %s N", argv[0]);
        return 1;
    }
    int N = atoi(argv[1]);
    srand(42); // keep uniform
    float *h_input, *h_output, *cpu_reduction_output;
    float *d_input, *d_output;

    h_input = (float*)malloc(N * sizeof(float));
    h_output = (float*)malloc(sizeof(float));
    cpu_reduction_output = (float*)malloc(sizeof(float));
    double cpu_result_double = 0;
    float cpu_result_float = 0;
    // rand() -> [0,RAND_MAX]
    // (float)rand() / (RAND_MAX + 1.0) -> [0,1)
    // [-10, 10)
    for (int i = 0; i < N; ++i) {
        h_input[i] = -10 + (float)rand() / (RAND_MAX + 1.0) * 20;
    }

    CUDA_CHECK(cudaMalloc((void**)&d_input, N * sizeof(float)));
    CUDA_CHECK(cudaMalloc((void**)&d_output, sizeof(float)));
    CUDA_CHECK(cudaMemcpy(d_input, h_input, N * sizeof(float),
                          cudaMemcpyHostToDevice));
    CUDA_CHECK(
        cudaMemcpy(d_output, h_output, sizeof(float), cudaMemcpyHostToDevice));


    {
        TimeCostCuda tc_gpu;
        // call cuda kernel
        solve_v1(d_input, d_output, N);

        CUDA_CHECK(cudaMemcpy(h_output, d_output, sizeof(float),
                              cudaMemcpyDeviceToHost));
        printf("gpu_v1(reduction) timecost:%.5fms output:%.5f\n",
               tc_gpu.get_time_cost(), h_output[0]);
    }
    sleep(3);
    if (0) {
        TimeCostCuda tc_gpu;
        // call cuda kernel
        solve_v2(d_input, d_output, N);

        CUDA_CHECK(cudaMemcpy(h_output, d_output, sizeof(float),
                              cudaMemcpyDeviceToHost));
        printf("gpu_v2(reduction) timecost:%.5fms output:%.5f\n",
               tc_gpu.get_time_cost(), h_output[0]);
    }
    sleep(3);
    {
        TimeCostCuda tc_gpu;
        // call cuda kernel
        solve_v3(d_input, d_output, N);

        CUDA_CHECK(cudaMemcpy(h_output, d_output, sizeof(float),
                              cudaMemcpyDeviceToHost));
        printf("gpu_v3(reduction) timecost:%.5fms output:%.5f\n",
               tc_gpu.get_time_cost(), h_output[0]);
    }
    sleep(3);
    ////////////////// cpu
    {
        TimeCost tc;
        cpu_reduction(h_input, cpu_reduction_output, N);

        printf("cpu(reduction) timecost:%.5fms output:%.5f\n",
               tc.get_time_cost(), cpu_reduction_output[0]);
    }
    {
        TimeCost tc;
        for (int i = 0; i < N; ++i) {
            cpu_result_double += h_input[i];
        }
        printf("cpu(double) timecost:%.5fms output:%.5f\n", tc.get_time_cost(),
               cpu_result_double);
    }
    {
        TimeCost tc;
        for (int i = 0; i < N; ++i) {
            cpu_result_float += h_input[i];
        }
        printf("cpu(float) timecost:%.5fms output:%.5f\n", tc.get_time_cost(),
               cpu_result_float);
    }
    printf("diff between gpu and cpu(double): %.5f\n",
           fabs(h_output[0] - cpu_result_double));
    CUDA_CHECK(cudaFree(d_input));
    CUDA_CHECK(cudaFree(d_output));
    free(h_input);
    free(h_output);
    return 0;
}
```

即使不优化 GPU 也是很快

```c
$ ./get_run.sh reduction.cu  10000000
gpu_v1(reduction) timecost:1.97664ms output:-12774.02539
gpu_v2(reduction) timecost:6104.17529ms output:-12774.03711
gpu_v3(reduction) timecost:2.14282ms output:-12774.03516
cpu(reduction) timecost:100.23700ms output:-12774.02734
cpu(double) timecost:33.83300ms output:-12774.02898
cpu(float) timecost:33.78500ms output:-12774.21582
diff between gpu and cpu(double): 0.00618
```

