---
categories: [Linux-Shell]
tags: Linux Socket Network C Syscall
---

# 写在前面









# Socket简介

|     属性     | Socket: 流(TCP) | Socket: 数据报(UDP) |
| :----------: | :-------------: | :-----------------: |
|   可靠传输   |       是        |         否          |
| 消息边界保留 |       否        |         是          |
|   面向连接   |       是        |         否          |

## 字节流

流socket(SOCK_STREAM)提供了一个可靠的双向的字节流通信信道. 

-   可靠性: 可以保证发送者传输的数据完整无缺到达接收应用程序, 或者收到一个传输失败的通知
-   双向的: 数据可以在两个socket之间的任意方向上传输
-   字节流: 与管道一样不存在消息边界的概念

## 数据报

数据报socket(SOCK_DGRAM)允许数据以被称为数据报的消息的形式进行交换. 

-   消息边界得以保留
-   数据传输不可靠
-   消息的到达可能是无序的/重复的或根本无法到达





# 常用系统调用

<img src="https://s2.loli.net/2023/03/26/1QUIs3j8FA6uRDT.png" alt="流socket上用到的系统调用.drawio" style="zoom:50%;" />

-   socket(): 创建一个新的socket. 
    ```c
    #include <sys/socket.h>
    
    int socket(int domain, int type, int protocol); // return file decriptor on success, -1 on error
    ```

    

-   bind(): 将一个 socket 绑定到一个地址上. 服务器需要使用该调用将其 socket 绑定到一个众所周知的地址上使得客户端定位到该 socket 上.
    ```c
    #include <sys/socket.h>
    
    int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen); // return 0 on success, -1 on error
    ```

    

-   listen(): 允许一个流 socket 接受来自其他 socket 的接入连接. 
    ```c
    #include <sys/socket.h>
    
    int listen(int sockfd, int backlog); // return 0 on success, -1 on error
    ```

    >   由于服务器可能忙于处理其他客户端的连接, 这就会导致客户端可能会在服务器调用accept() 之前调用connect(), 这就会产生一个未决连接, listen()调用的第二个参数backlog, 就是用来记录这样的未决连接的最大数量的. 
    >
    >   ```bash
    >   $ cat /proc/sys/net/core/somaxconn
    >   4096
    >   ```

    

-   accept(): 在一个监听流 socket 上接受来自一个对等应用程序的连接, 并可选地返回对等 socket 的地址. 
    ```c
    #include <sys/socket.h>
    
    int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
    // return file descriptor on success, -1 on error
    ```

    

-   connect(): 建立与另一个 socket之间的连接. 将文件描述符sockfd 引用的主动 socket 连接到地址通过addr 和addrlen 指定的监听socket上

    ```c
    #include <sys/socket.h>
    
    int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen); // return 0 on success, -1 on error
    ```

    与bind() 调用的参数指定方式相同

---

-   recvfrom(): 在一个数据报socket上接收数据报
    ```c
    #include <sys/socket.h>
    
    ssize_t recvfrom(int sockfd, void *buffer, size_t length, int flags, struct sockaddr *src_addr, socklen_t addrlen);
    // return number of bytes received, 0 on EOF, -1 on error
    ```

    

-   sendto(): 在一个数据报socket上发送数据报
    ```c
    #include <sys/socket.h>
    
    ssize_t sendto(int sockfd, void *buffer, size_t length, int flags, const struct sockaddr *dest_addr, socklen_t addrlen);
    // return number of bytes sent, -1 on error
    ```

    



## 通用socket地址结构

这里主要针对`bind()`的传入参数来说:

```c
struct sockaddr {
    sa_family sa_family;   // 地址族, 例如 AF_*
    char      sa_data[14]; // socket 地址
};
```



## 流socket的运作原理

下面这段描述摘自*Linux/Unix系统编程手册*P950, 感觉写的清晰易懂. 

1.   socket() 创建一个socket, 等价于安装一个电话, 为使两个应用程序都能通信, 通信双方都要创建一个socket
2.   通过流socket通信类似于一个电话呼叫, 一个应用程序在进行通信之前必须要将其socket连接到另一个应用程序的socket上
     连接过程如下:
     *   一个应用程序调用bind() 以将socket绑定到一个众所周知的地址上, 然后调用listen()通知内核它接受接入连接的意愿, 这一步类似于已经有了一个为众人所知的电话号码并确保打开了电话, 这样人们就可以打进电话了. 
     *   其他应用程序通过调用connect()建立连接, 同时指定需要连接的socket 地址, 这类似于拨某人电话号码. 
     *   调用listen() 的应用程序使用accept() 接受连接, 这类似于在电话响起时拿起电话, 如果在对等应用程序调用connect() 之前执行了accept(), 那么accept() 就会阻塞(一直"等待电话")
3.   一旦建立了一个连接, 就可以在应用程序之间(类似于两路电话会话)进行双向数据传输, 直到其中一个使用close() 关闭了连接为止. 通信是通过read()和write() 系统调用或者一些提供了额外功能的socket特定的系统调用(例如`send()`,`recv()`)来完成的. 



## 流socket I/O

一对连接的流socket 在两个端点之间提供了一个双向通信信道, 如下:

<img src="https://s2.loli.net/2023/03/26/K65Efwjxsg1NkGd.jpg" style="zoom:25%;" />

连接流socket上I/O的语义与管道上I/O的语义类似. 

-   要执行I/O就要使用read/write系统调用, socket是双向的, 所以两端都可以使用读写操作

-   一个socket可以使用close() 调用关闭或者在应用程序终止之后关闭. 之后当对等应用程序试图从连接的另一端读取数据时, 将会收到文件结束(当所有缓冲数据都被读取之后). 如果对等应用程序试图向其socket写入数据, 就会收到一个`SIGPIPE`信号. 系统调用返回 `EPIPE`错误. 

    >   处理方法是: 忽略`SIGPIPE`信号并通过`EPIPE`错误找出被关闭的连接. 



## 数据报socket的运作原理

其运作类似于邮政系统. 

1.   socket()调用等价于创建一个邮箱(假设送信和取信都是在邮箱中发生的), 所有需要发送和接收数据报的应用程序都需要使用socket()创建一个数据报socket
2.   为允许另一个应用程序发送其数据报(类比待发送的信件), 一个应用程序需要使用bind() 将其socket绑定到一个众所周知的地址上, 而一个客户端会通过向该地址发送一个数据报来发起通信. 
3.   要发送一个数据报, 一个应用程序需要调用sendto() , 它接收的其中一个参数就是数据报发送到的socket的地址, 这类似于将收信人的地址写到信件上并投递该信.
4.   为接收一个数据报, 一个应用程序需要调用recvfrom(), 它在没有数据报到达时会阻塞. 因为recvfrom() 允许获取发送者的地址, 因此可以在需要时发送一个响应. (在发送者的socket没有绑定到一个众所周知的地址上时是有用的, 客户端通常是会碰到这种情况)
5.   当不再需要socket时, 应用程序需要使用close() 关闭socket.

>   与邮政系统类似, 从某地向另一地发送信件时候不保证按照被发送的顺序到达, 甚至不能保证都到达. 
>
>   数据报还新增了邮政系统不具备的特点: 由于底层的联网协议有时候会重新传输数据包, 所以同一数据包可能会多次到达. 

<img src="https://s2.loli.net/2023/03/26/fXvz8RgVJokcEWb.png" alt="数据报socket系统调用概述.drawio" style="zoom:73%;" />

## 在数据报socket上使用connect()

虽然数据报是无连接的, 但是在数据报socket上应用connect() 调用仍然是起作用的, 调用后会让内核记录这个socket的对等socket的地址 (已连接的socket就是指这类socket, 未连接的数据报socket就是指数据报socket的默认行为)

当数据报socket已连接后:

-   数据报的发送可在socket上使用write()或send()完成并且会自动被发送到同样地对等socket上, 与sendto一样, 每个write() 调用会发送一个独立的数据报
-   在这个socket上只能读取由对等socket发送的数据报.





# 实例: UNIX Domain

即同一主机下的socket通信. 



## 地址绑定

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/un.h> // sockaddr_un
#include <sys/socket.h>

int main(int argc, char* argv[]) {
    const char* SOCKNAME = "/tmp/mysock";
    int sfd;
    struct sockaddr_un addr;
    // struct sockaddr_un {
    //     __SOCKADDR_COMMON(sun_);
    //     char sun_path[108]; /* Path name.  */
    // };

    sfd = socket(AF_UNIX, SOCK_STREAM, 0);

    if (sfd == -1) fprintf(stderr, "socket\n");

    memset(&addr, 0, sizeof(struct sockaddr_un));

    addr.sun_family = AF_UNIX;
    strncpy(addr.sun_path, SOCKNAME, sizeof(addr.sun_path) - 1);

    if (bind(sfd, (struct sockaddr*)&addr, sizeof(struct sockaddr_un)) == -1)
        fprintf(stderr, "bind\n");

    /* $ ls -lF /tmp/mysock */
    /* srwxrwxr-x 1 zorch zorch 0 Mar 26 21:38 /tmp/mysock= */
    return 0;
}

```

