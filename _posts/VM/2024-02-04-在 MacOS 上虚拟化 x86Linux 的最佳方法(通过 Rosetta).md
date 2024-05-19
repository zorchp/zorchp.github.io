---
categories: [VM]
tags: MacOS VM Linux
---

## 写在前面

>   买了 ARM 的 mac, 就注定了要折腾一下虚拟机了...

之前写过一篇文章是通过 utm 虚拟化archlinux, 其实本质上还是调用了 qemu-system-x86_64, 所以速度并不快, 后来想着能不能借用 Rosetta 的优势即原生转译, 来虚拟化 Intel 的 Linux.

 看了一些文章, 提到过用lima 管理虚拟机, 然后配置, 应该是最便捷的方法了, 不过这里先以 utm 的最新版设置为例讲讲, 之后再说 lima.

>   环境支持:
>
>   MacOS13+ (为了使用 apple 的虚拟化, 这个虚拟化支持在ARM 架构的 Linux 上使用 Rosetta跑 Intel 架构的程序)
>
>   m系列芯片

## 一些看过的博客

算是一个引子, 可以看看 Apple 官方的消息

1.   [苹果M系列处理器上的Linux虚拟机内Rosetta转译初体验 - wvbCommunity](https://community.wvbtech.com/d/3137);(感觉写的比较详细的博客, 还附了图就很棒)
2.   [Running Intel Binaries in Linux VMs with Rosetta | Apple Developer Documentation](https://developer.apple.com/documentation/virtualization/running_intel_binaries_in_linux_vms_with_rosetta);
3.   [Rosetta | UTM Documentation](https://docs.getutm.app/advanced/rosetta/); 这篇算是 utm 支持, 其实很多内容在 Apple 官方的文档有写了



开始折腾...



## UTM 方案: 支持桌面 UI

### 搞个镜像

```bash
wget https://cdimage.ubuntu.com/releases/22.04/release/ubuntu-22.04.3-live-server-arm64.iso
```

注意一定要下载 arm 的 Linux 镜像, 然后在这里面安装 Rosetta, 通过 Linux 内的 Rosetta 来转译运行 Intel 的程序. 

>   这里就用比较广泛使用的 Ubuntu 了, 注意如果用 rpm 系列的 Linux 发行版的话安装后面要用到的包就比较麻烦了, 先能用再说. 

### 打开 utm

勾选虚拟化, 勾选 Apple 虚拟化, 和启用 Rosetta. 

此外就是选上上面下载好的 ISO 镜像

开启之后按照安装步骤一点一点来走安装, 如果 utm 显示不好的话可以用 iterm 连接ssh, help 界面给出了秘钥.

安装之后 poweroff, 然后清除掉 iso, 进入系统. 

### 配置Rosetta

Debian 系列直接安装:

```bash
sudo apt install binfmt-support
sudo apt install spice-vdagent #剪贴板共享
```

然后挂载

```bash
sudo mkdir /media/rosetta
sudo mount -t virtiofs rosetta /media/rosetta
```

写入`/etc/fstab`: 

```bash
rosetta	/media/rosetta	virtiofs	ro,nofail	0	0
```

安装

```bash
sudo /usr/sbin/update-binfmts --install rosetta /media/rosetta/rosetta \
     --magic "\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x3e\x00" \
     --mask "\xff\xff\xff\xff\xff\xfe\xfe\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff" \
     --credentials yes --preserve no --fix-binary yes
```

看看情况:

```bash
$ cat /proc/sys/fs/binfmt_misc/rosetta
enabled
interpreter /mnt/lima-rosetta/rosetta
flags: OCF
offset 0
magic 7f454c4602010100000000000000000002003e00
mask fffffffffffefe00fffffffffffffffffeffffff
```



### 换源

```bash
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-backports main restricted universe multiverse

deb http://ports.ubuntu.com/ubuntu-ports/ jammy-security main restricted universe multiverse
# deb-src http://ports.ubuntu.com/ubuntu-ports/ jammy-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-proposed main restricted universe multiverse
# # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ jammy-proposed main restricted universe multiverse
```



### 跑代码

首先安装一下 multilib 版的 gcc, 即:

```bash
sudo apt install gcc-multilib-x86-64-linux-gnu g++-multilib-x86-64-linux-gnu
```

这样只是搞定了交叉编译的工具链, 对于一个 Intel 的程序, 还需要 Intel 的 ld-linux so 库支持, 从阿里云服务器里面 cp 一个, 之后又提示 libc 找不到, 接着 cp, 这样的示例程序就跑起来了.

```cpp
#include <iostream>

int main() {
    std::cout << "hello rosetta\n";
    return 0;
}
```

如果要 Rosetta 执行就这样来:

```bash
x86_64-gnu-linux-g++ a.cpp #交叉编译工具链, 通过apt 安装 gcc-multilib
/media/rosetta/rosetta ./a.out
```

>   缺啥动态库就补上



## lima 方案: 快速配置最小化 Linux

这里参考了下面的文章. 

>   [在 Apple Silicon macOS 上跑 Linux 虚拟机 + Rosetta - 杰哥的{运维，编程，调板子}小笔记](https://jia.je/software/2023/11/23/apple-silicon-linux-rosetta/#%E5%88%9B%E5%BB%BA-linux-%E8%99%9A%E6%8B%9F%E6%9C%BA);

前面通过 UTM 的方法配置了虚拟化, 并且得到了不错的效果, 下面看看更快速的方法

主要通过 lima 来做, lima 之前安装 docker 时候大家应该不陌生, 因为 docker 的 daemon 用到了colima , 本质上就是一个 Ubuntu 的 arm 版, 但是用 docker 还是有点不舒服, 为什么直接来一个完美的 Intel Linux 呢?

### 安装配置 lima

```bash
brew install lima
limactl start template://debian --rosetta --vm-type=vz
limactl shell debian # 进入 Debian arm
```

查看 Rosetta 支持情况:

```bash
$ cat /proc/sys/fs/binfmt_misc/rosetta
```

### 在 lime-debian 中安装 Intel centos7

其实 nerdctl 跟 docker 差不多, 熟悉一下命令行的操作就好了. 

运行

```bash
nerdctl run -it --platform amd64 centos:centos7
```

退出之后就关闭了, 需要 start一下再进去

>   注意在开启 limactl 时候, **不要挂代理**, 直接退出, 否则进入 lima 之后启动不了 nerdctl 虚拟机

```bash
nerdctl start centos-f32d1
nerdctl exec -it centos-f32d1 /bin/bash
```

不用了就关闭

```bash
nerdctl stop centos-f32d1
```

查看容器情况

```bash
$ nerdctl ps -a
CONTAINER ID    IMAGE                               COMMAND        CREATED         STATUS     PORTS    NAMES
f32d106b5240    docker.io/library/centos:centos7    "/bin/bash"    21 hours ago    Created             centos-f32d1
```

>   podman 类似: (例如 alpine 不支持 containerd, 也就是 nerdctl, 那就只能通过 apk add podman 安装 podman 来完成了)
>
>   ```bash
>   # 初次使用
>   podman run -it --arch amd64 debian:stable
>   # 退出之后通过 start开启
>   podman start xxx
>   # 之后进入通过 exec 完成
>   podman exec -it xxx bash
>   #不用了关闭
>   podman stop xxx
>   
>   #查看容器开启情况
>   podman ps -a
>   ```



下面的操作就在 centos7 里面执行了. 

安装其他软件

```bash
yum -y install epel-release # 安装其他软件源
yum repolist
curl -o /etc/yum.repos.d/konimex-neofetch-epel-7.repo https://copr.fedorainfracloud.org/coprs/konimex/neofetch/repo/epel-7/konimex-neofetch-epel-7.repo
yum install neofetch
```

>   [Installation · dylanaraps/neofetch Wiki](https://github.com/dylanaraps/neofetch/wiki/Installation#fedora--rhel--centos--mageia--openmandriva);

neofetch

<img src="/Users/zorch/Desktop/截屏2024-02-04 23.48.02.jpg" style="zoom:37%;" />

### benchmark

>   ```bash
>   yum install sysbench
>   ```



可喜可贺! M3Pro 加持, 终于跑过阿里云服务器了

先来看看 阿里云的 Server, 两核拉满

```bash
$ sysbench cpu --cpu-max-prime=20000000 --threads=2 run
sysbench 1.0.20 (using system LuaJIT 2.1.0-beta3)

Running the test with following options:
Number of threads: 2
Initializing random number generator from current time


Prime numbers limit: 20000000

Initializing worker threads...

Threads started!

CPU speed:
    events per second:     0.05

General statistics:
    total time:                          38.8369s
    total number of events:              2

Latency (ms):
         min:                                37191.83
         avg:                                38014.32
         max:                                38836.81
         95th percentile:                    38506.38
         sum:                                76028.64

Threads fairness:
    events (avg/stddev):           1.0000/0.00
    execution time (avg/stddev):   38.0143/0.82
```

再来看 lima 的 Debian(arm64) 虚拟机下的 centos7 (x86_64)的情况如何

```bash
# sysbench cpu --cpu-max-prime=20000000 --threads=2 run
sysbench 1.0.17 (using system LuaJIT 2.0.4)

Running the test with following options:
Number of threads: 2
Initializing random number generator from current time


Prime numbers limit: 20000000

Initializing worker threads...

Threads started!

CPU speed:
    events per second:     0.39

General statistics:
    total time:                          10.1988s
    total number of events:              4

Latency (ms):
         min:                                 4981.69
         avg:                                 5097.66
         max:                                 5216.57
         95th percentile:                     5217.92
         sum:                                20390.63

Threads fairness:
    events (avg/stddev):           2.0000/0.00
    execution time (avg/stddev):   10.1953/0.00
```

虽然层层嵌套, 但是得益于 Apple 的虚拟化以及 Rosetta 的转译执行, 其效率还是很高的!!!

>   回头看 qemu 模拟出的 x86_64, 实在是不忍直视. 



### orbstack benchmark

lima centos 7 with rosetta

```bash
[root@f32d106b5240 /]# sysbench cpu --cpu-max-prime=20000000 --threads=2 run
sysbench 1.0.17 (using system LuaJIT 2.0.4)

Running the test with following options:
Number of threads: 2
Initializing random number generator from current time


Prime numbers limit: 20000000

Initializing worker threads...

Threads started!

CPU speed:
    events per second:     0.36

General statistics:
    total time:                          11.0779s
    total number of events:              4

Latency (ms):
         min:                                 5322.30
         avg:                                 5489.98
         max:                                 5560.35
         95th percentile:                     5607.61
         sum:                                21959.92

Threads fairness:
    events (avg/stddev):           2.0000/0.00
    execution time (avg/stddev):   10.9800/0.10
```

orbstack 

```bash
[root@centos8 dom]# sysbench cpu --cpu-max-prime=20000000 --threads=2 run
sysbench 1.0.20 (using system LuaJIT 2.1.0-beta3)

Running the test with following options:
Number of threads: 2
Initializing random number generator from current time


Prime numbers limit: 20000000

Initializing worker threads...

Threads started!

CPU speed:
    events per second:     0.42

General statistics:
    total time:                          14.3311s
    total number of events:              6

Latency (ms):
         min:                                 4735.80
         avg:                                 4773.90
         max:                                 4822.22
         95th percentile:                     4855.31
         sum:                                28643.39

Threads fairness:
    events (avg/stddev):           3.0000/0.00
    execution time (avg/stddev):   14.3217/0.01
```

区别不大, 感觉主要是因为一个在 Docker 环境模拟, 一个是直接模拟, 但是易用性这块 orbstack 完胜. 

