---
categories: [C_C++]
tags: C++ CUDA
---

## 写在前面

> https://leetgpu.com/challenges/reduction





## reduction 实现(基础版)

```cpp
#include <cuda_runtime.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>

constexpr int BLOCK_SIZE = 256;

#define CUDA_CHECK(call)                                                  \
    do {                                                                  \
        cudaError_t err = call;                                           \
        if (err != cudaSuccess) {                                         \
            fprintf(stderr, "CUDA error %s:%d: %s\n", __FILE__, __LINE__, \
                    cudaGetErrorString(err));                             \
            exit(1);                                                      \
        }                                                                 \
    } while (0)

__global__ void block_reduce(const float* input, float* partial, int N) {
    __shared__ float cache[BLOCK_SIZE];
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
extern "C" void solve(const float* input, float* output, int N) {
    int blocks = min(65535, (N + BLOCK_SIZE - 1) / BLOCK_SIZE);
    float* d_partial;
    CUDA_CHECK(cudaMalloc((void**)&d_partial, blocks * sizeof(float)));
    block_reduce<<<blocks, BLOCK_SIZE>>>(input, d_partial, N);
    CUDA_CHECK(cudaDeviceSynchronize());
#if 0 // cpu partial reduction
    float* h_partial = (float*)malloc(blocks * sizeof(float));
    CUDA_CHECK(cudaMemcpy(h_partial.data(), d_partial, blocks * sizeof(float),
                          cudaMemcpyDeviceToHost)); // core
    for (int i = 0; i < blocks; ++i) {
        output[0] += h_partial[i]; // can not access device mem in host
    }
#else // GPU 2nd Reduction
    while (blocks > 1) {
        int next = (blocks + BLOCK_SIZE - 1) / BLOCK_SIZE;
        block_reduce<<<next, BLOCK_SIZE>>>(d_partial, d_partial, blocks);
        blocks = next;
    }
    CUDA_CHECK(
        cudaMemcpy(output, d_partial, sizeof(float), cudaMemcpyDeviceToDevice));
#endif
    CUDA_CHECK(cudaFree(d_partial));
}

void cpu_reduction(const flaot* input, float*output, int N) {
    for (int i = int(log2f(N)) + 1; i > 1; ) {

    }
}

int main(int argc, char** argv) {
    //
    if (argc != 2) {
        fprintf(stderr, "Usage: %s N", argv[0]);
        return 1;
    }
    int N = atoi(argv[1]);
    srand(42); // keep uniform
    float *h_input, *h_output;
    float *d_input, *d_output;

    h_input = (float*)malloc(N * sizeof(float));
    h_output = (float*)malloc(sizeof(float));
    double cpu_result = 0, cpu_reduction_result = 0;
    for (int i = 0; i < N; ++i) {
        h_input[i] = (float)rand() / (RAND_MAX + 1.0) * 3;
        cpu_result += h_input[i];
    }


    CUDA_CHECK(cudaMalloc((void**)&d_input, N * sizeof(float)));
    CUDA_CHECK(cudaMalloc((void**)&d_output, sizeof(float)));
    CUDA_CHECK(cudaMemcpy(d_input, h_input, N * sizeof(float),
                          cudaMemcpyHostToDevice));
    CUDA_CHECK(
        cudaMemcpy(d_output, h_output, sizeof(float), cudaMemcpyHostToDevice));
    solve(d_input, d_output, N);

    CUDA_CHECK(
        cudaMemcpy(h_output, d_output, sizeof(float), cudaMemcpyDeviceToHost));
    printf("cpu(double) output:%.5f\n", cpu_result);
    printf("cpu(reduction) output:%.5f\n", cpu_reduction_result);
    printf("gpu(reduction) output:%.5f\n", h_output[0]);
    printf("diff : %.5f\n", fabs(h_output[0] - cpu_result));
    CUDA_CHECK(cudaFree(d_input));
    CUDA_CHECK(cudaFree(d_output));
    return 0;
}
```





## 性能测试(CPU vs GPU)

```cpp
#include <cuda_runtime.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <chrono>
using namespace std::chrono;

constexpr int BLOCK_SIZE = 256;

#define CUDA_CHECK(call)                                                  \
    do {                                                                  \
        cudaError_t err = call;                                           \
        if (err != cudaSuccess) {                                         \
            fprintf(stderr, "CUDA error %s:%d: %s\n", __FILE__, __LINE__, \
                    cudaGetErrorString(err));                             \
            exit(1);                                                      \
        }                                                                 \
    } while (0)

class TimeCost {
public:
    TimeCost() : _start_time(std::chrono::high_resolution_clock::now()) {}

    void begin_time_point() {
        _start_time = std::chrono::high_resolution_clock::now();
    }

    double get_time_cost(bool is_reset = false) {
        auto end_time = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(
            end_time - _start_time);
        double cost = static_cast<double>(duration.count()) / 1e3;

        if (is_reset) {
            _start_time = std::chrono::high_resolution_clock::now();
        }

        return cost;
    }

private:
    std::chrono::high_resolution_clock::time_point _start_time;
};

class TimeCostCuda {
public:
    TimeCostCuda() {
        CUDA_CHECK(cudaEventCreate(&_start));
        CUDA_CHECK(cudaEventCreate(&_stop));
        CUDA_CHECK(cudaEventRecord(_start, 0));
    }

    ~TimeCostCuda() {
        CUDA_CHECK(cudaEventDestroy(_start));
        CUDA_CHECK(cudaEventDestroy(_stop));
    }

    double get_time_cost(bool is_reset = false) {
        CUDA_CHECK(cudaEventRecord(_stop, 0));
        CUDA_CHECK(cudaEventSynchronize(_stop));
        float elapsedTime;
        CUDA_CHECK(cudaEventElapsedTime(&elapsedTime, _start, _stop));


        if (is_reset) {
            CUDA_CHECK(cudaEventRecord(_start, 0));
        }
        return elapsedTime;
    }


private:
    cudaEvent_t _start, _stop;
};

__global__ void block_reduce(const float* input, float* partial, int N) {
    __shared__ float cache[BLOCK_SIZE];
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
extern "C" void solve(const float* input, float* output, int N) {


    int blocks = min(65535, (N + BLOCK_SIZE - 1) / BLOCK_SIZE);
    float* d_partial;
    CUDA_CHECK(cudaMalloc((void**)&d_partial, blocks * sizeof(float)));
    block_reduce<<<blocks, BLOCK_SIZE>>>(input, d_partial, N);
    CUDA_CHECK(cudaDeviceSynchronize());
#if 0 // cpu partial reduction
    float* h_partial = (float*)malloc(blocks * sizeof(float));
    CUDA_CHECK(cudaMemcpy(h_partial.data(), d_partial, blocks * sizeof(float),
                          cudaMemcpyDeviceToHost)); // core
    for (int i = 0; i < blocks; ++i) {
        output[0] += h_partial[i]; // can not access device mem in host
    }
#else // GPU 2nd Reduction
    while (blocks > 1) {
        int next = (blocks + BLOCK_SIZE - 1) / BLOCK_SIZE;
        block_reduce<<<next, BLOCK_SIZE>>>(d_partial, d_partial, blocks);
        blocks = next;
    }
    CUDA_CHECK(
        cudaMemcpy(output, d_partial, sizeof(float), cudaMemcpyDeviceToDevice));
#endif

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
    for (int i = 0; i < N; ++i) {
        h_input[i] = (float)rand() / (RAND_MAX + 1.0) * 3;
    }


    CUDA_CHECK(cudaMalloc((void**)&d_input, N * sizeof(float)));
    CUDA_CHECK(cudaMalloc((void**)&d_output, sizeof(float)));
    CUDA_CHECK(cudaMemcpy(d_input, h_input, N * sizeof(float),
                          cudaMemcpyHostToDevice));
    CUDA_CHECK(
        cudaMemcpy(d_output, h_output, sizeof(float), cudaMemcpyHostToDevice));
    TimeCostCuda tc_gpu;
    // call cuda kernel
    solve(d_input, d_output, N);

    CUDA_CHECK(
        cudaMemcpy(h_output, d_output, sizeof(float), cudaMemcpyDeviceToHost));
    printf("gpu(reduction) timecost:%.5fms output:%.5f\n",
           tc_gpu.get_time_cost(), h_output[0]);

    TimeCost tc;
    cpu_reduction(h_input, cpu_reduction_output, N);

    printf("cpu(reduction) timecost:%.5fms output:%.5f\n",
           tc.get_time_cost(true), cpu_reduction_output[0]);

    for (int i = 0; i < N; ++i) {
        cpu_result_double += h_input[i];
    }
    printf("cpu(double) timecost:%.5fms output:%.5f\n", tc.get_time_cost(true),
           cpu_result_double);
    for (int i = 0; i < N; ++i) {
        cpu_result_float += h_input[i];
    }
    printf("cpu(float) timecost:%.5fms output:%.5f\n", tc.get_time_cost(),
           cpu_result_float);
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
$ ./make.sh  reduction.cu && ./a.out 100000000

gpu(reduction) timecost:4.64150ms output:149976224.00000
cpu(reduction) timecost:650.92900ms output:149976240.00000
cpu(double) timecost:340.58000ms output:149976233.62818
cpu(float) timecost:385.87800ms output:67108864.00000
diff between gpu and cpu(double): 9.62818
```

