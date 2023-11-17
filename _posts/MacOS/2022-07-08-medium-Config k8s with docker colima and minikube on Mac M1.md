---
categories: [Tips]
tags: Tips Config Docker Kubernetes
---

# Preface

Recently, I've been studying some contents of cloud native, etc. Of course, the first one is the configuration of `docker`, `kubernetes` (hereinafter referred to as `k8s`), etc. This article will take **macOS12.3.1** as the main environment, with the architecture of **arm64**(Apple silicon m1), and I will introduce in detail how to configure the **lightweight** cloud native multi-node platform ` K8s` on Mac. The official recommended tool is `minikube`, but it is this software that I finally installed perfectly after a day of searching, debugging and configuring. Be sure to record this historic moment in detail!

It's been almost two years since Apple released m1 chip, but the adaptation of many softwares is still not very good, such as some virtualization programs, ` VirtualBox `, `VMware` and ` HyperKit`. These softwares can't be used as drivers of ` minikube` just because they don't adapt to arm architecture. So here I use ` qemu`, an open source ` x86` simulator with `colima`.

>   I refer many of articles, blogs and github issues from google, medium.github, etc.

# Install docker without docker desktop

Configuration of `K8s` is mainly done through `MiniKube`, and `MiniKube` needs to run in `docker`, which is equivalent to a component of `Docker`. Docker has been configured on my computer before, and it is through a graphical interface, namely `docker desktop`. Although this software is convenient, it takes up a lot of system resources to use. I've always wanted to find a way to **install docker without docker desktop**. The truth is, everything pays off, and many predecessors have written some valuable articles. Here I refer to [^1], [^2].

First of all, of course, you need to use `brew` to install two components of docker. 

```bash
brew install docker
brew install docker-compose
```

At this time, we found that the `docker` installation without graphical interface did not start the service, so we needed an additional virtual machine program called `colima`. We will talk about this later.



# Minikube Complete Configuration Guide

## Install minikube

Of course, it was done by an order, and there was no difficulty.

```bash
brew install minikube
```



If the configuration of minikube is done by the method given in [^1], that is, using `podman` instead of docker, it is necessary to compile minikube manually and attach other configurations, so there is no test here.

## Configure colima virtual machine support (daemon)



There are some configurations here. As mentioned before, docker didn't start the *service*. This is because docker desktop comes with a virtual machine when it is installed (which is directly integrated on Linux), so it can be directly deployed (so again, the resource occupation is relatively large). But when we directly installed `docker` through `brew`, Actually, only the cli(*command-line interface*) of ` docker` is installed. 

If Docker can really run, it needs a virtual machine support, which requires a software called ` colima`. For the specific introduction, please see here [^4]. Before that, I also studied containers such as ` podman`[^3],[^6], but all of them ended in failure when I run `minikube start`...

The configured `colima` environment is a Linux distribution called `alpine` by default. The following is the specific version information on `AlpineLinux`.

```bash
❯ colima start --cpu 2 --memory 2 --disk 10 # config vm with 2GB MEM, 2cores CPU and 10GB disk size
INFO[0000] starting colima
INFO[0000] runtime: docker
INFO[0000] preparing network ...                         context=vm
INFO[0000] starting ...                                  context=vm
INFO[0022] provisioning ...                              context=docker
INFO[0022] starting ...                                  context=docker
INFO[0028] done

❯ colima list
PROFILE    STATUS     ARCH       CPUS    MEMORY    DISK     RUNTIME    ADDRESS
default    Running    aarch64    2       2GiB      10GiB    docker

❯ colima ssh
colima:~$ uname -a
Linux colima 5.10.109-0-virt #1-Alpine SMP Mon, 28 Mar 2022 11:20:52 +0000 aarch64 Linux
colima:~$ cat /proc/version
Linux version 5.10.109-0-virt (buildozer@build-3-14-aarch64) (gcc (Alpine 10.3.1_git20210424) 10.3.1 20210424, GNU ld (GNU Binutils) 2.35.2) #1-Alpine SMP Mon, 28 Mar 2022 11:20:52 +0000
```

As you can see from the configuration process, `colima` is context supported by `docker`, which is also called docker `daemon`.

## Configure docker runtime

With virtual machine support, docker can run **without** `docker desktop`. Here is an example:

>   You should open the configured `colima` virtual machine environment first.

```bash
❯ docker run --rm -d --name nginx -p 8080:80 nginx:latest
1a874a4b15ff5d8f8cbac6dd5ac766067657df0f25328a8765daddceaa1a6ffc
```

And then open your browser, type `localhost:8080`, you can see below interface:

```lua
Welcome to nginx!
If you see this page, the nginx web server is successfully installed and working. Further configuration is required.

For online documentation and support please refer to nginx.org.
Commercial support is available at nginx.com.

Thank you for using nginx.
```



## Configure the `kicbase` container of minikube

This is also the most troublesome problem for me, but it is easy to solve. Before, `stderr` [^5] always popped up when `minikube start`, mainly saying that the website `gcr.io` was unreachable. 

```c
Unable to find image 'gcr.io/k8s-minikube/ Kicbase: v0.0.12-Snapshot3 @ sha256: 1D687Ba53E19DBE5FAFE4CC18AA07F269ECC 4B7B62251B5bf569DDB474E9B' locally
```

Later, I thought if I needed to change the image to get it (even if I had hung up the agent), but it didn't work. I searched online and found that there are two versions of this container, `kicbse`. 

On the official homepage of minikube [^10], it shows here that it only supports ` 0.0.17`. In addition, An article mentioned the `x86-only` version (it hasn't been updated for two years [Anjonne/kicbase tags \| Docker Hub](https://hub.docker.com/r/Anjonne/kicbase/tags)) ...

The required version when opening minikube by default is ` 0.0.32`, which is the problem. I finally finished downloading this package through docker's official container list [^9] . The command is as follows:

```bash
docker pull kicbase/stable:v0.0.32
```



Note that here, if the speed is slow (If you are in China), you can switch mirrors. By modifying the file ` ~/.docker/daemon.json`, the value of the key  `registry-mirrors` is as follows:

```json
{"experimental":false,"builder":{"gc":{"enabled":true,"defaultKeepStorage":"20GB"}},"features":{"buildkit":true},"registry-mirrors":["https://registry.docker-cn.com"]}
```



## the last config

There is one last problem, which is also mentioned in the issue interface of GitHub [^7], which is an error. The general content is as follows:

```lua
stderr:
W0706 14:21:42.889959    9689 initconfiguration.go:120] Usage of CRI endpoints without URL scheme is deprecated and can cause kubelet errors in the future. Automatically prepending scheme "unix" to the "criSocket" with value "/var/run/cri-dockerd.sock". Please update your configuration!
	[WARNING SystemVerification]: failed to parse kernel config: unable to load kernel module: "configs", output: "modprobe: FATAL: Module configs not found in directory /lib/modules/5.10.109-0-virt\n", err: exit status 1
	[WARNING Service-Kubelet]: kubelet service is not enabled, please run 'systemctl enable kubelet.service'
error execution phase wait-control-plane: couldn't initialize a Kubernetes cluster
To see the stack trace of this error execute with --v=5 or higher

💡  Suggestion: Check output of 'journalctl -xeu kubelet', try passing --extra-config=kubelet.cgroup-driver=systemd to minikube start
🍿  Related issue: https://github.com/kubernetes/minikube/issues/4172
```

This problem can be solved by adding the specified version, thanks to a comment from a GitHub developer[^7].

```bash
minikube start --kubernetes-version=v1.23.8
```



The last command of successfully configuring `minikube` is as follows:

```bash
❯ minikube start --vm-driver=docker --base-image="kicbase/stable:v0.0.32" --image-mirror-country='cn' --image-repository='registry.cn-hangzhou.aliyuncs.com/google_containers' --kubernetes-version=v1.23.8
😄  Darwin 12.3.1 (arm64) 上的 minikube v1.26.0
✨  Use docker driver according to user configuration
✅  Using mirror repository registry.cn-hangzhou.aliyuncs.com/google_containers
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

❯ minikube ip # check k8s ip
192.168.49.2

❯ minikube ssh # connect into daemon
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

## Close minikube service

It should be noted here that you can't shut down the cluster through `minikube stop`, which will lose the previously created environment and replace it with `minikube pause` and `minikube unpause`, as follows:

```bash
❯ minikube pause
⏸️  Pausing node minikube ...
⏯️  Paused 18 containers in: kube-system, kubernetes-dashboard, storage-gluster, istio-operator

❯ minikube unpause
⏸️  Unpausing node minikube ...
⏸️  Unpaused 18 containers in: kube-system, kubernetes-dashboard, storage-gluster, istio-operator

```

## Check minikube status

```bash
❯ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

❯ minikube dashboard
🤔  Checking dashboard in action ...
🚀  Launching proxy ...
🤔  Checking proxy in action ...
🎉  Opening http://127.0.0.1:58190/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ in your default browser...

```
`Minikube` dashboard is as follows.

<img src="https://s2.loli.net/2022/07/10/rGiVQUoTzFKkjf8.jpg" alt="截屏2022-07-10 15.47.01" style="zoom:45%;" />

## Check and close docker,colima

```bash
❯ docker ps # check docker process
CONTAINER ID   IMAGE                    COMMAND                  CREATED       STATUS       PORTS                                                                                                                                                                                                                           NAMES
35ebd027f112   kicbase/stable:v0.0.32   "/usr/local/bin/entr…"   3 hours ago   Up 3 hours   0.0.0.0:49167->22/tcp, :::49167->22/tcp, 0.0.0.0:49166->2376/tcp, :::49166->2376/tcp, 0.0.0.0:49165->5000/tcp, :::49165->5000/tcp, 0.0.0.0:49164->8443/tcp, :::49164->8443/tcp, 0.0.0.0:49163->32443/tcp, :::49163->32443/tcp   minikube

❯ docker stop 35ebd027f112 # CONTAINER ID
35ebd027f112

❯ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

❯ colima list
PROFILE    STATUS     ARCH       CPUS    MEMORY    DISK     RUNTIME    ADDRESS
default    Running    aarch64    2       2GiB      10GiB    docker

❯ colima stop # close colima vm
INFO[0000] stopping colima
INFO[0000] stopping ...                                  context=docker
INFO[0001] stopping ...                                  context=vm
INFO[0006] done


```

In this way, every time we use `docker/minikube`, we need to start ` colima` with `colima start`, which is also called the daemon of docker, and then enter ` minikube` with `minikube start` to start container nodes.

# Peroration

With reference to nearly a hundred blog posts, answers from issues and stack overflow, I could say that I have gained a lot. This is my first article in `medium`, if this article has any questions, welcome to point them out. I will be grateful. 

Certainly, if this article helps you, I will be very happy :laughing:~ 

>   For container **runtime**, please refer to [^8].

# Ref

[^1]:[Goodbye Docker Desktop, Hello Minikube! \| by Abhinav Sonkar | ITNEXT](https://itnext.io/goodbye-docker-desktop-hello-minikube-3649f2a1c469);
[^2]:[Run Docker without Docker Desktop on macOS \| Dhwaneet Bhatt](https://dhwaneetbhatt.com/blog/run-docker-without-docker-desktop-on-macos);
[^3]:[How to run Minikube with Podman. Since I switched from an Intel PC to a… \| by Jan Sagurna \| Towards Dev](https://towardsdev.com/how-to-run-minikube-with-podman-214310695e26);
[^4]:[abiosoft/colima: Container runtimes on macOS (and Linux) with minimal setup (github.com)](https://github.com/abiosoft/colima);
[^5]:[failed to download kic base image or any fallback image (unable to access gcr.io) · Issue #8997 · kubernetes/minikube (github.com)](https://github.com/kubernetes/minikube/issues/8997);
[^6]:[How to run Minikube with Podman. Since I switched from an Intel PC to a… \| by Jan Sagurna \| Towards Dev](https://towardsdev.com/how-to-run-minikube-with-podman-214310695e26);
[^7]:[Minikube didnt start · Issue #14477 · kubernetes/minikube (github.com)](https://github.com/kubernetes/minikube/issues/14477#issuecomment-1176188284);
[^8]:[Container Runtimes Part 1: An Introduction to Container Runtimes - Ian Lewis](https://www.ianlewis.org/en/container-runtimes-part-1-introduction-container-r);
[^9]:[kicbase/stable Tags \| Docker Hub](https://hub.docker.com/r/kicbase/stable/tags);
[^10]:[Package minikube/kicbase (github.com)](https://github.com/kubernetes/minikube/pkgs/container/minikube%2Fkicbase);

