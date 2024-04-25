---
categories: [Python]
tags: Python MacOS
---

## 写在前面

最近想编辑个 PDF 的书签, 因为都是同级缩进, 不美观. 但是用了 acrobat Pro 之后还是不行, 提示

```
The document could not be saved. There was a problem reading this document (109).
```

搜了半天发现好像是 PDF 文件的问题, 所以用 acrobat 是不行了, 想想别的方法. 看到一篇文章用了 pymupdf, 试试. 

[python:修改pdf的书签 - 沈钩 - 博客园](https://www.cnblogs.com/shengou/p/16931826.html);

>   收回之前文章的话, pymupdf 最新版 1.24.2 支持 arm 的, 之前不知道是怎么的安装失败了, 这次直接在 conda 的 python3.10 里面就安装好了. 

## 使用

首先导出 PDF 的书签列表

```python
import fitz


doc = fitz.open("input.pdf")
toc = doc.get_toc()
print(toc)
print(type(toc)) #list
```

直接改缩进级别为 2:

```python
for i in toc:
    if i[1][0].isdigit():
        i[0] = 2
```

写入

```python
doc.set_toc(toc)
doc.saveIncr()
```

此时就解决问题了..

