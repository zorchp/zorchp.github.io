---
categories: [Linux-Shell]
tags: Linux Shell
---





# 信号

| 信号值 | 宏名称  | 描述                           |
| ------ | ------- | ------------------------------ |
| 1      | SIGHUP  | 挂起进程                       |
| 2      | SIGINT  | 终止进程                       |
| 3      | SIGQUIT | 停止进程                       |
| 9      | SIGKILL | 无条件终止进程                 |
| 15     | SIGTERM | 尽可能终止进程                 |
| 17     | SIGSTOP | 无条件停止进程，但不是终止进程 |
| 18     | SIGTSTP | 停止或暂停进程，但不终止进程   |
| 19     | SIGCONT | 继续运行停止的进程             |

使用`trap`