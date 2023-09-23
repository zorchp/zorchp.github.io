---
categories: [C_C++]
tags: C Network Debug
---

# 问题

今天看了一下网络编程, 发现其中有一个接口函数很有意思, 就是从二进制转换到点分十进制表示的IP地址 的函数`inet_ntoa()`, 直接使用倒是没什么异样, 但是下面一个例子却出现了一个很有趣的现象:

```c
#include <netinet/in.h>
#include <stdio.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/_endian.h>

int main(int argc, char *argv[]) {
    struct sockaddr_in addr1, addr2;
    char *str_ptr;
    char str_arr[20];

    addr1.sin_addr.s_addr = htonl(0x1020304);
    addr2.sin_addr.s_addr = htonl(0x1010101);

    str_ptr = inet_ntoa(addr1.sin_addr);
    strcpy(str_arr, str_ptr);
    printf("Dotted-Decimal notation1: %s \n", str_ptr);

    inet_ntoa(addr2.sin_addr);
    printf("Dotted-Decimal notation2: %s \n", str_ptr);
    printf("Dotted-Decimal notation3: %s \n", str_arr);

    /*
        Dotted-Decimal notation1: 1.2.3.4
        Dotted-Decimal notation2: 1.1.1.1
        Dotted-Decimal notation3: 1.2.3.4
    */

    return 0;
}
```

这个例子是引用`TCP/IP网络编程`这本书上的, 可以看出第二次调用`inet_ntoa()`时候并没有将返回值赋值给变量`str_ptr`, 但是输出这个变量的时候还是发生了改变, 这是为什么呢?

>   书中给出的解释是:
>
>   该两数将通过参数传入的整数型地址转换为字符串格式并返回。但调用时需小心，返回值
>   类型为`char`指针。返回宇符串地址意味着字符串已保存到内存空间，但该函数未向程序员要求分
>   配内存，而是在内部申请了内存并保存了宇符串。也就是说，调用完该函数后，应立即将字符串
>   信息复制到其他内存空间。因为，若再次调用`inet_ntoa`函数．则有可能覆盖之前保存的字符串信
>   息。总之，再次调用`inet_ntoa`函数前返回的宇符串地址值是有效的。若需要长期保存，则应将字
>   符串复制到其他内存空间。

也就是说, 其内部会首先分配一段空间, 用来保存转换后的字符串, 所以第二次调用的时候虽然没赋值给`str_ptr`, 但是该变量仍能获取到这个值(通过指针).

通过查看`man inet_ntoa`发现:

> The string returned by inet_ntoa() resides in a static memory area.
>
> > inet_ntoa()返回的字符串驻留在静态内存区域。

这就是说其内部分配的是一份静态变量, 所以才导致了上述问题出现.

# 例子

下面来看一个我自己写的例子:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* f1(int a) {
    static char pp[20];
    char *c1 = "123", *c2 = "456";
    if (a) {
        strcpy(pp, c1);
    } else {
        strcpy(pp, c2);
    }
    return pp;
}
int main(int argc, char* argv[]) {
    char* p;
    p = f1(1);
    printf("%s", p);//123
    f1(0);
    printf("%s", p);//456
    return 0;
}
```

乍一看大家可能以为结果会是`123123`, 因为第二次调用并没有改变`p`的值, 但是由于在函数`f1()`的`char pp[20]`变量前面加上了`static`, 使`pp[20]`成为静态变量, 这就保存在全局变量区了, 在`f1`函数结束之后变量也不会销毁, 所以才能由指针`p`去获取一个新得到的值, 从而可以不赋值就能改值了.

