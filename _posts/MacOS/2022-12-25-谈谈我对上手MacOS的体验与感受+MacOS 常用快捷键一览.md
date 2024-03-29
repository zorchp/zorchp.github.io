---
categories: [Tips]
tags: MacOS Tips
---



# 写在前面

不知不觉间,我的MacBook Air已经陪伴我走过近两年的时光了, 虽然都说M1芯片是小白鼠, 但是在我的体验中, 除了一些专有软件外, 其他的问题都能得到不错的解决. 这当然要归功于无私奉献的开发者们以及Stack Overflow的热心人们. 

在从零开始配置Mac的时候当然也走了很多弯路, 但是现在我能说在配置Mac的一些开发环境方面也算是驾轻就熟. 

这篇文章中, 我想从以下几点来说说我的选择与体验. 

# 为什么没有继续使用win

开始学计算机, 最先接触的当然是Windows, 随着见识的增长, 其他操作系统才慢慢走进我的视野, 本科时候虽然使用win, 但是还是对Linux系比较感兴趣, 把Linux shell编程研究了个皮毛, 但是Linux(Ubuntu, manjaro, centos虚拟机+双系统都体验过)在win的本子上运行有这样几个问题:

1.   虚拟机的性能不能很好发挥, 例如显卡并行计算, 虽然这不失为一个实践(试错)的好平台.
2.   双系统虽然能得到跟物理机一样的操作体验, 但是对磁盘的读写要求太大, 电池管理也过于糟糕, 发热现象明显(当然,游戏本可能不存在这个问题). 
3.   双系统Linux经常会引发win的蓝屏问题, 虽然之后得到了解决, 但是这种不稳定的状况在开发过程中实在让人头疼. 
4.   自身的不稳定性, 上次更新Linux内核大版本之后, 开机直接卡住不动了, 遇到这样的情况只能重装. 

但是, Linux 的优越性以及进行编程开发时候的便捷高效还是让我十分喜爱的. 在win中编译`tex`文档和在双系统Ubuntu中, Linux速度就要快不少, 而且 Linux 中成熟的包管理系统也能让软件的安装成为一件十分便捷的事情. 

介于以上几点, 我就想找到一种能兼顾win的稳定性与不错的电池管理以及Linux的开发性能的一种系统, 当然, 就是MacOS. 

# MacOS初体验

2021年1月份我拿到了人生中第一台苹果产品, 就是M1MacBook Air, 8+256GB(这个内存配置看起来跟手机一样, 但是苦于没钱). 

刚到手就开始配置各种环境, 因为之前就了解过很多关于`brew`在`Apple silicon`中的配置, 当时还写博客记录了这些配置的具体过程, 还有就是常用的Python环境(通过brew安装了mini-forge), 以及一些`tex`编译软件(`mactex-no-gui`), 都是通过brew安装的, brew真的帮了我大忙. 

软件方面当然也用过一些破解, 这里要感谢`macwk`, 虽然现在已经宕机了. 当然还是支持正版的! 



# 一些我常用的系统级快捷键(文字编辑类)

这里我主要列出了在任何场景下都可以使用的光标移动命令, 这些命令其实是移植自`Emacs`, 或者说Shell终端的快捷键(可能是这样, 毕竟Mac本质就是Unix, FreeBSD, Linus没有与Apple合作). 

>   类似这样的快捷操作使得效率大大提高. 

下面简单列出来, 供大家参考, (甚至在我熟悉了 Vim 的快捷键之后还是会想去使用MacOS自带的这种快捷键)

一些快捷键是我熟悉了Emacs之后知道的, 还有的是我熟悉 iTerm 之后知道的, 其他的参考官网[^1]. 

这里我把`CapsLock` 映射成了 `control`, 因为不管是在`MacOS`系统下, 还是在 `vim` 中, `control` 都是必不可少的. 输入法切换我用了搜狗. (`shift` 切换)

>   其中:
>
>   -   ⌃: 表示`Control` 
>   -   ⌥: 表示`Option`(`Alt`)
>   -   ⌘: 表示`Command`(`Super`)
>   -   🌐: 表示`Fn`(地球仪键)
>   -   ⇧: 表示`Shift` 
>   -   ␣: 表示space, 空格键
>   -   终端: iTerm(iTerm下的快捷键需要配置一下`option`表示`ESC`)
>   -   正文: 比如Typora, Sublime等写作环境
>   -   Backspace, Delete 分别表示Windows中的前删除和后删除, 这里也沿用这一叫法, 而不是像Mac中叫Delete为Backspace.

## 移动类

|  快捷键  |                    记忆                    |                             含义                             |
| :------: | :----------------------------------------: | :----------------------------------------------------------: |
|   ⌃-A    | stArt(或许有点牵强, <br/>容易与Vim的A记混) | 跳到行首, 但是在Word中不要这样用, <br/>会被识别为*全选*(毕竟是MS家的产品) |
|   ⌃-E    |                    End                     |                跳到行尾, 我最喜欢的一个快捷键                |
|   ⌃-P    |                  Previous                  |                          跳到上一行                          |
|   ⌃-N    |                    Next                    |                          跳到下一行                          |
|   ⌃-F    |                  Forward                   |                      跳到下一字符(右移)                      |
|   ⌃-B    |                  Backward                  |                      跳到上一字符(左移)                      |
|   ⌥-F    |                  Forward                   |                  向后逐词移动, 类比Vim的`w`                  |
|   ⌥-B    |                  Backward                  |                  向前逐词移动, 类比Vim的`b`                  |
| ⌘-↑(🌐-←) |                                            |                         跳到文档开头                         |
| ⌘-↓(🌐-→) |                     -                      |                         跳到文档结尾                         |
|   ⌃-O    |                    Open                    |                       光标位置另起一行                       |

一般像逐词移动这种在终端中比较常用, 特别是命令比较长的时候. 

>   并且在正文中使用`Option`会显示特殊字符, 并不会移动光标. 

## 删除类

| 快捷键 |  记忆  |          含义           |
| :----: | :----: | :---------------------: |
|  ⌃-H   |   -    | 左删除, 相当于Backspace |
|  ⌃-D   | Delete |  右删除, 相当于Delete   |
|  ⌃-U   |        | 删除光标到行首(仅终端)  |
|  ⌃-K   |   -    |  删除光标到行尾(普适)   |
|  ⌥-D   | Delete |      后向逐词删除       |
|  ⌃-L   | Clear  | 终端清屏(复位, redraw)  |

前两个常用, 后面的终端常用. 

## 选区类

| 快捷键 |   记忆   |                 含义                 |
| :----: | :------: | :----------------------------------: |
| ⌃-⇧-E  |   End    | 选中光标到行尾的字符(注意快捷键冲突) |
| ⌃-⇧-A  |    -     | 选中光标到行首的字符(注意快捷键冲突) |
| ⌃-⇧-F  | Forward  |        选中光标往前的一个字符        |
| ⌃-⇧-B  | Backward |        选中光标往后的一个字符        |
| ⌃-⇧-N  |   Next   |          选中光标往上的一行          |
| ⌃-⇧-P  | Previous |          选中光标往下的一行          |

## 其他

| 快捷键 |   记忆   |               含义                |
| :----: | :------: | :-------------------------------: |
|  ⌃-C   |   Cut    |          中断命令行执行           |
|  ⌃-D   |    -     |        退出程序或者命令行         |
|  ⌃-Z   |    -     |        挂起(转入后台执行)         |
|  ⌃-T   | Transfer |   交换光标位置的两字符(很实用)    |
|  ⌃-M   |    -     |         相当于回车(ENTER)         |
|  ⌃-I   |    -     |         相当于制表位(TAB)         |
| ⌃-⌘-␣  |    -     | 调出emoji表情选取界面(字符检视器) |



## Unicode支持

一些西班牙文, 德语的字母也可以直接打出来(**原生英文输入法**下):

>   忘了的话可以用虚拟键盘看一下

| 键位(Option+下面的键) | 效果 |
| :-------------------: | :--: |
|           e           |  é   |
|           u           |  ü   |
|           i           |  î   |
|           n           |  ñ   |
|   `` ` ``(backquote)    |  ò   |



# 快捷键之系统操作类

## 访达篇

|   快捷键   |           记忆            |             含义              |
| :--------: | :-----------------------: | :---------------------------: |
|    ⌘-E     |           eject           | 推出可移动设备或者dmg安装镜像 |
|    ⌘-N     |            new            |         新建访达窗口          |
|   ⌘-⇧-N    |            new            | 访达窗口所在目录下新建文件夹  |
|   ⌘-⇧-G    |           goto            |         转到指定目录          |
| ⌘+⇧+.(dot) | `.`开头的是<br />隐藏文件 |  显示/不显示隐藏文件/文件夹   |

## 窗口篇

| 快捷键 |    记忆     |                 含义                 |
| :----: | :---------: | :----------------------------------: |
|  ⌘-H   |    hide     |      隐藏当前app的**所有**窗口       |
|  ⌘-M   |   minimum   |      隐藏当前app的**当前**窗口       |
|  🌐-F   | full-screen | 全屏/取消全屏当前窗口(有的app不支持) |
|        |             |                                      |

## 其他

|   快捷键   | 记忆 |                          含义                           |
| :--------: | :--: | :-----------------------------------------------------: |
|   ⌥-⌘-⎋    |  -   | 强制退出程序, 宕机时候使用, 有点像win的任务管理器(实用) |
|   ⌃-⌘-Q    |  -   |                          锁屏                           |
| ⌘-,(comma) |  -   |        偏好设置(几乎所有应用程序都是这个快捷键)         |
|    🌐-Q     |  -   |   快速打开备忘录, 备忘录会**固定**在桌面, 很方便摘录    |



# 经典小技巧

## 触发角

Windows中习惯了光标移动到屏幕右下角显示桌面, 在MacOS中, 当然不能没有这个操作, 在系统偏好设置->桌面与屏幕保护程序->右下角`触发角`中, 可以设置四个触发角的各种行为. 

## ⌘的妙用

-   按住⌘后可以移动**菜单栏**中的各种图标, 更改排列顺序, 还可以拖拽到远处显示✖️后删除. 



## ⌥的妙用

-   **微调**音量, 按住⌥+⇧后调整音量可以使音量的调整从大格变成¼格. (**亮度同理**)
-   在启动台按住⌥**卸载**从App Store安装的程序, 长按某一个应用程序图标也有类似的效果
-   在程序左上角的**小绿点**位置按住⌥可以**分割**窗格, 控制程序窗口的对齐方式, 光标停留在小绿点上也有类似的效果
-   点一下, 然后按住⌥就会显示**系统信息**, 直接点击即可进入. 
-   按住⌥再点击菜单栏的WiFi/蓝牙图标, 会显示详细信息. 
-   在访达的菜单栏中按住⌥再点`文件`等选项卡, 会有一些不一样的内容. (针对文件的右键操作同理, 一个不错的应用是拷贝路径)

# 后记

持续更新... 

# Ref

[^1]:[Mac 键盘快捷键 - 官方 Apple 支持 (中国)](https://support.apple.com/zh-cn/HT201236);
