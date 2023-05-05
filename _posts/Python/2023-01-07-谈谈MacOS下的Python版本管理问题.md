---
categories: [Python]
tags: MacOS Python Tips 
---

# 写在前面

MacOS上有很多Python, 管理起来可是个麻烦事, 并且一不小心就把包安到系统自带的Python里面了, 加上Python2的历史遗留问题, 让MacOS下的Python版本管理难上加难. 如果凑巧还是homebrew的用户的话, Python又多了一个, 如果不巧电脑又是m1系列芯片的mac, 那么在brew安装时候, 还要安装Rosetta2转译的Python, 这么多的Python是不是头昏眼花了...

>   当然啦, MacOS12.3的发布去掉了MacOS系统自带的Python2.7, 也算是解决了一个老大难问题了. 

下面来说说如何区分MacOS下的Python, 以及如何为指定的Python安装包. 

# 区分Python

以我的电脑为例, 我的电脑是m1芯片的Mac, 系统版本`12.6`, 上面提到的几种Python恰好我都有...

我先列一个我电脑中Python的版本与路径:

|   Python版本   |                         Python路径                         |   支持的架构    | 备注                                                         |
| :------------: | :--------------------------------------------------------: | :-------------: | ------------------------------------------------------------ |
|  `Python2.7`   |                     `/usr/bin/python`                      |        -        | 系统自带的Python2, <br />在MacOS12.3往后就被删除了           |
| `Python3.9.6`  |                     `/usr/bin/python3`                     | `x86_64 arm64e` | 系统自带的Python3, 如果安装了xcode, 那么就是xcode内置的, 如果没安装xcode, 那就是xcode的命令行工具内置的 |
| `Python3.8.9`  |                 `/usr/local/bin/python3.8`                 |    `x86_64`     | Rosetta2转译版brew安装的Python                               |
| `Python3.10.9` |                `/opt/homebrew/bin/python3`                 |     `arm64`     | 本地编译brew安装的Python (原生支持m1)                        |
| `Python3.9.15` | `/opt/homebrew/Caskroom/`<br />`miniforge/base/bin/python` |     `arm64`     | 通过本地编译brew安装的mini-forge中<br />base环境的Python     |
|      ...       |                                                            |                 | 一些额外的conda虚拟环境中的Python这里就不多说了              |

>   一些区分的方法
>
>   1.   查看程序的架构: (一定是绝对路径)
>
>        ```bash
>        lipo -archs /usr/bin/python3
>        ```
>
>   2.   查看MacOS版本: 
>        ```bash
>        sw_vers
>        ```
>
>   3.   查看Python位置:
>        ```bash
>         ==> which python3
>        /opt/homebrew/bin/python3
>        ```
>
>   4.   查看Python版本: 
>
>        ```bash
>        python -V # 或者 `python --version`
>        ```
>
>   5.   查看pip版本及路径: (路径很关键, 类Unix系统中pip安装有两个位置, 分别是家目录和系统目录)
>
>        ```bash
>        pip -V # pip --version
>        ```
>
>        对于系统级的Python, 上面的命令查看的是第三方包的安装位置, 然而一些内置的包路径并不在上述目录中, 这里给出一种方法, 就是关于查看内置包的路径的:
>
>        ```bash
>        # 进入Python
>         ==> /usr/bin/python3
>        Python 3.9.6 (default, Sep 26 2022, 11:37:49)
>        [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
>        Type "help", "copyright", "credits" or "license" for more information.
>        >>> import os
>        >>> os.__file__
>        '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/os.py'
>        >>>
>        ```

# 指定Python的第三方包安装

这里我推荐使用`mini-forge`的虚拟环境(就是一个最小化的conda环境)作为Python的主要运行环境, 因为brew安装的Python版本更新很快, 不是一个稳定的环境, 系统自带的Python也会随着xcode的更新或者系统的更新而改变, 所以最好不要用来做Python的实际运行环境. 

>   (当然, 一些小的实例代码, 不依赖三方库的Python代码都是可以随便挑一个Python解释器运行的, 没有问题)

针对终端下默认的Python, 我现在是用了`/opt/homebrew/bin/python3`这个, 所以就要导入环境变量:

```bash
export PATH="/opt/homebrew/bin/:$PATH"
```

不过直接用系统自带也可以的. 

在安装第三方包的时候, 不要直接开始用pip, 先看一下pip的位置:

```bash
 ==> which pip
/opt/homebrew/bin/pip
```

我更喜欢用`python -m pip install xxx`的方式, 不用考虑安装位置不对的问题. 

当然了, 用Conda就更方便了(虽然少数包只能通过pip来安装)

```bash
conda activate xxx
conda install xxx
```

这里有一个小Tip, 可以在`~/.zshrc`文件中写入:

```bash
alias py39="conda activate py39"
alias dea="conda deactivate"
```

>   然后保存好之后执行`source ~/.zshrc`让更改生效. 

这就相当于给`py39`这个虚拟环境的激活和取消激活做了一个别名(快捷命令), 用起来更方便.

