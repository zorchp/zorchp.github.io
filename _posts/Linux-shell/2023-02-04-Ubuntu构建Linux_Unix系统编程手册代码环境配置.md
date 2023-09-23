---
categories: [Linux-Shell]
tags: OS Linux C
---

# 方法

>   代码:
>
>   [Distribution version (man7.org)](https://man7.org/tlpi/code/download/tlpi-221220-dist.tar.gz);

## 安装所需的库

```bash
sudo apt install gdb
sudo apt install make
sudo apt install gcc-multilib
sudo apt install libcap-dev # sys/capability.h
sudo apt install libacl1-dev # sys/acl.h
```



## 修改文件

```bash
vi progconc/syscall_speed.c

# 解注释第一行`#include "tlpi_hdr.h"`
```



## 构建

```bash
make
```

