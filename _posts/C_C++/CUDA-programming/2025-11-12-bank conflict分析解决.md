---
categories: [C_C++]
tags: C++ CUDA
---



## 写在前面



## cuda 硬件: 存储视角

> https://zhuanlan.zhihu.com/p/4746910252  写的真好

warp是SM的基本执行单元，一个block内相邻的32个线程划分为一个warp，一个warp内的32个线程按照[SIMT](https://zhida.zhihu.com/search?content_id=249971642&content_type=Article&match_order=1&q=SIMT&zhida_source=entity)的模式来执行指令。

[Cuda shared memory](https://zhida.zhihu.com/search?content_id=249971642&content_type=Article&match_order=1&q=Cuda+shared+memory&zhida_source=entity)按照4字节一个bank，总共32个bank（128字节）来组织，其store和load操作在一定情况下存在[bank conflict](https://zhida.zhihu.com/search?content_id=249971642&content_type=Article&match_order=1&q=bank+conflict&zhida_source=entity)的情况：

- 不同的线程访问同一bank的不同address时就会出现bank conflict。
- bank conflict只发生在同一个warp的不同线程间。
- 如果多个线程访问shared memory的相同bank的相同address，实际效果是broadcast，非bank conflict。
- bank conflict只发生在shared memory的读写操作上，global memory的读写操作不会有bank conflict产生。







```mermaid

```

