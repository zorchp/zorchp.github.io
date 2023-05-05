---
categories: [LaTeX]
tags: LaTeX Debug
---

# 问题

最近有同学问我在 Windows 上使用 WinEdt 这款编辑器为什么会提示系统找不到文件, 我搜索一下发现大概率是 $\TeX \rm Live$ 发行版没有正确安装/配置导致的. 

但是令我百思不得其解的就是, 明明成功安装了, 却还是提示有问题, 这就很奇怪了.

>   报错信息:
>   ```lua
>   C:\texlive\2023\bin\windows\runscript.tlu:921: command failed with exit code 1:
>   perl.exe c:\texlive\2023\texmf-dist\scripts\texlive\fmtutil.pl  --user --byfmt xelatex
>   I can't find the format file `xelatex.fmt'!
>   ```



很奇怪, 后来发现原来是在安装了 texlive 之后, 又安装了 WinEdt 导致的...

WinEdt 会修改系统的环境变量, 主要是因为这个编辑器有可能会自带一个 ctex 发行版, 而 ctex 发行版本来就不支持了(除了一些很老的期刊), 这就导致了问题..



# 解决方案

这里参考了

>   [知乎-[LaTeX 发行版] TeX Live 无法使用，uninitialized value $ver](https://zhuanlan.zhihu.com/p/60244068);

里面提到了一个 ctex 论坛的 issue:

>   [issue-comment](https://github.com/CTeX-org/forum/issues/5#issuecomment-451772490);
>
>   解决方法很简单： windows 操作系统的环境变量里添加 PATH：c:\Windows\System32.

或者说, 采用

```lua
%SystemRoot%\System32
```

作为 Path 系统变量也可. 

这里主要是因为 WinEdt 内的 ctex 发行版(其实是一个 miktex 引擎)会覆盖这个环境变量, 导致 texlive 发行版找不到 tex 引擎以及对应的 fmt 文件, 引起了上述的错误.

所以, 加上之后, 就好了...



当然, 如果还报错, 就可以直接 `win+x` 进入管理员终端(Windows11)或者 powershell(Windows10), 然后输入:

```lua
fmtutil-sys --all
```

耐心等待执行完成, 就可以了. 

## 关于 WinEdt

这个编辑器, 其实做科研的朋友们都比较喜欢用的, 符号之类的用起来都很方便, 可惜是付费(需要一些魔法)

由于中文支持不是默认的, 针对这个编辑器就需要改一下 execution mode, 将默认的tex 引擎改成 xelatex 即可(删掉之前的 pdf 改成 xe 就行了)

然后就是 texlive 的路径, 因为之前安装 WinEdt 时候有了 ctex 这个难缠的东西, 还需要把 texlive 的路径放进去, 其他的帮助路径之类的直接诶自动检查即可. 



# 后记-关于 texlive 的安装与卸载

前面一顿操作, 其实就是一个小小的环境变量问题.. 这里顺便说一下 texlive 的安装与卸载. 

## 安装

安装的话, 这里需要注意, 大家之前都是默认 full 安装的, 我觉得时间花费太久了, 就选择 medium 安装, 结果事实就是每次编译不同的模板都会提示有缺失的包, 而 texlive 的 tlmgr 又不会像 miktex 的管理器一样自动下载安装需要的包, 就导致每次都要手动安装, 并且可能缺失的包名称和要安装的包名称并不一样...

为了省事, 占用一些磁盘空间而安装 full 版本的 texlive 还是很有必要的(texlive2023 最新发行版大概占用 8GB)



然后就是安装包时候(如果真的需要安装的话), 那就要用管理员权限进入终端(用 win+x 我觉得是最快的方法)

>   如果提示 gpg 未验证:
>
>   就在终端输入: 
>
>   ```lua
>   tlmgr --repository http://www.preining.info/tlgpg/ install tlgpg
>   ```
>
>   并运行即可

然后需要先更新一下:

```lua
tlmgr --all --self update
```

然后才可以搜索 + 安装:

```lua
tlmgr search --file xxx --global
tlmgr install xxx
```



## 卸载

>   其实直接右键删除是可以的

但是最好不要这样, 在 Windows 下卸载 texlive 发行版, 其实可以运行:

>   [3.6 Uninstalling TeX Live](https://www.tug.org/texlive/doc/texlive-en/texlive-en.html#x1-380003.6);

```lua
tlmgr uninstall --all
```

MacOS 或者 Linux 当然可以用包管理器了(perfect). 

