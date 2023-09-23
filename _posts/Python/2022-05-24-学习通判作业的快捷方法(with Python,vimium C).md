---
categories: [Python]
tags: Python Tips
---

# 写在前面

分享一个在学习通平台判作业比较快的方法, 具体谁需要用呢, 这里就不多说了. 

主要用到了edge浏览器中的`vimium C`全键盘操作插件以及`Python`的`pyAutoGUI`库, 实现了点击的功能.



# 插件的配置

直接在插件商店下载安装就可以了, 这里不多说.

>   后来发现直接用Python脚本作就可以了, `G`键到最下面和`f`超链接跳转的方法稳定性不高.



# PyAutoGUI的安装

```bash
pip install pyautogui
```

这个安装之后就可以用了. 

# 脚本实现

具体的点击代码的话需要根据屏幕的大小来判断, 可以采用下面的脚本选取要点击的点的坐标, 我用的Mac可能不太一样. 

```python
import pyautogui
import time

while True:
    x, y = pyautogui.position()
    print('\r', 'x:' + str(x) + ' y:' + str(y), end='\n')
    time.sleep(0.1)

```

然后就是主要的点击, 一开始我想的是用`vimium C`内置的`f`超链接跳转命令, 但是交的作业是图片还是PDF会导致这个跳转每次都不一样, 这个方法稳定性不高, 之后我想到了每次用`G`翻页到最下面, 然后点击`A`和`提交并进入下一份`, 就可以解决这个问题了.

```python
from pyautogui import click, press
from time import sleep
# sleep(1)


def test():
    click(1039, 489)
    sleep(1)
    press('G')
    sleep(.5)
    click(495, 395)
    sleep(1)
    click(1295, 860G
    #press("f")
    #sleep(.5)
    #press("s")
    #sleep(.5)
    #press("d")
    #sleep(.5)
    #press("f")
    #sleep(.5)
    #press("s")
    #sleep(.5)
    #press("g")
    sleep(1)

for i in range(3):
    test()

```

既然这样,不如直接使用`pyautogui`脚本, 将`G`替换成`end`, 就不需要额外的插件了, 简直方便~

```python
from pyautogui import click, press
from time import sleep


def test():
    click(1039, 489)
    sleep(1)
    press('end')
    sleep(.5)
    click(495, 395)
    sleep(1)
    click(1295, 860)

    sleep(1)

for i in range(3):
    test()

```

