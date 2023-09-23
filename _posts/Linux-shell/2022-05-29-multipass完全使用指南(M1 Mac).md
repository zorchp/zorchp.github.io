---
categories: [Linux-Shell]
tags: Linux Tips
---

# 写在前面

最近有虚拟机的需求, 我第一个想到了之前就有推荐过的multipass[^2], 至于为什么没有选parallel desktop. 主要还是不想花太多内存在图形用户界面上, 专注于命令行会好一些, 因为我电脑的架构是arm, 就只能安装arm版本的Ubuntu, 下面汇总一下主要的安装与配置命令以及图形界面的安装(基于Microsoft远程桌面, 这样消耗的内存会少一些).

>   环境: 
>   macOS 12.3.1 Apple silicon
>   multipass 1.9.0

安装起来比较简单, 直接
```sh
brew install --cask multipass
```

可选的安装:(图形界面)

```sh
brew install --cask microsoft-remote-desktop
```



# 主要配置

## 创建一个虚拟机

一条命令完事:

```sh
multipass launch --name vm1 --mem 2G --disk 40G --cpus 2 impish
```

下面解释一下具体的选项:

>   ```sh
>   $  multipass help launch
>   Usage: multipass launch [options] [[<remote:>]<image> | <url>]
>   Create and start a new instance.
>   
>   Options:
>     -h, --help           Display this help
>     -v, --verbose        Increase logging verbosity. Repeat the 'v' in the short
>                          option for more detail. Maximum verbosity is obtained
>                          with 4 (or more) v's, i.e. -vvvv.
>     -c, --cpus <cpus>    Number of CPUs to allocate.
>                          Minimum: 1, default: 1.
>     -d, --disk <disk>    Disk space to allocate. Positive integers, in bytes, or
>                          with K, M, G suffix.
>                          Minimum: 512M, default: 5G.
>     -m, --mem <mem>      Amount of memory to allocate. Positive integers, in
>                          bytes, or with K, M, G suffix.
>                          Minimum: 128M, default: 1G.
>     -n, --name <name>    Name for the instance. If it is 'primary' (the
>                          configured primary instance name), the user's home
>                          directory is mounted inside the newly launched instance,
>                          in 'Home'.
>     --cloud-init <file>  Path to a user-data cloud-init configuration, or '-' for
>                          stdin
>     --network <spec>     Add a network interface to the instance, where <spec> is
>                          in the "key=value,key=value" format, with the following
>                          keys available:
>                           name: the network to connect to (required), use the
>                          networks command for a list of possible values, or use
>                          'bridged' to use the interface configured via `multipass
>                          set local.bridged-network`.
>                           mode: auto|manual (default: auto)
>                           mac: hardware address (default: random).
>                          You can also use a shortcut of "<name>" to mean
>                          "name=<name>".
>     --bridged            Adds one `--network bridged` network.
>     --timeout <timeout>  Maximum time, in seconds, to wait for the command to
>                          complete. Note that some background operations may
>                          continue beyond that. By default, instance startup and
>                          initialization is limited to 5 minutes each.
>   
>   Arguments:
>     image                Optional image to launch. If omitted, then the default
>                          Ubuntu LTS will be used.
>                          <remote> can be either ‘release’ or ‘daily‘. If <remote>
>                          is omitted, ‘release’ will be used.
>                          <image> can be a partial image hash or an Ubuntu release
>                          version, codename or alias.
>                          <url> is a custom image URL that is in http://, https://,
>                          or file:// format.
>   ```

-   `--name`, `-n`, 指出虚拟机实例的名称, 默认为`primary`

-   `--mem`, `-m`, 虚拟机所用的物理内存, 默认为`1GB`

-   `--disk`, `-d`, 磁盘大小, 默认为`5GB`

-   `--cpus`, `-c`, 使用的CPU核数, 默认为`1`

-   `impish`, 使用的Ubuntu版本, 采用`multipass find`可以找出所有支持的版本, 最新版为`22.04`.

    >   Image                       Aliases           Version          Description
    >   18.04                       bionic            20220523         Ubuntu 18.04 LTS
    >   20.04                       focal,lts         20220505         Ubuntu 20.04 LTS
    >   21.10                       impish            20220309         Ubuntu 21.10
    >   22.04                       jammy             20220506         Ubuntu 22.04 LTS
    >   anbox-cloud-appliance                         latest           Anbox Cloud Appliance
    >   charm-dev                                     latest           A development and testing environment for charmers
    >   docker                                        latest           A Docker environment with Portainer and related tools
    >   minikube                                      latest           minikube is local Kubernetes



## 一些默认的配置位置

这部分的内容我是参考了好多资料[^1]才知道的, 当然也有自己的探索, 通过`find`命令找出系统中的缓存镜像的位置. 

-   配置文件, 这里指的是虚拟机的配置文件`.json`, 用于在创建已经有的实例后, 还能够修改系统的内存,CPU等参数的配置文件, 由于架构不同, 以及所采用的模拟方式不同, 这里我仅列出我的电脑中可以用的配置文件的存放路径:
    ```sh
    sudo su
    cat /var/root/Library/Application\ Support/multipassd/qemu/multipassd-vm-instances.json
    ```

    或者直接用:

    ```sh
    sudo cat /var/root/Library/Application\ Support/multipassd/qemu/multipassd-vm-instances.json
    ```

    

    这里可以先进入管理员环境, 方便找到目录, 当然直接用`sudo`以及编辑器打开也可以, 我这里的配置如下:

    ```json
    {
        "vm1": {
            "deleted": false,
            "disk_space": "42949672960",
            "mac_addr": "52:54:00:aa:1b:c7",
            // ...
            "mem_size": "2147483648",
            "num_cores": 2,
            "ssh_username": "ubuntu",
            "state": 0
        }
    }
    ```

    有了这个文件, 就可以愉快地进行针对已创建实例的CPU核数修改等操作了, 下面参考了[^4].

    >   ```sh
    >   # stop multipassd 
    >   sudo launchctl unload /Library/LaunchDaemons/com.canonical.multipassd.plist
    >   
    >   # edit /var/root/Library/Application\ Support/multipassd/qemu/multipassd-vm-instances.json
    >   # you'll need sudo for that
    >   sudo vi /var/root/Library/Application\ Support/multipassd/qemu/multipassd-vm-instances.json
    >   
    >   # start multipassd again
    >   sudo launchctl load /Library/LaunchDaemons/com.canonical.multipassd.plist
    >   ```

    <font size=5px color=red>注意:</font>

    -   `launchctl unload`和`launchctl load`, 这两个步骤是必须的, 如果没有停掉服务直接修改配置文件的话, 之后开启虚拟机会导致配置被之前的内容覆盖, 并不会生效. 在重新加载服务之后需要等一段时间, 然后开启虚拟机, 否则会提示错误

        ```sh
        shell failed: cannot connect to the multipass socket
        Please ensure multipassd is running and '/var/run/multipass_socket' is accessible
        ```

    这里我用修改内核为例, 通过`htop`命令查看内核, 发现确实被修改了.

-   缓存镜像下载后的存放位置:
    ```sh
    find /private/var -name *ubuntu*
        /private/var/root/Library/Application Support/multipassd/qemu/vault/instances/vm1/ubuntu-22.04-server-cloudimg-arm64.img
        /private/var/root/Library/Caches/multipassd/qemu/vault/images/jammy-20220506/ubuntu-22.04-server-cloudimg-arm64.img
        /private/var/root/Library/Caches/multipassd/qemu/vault/images/impish-20220309/ubuntu-21.10-server-cloudimg-arm64.img
    ```

    至于为什么要知道这个文件的存放位置, 主要还是因为电脑的内存不够, 一些不必要的缓存就一定要删除了, 这里列出通过`find`命令找到的一些缓存目录, 令人惊讶的是, `/var/root/`里面竟然还有桌面文件夹等文件夹, 像是一个新的系统, 以后再来探索这里面的东西吧.





# 图形界面

有一些开发环境不得不用图形界面, 这里也采用了官网推荐的一个方法[^3], 通过迂回的方式安装并显示图形界面. 因为需要安装软件包, 这里需要先进行镜像的配置, 主要的方法就参考清华镜像了[^5], 这里需要注意: 如果你用的也是arm架构的话, 镜像源需要采用的是`ubuntu-port`. 

```sh
sudo apt update
sudo apt install ubuntu-desktop xrdp
```

设置密码:

```sh
sudo passwd ubuntu
```

然后通过`brew`安装`microsoft-remote-desktop`, 上面已经提到了. 

通过在虚拟机中输入`ip addr`来查看IP地址, 输入到远程桌面即可连接.



# 配置代理

解决`git`速度太慢的情况, 而且做开发不用代理可以说几乎是不可能的, 这里以`clashx`为例配置一下在`multipass`中走代理的方法, 需要在`clashx`中打开**允许局域网连接**(allow LAN). 

然后查看物理主机的IP地址, 通过`ifconfig|grep inet`查看, 然后是端口, 这里默认应该就是`7890`了, 在虚拟机中输入
```sh
export ALL_PROXY=socks5://10.5.46.249:7890
```

然后测试一下: (这里不能用`ping`命令, 因为`ping`采用的协议使其不能通过代理走流量)
```sh
curl -vv https://www.google.com
```

发现已经能成功连接了. 

通过`unset ALL_PROXY`取消设置代理. 

# 参考

[^1]:[multipassd-vm-instances.json Empty file · Issue #2494 · canonical/multipass (github.com)](https://github.com/canonical/multipass/issues/2494);

[^2]:[Multipass Documentation | Multipass documentation](https://multipass.run/docs);
[^3]:[Graphical desktop in Multipass | Multipass documentation](https://multipass.run/docs/graphical-desktop-in-multipass);

[^4]:[更改实例的 CPU 数量 ·第1158期 ·规范/多通道 (github.com)](https://github.com/canonical/multipass/issues/1158);
[^5]:[ubuntu-ports | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu-ports/);
