---

---



## 写在前面





## 基本信息

```bash
$ cat /etc/redhat-release
CentOS Stream release 9

$ uname -r
6.12.9-orbstack-00297-gaa9b46293ea3
```





## 安装常用的包

### dev toolchain

```bash
## for gcc-14
sudo yum install epel-release

## optional: for latest gcc
#sudo yum install gcc-toolset-14 gdb

## for gcc(11) llvm and clang
sudo yum install llvm-toolset

# [optional]
# sudo dnf debuginfo-install glibc-2.34-148.el9.x86_64 libgcc-11.5.0-2.el9.x86_64 libstdc++-11.5.0-2.el9.x86_64

## clang-format
sudo yum install python3-pip
$ python -m pip install clang-format autopep8
$ which clang-format
~/.local/bin/clang-format
```

### 编辑器

```bash
$ rpm -qa | grep vim
vim-minimal-8.2.2637-21.el9.x86_64
vim-filesystem-8.2.2637-21.el9.noarch

## 此时只需要安装其他两个即可
$ sudo yum install vim-common vim-enhanced
```



### 其它工具

```bash
sudo yum install which git  ag ctags
```



```c
### git config
$ vi ~/.gitconfig
[user]
	 name = zorch
	 email = zorch@gmail.com

[core]
	quotepath = false
[filter "lfs"]
	required = true
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
	process = git-lfs filter-process
[credential]
	helper = cache
```





### 配置

```bash
## 
alias vb='vi ~/.bashrc'
alias sb='source ~/.bashrc'

export PATH=/opt/rh/gcc-toolset-14/root/bin/:$PATH
```





### gdb调试相关

```
$ sudo su
# cat /proc/sys/kernel/core_pattern
|/usr/lib/systemd/systemd-coredump %P %u %g %s %t %c %h
# echo core-%t > /proc/sys/kernel/core_pattern
```

