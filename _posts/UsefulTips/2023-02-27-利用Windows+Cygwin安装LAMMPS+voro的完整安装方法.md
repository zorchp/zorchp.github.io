---
categories: [Tips]
tags: Windows Linux Tips
---

# 写在前面

最近有朋友问我如何安装一个叫做`voro++`的工科分析软件, 由于这个软件年代过于久远(2013), 并且是C++写的, 在win下需要编译安装, 就折腾了一下, 后来发现在Windows下直接安装的LAMMPS不能编译voro, 那么还得先手动编译安装一个LAMMPS, 折腾了好久, 终于完成了..

主要困难的地方还是在`cygwin`的包管理上, 由于没办法直接通过包管理器来安装(事实上有一个包管理器, 但是还需要一些特殊工具才能安装, 实在是麻烦), 那就只能每次需要什么包, 就从setup程序中选中那些包来安装了...

其次就是编译工具链方面, cmake/Make/gcc/g++/这些工具都是必备的, 甚至检测依赖时候显示`FFmpeg`和`clang-format`也是需要的, 相当繁琐. 

当然在这之中也学到了一些Linux下(实际上Cygwin就是一个win下的Linux模拟环境)实际编译大型项目的一些经验吧, 当时(2013)可能最好的win下Linux模拟器就是Cygwin了, 现在来看, 还是wsl/wsl2更胜一筹, 不过对于这种并行计算软件, 不知道用子系统能不能最大化利用计算资源呢?

---

首先就是编译安装LAMMPS, 参考了:

1.   [8.6.4. Using LAMMPS on Windows 10 with WSL — LAMMPS documentation](https://docs.lammps.org/Howto_wsl.html#download-lammps);(不过这里我仍然使用的是Cygwin, 而不是wsl, 事实证明还是wsl香)

     >   下载LAMMPS源码这里需要注意, 我直接采用了option1的方法, 使用2020版的源码, 后来实测可以使用, 但是如果要安装最新的2022版, 会有一些C库函数的问题(目前在Cygwin下还未解决). 

2.   [Can we use OpenMpi on Docker Container? · Issue #3625 · open-mpi/ompi (github.com)](https://github.com/open-mpi/ompi/issues/3625#issuecomment-305782099);(修复了一个关于ssh的问题, 主要报错如下)

     >   The value of the MCA parameter "plm_rsh_agent" was set to a path
     >   that could not be found:
     >
     >   plm_rsh_agent: ssh : rsh
     >
     >   Please either unset the parameter, or check that the path is correct







# 准备工作: cygwin

首先就是下载Cygwin了, 官网[setup-x86_64.exe (cygwin.com)](https://www.cygwin.com/setup-x86_64.exe)就有, 双击安装包之后, 前面的全部默认即可, 之后的话遇到是否选择代理, 就选直接连接(direct connection)即可. 

然后就是选择镜像, 选aliyun的就行(很快), 然后选要安装的包, 这里的话安装的包我都列在下面. 

!!注意!!: 一开始默认是`Pending`, 这时候搜不到全部包, 需要在第一个下拉菜单中选择full, 然后搜索包名称才行. 

>   -   make (源码构建工具)
>   -   cmake (比make智能/简单的源码构建工具)
>   -   git (代码管理工具)
>   -   gcc-core (c编译器)
>   -   gcc-g++ (C++编译器)
>   -   openssh (ssh服务器/客户端)
>   -   openmpi (并行计算要用)
>   -   wget (下载器)
>   -   binutils (二进制文件构建工具包)
>   -   bzip2 (压缩/解压工具)
>   -   tar (压缩/解压工具)
>   -   git-clang-format (代码格式化工具, 以及clang编译器)
>   -   vim (命令行编辑器)

安装的话, 只需要将`Keep`改成对应的版本即可(这里建议都选择最新版(下拉列表的最后一行)), 





# 安装LAMMPS



## 下载源码

上面也提到了, 这里使用的是2020版, 可能有些旧, 但是却是可以在Cygwin下运行的LAMMPS版本(实际上也就是能在Windows下运行的版本了, 而且可以安装voro扩展)

```bash
wget https://github.com/lammps/lammps/archive/stable_3Mar2020.tar.gz
tar xvzf stable_3Mar2020.tar.gz
cd lammps
```



>   使用GitHub发布的2022最新版, 会出现问题. 具体原因是2022版LAMMPS源码使用了一些POSIX的扩展C函数, 例如`posix_memalign`, 还有很多非ANSI C的库函数, 所以有条件还是上Linux双系统吧...

然后新建一个构建目录:

```bash
mkdir build
cd build
```



## cmake

参数`-D LAMMPS_MACHINE=mpi`指的是是否开启并行计算(mpi支持)

```bash
cmake -D LAMMPS_MACHINE=mpi -D PKG_MANYBODY=on -D PKG_MOLECULE=on -D PKG_VORONOI=on ../cmake
```

>   `-D PKG_包名称=on`这个指的就是在编译安装LAMMPS时候需要的额外可选包, 更多信息可参考文档:
>
>   [8.6.4. Using LAMMPS on Windows 10 with WSL — LAMMPS documentation](https://docs.lammps.org/Build_extras.html#voronoi-package);

这里可能会有个小问题, cmake会出现:

```c
CMake Error: Could not find CMAKE_ROOT !!!
CMake has most likely not been installed correctly.
Modules directory not found
```

于是, 参考了[14.04 - CMake Error: Could not find CMAKE_ROOT? - Ask Ubuntu](https://askubuntu.com/questions/1014670/cmake-error-could-not-find-cmake-root);

解决方案:

```bash
vi ~/.bashrc
# 加上:
export CMAKE_ROOT="/usr/share/cmake-3.23.2/"
```

这个版本要看实际安装的cmake版本, 不加这个环境变量的话会有问题. 

## make

最后的构建: 8代表使用8核跑满, 如果没有8核就改成4或者其他

```bash
make -j 8
make install 
```



## 后续工作: 环境变量



这时候就完整安装了, 如果你进入build目录, 就会发现有`lmp.exe`可执行文件, 但是, 双击之后并不会出现内容, 而是提示一些Cygwin的dll文件找不到, 不要慌, **在Windows系统下**, 为Cygwin/bin目录加上环境变量再说:

```c
C:\cygwin64\bin
```

然后就是cygwin的环境变量:

```bash
# vi ~/.bashrc
export PATH="/home/Administrator/.local/bin/:$PATH"
```



# 安装voro++

## 下载源码

```bash
wget https://math.lbl.gov/voro++/download/dir/voro++-0.4.6.tar.gz
tar zxfv voro++-0.4.6.tar.gz
cd voro++-0.4.6
```

## 编译安装

```bash
make
sudo make install
```





## 重新编译LAMMPS

```bash
# 进入到lammps文件夹中lib/voronoi目录，更改Makefile.lammps:
voronoi SYSINC = -I/usr/local/include/voro++
voronoi SYSLIB = -lvoro++
voronoi SYSPATH = -L/usr/local/lib
```



编译:

```bash
# 进入lammps文件夹中src目录：
make yes-voronoi
sudo make voro -j 4 #视个人情況编译
```



# 后记

后来发现, 采用cygwin在Windows上安装LAMMPS的话, 并不是最佳的方案, cygwin只是一个在LAMMPS上安装voro++补充包的一种方法, 并不能对LAMMPS的并行计算起到支持, 所以还是老老实实wsl. (毕竟是LAMMPS官方推荐的方法)

对于这部分内容, 可以参考:

[8.6.4. Using LAMMPS on Windows 10 with WSL — LAMMPS documentation](https://docs.lammps.org/Howto_wsl.html)

然后, 就是熟悉的Ubuntu环节了. 

