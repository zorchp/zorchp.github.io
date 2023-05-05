---
categories: [LaTeX]
tags: Windows LaTeX Debug Tips
---

# 问题与解决

安装字体simsun之后, 在$\LaTeX$文中写:

```latex
\setCJKmainfont{simsun}
```

显示没法找到字体, 如果安装之后还是找不到, 大概率是字体名称不对的问题, 通过

```bash
fc-list :lang=zh-cn
```

查找字体, 然后看看字体名称是什么:

```bash
SimSun
```

这就对了.(这里面的输出可能会有乱码, 不重要, 找字体英文名称即可)

同理还有:

```bash
SimHei
```

当然, 前提是`win+R`运行框输入`fonts`跳转到的文件夹中有要导入的字体, 如果没有需要安装, 安装的话需要`为所有用户安装`, 否则还是找不到. 

备选方案:(终端`cmd`或`powershell`管理员模式下运行)

```bash
fc-cache -rv
```

刷新字体缓存.