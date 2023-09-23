---
categories: [Python]
tags: Python glob
---



# 写在前面

补一补之前就想写的关于`glob`库(Filename globbing utility, Unix style pathname pattern expansion, 类Unix路径名模式扩展)的使用, 有了这个库, 通过Python读取文件(主要是递归方式读取), 就再也不用`os.walk()`那样复杂了, 虽然可定制性提高了, 代码的复杂度也上去了, 通常是记不住代码还要重新去找. 



简单介绍一下`glob`, 其实就是`os`库的一个封装, 不过完美的支持了正则表达式语法, 这次先简单介绍一下库的用法, 之后有时间可以深入剖析一下这个库实现的源码. 



# 基本操作

这个库主要有三个方法, 分别是:

```python
In [2]: import glob

In [3]: glob.__all__
Out[3]: ['glob', 'iglob', 'escape']
```



主要使用的是第一个方法`glob`, 用来读取文件(目录), 之后的两个分别是返回生成器和忽略特殊字符匹配(取消正则表达式语法支持). 这里着重介绍第一种.(测试案例使用了官方文档[^1]的例子)



```python
import glob

# 同级目录执行: 
# touch 1.gif 2.txt card.gif

g1 = glob.glob(pathname='./*.gif')
# print(g1)
# # ['./1.gif', './card.gif']

g2 = glob.glob('./[0-9].*')
# print(g2)
# # ['./1.gif', './2.txt']

g3 = glob.glob('./?.gif')
# print(g3)  # ['./1.gif']
```



# 读取任意路径

之后是一些我自己的例子:

```python
.
└── glob_test
    ├── 1.gif
    ├── 2.txt
    ├── card.gif
    └── glob_1.py # 这个是测试的代码文件
```



```python
import os
import glob


# 在当前目录的上一级目录中创建文件夹decorator,里面有三个文件:
# decorator1.py
# decorator2.py
# test1.py
g4 = glob.glob('./../decorator/*.py')
for i in g4:
    print("#", "*" * 70)
    print(os.path.abspath(i))
    print("#", "*" * 70)
    with open(i, 'r') as f:
        print("文件中的字符数:", len(f.read()))
        print()
'''结果:
# **********************************************************************
/Users/hep/code/py_Proj/grammar-py/decorator/decorator1.py
# **********************************************************************
文件中的字符数: 210

# **********************************************************************
/Users/hep/code/py_Proj/grammar-py/decorator/test1.py
# **********************************************************************
文件中的字符数: 197

# **********************************************************************
/Users/hep/code/py_Proj/grammar-py/decorator/decorator2.py
# **********************************************************************
文件中的字符数: 837

'''
```

那么, 读取任意路径下的任意文件(通过正则表达式), 使用`glob`就不在话下啦~

>    不过需要注意在Windows之中用的话相对路径虽然可以写成`./`的形式, 但是路径字符串分割的时候还是要用`\\`. 否则会出现一些问题. 



这里再介绍一种操作, 就是参数`recursive=True`, 下面是另一个例子:

需要在`decorator`文件夹下创建一个`test`文件夹,然后里面创建几个`.py`文件.

```python
.
├── decorator
│   ├── decorator1.py
│   ├── decorator2.py
│   ├── test
│   │   └── aa.py
│   └── test1.py
└── glob_test
    ├── 1.gif
    ├── 2.txt
    ├── card.gif
    └── glob_1.py # 这个是测试的代码文件
```



```python
g5 = glob.glob('./../decorator/**/*.py', recursive=True)
for i in g5:
    print("#", "*" * 70)
    print(os.path.abspath(i))
    print("#", "*" * 70)
    with open(i, 'r') as f:
        print("文件中的字符数:", len(f.read()))
        print()

'''结果:
# **********************************************************************
/Users/xxx/code/py_Proj/grammar-py/decorator/decorator1.py
# **********************************************************************
文件中的字符数: 210

# **********************************************************************
/Users/xxx/code/py_Proj/grammar-py/decorator/test1.py
# **********************************************************************
文件中的字符数: 197

# **********************************************************************
/Users/xxx/code/py_Proj/grammar-py/decorator/decorator2.py
# **********************************************************************
文件中的字符数: 837

# **********************************************************************
/Users/xxx/code/py_Proj/grammar-py/decorator/test/aa.py
# **********************************************************************
文件中的字符数: 10


'''
```

如果不加参数的话, 就不能递归遍历, 导致没法读取子文件夹下的文件. 



# 参考

[^1]: [glob — Unix style pathname pattern expansion — Python 3.10.4 documentation](https://docs.python.org/3/library/glob.html?highlight=glob#module-glob);