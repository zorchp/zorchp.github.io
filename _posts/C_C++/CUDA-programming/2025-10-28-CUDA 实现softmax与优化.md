---
categories: [C_C++]
tags: C++ CUDA
---

## 写在前面

> https://leetgpu.com/challenges/softmax
>
> https://leetgpu.com/challenges/softmax-attention



## 前置知识

### safe-softmax 的原理与推导

> https://arxiv.org/pdf/1805.02867

传统的 softmax 是
$$
y=Softmax(x)\ \ \text{define as:}\\
y_i=\frac{e^{x_i}}{\sum\limits_{j=1}^Ve^{x_j}}
$$
但是直接计算的过程中存在过大或者过小的问题.  于是有了下面的 safe-softmax
$$
y_i=\frac{e^{x_i-\max_{k=1}^Vx_k}}{\sum\limits_{j=1}^Ve^{x_j-\max_{k=1}^Vx_k}}
$$
本质上就是都减去了一个最大值, 对于指数运算来说, 这是可以提出来的, 所以和上面的结果一致. 

计算方式比较 trivial, 就是 3 pass算法

1. 遍历找最大值
2. 遍历算 sum
3. 遍历计算每一个 softmax 值

但是这样是比较低效的, 因为前两个 pass 可以合并起来. 看下面的 2-pass 计算 safe-softmax 方法

### 2pass softmax

重点看第一个 pass, 这里直接计算了最大值和 sum. 

```c
m_0 = -FLT_MAX;
d_0 = 0;
for (int j = 1; j < V; ++j) {
    m_j = max(m_{j-1}, x_j);
    d_j = d_{j-1} * exp(m_{j-1} - m_j) + exp(x_j - m_j);
}
```

可以用数学归纳法证明. 

### flash-attn

> https://courses.cs.washington.edu/courses/cse599m/23sp/notes/flashattn.pdf



### exp 函数的调用

> https://stackoverflow.com/questions/7257843/difference-between-exp-expf-and-expf-in-cuda

The differences are explained in the [CUDA C Programming Guide](http://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#mathematical-functions-appendix), appendix D.

- `exp()` should be used for double precision, although should be overloaded for single
- `expf()` should be used for single precision (`float`)
- `__expf()` is the fast-math version, the performance is faster with some loss of precision (dependent on the input value, see the [guide](http://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#mathematical-functions-appendix) for more details).



## softmax实现(基础版)

```cpp

```





## 性能测试(CPU vs GPU)

```cpp

```



