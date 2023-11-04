---
categories: [Tips]
tags: Linux MacOS
---

# 写在前面

之前写了关于 qemu 安装 archlinux 的文章, 但是还有一些内容没得到解决, 比如很多时候 ssh 连接不成功, 这时候用图形界面(默认选项)的优势就体现出来了, 并且如果需要传输文件或者需要使用对外的端口, 仅转发一个22端口是不够的, 最后就是 gdb 调试的整套环境的配置, 这些问题都要解决. 

>   因为服务器太贵了, 也不想续费, 还是本地老老实实跑qemu虚拟机吧...





# qemu 的配置-完善版

## 之前的配置

```bash
#!/usr/bin/env bash

diskfile="$HOME/Documents/archlinux-x86_64-cc.qcow2"

# if [ $# -ne 1 ]; then
# 	echo "USAGE: $0 disk"
# 	echo " e.g.: $0 Archlinux.qcow2"
# 	exit 1
# fi

if [ ! -f $1 ]; then
	echo "could not open $1 : no such file"
	exit 1
fi

nohup qemu-system-x86_64 \
	-m 2G \
	-smp cores=3,threads=1,sockets=1,maxcpus=3 \
	-display none \
	-nographic \
	-drive file=${diskfile},if=virtio,cache=none \
	-nic user,hostfwd=tcp::60024-:8000,hostfwd=tcp::60022-:22 \
	-accel tcg \
	-cpu qemu64 \
	-machine q35 \
	-monitor tcp:127.0.0.1:60023,server,nowait &

# -D $HOME/Documents/archlinux-vm.log \
```

一些改动:

-   去掉了日志记录(注释掉了, 放在 28 行), 因为一般来说不会记录日志, 目前还没遇到异常退出的情况
-   用绝对路径导入虚拟机, 便于配置 alias 
-   如果遇到 ssh 连接不上的情况, 可以注释掉 19,20 行, 注意反斜杠的转义影响, 这样就会开启图形化终端了. 
-   端口转发, 下面 会讲

## 端口转发

这里比较恶心, 一开始我天真的以为多加入一行端口转发规则即可, 结果怎么也不行, 甚至 ssh 连接都出问题了. 后来发现应该是对指定网卡(nic)上做端口转发, 这在`nc`进入 monitor 之后使用`info usernet` 查看就明白了.



所以要加多个端口的转发规则, 只需要使用`,` 分隔的`hostfwd`键值对即可. 



## ssh相关

如果 ssh 连接失败, 可以先等一会, 虽然虚拟机开启来了, 但是 ssh 服务要等一段时间... 耐心等待即可, 推荐用:

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub -f arch@127.0.0.1
```

之后连接就不需要输入密码了. 



# 测试

## gdb 相关环境配置

事实上直接 pacman -Sy 即可, 这里列出需要安装的一些包:

```bash
sudo pacman -Sy clang gdb gcc git make cmake vim
```





## 性能

跟原生的 x86_64 肯定没法比, 这里给出阿里云的轻量应用服务器跑 sysbench 的对比:

核数都设置了一样的, 性能是阿里云的三分之一左右, 但是想到测试机器是 Mac 的第一款 M1 8+256Air, 感觉已经很不错了...

### 阿里云服务器

```c
 ==> sysbench cpu --cpu-max-prime=20000000 --threads=2 run
sysbench 1.0.18 (using system LuaJIT 2.1.0-beta3)

Running the test with following options:
Number of threads: 2
Initializing random number generator from current time


Prime numbers limit: 20000000

Initializing worker threads...

Threads started!

CPU speed:
    events per second:     0.05

General statistics:
    total time:                          42.3594s
    total number of events:              2

Latency (ms):
         min:                                40657.72
         avg:                                41508.45
         max:                                42359.17
         95th percentile:                    42134.07
         sum:                                83016.89

Threads fairness:
    events (avg/stddev):           1.0000/0.00
    execution time (avg/stddev):   41.5084/0.85
```



### archlinux 虚拟机(通过 qemu 在 arm Mac 上模拟)

```c
===============================================================
#!/usr/bin/env bash

qemu-system-x86_64 \
    -m 2G \
    -smp cores=2,threads=2,sockets=1,maxcpus=4 \
    -nographic \
    -drive file=Arch-Linux-x86_64-basic.qcow2,if=virtio,cache=none \
    -nic user,hostfwd=tcp::60022-:22 \
    -accel tcg \
    -monitor tcp:127.0.0.1:60023,server,nowait
====================================================================



[arch@archlinux ~]$ sysbench cpu --cpu-max-prime=20000000 --threads=4 run
sysbench 1.0.20 (using system LuaJIT 2.0.5)

Running the test with following options:
Number of threads: 4
Initializing random number generator from current time


Prime numbers limit: 20000000

Initializing worker threads...

Threads started!

CPU speed:
    events per second:     0.03

General statistics:
    total time:                          138.9636s
    total number of events:              4

Latency (ms):
         min:                               138146.60
         avg:                               138423.84
         max:                               138962.00
         95th percentile:                   100000.00
         sum:                               553695.34

Threads fairness:
    events (avg/stddev):           1.0000/0.00
    execution time (avg/stddev):   138.4238/0.32
```

改动核数对性能影响不大, 可能多核模拟导致的吧..
