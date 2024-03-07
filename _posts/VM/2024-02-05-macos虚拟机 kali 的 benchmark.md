---
categories: [VM]
tags: MacOS VM Kali
---

# 写在前面

跑一下 arm 架构的 kali Linux 在 MacOS 上使用 qemu 虚拟化和 Apple 虚拟化的 benchmark.

>   结果证明, arm 架构没有明显优势, 但是在qemu 模拟 Intel 架构时候就拉胯很多, 还得是 Rosetta 来转译 Intel



# qemu 模拟

从utm 的虚拟机市场直接安装的, 比较丝滑

<img src="https://cdn.jsdelivr.net/gh/zorchp/blogimage/%E6%88%AA%E5%B1%8F2024-02-05%2018.26.39.jpg" alt="截屏2024-02-05 18.26.39" style="zoom:30%;" />



# Apple 虚拟化

自己安装, 注意不要选所有推荐的工具, 要不然要等很久, 就选 top10 工具即可. 

<img src="https://cdn.jsdelivr.net/gh/zorchp/blogimage/%E6%88%AA%E5%B1%8F2024-02-05%2018.42.49.jpg" alt="截屏2024-02-05 18.42.49" style="zoom:23%;" />

区别不大, 但是还是有优势的, 因为可以跑 Rosetta. 