---
categories: [Python]
tags: Python Debug
---

# 一个问题

最近刷力扣,想试试 Python 新支持的海象操作符, 其实就是能在语句中赋值, 类似下面这样:

```python
if (n:=len(nums)):
    return False
```

但是当出现下面这种情况的时候, 赋值就会失败:

```python
if True or (a:=1):
    print(a)
'''
NameError: name 'a' is not defined
'''
```

出现这个错误的原因就是 Python 中`and`和`or`的优先级问题, 当语句中先出现`or`的时候, 如果`or`前面的值为`True`, 那这个语句就判断为真,而不会进行之后的判断了, 所以后面的赋值就不会执行.
那么问题来了, 当一条判断语句中同时出现`and` 和`or`, 这时候其优先级是如何呢?
根据以往的经验, `and`要比`or`的优先级高, 然后`not`的优先级又要比`and`高.(但是一般为保险起见,还是在具有`and`操作符的两端加上小括号)

下面我引用了一段博客上看到的内容, 大家可以参考这篇文章,([Python and or not 优先级](https://blog.csdn.net/m0_51284422/article/details/109441190)) 写的非常详细了.

> - not：如果 x 是假的，则“非假”为真，否则 x 是真的，则非真为假
> - and: 找到并返回第一个 False(假)或最后一个 True(真)
> - or: 找到并返回第一个 True(真)或最后一个 False(假)

