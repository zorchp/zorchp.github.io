---
categories: [Linux-Shell]
tags: C++ CMake Make
---

## 写在前面



没有root 权限安装源码软件的时候, 指定路径为`~/local/bin` 就很有用了



## make

通常是在configure 脚本配置的. 

如果有 configure 脚本, 就是用`--prefix=$HOME/local`指定安装路径



## cmake

```bash
cmake .. -DCMAKE_INSTALL_PREFIX=$HOME/local
```

