---
categories: [Tips]
tags: GIMP MacOS Tips
---

# 写在前面

在Mac上使用GIMP也有段时间了, 虽然用起来还是一股*理科风*, 但是还是不影响使用, 之前就看过一个介绍`G'MIC`插件的视频, 其中的滤镜效果确实很不错, 但是一直安装失败(可能是m1的原因), 这次看到GIMP更新到了Apple silicon的原生支持: `2.10.32-1版本`, 赶紧来体验一下, 顺便思考了一下如何安装`G'MIC`.



# 更新GIMP

```bash
brew upgrade gimp
```



# 安装G'MIC

这里我试了一下, 把官方[^1](其实是非官方, 因为Mac用户少)给出的插件(在[GitHub](https://github.com/aferrero2707/gimp-plugins-collection/releases))解压到对应目录, 并不能读取出来, 但是官网给出的第二个链接[^2]竟然可以打开G'MIC(其实是一个GIMP的衍生版本, 图标也很类似, 叫做McGimp)

![截屏2022-12-05 16.59.03](https://s2.loli.net/2022/12/05/3OHvm41AjJpXFq5.jpg)

应该是大佬的魔改版, 只不过架构还是Intel, 但是不急, 从他的安装目录下面找到插件目录, 然后把`gmic-qt`复制到GIMP的插件目录下, 就能在GIMP中使用G'MIC滤镜了~

# ref

[^1]:[G'MIC - GREYC's Magic for Image Computing: A Full-Featured Open-Source Framework for Image Processing - Download (gmic.eu)](https://gmic.eu/download.html);
[^2]:[Partha's Place](https://www.partha.com/);