---
categories: NetWork
tags: NetWork
---

# 写在前面

为了学网络编程, 数据报的各种走向和信息的传递, 需要研究一下抓包工具, 也算是对理论知识的一个巩固吧



## 一些学习资料

-   [Wireshark Masterclass - YouTube](https://www.youtube.com/playlist?list=PLW8bTPfXNGdC5Co0VnBK1yVzAwSSphzpJ);
-   Wireshark 数据分析-第三版
-   wireshark 网络分析从入门到实践



# 基本认识-安装和配置

## 安装(MacOS-brew)

>   ```bash
>   brew install --cask wireshark
>   # 一定要用 cask 选项, 否则先安装命令行之后命令行版本会跟 gui 界面的 wireshark冲突
>   brew list wireshark
>   ==> App
>   /Applications/Wireshark.app (680 files, 217.8MB)
>   ...
>   ```

## 配置

<img src="https://cdn.jsdelivr.net/gh/zorchp/blogimage/%E6%88%AA%E5%B1%8F2023-12-07%2013.15.16.png" alt="截屏2023-12-07 13.15.16" style="zoom:50%;" />

首先在右下角有一个配置, 可以搞一个自己的配置文件, 右键->New... 创建一个自己的配置, 例如

<img src="https://cdn.jsdelivr.net/gh/zorchp/blogimage/%E6%88%AA%E5%B1%8F2023-12-07%2013.15.31.png" alt="截屏2023-12-07 13.15.16" style="zoom:50%;" />

然后

# 完整流程

-   选择合适的网卡
-   开始捕获数据报
-   过滤掉无用的数据报
-   将捕获到的数据包保存为文件

