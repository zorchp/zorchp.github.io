---
categories: [LaTeX]
tags: MacOS LaTeX Tips
---

# 写在前面

最近接触到一款不错的$\TeX$发行版的附带工具, 名为`latexdiff`, 作用的话顾名思义, 就像在`Unix/Linux`系统中的`diff`和`vimdiff`一样, 用来检查文件的变化并作出标记, 当然这里因为带有了`latex`, 所以当然也有了一点$\LaTeX$的风格, 就是通过$\LaTeX$来标记修改过的文档, 用起来是很方便好用的.



# 使用方法-以vscode为例

>   环境:
>   MacOS12.3.1 M1
>   MacTeX2022
>   VSCode1.67.1

这里简单介绍一下`latexdiff`的使用方法, 通过在vscode中的简单配置, 就能得到需要的标记文档啦. 前提是已经安装了`TeXLive`(Windows)以及`MacTeX`(macOS), 并且已经正确配置好了vscode的`LaTeXWorkshop`.

首先当然需要在vscode中打开文件夹, 并且调出相应路径的终端, 如下所示:

<img src="https://s2.loli.net/2022/05/12/vHQbd1lBEuOVatf.png"/>

打开终端之后, 就可以通过`latexdiff`命令进行标注文件的生成了, 下面是针对上面例子的生成命令, 如果文件名过长的话, 可以通过`TAB`键进行补全, 这里需要注意的是: 

-   `>`这个符号两边的空格不能丢; 
-   文件名需要写全名而不是只有前面的部分而没有后缀; 
-   文件名中如果包含空格, 需要采用转义字符, 例如文件`test 1.tex`在终端中需要写成`test\ 1.tex`, 这也可以通过`TAB`补全实现; 
-   其中`diff.tex`这个文件名可以任意更改. 

```bash
latexdiff test1.tex new.tex > diff.tex
```

<img src="https://s2.loli.net/2022/05/12/Z2whMouqdImHWek.png"/>

如果命令执行之后**没输出任何东西**, 那么说明生成成功了, 可以运行(编译)试试. 得到的结果如下:

<img src="https://s2.loli.net/2022/05/12/p7aqXx5QI4olyTP.png"/>

