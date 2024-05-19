---
categories: [Linux-Shell]
tags: Linux Unix Shell
---

# 写在前面

记录一些常用的shell命令(主要是系统层面), 我分别在两个平台下进行测试:

1.   MacOS 12.6(arm)
2.   Ubuntu(arm, multipass)

由于业界的标准还是Linux, 这里以Linux为主, 对于MacOS的话其实可以直接从GUI界面得到, 除非对于一些开发层面的内容需要命令行.

# Ubuntu版



## 系统基本信息

这部分参考了一篇博客[^1], 写的相当详细, 也是基于Ubuntu的. 给出了很多基本的系统信息, 主要是软件层面.

```bash
# 查看系统内核版本, 系统名称
ubuntu@vm1:~$ cat /proc/version
Linux version 5.4.0-126-generic (buildd@bos02-arm64-060) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1)) #142-Ubuntu SMP Fri Aug 26 12:15:55 UTC 2022
```



```bash
# 系统信息
ubuntu@vm1:~$ uname -a
Linux vm1 5.4.0-126-generic #142-Ubuntu SMP Fri Aug 26 12:15:55 UTC 2022 aarch64 aarch64 aarch64 GNU/Linux
```





```bash
# 主机名控制信息
ubuntu@vm1:~$ hostnamectl
   Static hostname: vm1
         Icon name: computer-vm
           Chassis: vm
        Machine ID: 4629426ffee349c3be9111c661c3ac64
           Boot ID: b0e55a46b1e343ef9db67a6aa6652477
    Virtualization: qemu # 从这里可以看出来具体的架构以及虚拟化支持
  Operating System: Ubuntu 20.04.5 LTS
            Kernel: Linux 5.4.0-126-generic
      Architecture: arm64
```





```bash
# 操作系统发行版信息
ubuntu@vm1:~$ cat /etc/os-release
NAME="Ubuntu"
VERSION="20.04.5 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.5 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
```





```bash
# 输出特定发行版的信息
ubuntu@vm1:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.5 LTS
Release:	20.04
Codename:	focal
```



## 进程控制与管理



这里





# MacOS版



# ref

[^1]:[How to check os version in Linux command line - nixCraft (cyberciti.biz)](https://www.cyberciti.biz/faq/how-to-check-os-version-in-linux-command-line/);

[^2]: