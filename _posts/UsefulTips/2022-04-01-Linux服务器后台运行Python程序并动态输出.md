---
categories: [Tips]
tags: Linux Tips
---

# 写在前面

室友最近经常通过外部服务器运行深度学习训练程序, 服务器主机当然是基于命令行的Ubuntu, (或者red hat), 但是直接通过xterm运行总会出现`重连之后程序运行中止`的问题, 因为我之前接触过一些简单的Linux shell运维, 在这里通过一个简单的命令搞定了这个问题. 

下面主要在我的Mac上进行测试, 对于Linux可能在命令参数上略有不同, 这个稍后有提及. 

# Mac测试后台运行与实时输出

测试程序(`tail_test.py`)如下, 一秒打印一个数字:

```python
#!/usr/local/bin/python3
from time import sleep


for i in range(10000):
    print(i)
    sleep(1)

```

脚本文件(`test.sh`, 这个名字在 `kill`进程时候还会用到)设置为:

```bash
#!/bin/bash

/usr/local/bin/python3 -u tail_test.py 

```

这时候需要先给脚本添加权限:

```bash
chmod 755 test.sh
```



使用的后台运行命令:

```bash
nohup ./test.sh > ret.txt 2>&1 &
```

这时候会给出进程号:

```bash
❯ nohup ./test.sh > ret.txt 2>&1 &
[1] 12889

```

完全退出终端, 再次进入, 通过下面的命令可以看出执行结果最新的几行.

```bash
❯ tail -f ret.txt
61
62
63
64
65
66
67
68
69
```



退出程序的话可以通过:

```bash
❯ ps aux|grep test
xxx              15454   0.0  0.0 408628368   1616 s000  S+    9:36上午   0:00.00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn --exclude-dir=.idea --exclude-dir=.tox test
xxx              12890   0.0  0.1 408865488   7984   ??  SN    9:33上午   0:00.06 /Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/Resources/Python.app/Contents/MacOS/Python -u tail_test.py
xxx              12889   0.0  0.0 408628896   2000   ??  SN    9:33上午   0:00.00 /bin/bash ./test.sh
❯ kill -9 12889
❯ kill -9 12890
```

这时候看后台, `test.sh`已经终止了.

# 关于命令的几点解释

这里面主要采用了`Python`的命令行执行参数[^2], `-u`, 细心的话在PyCharm运行Python文件时候应该可以发现这个参数, 就是动态刷新输出(不使用缓存)并显示. 

然后是`nohup`命令[^1], 不挂起运行命令. 可以在后台运行,

>   ### 语法格式
>
>   ```
>    nohup Command [ Arg … ] [　& ]
>   ```
>
>   ### 参数说明：
>
>   **Command**：要执行的命令。
>
>   **Arg**：一些参数，可以指定输出文件。
>
>   **&**：让命令在后台执行，终端退出后命令仍旧执行。

最后就是`2>&1`了,将标准错误重定向到标准输出. 



# 2022.4.6更新(使用tmux终端复用神器)

上面提到的使用`nohup`命令的方法有一些弊端: 

1.   命令繁杂, 对初学者不太友好, 需要记住很多文件的位置(bash脚本, 以及Python执行文件), 当然 直接写在一行上不需要shell脚本也可以, 但是并不方便之后的维护.
2.   输出的内容可能非常多, 这就导致最后的结果文档可能会非常大. 一个例子就是深度学习模型训练过程中, 因为epoch的增加导致的冗杂输出结果的增加, 打开最终的一个结果文档可能要花很长时间(这还是在确定电脑ram足够大的前提下).
3.   后台管理比较麻烦. 如果需要中断程序的运行, 需要查询进程号并且杀死进程, 操作起来比较麻烦, 而且通过bash脚本运行Python文件的话,系统会同时开启两个人进程, `Python`和`sh`, 这两个进程号连续的进程需要都被杀死才能终止正在运行的程序. 



由于上面几点, 有位同学找到了更好的解决方案, 那就是终端复用器`tmux`, 这个东西可以在后台执行终端, 相当于开启了一个新的会话, 这样的话就算关闭了ssh连接, 也能通过简单的命令找回之前的会话, 简单的两行命令就可以解决[^3].

```bash
# 新建会话, 在这里面输入要运行的命令, 默认的会话窗口标记为0
tmux
# 找回名称为0的会话
tmux attach -t 0

```







# 参考

[^1]:[Linux nohup 命令 | 菜鸟教程 (runoob.com)](https://www.runoob.com/linux/linux-comm-nohup.html);
[^2]:[解析python 命令的-u参数_wonengguwozai的博客-CSDN博客_python-u](https://blog.csdn.net/wonengguwozai/article/details/81668240);
[^3]:[Tmux 使用教程 - 阮一峰的网络日志 (ruanyifeng.com)](https://www.ruanyifeng.com/blog/2019/10/tmux.html);