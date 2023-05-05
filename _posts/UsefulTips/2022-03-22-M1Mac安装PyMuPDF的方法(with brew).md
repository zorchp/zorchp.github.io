---
categories: [Tips]
tags: Tips Python
---



# 写在前面

前阶段有人问我如何在M1芯片的macOS上安装`PyMuPDF`这个包, 我的环境是采用`conda`安装的`Python3.9`, 直接采用`pip install fitz`进行安装之后, 虽然成功安装了, 但是导入时候出现了报错, 后来通过github的讨论界面[^1]得到了答案.



# 解决

```bash
pip install fitz
brew install mupdf swig freetype
pip install https://github.com/pymupdf/PyMuPDF/archive/master.tar.gz
pip install frontend
```

这样之后就不会有问题了. 

```c
❯ ipy
Python 3.8.12 | packaged by conda-forge | (default, Oct 12 2021, 21:21:17)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.24.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import fitz

In [2]:
```



[^1]:[Unable to install under M1 Macintosh mode (works in x86/rosetta 2 mode) · Discussion #875 · pymupdf/PyMuPDF (github.com)](https://github.com/pymupdf/PyMuPDF/discussions/875);