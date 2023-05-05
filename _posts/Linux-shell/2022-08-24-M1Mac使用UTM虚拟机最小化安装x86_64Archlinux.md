---
categories: [Linux-Shell]
tags: MacOS Tips UTM Archlinux
---

# 写在前面

最近看操作系统的课程, 需要用到gnu的代码调试工具`gdb`, 但是在arm的Mac中并不能安装(只能安装x86_64架构的)

>   ```bash
>   ❯ brew install gdb
>   gdb: The x86_64 architecture is required for this software.
>   Error: gdb: An unsatisfied requirement failed this build.
>   ```

正好前几天看到有人用UTM在m1mac上成功安装了Win10(amd64), 我也尝试着安装来着, 但是Win10资源占用太大了, 8GB内存实在吃不消, 特别烫然后还很多bug, 后来我想索性试试Linux, 直接安装命令行界面并通过物理机ssh到虚拟机. 

在尝试过Debian之后发现安装速度太慢了, 一不小心又设置了个gnome桌面... 更是内存大户. 最近很火的Archlinux之前也没体验过, 那就来试试吧~

下面主要详解在UTM虚拟机中安装最小化Archlinux(amd64)的主要过程以及其他相关配置: 

1.   非Root用户与相关设置;
2.   网络与代理;
3.   ssh连接;
4.   C/C++开发环境配置.

系统安装部分主要参考[^1],[^2],其余配置参考了[^3],[^4],

# 系统安装

首先进入[Index of /archlinux/iso/latest/ | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/archlinux/iso/latest/)下载Archlinux的ISO镜像包. 这里下载的是最新的[archlinux-2022.08.05-x86_64.iso](https://mirrors.tuna.tsinghua.edu.cn/archlinux/iso/latest/archlinux-2022.08.05-x86_64.iso), 然后打开UTM, 选择模拟, 这样就可以使用不同架构的系统环境, 但是相应的性能会有一些差. 内核和内存越大越好, 但是也要根据自己的物理机的情况进行分配, 例如我的机器是8GB+256GB, 我给分配了3内核3GB内存和35GB磁盘, 之后系统安装时候还可以使用交换空间(swap)提高内存. 

完成之后, 打开虚拟机(要等一段时间), 进入archlinux安装, 显示的界面如下:



![截屏2022-08-29 12.52.26](../../../../Library/Application%20Support/typora-user-images/%E6%88%AA%E5%B1%8F2022-08-29%2012.52.26.jpg)



>   在此之前可以通过gnupg验证镜像的签名是否一致, 这里就不详述了.

## 同步时间服务器

```bash
timedatectl set-ntp true
```

## 分配磁盘空间并格式化

通过下面的命令查看磁盘, 一般会有一个`/dev/sda`和一个`loop`, 我们这里只需要分配`/dev/sda`即可. 

```bash
fdisk -l
```

然后

```bash
fdisk /dev/sda
```

这时候就进入分区工具了:

下面针对UEFI启动方式进行磁盘的分配与格式化, 这里分了三个分区, 分别是:

|   挂载点    |    分区     |  大小  |   分区类型(fdisk代号)   | 文件系统 |
| :---------: | :---------: | :----: | :---------------------: | -------- |
| `/mnt/boot` | `/dev/sda1` | 300MB  |     EFI系统分区(1)      | FAT      |
|  `[SAWP]`   | `/dev/sda2` |  2GB   |     Linux Swap(19)      |          |
|   `/mnt`    | `/dev/sda3` | 32.7GB | Linux x86_64根目录(`/`) | ext4     |

### 创建分区

>   输入`g`创建GPT分区表. 
>
>   输入`n`, 创建新分区
>
>   第一问：Partition number（分区号）保持默认. 
>
>   第二问：First sector（起始扇区）保持默认. 
>
>   第三问：Last sector（结束扇区）填入`+300MB`, 表示创建一个`300MB`的EFI启动引导分区. 
> 
>   输入`t`, 修改分区类型. 
>
>   第一问：Partition type（分区类型）输入`1`（EFI分区）. 
>
>   EFI分区创建完成. 

---

>   再次输入`n`, 创建新分区
>
>   第一问：Partition number（分区号）保持默认. 
>
>   第二问：First sector（起始扇区）保持默认. 
>
>   第三问：Last sector（结束扇区）键入`+2GB`, 创建一个2GB的交换空间. 
>
>   输入`t`, 修改分区类型. 
> 
>   第一问：Partition type（分区类型）输入`19`（交换空间）. 
>
>   交换空间创建完成. 

---

>   再次输入`n`, 创建新分区
>
>   第一问：Partition number（分区号）保持默认. 
>
>   第二问：First sector（起始扇区）保持默认. 
>
>   第三问：Last sector（结束扇区）默认, 即分配剩余所有的空间到根目录.
>
>   系统分区创建完成. 
> 
>   输入`w`, 写入修改. 
>
>   分区完成. 
>

### 格式化

```bash
#格式化EFI分区
mkfs.fat -F 32 /dev/sda1

#格式化swap
mkswap /dev/sda2

#格式化根目录
mkfs.ext4 /dev/sda3
```

### 挂载

```bash
#挂载根目录
mount /dev/sda3 /mnt

#创建EFI分区的挂载目录
mkdir -p /mnt/boot/efi

#挂载EFI分区
mount /dev/sda1 /mnt/boot/efi

```

### 启动交换空间

```bash
#启动交换空间
swapon /dev/sda2
```



## 网络配置与工具安装

```bash
dhcpcd
```

下面检测一下:

```bash
ping www.baidu.com
```

然后这里需要更换一下软件源镜像, 要不然之后系统安装会比较慢.

换源的话比较简单, 这里以清华镜像[^4]为例. 直接在**管理员权限下**使用:

```bash
nano /etc/pacman.d/mirrorlist
```

添加一行:

```bash
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch
```

然后`ctrl+O`保存, `ctrl+X`退出, 更新镜像缓存即可:

```bash
pacman -Syy
```



## 系统的安装

通过下面的命令安装系统与必备的软件:

```bash
pacstrap /mnt base base-devel linux linux-firmware
```

这里需要等待一段时间.. 

```bash
#生成挂载信息(fstab文件)
genfstab -U /mnt >> /mnt/etc/fstab

#进入新系统
arch-chroot /mnt
```

之后需要安装一些工具, 因为虽然默认安装的ISO镜像提供了部分工具(例如`dhcpcd`), 但是安装的新系统并没有, 如果不安装之后就没法联网了(还得重新挂载安装镜像)

```bash
#安装必备工具
pacman -Syu && pacman -S vim dhcpcd networkmanager grub
```

### 设置时区,语言,主机名

```bash
#时区:上海
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
#设置时间同步
hwclock --systohc

#本地化
#设置编码为utf8
vim /etc/locale.gen
# x掉`en_US.UTF-8 UTF-8`前面的`#`
# ZZ保存退出

# 生成locale配置信息
locale-gen

#添加语言(建议英文)
vim /etc/locale.conf
# 加入: `LANG=en_US.UTF-8` 保存退出

#添加主机名
vim etc/hostname
# 加入你的主机名, 保存退出

#修改hosts
vim /etc/hosts
# 加入:
# `127.0.0.1	localhost
#  ::1		localhost`


# 配置root密码: 
passwd
#需要确认

```



## 引导的配置与生成

安装引导程序:

```bash
grub-install --target=x86_64-efi --efi-directory=/boot/efi --removable
```

生成引导的配置文件:

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```



## 收尾工作

这里要注意的是, 一般比较推荐的是`reboot`, 即重启, 但这里由于要弹出镜像,我更推荐的是使用`poweroff`进行关机, **弹出镜像**之后再开机, 这样就可以直接进入刚才安装好的系统中了, 如果不弹出安装镜像那就还只能通过挂载点进入系统, 比较麻烦.

首先退出`arch-chroot`环境, 用`exit`或者`CTRL+D`都可. 

然后取消挂载:

```bash
umount -R /mnt
```

通过`poweroff`关机, 然后移除安装介质, 这里就是移除UTM挂载的安装镜像.



# 安装后的配置

这里是在重新开启archlinux虚拟机之后的一些配置.

## 添加用户

这里需要使用:

```bash
useradd -m -g users -G wheel -s /bin/bash 用户名 
passwd 用户名
```

进行普通权限用户的添加, 然后在后面登陆`ssh`的时候就可以先用这个用户名来进行识别, 最后通过`su root`进入管理员权限.

## 网络与代理配置

首先需要开启网络配置的系统服务. (root)

```bash
systemctl enable dhcpcd #启用开机启动
systemctl start dhcpcd #开启服务
```

关于代理这里我用的是clash, 开启允许局域网连接之后, 还需要知道物理机的ip地址, 这里的ip是内网ip, 我的是`192.168.3.8`, 那么这里就需要在archlinux中采用

```bash
export http_proxy=192.168.3.8:7890 https_proxy=192.168.3.8:7890
```

用Google测试一下(`curl`):

```bash
[root@test test]# export http_proxy=192.168.3.8:7890 https_proxy=192.168.3.8:7890
[root@test test]# curl -vv google.com
* Uses proxy env variable http_proxy == '192.168.3.8:7890'
*   Trying 192.168.3.8:7890...
* Connected to 192.168.3.8 (192.168.3.8) port 7890 (#0)
> GET http://google.com/ HTTP/1.1
> Host: google.com
> User-Agent: curl/7.84.0
> Accept: */*
> Proxy-Connection: Keep-Alive
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 301 Moved Permanently
< Content-Length: 219
< Cache-Control: public, max-age=2592000
< Connection: keep-alive
< Content-Type: text/html; charset=UTF-8
< Date: Tue, 30 Aug 2022 04:26:31 GMT
< Expires: Thu, 29 Sep 2022 04:26:31 GMT
< Keep-Alive: timeout=4
< Location: http://www.google.com/
< Proxy-Connection: keep-alive
< Server: gws
< X-Frame-Options: SAMEORIGIN
< X-Xss-Protection: 0
<
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
* Connection #0 to host 192.168.3.8 left intact
```

配置好代理主要是想用`tldr`查看命令, 还是比较方便的, 取消代理的话通过下面的命令完成:

```bash
unset http_proxy https_proxy
```



## ssh配置

```bash
pacman -Sy openssh
systemctl enable sshd #开机启动
 
systemctl start sshd.service #立即启动
```



我在iTerm中用ssh命令进行连接, 就可以顺利访问了:

```bash
❯ ssh -Y test1@192.168.205.9 #-Y 表示允许X11, 通过用户名方式登录,避免重复
test1@192.168.205.9's password:
X11 forwarding request failed on channel 0
Last login: Thu Aug 25 01:08:16 2022 from 192.168.205.1
[test1@test ~]$
```

当然, 这里建议还是使用`用户名@ip_address`的方式进行连接, 否则多个虚拟机的话可能会冲突.

配置好之后就可以最小化UTM 了, 直接用iTerm, 体验会好很多~



## GCC配置

这里比较简单, `gcc`默认已经安装, 所以直接安装`gdb`即可:

```bash
pacman -Sy gdb
```



演示一个`gdb`调试的例子:

![截屏2022-08-30 12.31.30](../../../../Library/Application%20Support/typora-user-images/%E6%88%AA%E5%B1%8F2022-08-30%2012.31.30.jpg)



# reference

[^1]:[Installation guide (简体中文) - ArchWiki (archlinux.org)](https://wiki.archlinux.org/title/Installation_guide_(简体中文));
[^2]:[archlinux安装教程2021.7.26_liaouser的博客-CSDN博客_archlinux安装](https://blog.csdn.net/qq_55239087/article/details/119106558);
[^3]:[Archlinux 安装教程 - 撸代码 - LuCode.net](https://blog.lucode.net/linux/archlinux-install-tutorial.html);
[^4]:[archlinux | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/archlinux/);
[^5]:[command line - Why the "v" in mkfs.vfat? - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/263606/why-the-v-in-mkfs-vfat);