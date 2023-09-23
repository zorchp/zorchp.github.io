---
categories: [Tips]
tags: Tips Sublime
---

# 写在前面

越来越离不开`Sublime Text`(下称`ST`) 这款轻量级跨平台编辑器了, 满足我对轻量化编辑代码的所有要求, 并不像`VSCode`一样臃肿, 内存占用也不大, 但是有一点不太好的就是现在插件市场的插件很多都不维护了, 就导致现在大多数开发者都转向vscode阵营了(我不想做大多数). 

我可是放不下这款超级棒的编辑器的, 不管是刷LeetCode还是写小的测试程序, 都让我觉得非常舒服. 但是最近遇到了一个问题, 就是在ST中写C++时候代码格式化总是不好用, 一开始我用的是一款叫做`CoolFormat`的插件, 但是遇到C++代码总是提示`Cannot format this file`, 网上找到的推荐插件是`SublimeAStyleFormatter`[^2], 据说用来格式化C-like代码都比较好, 并且内置了`astyle`引擎, 可以定制代码段的格式化风格, 具体的话可以看看官网[^1]. 

如果你用的是arm Mac的话, 这里安装之后还得配置一下, 因为这个插件好久不更新了, 对于armMac的支持还没有, 不过看到了issue[^3]中的解决方案, 我成功实现了C++代码的ST代码格式化方法. 

顺带提一下Python和JSON的格式化, 都有对应的插件, 比较方便. 

>   Sublime Text 4: Build 4126
>   MacOS 12.3.1 (arm64)

# C++代码格式化(SublimeAStyleFormatter)

直接调出packageControl(command+shift+P), 输入`insp`进入`Package Install`, 输入包名称即可安装.

之后就是配置在arm Mac中成功运行Astyle:

```bash
❯ cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/SublimeAStyleFormatter/pyastyle/python3/

❯ mkdir _darwin

❯ cd _darwin

❯ touch __init__.py

❯ pip install pyastyle# 这里我用到的Python是Mac中自带的
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Requirement already satisfied: pyastyle in /Users/xxx/Library/Python/3.8/lib/python/site-packages (1.1.5)

❯ which pip
/Users/xxx/Library/Python/3.8/bin//pip

❯ cp /Users/xxx/Library/Python/3.8/lib/python/site-packages/pyastyle.cpython-38-darwin.so pyastyle.so

❯ cd ..
❯ ls
__init__.py       _linux_x86        _local_arch       _win32
_darwin           _linux_x86_64     _macosx_universal _win64
❯ subl __init__.py # 编辑这个文件, 注释掉所有的内容, 加入内容, 修改后如下
```

```python
# try:
#     from ._local_arch.pyastyle import *
#     platform = "Local arch"
# except ImportError:
#     try:
#         from ._linux_x86_64.pyastyle import *
#         platform = "Linux 64 bits"
#     except ImportError:
#         try:
#             from ._linux_x86.pyastyle import *
#             platform = "Linux 32 bits"
#         except ImportError:
#             try:
#                 from ._win64.pyastyle import *
#                 platform = "Windows 64 bits"
#             except ImportError:
#                 try:
#                     from ._win32.pyastyle import *
#                     platform = "Windows 32 bits"
#                 except ImportError:
#                     try:
#                         from ._macosx_universal.pyastyle import *
#                         platform = "MacOS X Universal"
#                     except ImportError:
#                         raise ImportError(
#                             "Could not find a suitable pyastyle binary for your platform and architecture.")

try:
    from ._darwin.pyastyle import *
    platform = "MacOS X Darwin"
except ImportError:
    raise ImportError(
        "Could not find a suitable pyastyle binary for your platform and architecture.")

```



然后重启ST, 打开一个C++文件,可以看到`AstyleFormatter`的`Format`已经可以点击了. 

![截屏2022-07-29 18.30.04](https://s2.loli.net/2022/07/29/so3rHymgipqvElU.jpg)





# 快捷键配置

这里我设置了三个快捷键, 如下: 

其中python的格式化和JSON的格式化分别通过`Anaconda`和`jsFormat`这两个插件完成的. 

```json
{
        "keys": ["super+alt+/"], //format C/C++
        "command": "astyleformat",
        "context": [{
            "key": "astyleformat_is_enabled",
            "operator": "equal",
            "operand": ""
        }]
    }, {
        "keys": ["super+k", "super+f"],
        "command": "astyleformat",
        "args": {
            "selection_only": true
        },
        "context": [{
            "key": "astyleformat_is_enabled",
            "operator": "equal",
            "operand": ""
        }]
    }, {
        "keys": [
            "command+i"
        ],
        "command": "reindent"
    }, {
        "keys": [
            "ctrl+shift+s"
        ],
        "command": "auto_save"
    }, {
        "keys": [
            "super+alt+j" // format json
        ],
        "command": "js_format"
    }, {
        "command": "anaconda_auto_format",
        "keys": ["super+alt+l"], //format python
        "context": [{
            "key": "selector",
            "operator": "equal",
            "operand": "source.python"
        }]
    },
```



# Ref

[^1]:[Artistic Style (sourceforge.net)](http://astyle.sourceforge.net/astyle.html);
[^2]:[SublimeAStyleFormatter - Packages - Package Control](https://packagecontrol.io/packages/SublimeAStyleFormatter);

[^3]:[Formatting Not Working - M1 Macs (darwin/arm64) Unsupported · Issue #95 · timonwong/SublimeAStyleFormatter (github.com)](https://github.com/timonwong/SublimeAStyleFormatter/issues/95);