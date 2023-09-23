---
categories: [Tips]
tags: Tips Config Docker Kubernetes
---

# 写在前面

最近一直在研究云原生等的一些内容, 当然首当其冲的就是docker,kubernetes(下称k8s)等的配置了, 本文将以macOS12.3.1为主要环境, 架构为arm64(Apple silicon m1), 详细介绍如何在Mac上配置轻量级的云原生多节点平台`k8s`, 官方推荐的工具是`minikube`, 但是就是这个软件, 在各种搜索debug与配置了一天我才终于完美安装了. 一定要详细记录一下这个历史性的时刻!

距离苹果发布m1芯片其实已经过去了快两年, 但是很多软件的适配其实还是不太好的, 例如一些虚拟化程序, `virtualbox`, `VMware`, `hyperkit`, 这些软件都不能作为`minikube`的驱动, 只是因为并没有适配arm架构. 所以这里我采用了`qemu`这款开源的`x86`模拟程序. 



>   插句题外话, 在使用这类由活跃的开源社区和团队打造的程序时候, 如果想得到最新的版本更新日志与问题等, 第一说的资料还是`GitHub issue`, 其他的文章和博客大多出自这里, 当然主要还是通过Google的方式进入的, 其次才是`stack overflow`, 当然, 我最近又发现了几个不错的技术论坛和高质量的技术博客, 就是[Hacker News (ycombinator.com)](https://news.ycombinator.com/)和[Medium](https://medium.com/), 可供大家参考.



# docker without docker desktop

配置`k8s`主要是通过`minikube`完成的, 而`minikube`需要在`docker`中运行, 相当于是`docker`的一个组件, 之前在我的电脑上已经配置过docker, 是通过图形界面的方式, 即`docker desktop`. 这款软件虽然方便, 但是用起来是很占用系统资源的, 这里我就一直想去寻找一种`without docker desktop`的方式, 安装docker. 事实就是, 功夫不负有心人, 已经有很多前辈写了一些很有价值的文章, 这里我参考了[^1],[^2].

首先当然是需要采用`brew`安装两个`docker`的组件.

```bash
brew install docker
brew install docker-compose
```

这时候我们发现不用图形界面的`docker`安装并没有启动服务, 所以需要一个额外的虚拟机程序, 这个我们下面再说.



# minikube的完全配置

## 安装minikube

这里当然是一条命令完成的, 没有什么困难的.

```bash
brew install minikube
```

如果通过[^1]中给出的方法, 即通过`podman`代替docker进行minikube的配置, 则需要手动编译minikube并附带其他配置, 这里就不做测试了. 

## 配置colima虚拟机支持(daemon)

这里的配置就有的说了, 之前提到, docker并没有启动服务, 这是因为docker desktop安装时候自带了虚拟机(这在Linux上是直接集成的), 所以可以直接部署(所以同样地, 资源占用才比较大), 但是当我们直接通过`brew`安装了`docker`,实际上安装的只有`docker`的cli(*command-line interface*), 即命令行界面, 真正能让docker跑起来的话, 还需要一个虚拟机支持, 这就需要一个叫做`colima`的软件, 具体的介绍可以看看这里[^4], 在此之前我也研究过诸如`podman`等的容器, 但是均以失败告终[^3],[^6]. 都是倒在了`minikube start`上...

配置的`colima`环境默认是一个叫做alpine的Linux发行版, 下面是具体的版本信息.

```bash
❯ colima start --cpu 2 --memory 2 --disk 10
WARN[0000] already running, ignoring

❯ colima list
PROFILE    STATUS     ARCH       CPUS    MEMORY    DISK     RUNTIME    ADDRESS
default    Running    aarch64    2       2GiB      10GiB    docker

❯ colima ssh
colima:~$ uname -a
Linux colima 5.10.109-0-virt #1-Alpine SMP Mon, 28 Mar 2022 11:20:52 +0000 aarch64 Linux
colima:~$ cat /proc/version
Linux version 5.10.109-0-virt (buildozer@build-3-14-aarch64) (gcc (Alpine 10.3.1_git20210424) 10.3.1 20210424, GNU ld (GNU Binutils) 2.35.2) #1-Alpine SMP Mon, 28 Mar 2022 11:20:52 +0000
```

从配置过程中即可看到, colima就是通过docker进行

## 配置docker运行环境(runtime)

有了虚拟机支持, docker就能不通过`docker desktop`来运行了, 下面是一个例子:

先打开配置好的`colima`虚拟机环境

```bash
docker run --rm -d --name nginx -p 8080:80 nginx:latest
```



## 配置minikube的kicbase容器

这也是最让我头疼但是却很好解决的一个问题, 之前在`minikube start`时候总是弹出`stderr`[^5], 主要是说网址`gcr.io`不可达, `Unable to find image 'gcr.io/k8s-minikube/kicbase:v0.0.12-snapshot3@sha256:1d687ba53e19dbe5fafe4cc18aa07f269ecc4b7b622f2251b5bf569ddb474e9b' locally`, 后来我想到是不是需要更换镜像才能获取(即使我已经挂了代理), 但是并不行, 这里我看了很多CSDN的换源的文章,但是试过了并不行, 自己上网搜索发现, kicbse这个容器有两个版本, 在minikube官方的主页[^10]上, 这里显示只支持到了`0.0.17`. 另外, 一篇CSDN文章[^11]中提到的是只支持x86的版本(已经两年没有更新了[anjone/kicbase Tags | Docker Hub](https://hub.docker.com/r/anjone/kicbase/tags))..



默认开启minikube时候需要的版本是`0.0.32`, 这就是问题所在了, 通过docker官方的容器列表[^9], 我才最终完成了这个包的下载.. 命令如下:

```bash
docker pull kicbase/stable:v0.0.32
```

注意, 这里如果速度比较慢的话, 可以切换镜像, 通过修改`~/.docker/daemon.json`文件, 修改键`registry-mirrors`的值为如下网址:

```json
{"experimental":false,"builder":{"gc":{"enabled":true,"defaultKeepStorage":"20GB"}},"features":{"buildkit":true},"registry-mirrors":["https://registry.docker-cn.com"]}
```



## 最后的配置

最后还有一个问题, 这也在GitHub的issue界面中有所提及[^7], 就是一个报错, 大致内容如下:

```lua
stderr:
W0706 14:21:42.889959    9689 initconfiguration.go:120] Usage of CRI endpoints without URL scheme is deprecated and can cause kubelet errors in the future. Automatically prepending scheme "unix" to the "criSocket" with value "/var/run/cri-dockerd.sock". Please update your configuration!
	[WARNING SystemVerification]: failed to parse kernel config: unable to load kernel module: "configs", output: "modprobe: FATAL: Module configs not found in directory /lib/modules/5.10.109-0-virt\n", err: exit status 1
	[WARNING Service-Kubelet]: kubelet service is not enabled, please run 'systemctl enable kubelet.service'
error execution phase wait-control-plane: couldn't initialize a Kubernetes cluster
To see the stack trace of this error execute with --v=5 or higher

💡  建议：检查 'journalctl -xeu kubelet' 的输出，尝试启动 minikube 时添加参数 --extra-config=kubelet.cgroup-driver=systemd
🍿  Related issue: https://github.com/kubernetes/minikube/issues/4172
```

通过添加指定版本就可以解决此问题, 这还要感谢一个GitHub开发者的评论.

```bash
minikube start --kubernetes-version=v1.23.8
```



最后的成功配置`minikube`的命令如下:

```bash
❯ minikube start --vm-driver=docker --base-image="kicbase/stable:v0.0.32" --image-mirror-country='cn' --image-repository='registry.cn-hangzhou.aliyuncs.com/google_containers' --kubernetes-version=v1.23.8
😄  Darwin 12.3.1 (arm64) 上的 minikube v1.26.0
✨  根据用户配置使用 docker 驱动程序
✅  正在使用镜像存储库 registry.cn-hangzhou.aliyuncs.com/google_containers
📌  Using Docker Desktop driver with root privileges
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
🔥  Creating docker container (CPUs=2, Memory=1980MB) ...
    > kubeadm.sha256: 64 B / 64 B [--------------------------] 100.00% ? p/s 0s
    > kubelet.sha256: 64 B / 64 B [--------------------------] 100.00% ? p/s 0s
    > kubectl.sha256: 64 B / 64 B [--------------------------] 100.00% ? p/s 0s
    > kubelet: 116.72 MiB / 116.72 MiB [-----------] 100.00% 1.56 MiB p/s 1m15s

    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔎  Verifying Kubernetes components...
    ▪ Using image registry.cn-hangzhou.aliyuncs.com/google_containers/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default

❯ minikube ip
192.168.49.2

❯ minikube ssh
docker@minikube:~$ uname -a
Linux minikube 5.10.109-0-virt #1-Alpine SMP Mon, 28 Mar 2022 11:20:52 +0000 aarch64 aarch64 aarch64 GNU/Linux

docker@minikube:~$ ls

docker@minikube:~$ ll
total 32
drwxr-xr-x 1 docker docker 4096 Jul  6 14:25 ./
drwxr-xr-x 1 root   root   4096 Jun 15 21:06 ../
-rw-r--r-- 1 docker docker  220 Jun 15 21:06 .bash_logout
-rw-r--r-- 1 docker docker 3771 Jun 15 21:06 .bashrc
-rw-r--r-- 1 docker docker  807 Jun 15 21:06 .profile
drwxr-xr-x 1 docker docker 4096 Jul  6 14:25 .ssh/
-rw-r--r-- 1 docker docker    0 Jul  6 14:25 .sudo_as_admin_successful

docker@minikube:~$ cat /proc/version
Linux version 5.10.109-0-virt (buildozer@build-3-14-aarch64) (gcc (Alpine 10.3.1_git20210424) 10.3.1 20210424, GNU ld (GNU Binutils) 2.35.2) #1-Alpine SMP Mon, 28 Mar 2022 11:20:52 +0000
```

# 关闭minikube服务

这里需要注意的是, 不能通过`minikube stop`关闭集群, 这样会丢失之前创建的环境, 取而代之的是`minikube pause`以及`minikube unpause`, 如下:

```bash
❯ minikube pause
⏸️  Pausing node minikube ...
⏯️  Paused 14 containers in: kube-system, kubernetes-dashboard, storage-gluster, istio-operator

```

然后就是查看和关闭docker以及colima:

```bash
❯ docker ps
CONTAINER ID   IMAGE                    COMMAND                  CREATED       STATUS       PORTS                                                                                                                                                                                                                           NAMES
35ebd027f112   kicbase/stable:v0.0.32   "/usr/local/bin/entr…"   3 hours ago   Up 3 hours   0.0.0.0:49167->22/tcp, :::49167->22/tcp, 0.0.0.0:49166->2376/tcp, :::49166->2376/tcp, 0.0.0.0:49165->5000/tcp, :::49165->5000/tcp, 0.0.0.0:49164->8443/tcp, :::49164->8443/tcp, 0.0.0.0:49163->32443/tcp, :::49163->32443/tcp   minikube

❯ docker stop 35ebd027f112
35ebd027f112

❯ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

❯ colima list
PROFILE    STATUS     ARCH       CPUS    MEMORY    DISK     RUNTIME    ADDRESS
default    Running    aarch64    2       2GiB      10GiB    docker

❯ colima stop
INFO[0000] stopping colima
INFO[0000] stopping ...                                  context=docker
INFO[0001] stopping ...                                  context=vm
INFO[0006] done

```

这样的话, 我们在每次使用docker/minikube的时候, 就需要先开启`colima`, 这也被称为docker的守护进程(daemon), 然后再进入`minikube`, 启动节点.

# 小结

这里参考了近百篇博客文章,issue以及stack overflow的回答, 可以说是收获满满. 其中配置代理部分我没有太弄明白, 之后再补上, 事实就是不采用代理的话速度也已经相当快了. 



>   关于容器运行时部分, 可以参考[^8].

# 参考

[^1]:[Goodbye Docker Desktop, Hello Minikube! | by Abhinav Sonkar | ITNEXT](https://itnext.io/goodbye-docker-desktop-hello-minikube-3649f2a1c469);
[^2]:[Run Docker without Docker Desktop on macOS | Dhwaneet Bhatt](https://dhwaneetbhatt.com/blog/run-docker-without-docker-desktop-on-macos);
[^3]:[How to run Minikube with Podman. Since I switched from an Intel PC to a… | by Jan Sagurna | Towards Dev](https://towardsdev.com/how-to-run-minikube-with-podman-214310695e26);
[^4]:[Colima：MacOS 上的极简容器运行时和 Kubernetes（支持 m1） - SegmentFault 思否](https://segmentfault.com/a/1190000041183915);

[^5]:[failed to download kic base image or any fallback image (unable to access gcr.io) · Issue #8997 · kubernetes/minikube (github.com)](https://github.com/kubernetes/minikube/issues/8997);
[^6]:[How to run Minikube with Podman. Since I switched from an Intel PC to a… | by Jan Sagurna | Towards Dev](https://towardsdev.com/how-to-run-minikube-with-podman-214310695e26);
[^7]:[Minikube didnt start · Issue #14477 · kubernetes/minikube (github.com)](https://github.com/kubernetes/minikube/issues/14477#issuecomment-1176188284);
[^8]:[容器运行时第 1 部分：容器运行时简介 - Ian Lewis](https://www.ianlewis.org/en/container-runtimes-part-1-introduction-container-r);
[^9]:[kicbase/stable Tags | Docker Hub](https://hub.docker.com/r/kicbase/stable/tags);
[^10]:[Package minikube/kicbase (github.com)](https://github.com/kubernetes/minikube/pkgs/container/minikube%2Fkicbase);
[^11]:[minikube start启动集群失败Unable to find image gcr.io/k8s-minikube/kicbase:v0.0.10_kelsel的博客-CSDN博客](https://blog.csdn.net/kelsel/article/details/107728562?ops_request_misc=%7B%22request%5Fid%22%3A%22165712823316782390538774%22%2C%22scm%22%3A%2220140713.130102334.pc%5Fblog.%22%7D&request_id=165712823316782390538774&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-107728562-null-null.185^v2^control&utm_term=minikube&spm=1018.2226.3001.4450);
