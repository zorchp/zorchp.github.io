---
categories: [forJobs]
tags: C++ Interview
---





1.   注意 epoll_ctl 的参数顺序!!!

     >   ```c 
     >   int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event);
     >   ```
     >
     >   交换第二三参数之后, 会导致注册事件失败, 不触发写回事件, 客户端获取不到数据一直阻塞

2.   html 等资源的路径 使用**绝对路径**或者 `getcwd` + 字符串拼接

     >   

3.   





