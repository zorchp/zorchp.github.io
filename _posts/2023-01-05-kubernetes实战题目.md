---
tags: Docker Kubernetes Interview
---



1.   容器的基本实现技术有哪些？ namespace, cgroup, chroot

2.   从镜像启动容器的命令: docker run

3.   关于创建镜像的构建上下文, 理解错误的是:

     “构建上下文”可以是一个本地的目录

     “构建上下文”里的文件会被发送给 Docker daemon

     “构建上下文”可以是一个“.”, 表示当前目录

     可以不显式给出“构建上下文”，Docker 会默认使用当前目录

     >    (D，错误，“构建上下文”是 docker build 的必须参数)

4.   关于这个镜像“nginx:1.23-alpine”，哪些说法是正确的？

     A

     它是 Docker Hub 上的官方镜像

     B

     镜像的基础操作系统是 Alpine Linux

     它不能运行在 Ubuntu、Centos 等系统的 Docker 环境里

     D

     镜像里打包的是反向代理应用 Nginx

5.   Docker 容器与外部环境交换信息有哪些方式？

     A

     docker cp

     docker run -d

     C

     docker run -v

     docker run -p

     >   答案：ACD

     题目解析

     A，正确，在容器和宿主机之间拷贝文件
     B，错误，这是在后台启动容器的命令
     C，正确，为容器挂载本地目录
     D，正确，映射容器的端口号

6.   哪些是 Kubernetes 的核心组件？

     A

     apiserver

     B

     etcd

     C

     scheduler

     D

     controller-manager

7.   关于 YAML 语言的描述，下面哪个是错误的？

     YAML 语言是 JSON 的超集

     YAML 支持的复杂类型是数组和字典

     一份 YAML 文件里可以有多个 YAML 对象

     >   DYAML 里没有注释语法

8.   关于 Pod 的理解，下面哪个是错误的？

     Pod 是 Kubernetes 管理应用的最小单位

     Pod 里的关键字段是“spec.containers”

     可以不用 YAML 文件，直接从命令行创建 Pod

     Pod 里只能包含一个容器

     >   (D，错误，虽然大多数情况下 Pod 里只有一个容器，但它可以编排多个密切协同工作的容器)

9.   关于 Job 和 CronJob 的理解，下面哪些是正确的？

     A

     Job 和 CronJob 代表的是离线业务

     B

     Job 只运行一次，CronJob 可以运行多次

     CronJob 用字段“jobTemplate”直接操作 Pod 工作

     D

     Job 里会包含一个 Pod 模板

10.   关于 ConfigMap 和 Secret 的理解，哪些是错误的？

      A

      ConfigMap 是明文信息，Secret 是机密信息

      ConfigMap 可以加载成环境变量，Secret 只能加载成文件形式

      ConfigMap 没有“spec”字段，只有“data”字段

      D

      Secret 的 Base64 编码实现了机密信息的安全存储

      答案：BD

      >   题目解析

      A，正确，参见第 14 讲
      B，错误，ConfigMap 和 Secret 都可以加载成环境变量和文件的形式
      C，正确，参见第 14 讲
      D，错误，Base64 只是编码转换，并不是加密算法，可以很容易解码得到原文

11.   关于 kubeadm 搭建 Kubernetes 集群的说法，正确的有哪些？

      A

      kubeadm 把一些 Kubernetes 的关键组件打包成镜像，以容器的方式运行

      B

      master 节点的安装命令是“kubeadm init”

      C

      集群里的节点必须要改 hostname，不能重名

      D

      必须安装网络插件（如 Flannel）后集群才能正常工作

12.   关于 Deployment 对象的理解，哪些是正确的？

      A

      Deployment 通常用来部署无状态应用

      如果 Pod 意外被销毁，我需要手工操作 Deployment 恢复实例数量(自动)

      C

      Deployment 部署之后可以用“kubectl scale”任意调整实例的数量

      D

      Deployment 里的“replicas”字段可以是 0

13.   关于 DaemonSet 对象的理解，哪些是正确的？(BCD)

      DaemonSet 可以使用“kubectl scale”调整实例数量(DaemonSet 的实例数量与集群节点相关，无法调整)

      DaemonSet 相当于是节点上的守护进程

      DaemonSet 无法设置 replicas 字段

      DaemonSet 可以使用“容忍度”来容忍节点的“污点”

14.   关于 Service 对象的理解，哪些是正确的？

      A

      Service 是四层的负载均衡

      B

      Service 基于 DNS 插件实现了域名解析

      C

      Service 的 IP 地址是虚拟的

      Service 的 NodePort 特性只适用于某些特定节点

      >   (NodePort 会在集群的每个节点上都生效)

15.   关于 Ingress、Ingress Class、Ingress Controller 这些对象，哪些理解是正确的？(ABCD)

      Ingress 定义了七层负载均衡规则

      Ingress Class 解耦了 Ingress 和 Ingress Controller

      Ingress Controller 可以有多个不同的实现，多个不同的实例

      Ingress 自身没有流量分发能力，必须配合 Ingress Controller 一起使用

16.   关于 PV/PVC，下面哪个说法是错误的？

      PV 表示持久化存储，一般由系统管理员创建

      Kubernetes 不允许超量分配，也就是说如果 PV 容量大于 PVC，就不会绑定

      StorageClass 绑定 Provisioner 对象，就能够自动管理存储、创建 PV

      只有使用 PVC 才能申请到 PV 对象

      >   B，错误，只要 PV 容量满足 PVC 就可以分配，不存在超量问题

17.   关于 StatefulSet，下面哪个说法是正确的？

      A

      有状态的应用只能用 StatefulSet 部署

      StatefulSet 里的关键字段是“serviceName”

      StatefulSet 管理的 Pod 名字是随机生成的

      “volumeClaimTemplates”字段里包含的是 PV 存储对象定义

      >   题目解析

      A，错误，Deployment、DaemonSet 也可以部署有状态应用，只是状态无法保存
      B，正确，参见第 26 讲
      C，错误，StatefulSet Pod 的名字按顺序编号，是固定的
      D，错误，“volumeClaimTemplates”字段里是 PVC 定义

18.   关于滚动更新，下面哪个说法是错误的？

      滚动更新不适用 DaemonSet

      B

      滚动更新会自动记录操作历史

      滚动更新是两个同步进行的扩容和缩容过程

      滚动更新只能回退到最近的历史版本

      D，错误，用参数“--to-revision”可以回退到任意一个历史版本

19.   关于容器检查，下面哪个说法是错误的？

      A

      有 Startup、Liveness、Readiness 三种健康探针

      Readiness 探针失败就会重启容器

      可以使用 Shell、TCP Socket、HTTP Get 三种方式

      Startup 检查失败就不会执行后两种探针

      >   B，错误，Readiness 探针失败只是不会被 Service 分配流量

20.   关于集群的系统监控，哪些理解是正确的？

      A

      Metrics Server 是一种插件，可以收集 CPU、内存等指标

      B

      HorizontalPodAutoscaler 的能力基于 Metrics Server，没有它就无法工作

      HorizontalPodAutoscaler 适用于 Deployment、DaemonSet、StatefulSet

      没有 Grafana，Prometheus 也可以正常工作

      C，错误，HorizontalPodAutoscaler 只能用于 Deployment 和 StatefulSet

      

