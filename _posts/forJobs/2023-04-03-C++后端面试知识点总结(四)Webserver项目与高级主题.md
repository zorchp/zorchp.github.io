---
categories: [forJobs]
tags: C++ Interview
---

# 写在前面



# 基本知识



## cookie和session的区别





## 作业和进程的区别

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