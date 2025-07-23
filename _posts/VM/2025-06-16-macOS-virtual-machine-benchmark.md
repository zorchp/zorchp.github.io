---

---





## 写在前面



## 环境

``` 
macOS 15.5 
xcode 26beta

M2 16GB
```



``` 
container run -it  --arch amd64 --name fedora_amd  fedora
container start fedora_amd
container exec -it fedora_amd bash
```



测试命令



``` bash
 ==> sysbench --version
sysbench 1.0.20
# 单核性能
sysbench cpu --cpu-max-prime=20000 --threads=1 run
# 多核性能
sysbench cpu --cpu-max-prime=20000 --threads=4 run
```



指标

```
CPU speed:
    events per second: 
```



## host 架构(aarch64)

| 环境                    | 单核 CPU speed | 多核 CPU speed |
| ----------------------- | -------------- | -------------- |
| macOS host              | 13933446.12    | 51587964.89    |
| macOS container(fedora) | 4310.26        | 15665.61       |
| orb(kali)               | 4293.26        | 15844.90       |
| utm                     | 4302.44        | 15623.52       |
| lima(debian,qemu)       | 3777.77        | 13827.43       |



## x86_64 模拟

| 环境                    | 单核 CPU speed | 多核 CPU speed |
| ----------------------- | -------------- | -------------- |
| macOS container(fedora) | 3131.08        | 11755.65       |
| orb(centos9)            | 3135.48        | 11687.90       |
| lima(rosetta,alpine)    | 2630.40        | 9911.70        |
| utm                     |                |                |



## 环境搭建备份

```
yum install openssh openssh-server systemctl clang llvm c++ gdb lldb top which su
ssh-keygen -A
sshd -D
```





## 总结

差的不是很大, 但是毕竟是 apple 自研/swift 原生支持. 还是可以期待一波的. 
