---
categories: [Debug]
tags: Emacs debug
---



# 问题

>   环境
>
>   MacOS12 Apple silicon
>
>   emacs-plus 27.2

安装了pylsp之后仍然显示无法找到, 并且已经设置好环境变量. 报错:

```c
Command "pyls" is not present on the path.
Command "pylsp" is not present on the path.
```





# 解决方法

原因分析: 网上很多方法都不凑奏效, 于是我决定从官方文档开始寻找解决方案, 在[^1]这块我发现`List of directories which will be considered to be libraries.`默认参数为`/usr/`, 但是我的pylsp是采用`/opt/homebrew/`安装的, 猜想可能是这个原因, 于是我在配置文件里面进行更改, 

添加

```lisp
(setq lsp-clients-pylsp-library-directories "<pyls dir>")
```

对我的emacs来说, 我添加的目录位于`/opt/homebrew/bin/`, 重启emacs之后打开Python文件, pylsp生效.



# 主要参考

[^1]:官方文档:[Python (Pylsp) - LSP Mode - LSP support for Emacs (emacs-lsp.github.io)](https://emacs-lsp.github.io/lsp-mode/page/lsp-pylsp/#available-configurations);
