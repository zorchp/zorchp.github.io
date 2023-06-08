---
categories: [forJobs]
tags: C++ Interview
---

# 写在前面



# 基本知识



# 阻塞/非阻塞, 同步/异步

网络 IO 阶段 1: 数据就绪(位于操作系统的 TCP 接收缓冲区)

-   阻塞: 调用 IO 方法的线程进入阻塞状态
-   非阻塞: 不会改变线程状态, 通过返回值判断

网络 IO 阶段 2: 数据读写(用户的应用程序)

-   同步: 花程序自身的时间
-   异步: 操作系统就绪之后进行通知



## cookie和session的区别



-   

## recv和read用法有什么区别



## LRU 和 LFU





## reactor模式和proactor模式

-   reactor模式: 要求主线程(I/O处理单元)只负责监听文件描述符上是否有事件发生, 有的话就立即将该事件通知工作线程(逻辑单元). 除此之外, 主线程不做任何实质性的工作, 读写数据/接受新链接/处理客户端请求均在工作线程上完成. 
-   proactor模式: 将所有I/O操作都交给主线程和内核来处理, 工作线程仅仅负责业务逻辑. 





# I/O多路复用



## select

用途: 在一段指定时间内, 监听用户感兴趣的文件描述符上的可读可写和异常事件. 

```c
#include <sys/select.h>

int select(int nfds, fd_set* readfds, fd_set* write_fds, fd_set* exceptfds, struct timeval* timeout);
```







## epoll

```c
#include <sys/epoll.h>

int epoll_create(int size);
int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event);

int epoll_wait(int epfd, struct epoll_event *events,
                      int maxevents, int timeout);
int epoll_pwait(int epfd, struct epoll_event *events,
                      int maxevents, int timeout,
                      const sigset_t *sigmask);
```



### 水平触发和边缘触发

-   水平触发通知(LT, Level Trigger): 如果文件描述符上可以非阻塞地执行I/O系统调用, 此时认为它已经就绪. 
-   边缘触发通知(ET, Edge Trigger): 如果文件描述符自上次状态检查依赖有了新的I/O活动( 比如新的输入), 则需要触发通知. 

其中, LT是epoll默认的工作模式, 这种模式下epoll相当于一个效率较高的poll. 

当向epoll内核事件表中注册一个文件描述符上的EPOLLET事件时, epoll将以ET模式操作文件描述符, 这是高效工作模式. 

>   关于读事件，如果业务可以保证每次都可以读完，那就可以使用ET，否则使用LT。
>
>   对于写事件，如果一次性可以写完那就可以使用LT，写完删除写事件就可以了；但是如果写的数据很大也不在意延迟，那么就可以使用ET，因为ET可以保证在发送缓冲区变为空时才再次通知（而LT则是发送缓冲区空了就可以通知就绪，这样就每次触发就只能写一点点数据，内核切换开销以及内存拷贝开销过大）
>
>   作者：心痕
>   链接：https://www.zhihu.com/question/272447529/answer/1414142223
>   来源：知乎
>   著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# 多线程

```c
#include <pthread.h>

int pthread_create(pthread_t *thread, const pthread_attr_t *attr,
                   void *(*start_routine) (void *), void *arg);
```





# 基本框架

>   基本框架类似, 不同之处在于逻辑处理. 

读取信息->解析请求信息->作出响应(发回数据)

I/O 处理单元->逻辑单元->网络存储单元

|     模块     | 功能                                                     | 具体功能                                                     |
| :----------: | -------------------------------------------------------- | ------------------------------------------------------------ |
| I/O 处理单元 | 处理客户连接, 读写网络数据(基本)                         | 等待并接受新的客户连接, <br />接收客户数据, <br />将服务器响应数据返回给客户端 |
|   逻辑单元   | 业务进程或线程(多个, 实现并发), 解析请求, 给出响应(HTTP) | 分析并处理客户数据, <br />将结果传递给I/O 处理单元<br />或者直接发送给客户端 |
| 网络存储单元 | 数据库, 文件或缓存, 客户访问资源, 存储客户信息           | -                                                            |
|   请求队列   | 各单元之间通信方式的抽象                                 | 池的一部分, <br />多逻辑单元同时访问一个存储单元时,<br />需要采用某种机制来协调处理竞态条件 |

>   注意:
>
>   1.   数据收发不一定在 I/O 处理单元中执行, 也可以在逻辑单元中执行, 具体要看使用了哪种事件处理模式(proactor, reactor)
>   2.   



## 事件处理模式

服务器要处理三类事件: I/O 事件, 信号, 定时事件. 

### proactor: 工作线程只执行逻辑处理

将所有 I/O 操作都交给主线程和内核来处理(读写), 工作线程仅负责业务逻辑. 

使用**异步 I/O** 模型(以 aio_read, aio_write为例) 实现proactor模式的工作流程:

1.   主线程调用 aio_read 向内核注册 socket 上的读完成事件, 并且告诉内核用户读缓冲区的位置, 以及读操作完成时如何通知应用程序. (信号)
2.   主线程继续处理其他逻辑
3.   当 socket 上的数据被读入用户缓冲区(注意这里的用户是指服务端的用户态进程)后, 内核将向应用程序发送一个信号, 通知应用程序已经可用
4.   应用程序预先定义好的信号处理函数选择一个工作线程处理客户请求, 工作线程处理完客户请求之后, 调用 aio_write 向内核注册 socket 上的写完成事件, 并告诉内核用户写缓冲区的位置, 以及写操作完成时如何通知应用程序. 
5.   主线程继续处理其他逻辑
6.   当用户缓冲区的数据被写入 socket 之后, 内核将向应用程序发送一个信号, 以通知应用程序已经发送完毕
7.   应用程序预先定义好的信号处理函数选择一个工作线程做善后处理, 例如决定是否关闭 socket fd. 



使用**同步 I/O** 模型(epoll)模拟的 proactor 模式的工作流程为:

1.   主线程往 epoll 内核事件表中注册 socket 上的读就绪事件, 
2.   主线程等待 socket 上有数据可读(epoll_wait)
3.   socket 上有数据可读时, epoll_wait 通知主线程, 主线程从 socket 循环读取数据, **直到没有更多数据可读**, 然后将读取到的数据封装成请求对象, 插入请求队列. (交给工作线程时必须读取出全部的数据)
4.   睡眠在请求队列上的某个工作线程被唤醒, 它获得请求对象并处理客户请求, 然后往 epoll 内核事件表中注册 socket 上的写就绪事件
5.   主线程等待 socket 可写(epoll_wait)
6.   socket 可写时, epoll_wait 通知主线程, 主线程往 socket 上写入服务器处理客户请求的结果(发回客户端). 



### reactor: 工作线程执行读写操作

要求主线程(I/O 处理单元) **只负责监听** 文件描述符上是否有事件发生, 有的话立即将该事件**通知**工作线程(子线程, 逻辑单元), 将 socket 可读可写事件放入请求队列, 交给工作线程处理. 除此之外, 主线程不做任何其他实质性的工作. 读写数据, 接受新连接, 处理客户请求都在工作线程中完成. 



使用**同步 I/O** 实现的 reactor 模式工作流程: (以epoll为例, 下面的步骤建议全文背诵)

1.   主线程向 epoll 内核事件表中注册 socket 上的读就绪事件 (初始化, epoll_create, epoll_ctl)
1.   主线程等待 socket 上有数据可读 (epoll_wait)
1.   当 socket 上有数据可读时, epoll_wait 通知主线程, 主线程将 socket 可读事件(和相关信息)放入请求队列
1.   睡眠在请求队列上的工作线程被唤醒, 从 socket 读取数据, 处理客户请求, 往 epoll 内核事件表中注册该 socket 上的写就绪事件
1.   主线程调用 epoll_wait 等待 socket 可写
1.   socket 可写时, epoll_wait 通知主线程, 主线程将 socket 可写事件放入请求队列
1.   睡眠在请求队列上的某个工作线程被唤醒, 往 socket 写入服务器处理客户请求的结果(发回客户端)

## 为什么不用 proactor?

因为在 Linux 中,proactor 主要采用异步 I/O 提高整体性能, 但是目前的 Pthread 库给出的 aio 操作都是在用户空间中执行的, 速度比较慢

# 工具函数

## 错误处理

仅仅为了调试, 后期日志系统时候会改

```cpp
#define ERR(x) fprintf(stderr, "%s error \n", #x), exit(-1)
```







# 基本通信模块

## 连接方面

### 服务端

这里先三步走: 创建+绑定+监听

```cpp
// create socket
int lfd = socket(AF_INET, SOCK_STREAM, 0);
if (lfd == -1) ERR(socket);

struct sockaddr_in saddr;
saddr.sin_family = AF_INET;
saddr.sin_port = htons(9006);
saddr.sin_addr.s_addr = INADDR_ANY; // 0.0.0.0 default all addr

int err = bind(lfd, (struct sockaddr *)&saddr, sizeof(saddr));
if (err == -1) ERR(bind);

err = listen(lfd, 128);
if (err == -1) ERR(listen);
```

主事件循环, 用于创建多线程处理通信: (阻塞 accept 等待连接)

```cpp
```







# 解析 HTTP 请求

```http
GET / HTTP/1.1
Host: 127.0.0.1:9006
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
```





# 开发工具的使用



## vim



## gdb

多线程调试

## git



### rebase:

>   [关于 Git 变基](https://docs.github.com/zh/get-started/using-git/about-git-rebase)

`git rebase` 命令用于轻松更改一系列提交，修改存储库的历史记录。 您可以重新排序、编辑提交或将提交压缩到一起。

通常，你会使用 `git rebase` 来：

-   编辑之前的提交消息
-   将多个提交合并为一个
-   删除或还原不再必要的提交

