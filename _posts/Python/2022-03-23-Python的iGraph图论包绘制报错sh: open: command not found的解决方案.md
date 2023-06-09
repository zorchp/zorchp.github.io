---
categories: [Python]
tags: Python GT Debug
---



# 问题

在macOS中使用Python 的iGraph包进行图的绘制时, 报错`sh: open: command not found`, 这个问题是由于iGraph包通过macOS内置的`open`命令进行图片的打开, 而`open`命令的路径未被读取导致[^1]. 



# 解决

在家目录中(`/Users/XXX/`)新建文件`.igraphrc`, 写入以下内容

```bash
[apps]
image_viewer = /usr/bin/open
```

如果不放心, 可以通过以下命令查找`open`的位置:

```bash
❯ which open
/usr/bin/open
```



# 参考

当然是万能的Stack Overflow:

[^1]:[visualization - Unable to see a plot produced by python igraph in OS X 10.10.2 - Stack Overflow](https://stackoverflow.com/questions/29352713/unable-to-see-a-plot-produced-by-python-igraph-in-os-x-10-10-2);