---
categories: [Linux-Shell]
tags: MacOS launchctl
---

# 写在前面

深入了解MacOS, 就不得不提一下`launchctl`命令, 其实就像`Linux`下的`systemctl`有异曲同工之妙, 但是还有一些不一样的地方, 其功能也是相当强大, 下面来总结一下这个命令与常见用法[^1], 主要包括以下几点:

1.   守护进程(开机启动项与后台服务项)[^2]
2.   定时任务

# 预备知识

>   [维基百科](http://en.wikipedia.org/wiki/Launchd)将 launchd 定义为“一个统一的开源服务管理框架，用于启动、停止和管理守护进程、应用程序、进程和脚本。它由Apple的Dave Zarzycki编写和设计，随Mac OS X Tiger一起推出，并根据Apache许可证获得许可。

先来看一下MacOS中能通过`launchctl`创建守护进程的一些文件的存放位置:

```lua
~/Library/LaunchAgents 由用户自己定义的任务项
/Library/LaunchAgents 由管理员为用户定义的任务项
/Library/LaunchDaemons 由管理员定义的守护进程任务项
/System/Library/LaunchAgents 由Mac OS X为用户定义的任务项
/System/Library/LaunchDaemons 由Mac OS X定义的守护进程任务项
```



# 守护进程(daemon)









# ref

[^1]:[launchctl Man Page - macOS - SS64.com](https://ss64.com/osx/launchctl.html);
[^2]:[A launchd Tutorial](https://www.launchd.info/);