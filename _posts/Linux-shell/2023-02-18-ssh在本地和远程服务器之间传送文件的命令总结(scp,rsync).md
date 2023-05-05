---
categories: [Linux-Shell]
tags: ssh Server Linux
---

# 写在前面

关于云服务器, 之前介绍过不少文章, 但是当时依赖于一个名叫`Termius`的ssh图形化客户端, 好像是只有MacOS有, 传送文件只需要拖拽即可, 后来发现还是要多学点命令来完成文件传输才行, 下面来看看用`scp`以及`rsync`在本地和远端传送文件/文件夹的一些方法. 

环境:

-   物理主机: MacOS12.6 M1
-   服务器(云主机): Ubuntu 20.04 x86_64

>   参考:
>
>   1.   [通过 SSH 在远程和本地系统之间传输文件的 4 种方法 - 腾讯云开发者社区-腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/1990568);
>
>        



# 准备工作: 配置ssh免密登录

>   参考: 
>
>   [SSH 三步解决免密登录\_jeikerxiao的博客-CSDN博客\_ssh免密](https://blog.csdn.net/jeikerxiao/article/details/84105529);

这样之后每次传输文件就不用输入密码了. 

# scp命令

一个类似`cp`命令的命令, 很贴合一般的文件传输语法. 

>   注意, 下面的操作都在物理主机上完成, 而不是云主机. 

## 本地文件/目录上传至云服务器

```bash
scp /path/filename username@servername:/path
```

如果要传送目录, 可以用`-r`选项(递归传输), 如果子文件比较多且琐碎, 可以用`tar`先打包再上传. 



## 远程文件下载至本地

```bash
scp username@servername:/path/filename ~/local_dir
```

与上述情况同理, 目录采用`-r`选项. 





# rsync文件同步命令

语法与`scp`几乎一致, 注意下面的命令也都是在物理主机上使用的. 

macos自带了rsync, 不过版本比较低了, 最新版可以用`brew`安装:

```bash
brew install rsync
```



## 向远程服务器上传文件

```bash
rsync filename username@ip_address:/home/username
```

同样使用`-r`选项传输目录. 





## 下载远程服务器文件到本地

```bash
rsync username@ip_address:/home/username/filename ~/path
```



