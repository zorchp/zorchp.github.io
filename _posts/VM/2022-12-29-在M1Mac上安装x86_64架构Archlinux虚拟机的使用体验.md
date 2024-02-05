---
categories: [Tips]
tags: MacOS Linux Tips
---

# 写在前面

在M1(ARM64)Mac上使用Intel架构的Archlinux也有一段时间了,  总的来说还是不错的, 毕竟我这8+256的小电脑都能带得动, 虽然跟原生的架构相比速度肯定略慢, 但是日常写个汇编, 写个C还是相当足够了, 下面谈谈我的主要配置, 以及使用的一些体验~
<!--more-->
下面是我的物理机配置与虚拟机配置:

```lua
 ==> neofetch                                                        [21:13:29]
                    'c.          hep@hep
                 ,xNMM.          -------
               .OMMMMo           OS: macOS 12.5.1 21G83 arm64
               OMMM0,            Host: MacBookAir10,1
     .;loddo:' loolloddol;.      Kernel: 21.6.0
   cKMMMMMMMMMMNWMMMMMMMMMM0:    Uptime: 28 days, 15 mins
 .KMMMMMMMMMMMMMMMMMMMMMMMWd.    Packages: 335 (brew)
 XMMMMMMMMMMMMMMMMMMMMMMMX.      Shell: zsh 5.8.1
;MMMMMMMMMMMMMMMMMMMMMMMM:       Resolution: 1440x900
:MMMMMMMMMMMMMMMMMMMMMMMM:       DE: Aqua
.MMMMMMMMMMMMMMMMMMMMMMMMX.      WM: Rectangle
 kMMMMMMMMMMMMMMMMMMMMMMMMWd.    Terminal: iTerm2
 .XMMMMMMMMMMMMMMMMMMMMMMMMMMk   Terminal Font: FiraCodeRoman-Regular 16
  .XMMMMMMMMMMMMMMMMMMMMMMMMK.   CPU: Apple M1
    kMMMMMMMMMMMMMMMMMMMMMMd     GPU: Apple M1
     ;KMMMMMMMWXXWMMMMMMMk.      Memory: 1377MiB / 8192MiB
       .cooc,.    .,coo:.

```

然后是虚拟机Archlinux的配置:

```lua
 >>> neofetch                                                         [5:11:48]
                   -`                    root@test
                  .o+`                   ---------
                 `ooo/                   OS: Arch Linux x86_64
                `+oooo:                  Host: KVM/QEMU (Standard PC (Q35 + ICH
               `+oooooo:                 Kernel: 5.19.7-arch1-1
               -+oooooo+:                Uptime: 22 mins
             `/:-:++oooo+:               Packages: 249 (pacman)
            `/++++/+++++++:              Shell: zsh 5.9
           `/++++++++++++++:             Resolution: 1280x800
          `/+++ooooooooooooo/`           Terminal: /dev/pts/1
         ./ooosssso++osssssso+`          CPU: QEMU Virtual version 2.5+ (3) @ 9
        .oossssso-````/ossssss+`         GPU: 00:01.0 Red Hat, Inc. Virtio GPU
       -osssssso.      :ssssssso.        Memory: 145MiB / 2913MiB
      :osssssss/        osssso+++.
     /ossssssss/        +ssssooo/-
   `/ossssso+/:-        -:/+osssso+-
  `+sso+:-`                 `.-/+oso:
 `++:.                           `-/+/
 .`                                 `/

```



# 我的配置

## 编辑器:VIM

由于安装的是纯命令行界面, 想使用现代的IDE是不可能了( 有条件的大内存MAC其实可以装KDE桌面), 并且虽然使用了X11, 其支持的编辑器还是很难受, 最后还是决定使用vim, 精进一下VIM技巧. 

虽然我是一个忠实的Sublime用户, 但是最近也逐渐转入VIM阵营了, 因为Sublime的纯命令行支持真的很差, 动不动插件就出问题了, 配置起来还比较麻烦. (虽然速度上确实没的说, 跟VSCode比起来简直不要再轻量.)

下面是一个VIM界面, 其实我只做了最基本的配置, 也参考了一些网上的博客, 主要是一个括号补全的插件和clang-format插件, 



## git支持





## shell:zsh与相关插件(无主题)







## X11配置:图形界面与SSH









# 使用体验



## 优势

### x86_64架构的完美模拟

跑Intel汇编, 或者一些简单的TCP Server都不成问题, 也算是弥补了m1芯片的一个缺陷了. 





## 劣势

### 纯命令行(这是不是也算优势呢)





### 速度较慢

所以像`oh-my-zsh`这样的主题配置插件(framework其实更加贴切) 根本不能安, 安上之后速度肉眼可见的慢, 简直影响心情.

后来虽然卸载了omz, 直接用原生的补全插件和高亮插件, 有时候编译之后还是显得有一定的延迟, 我认为内核分配数已经够了(3个), 有条件的话肯定是越大越好, 当然, 这个系统本来就是模拟出来的, 速度慢点也很合理..

总的来说, 为了满足使用M1Mac在x86_64下编程可真的是让我费足了心思, 一开始想到装Windows虚拟机, 奈何内存直接拉满, 温度也是居高不下, 我这8GB怎么够一个Windows折腾呢? 然后还试过用pd(太贵了)装kali, 直到后来遇到了UTM这个神器, 我才找到了门路.. 虽然UTM的引擎用的也是开源的QEMU, 但是奈何自己水平还没达到直接用QEMU手动模拟出一个X86_64的系统出来, 还得借助UTM来做, 不过我已经十分满意了:laughing:~



# 一些注意

1.   建议还是经常对`archlinux.utm`, 也就是虚拟机的镜像文件进行备份, 也不是很大(4GB), 这样可以避免系统因为内核升级而崩溃(之前的Manjaro就给了我教训, 事实就是archlinux比Manjaro还不稳定), 直接传网盘或者U盘本地备份都行.
2.   虚拟机不用了还是要及时`poweroff`掉虚拟机, 这样可以避免Mac主机的电量以及系统资源的消耗, 毕竟在Mac上用了这么多年, 已经养成直接扣盖子走人的习惯了...
3.   有条件的话(内存至少16GB, 内核数至少10+)还是建议用KDE桌面, 我是非常期待archlinux的酷炫桌面的!
4.   