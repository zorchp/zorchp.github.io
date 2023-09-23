---
categories: [Tips]
tags: MacOS Tips
---

# 写在前面

最近有同学问我`Pajek`大型网络分析软件的安装方法, 由于机型一样, 正好就帮助安装了, 下面列出来主要的配置环境以及主要方法, 主要用到了Stack Overflow的一个回答中的方法[^1], 供大家参考. 

>   环境:
>
>   MacOS 12.3 Apple Silicon M1
>   brew 
>   wine-stable



## 思路

需要先安装包管理软件`brew`, 然后通过`brew`安装`xquartz`和`wine`, 最后解压缩`Pajek`可执行文件即可通过`wine`运行. 

>   可能运行之中还有一些小小的bug, 不过应该不影响使用. 

# 安装主要步骤

如果电脑还没配置过brew, 那就需要先操作一番了.

## 安装brew

这里可以直接看我之前的文章, 就是关于`brew`的完美安装. 

## 通过brew安装xquartz和wine框架

```bash
brew install --cask xquartz
brew install --cask --no-quarantine wine-stable
```

注意这里安装`wine-stable`的时候, 通过brew下载安装的话速度有点慢, 这里我将下载好的源码文件放在了[CSDN](https://download.csdn.net/download/qq_41437512/85020998)中, 大家可以下载使用. 将该文件放在`~/Library/Caches/Homebrew/downloads/`中, 可以通过执行:

```bash
cp ~/Downloads/7e7af51c8e0e6318d2982ebbe1a997e1c7eb964c97c6e554fc627558f46b2e1b--wine-stable-7.0-osx64.tar.xz ~/Library/Caches/Homebrew/downloads/
```

之后使用上面的第二条`brew`命令就可以安装了. 

如果提示不能安装任意来源软件的话可执行[^2]:

```bash
sudo spctl --master-disable
```



之后在Pajek官网下载64位软件的可移植压缩包[^3], 解压之后执行:

```bash
wine64 ~/Downloads/Pajek64/Pajek.exe
```

即可运行该程序. 



# 主要参考

[^1]:[macos - Installing Pajek on M1 Mac - Super User](https://superuser.com/questions/1637939/installing-pajek-on-m1-mac)
[^2]:[Mac中常用的终端配置命令总结_zorchp的博客-CSDN博客](https://zorchp.blog.csdn.net/article/details/113554325);
[^3]:[**Install-Zip**](http://mrvar.fdv.uni-lj.si/pajek/Setup514/64/Pajek64.zip);
