---
categories: [Tips]
tags: Linux MacOS
---

# 写在前面

UTM 虚拟机可以卸载了, 命令行才是永远滴神, M1 MacBook Air 又能再战了!



之前一直用 UTM 的虚拟化开启 x86_64 的 Linux 虚拟机的, 但是我发现 UTM 好像不是必须的, 只要有qemu 就可以了, 下面就看看如何不通过图形界面前端(UTM)开启虚拟化支持, 这里主要用到的软件就是 iterm, Mac 下最强的终端模拟器. 





# 准备工作

## brew

最强包管理器, 安装

```bash
brew install qemu
```



## 下载 qcow2 格式的 archlinux 虚拟机磁盘文件

下载链接:

[archlinux-images-latest安装包下载_开源镜像站-阿里云](https://mirrors.aliyun.com/archlinux/images/latest/?spm=a2c6h.25603864.0.0.73e84298wr5uzN);

这里要注意, 这个虚拟机开启之后是需要密码登录的, 参考:

-   [Arch Linux / arch-boxes · GitLab](https://gitlab.archlinux.org/archlinux/arch-boxes/);
-   [qcow2 image password ? / Newbie Corner / Arch Linux Forums](https://bbs.archlinux.org/viewtopic.php?id=269955);

>   用户名: arch
>
>   密码: arch









## 配置$\bigstar$



```bash
#!/usr/bin/env bash

if [ $# -ne 1 ]; then
	echo "USAGE: $0 disk"
	echo " e.g.: $0 Archlinux.qcow2"
	exit 1
fi

if [ ! -f $1 ]; then
	echo "could not open $1 : no such file"
	exit 1
fi

nohup qemu-system-x86_64 \
	-m 2G \
	-smp cores=3,threads=1,sockets=1,maxcpus=3 \
	-display none \
	-nographic \
	-drive file=$1,if=virtio,cache=none \
	-nic user,hostfwd=tcp::60022-:22 \
	-accel tcg \
	-cpu qemu64 \
	-machine q35 \
	-D archlinux-vm.log \
	-monitor tcp:127.0.0.1:60023,server,nowait &
```

下面详细解释一下脚本中的一些参数:

-   使用方法就是脚本名`./run.sh archlinux.qcow2` 默认用`nohup` 执行, log 输出到`archlinux-vm.log` 中, 启动的BOOT提示在`nohup.out`中

-   -m: 内存, 默认单位是 MB, 可以指定为2G

-   -smp: CPU 核数, 设置需要参考下面的公式: 

    >   qemu-system-x86_64: Invalid CPU topology: product of the hierarchy must match maxcpus: 
    >
    >   >   sockets (1) * dies (1) * cores (2) * threads (2) != maxcpus (2)
    >

-   -display: 显示设置, 默认的话会开一个新的窗口, 应该是 MacOS 下的 cocoa 窗口, 这个其实类似于 UTM 界面的设置, 我感觉没必要, 就关闭了

    >   -display none
    >                   select display backend type
    >                   The default display is equivalent to
    >                   "-display cocoa"

-   -nographic: 不显示图形化, 将内容重定向到 IO

    >   disable graphical output and redirect serial I/Os to console

-   -drive: 指定磁盘文件, 这里就用镜像站下载的 qcow2 文件即可, 使用 virtio 开启网卡虚拟化, 并且禁用缓存(wiki 说的, 不知道为什么)

-   -nic: 网卡配置, 设置端口转发, 用于之后的 ssh 连接, 将客户机(虚拟机)的 22 端口暴露到宿主机(物理机)的60022 端口(Mac 需要开启防火墙)

-   -accel: 硬件加速, Mac 仅 tcg 模式可用

-   -cpu: qemu64 型号

-   -machine: 默认就是 q35

-   -D: 日志

-   -monitor: 监视器, 用于命令行操控虚拟机, 并可以在虚机运行中修改某些虚拟机配置的参数, 具体可以参考:

    >   [QEMU Monitor — QEMU documentation](https://www.qemu.org/docs/master/system/monitor.html);
    >
    >   [Qemu Monitor](https://hhb584520.github.io/kvm_blog/2017/02/17/qemu-monitor.html);(中文)





## ssh 连接

一般来说, 开启之后只要不报错, 就可以静候佳音了, 在 CPU 占用率降低之后, 虚拟机就开起来了, 此时可以用:

```bash
lsof  -iTCP:60022
```

检查端口监听情况, 然后连接:

```bash
ssh arch@127.0.0.1 -p 60022
```

## monitor 连接



```bash
nc 127.0.0.1 60023 # 端口需要和配置中的保持一致
```









# 其他踩坑

## (可能遇到的问题) 安装包时提示签名有问题



[[SOLVED\] Problem with pacman update - Signature is unknown trust / Newbie Corner / Arch Linux Forums](https://bbs.archlinux.org/viewtopic.php?id=143337);

>   ```bash
>   sudo rm -rf /etc/pacman.d/gnupg
>   pacman-key --init
>   pacman-key --populate archlinux
>   ```



## ssh连接

ssh 连接提示: kex_exchange_identification: read: Connection reset by peer

参考:

[ssh - How can I fix "kex_exchange_identification: read: Connection reset by peer"? - Stack Overflow](https://stackoverflow.com/questions/69394001/how-can-i-fix-kex-exchange-identification-read-connection-reset-by-peer);

>   关闭全局代理/防火墙试试



