---
tags: C++
categories: C++
---

# 前言

本文仅针对 MacOS 以及 Linux 平台(Ubuntu)的 llvm-clang++ 和 g++编译器测试, 用于跨平台程序开发. 

# 区分运行环境(操作系统)

```cpp
#ifdef __APPLE__
#include "zemaphore.h" // 自定义
#elif __linux__
#include <semaphore.h> // pthread
#endif
```



# 区分编译器

因为 clang 也采用了 gcc 的部分扩展, 所以包含了`__GNUG__`宏, 于是只能通过双重判定来做:

```cpp
#ifdef __GNUG__
#ifndef __clang__
    printf("lg of %d is %d\n", x, std::__lg(x)); // 3
#endif
#endif
```

测试: (位运算)

```cpp
#include <cstdio>
#include <algorithm>


void t1() {
    unsigned x = 11;
    // definition in countl.h
#ifdef __clang__
    printf("clz of %d is %d\n", x, std::__libcpp_clz(x));
    printf("lg2i of %d is %d\n", x, std::__log2i(x));
    printf("countl of %d is %d\n", x, std::__countl_zero(x));
    printf("ctz of %d is %d\n", x, std::__libcpp_ctz(x));
#endif
    // clz of 11 is 28
    // lg2i of 11 is 3
    // countl of 11 is 28
    // ctz of 11 is 0
#ifdef __GNUG__
#ifndef __clang__
    printf("lg of %d is %d\n", x, std::__lg(x)); // 3
#endif
#endif
}

int main(int argc, char *argv[]) {
    t1();
    return 0;
}
```

