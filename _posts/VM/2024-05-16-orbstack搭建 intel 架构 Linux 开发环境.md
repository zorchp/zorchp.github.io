---

---

## 写在前面

体验下来就一个字: 快!

而且无缝衔接(seamless)很舒服, benchmark 显示跟之前的 lima 虚拟机+rosetta转译执行的nerdctl 的 Linux 的 benchmark差不多. 

个人版是 free 的, 给 30 天的商业版试用, 30 天之后变成个人版, 没啥区别. 

## 配置amd开发环境

先装个 Ubuntu, 勾选 intel , 默认采用 Rosetta 转译执行. 

安装一些包:

```bash
sudo apt install gcc g++ gdb nasm man make neofetch llvm lldb clang gcc-multilib
```



这样就能愉快地在arm 的 MacOS写x64汇编了(但是 avx 不支持). 

## 遇到的问题

1.   gdb/lldb 都不能正常运行, 感觉还是 Rosetta 的锅, 看 issue 有用 vscode 的封装实现 debug 的, 但是感觉太麻烦了. 
     ```c
     warning: linux_ptrace_test_ret_to_nx: Cannot PTRACE_GETREGS: Input/output error
     warning: linux_ptrace_test_ret_to_nx: PC 0x9ffffe9a0 is neither near return address 0x7ffffffc2000 nor is the return instruction 0x5555559815f1!
     Couldn't get CS register: Input/output error.
     ```

     更新: 看文档[Linux machines · OrbStack Docs](https://docs.orbstack.dev/machines/#debugging-with-gdb-lldb); 提到了使用 qemu 以及远程调试就可以了
     
2.   

3.   



## 配置 arm 开发环境

由于 MacOS 没法直接安装 gnu-as, 这里再创建一个 arm 的 Ubuntu, 使用起来也是很方便, 而且调试之类的也不在话下



```bash
sudo apt install gcc g++ gdb man make
```

as就包含在 binutils 里面, 所以安装了之后已经含有了

```c
$ as -v
GNU assembler version 2.41 (aarch64-linux-gnu) using BFD version (GNU Binutils for Ubuntu) 2.41
```

