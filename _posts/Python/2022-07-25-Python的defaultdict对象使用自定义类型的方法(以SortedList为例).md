---
categories: [Python]
tags: Python 
---

# 写在前面

>   最近写周赛题, 逃不开的一种题型是设计数据结构, 也就是第三题, 做这种题需要的就是对语言中的容器以及常用排序查找算法的掌握, 而我只熟悉了最基本的一些方法, 做起这些题来总是超时...

为了搞定这些题, 我决定学习一下大佬们的做法, 特别是优先队列的方法维护有序容器以及有序列表等容器, 这些都在`Python`中封装好了, 用起来很是方便, 但是采用`defaultdict`的时候, 其缺省数据类型常常需要与题目给出的特定结构匹配, 这就需要定义一个新的数据类型, 下面我就以一种十分常用的结构`SortedList`为例, 设置自定义的数据类型(本例为将默认的升序列表变成降序列表). 

其他的数据结构当然也可以根据下面列出的方法来改, 主要知识点就是函数与类的运用了. 这里我参考了Stack Overflow的一个回答[^1], 可以举一反三. 

# 第一种方法: 封装成函数

首先导入需要的函数, 其中`neg`方法可以用`lambda x: -x`代替, 本质上是一样的, 下面写的代码这两种均可.

```python
from collections import defaultdict
from sortedcontainers import (SortedList as SL, SortedKeyList as SKL)
from operator import neg  # or `lambda x: -x`
```

然后我们来看第一种方法, 其实封装成函数本质上就是将自定义对象作为函数返回值, 下面给出两种实现, 其实不传入参数也可以, 但是这样的话下面的第`15`行就不能使用了, 只能通过`add()`来添加值, 还是有局限的.

代码中的`d2`直接用一个新的`lambda`函数, 定义键, 就不需要考虑直接初始化失效的情况.

```python
def reverseSL(x=None):
    return SL(iterable=x, key=lambda x: -x)

def reverseSL1_no_args():
    return SL(key=lambda x: -x)

d1 = defaultdict(reverseSL)
d2 = defaultdict(lambda: SL(key=neg))

data = [3, 2, 4, 1]
for i in data:
    d1[1].add(i)
    d2[1].add(i)
# 也可以直接加入排序列表
d1[2] = reverseSL([1, 2])
d2[2] = reverseSL([1, 2])
print(d1)
print(d2)

```

可以得到如下的结果:

```lua
defaultdict(<function reverseSL at 0x100a680d0>, {1: SortedKeyList([4, 3, 2, 1], key=<function reverseSL.<locals>.<lambda> at 0x100c659d0>), 2: SortedKeyList([2, 1], key=<function reverseSL.<locals>.<lambda> at 0x100caa550>)})
defaultdict(<function <lambda> at 0x100c65820>, {1: SortedKeyList([4, 3, 2, 1], key=<built-in function neg>), 2: SortedKeyList([2, 1], key=<function reverseSL.<locals>.<lambda> at 0x100cb9940>)})
[Finished in 214ms]
```

如果第`15`行改为:

```python
d1[2] = reverseSL_no_args([1, 2])
```

就会提示:`TypeError: reverseSL_no_args() takes 0 positional arguments but 1 was given`, 但是`add()`方法不会有问题.

# 第二种方法: 类封装

这种方法比较复杂, 并且有一个小坑, 这里先看第一个类的代码. 

我这里实现了两个类, 其中`mySL1`采用的是`组合`的面向对象设计方法, `mySL2`用的是`继承`. 第一种代码比较多, 因为里面添加了一个组件`SortedList`, 就需要重写`add()`. 

```python
class mySL1:
    def __init__(self, iterable=None):
        self.sl = SL(iterable=iterable, key=lambda x: -x)

    def add(self, item):
        self.sl.add(item)

    def get(self):
        return list(self.sl)

    def __repr__(self):
        return repr(self.sl)
```

其中的`__repr__`是可选的, 只是为了清楚地显示已加入到`defaultdict`的数据情况. 不写的话还得调用`get()`方法, 进行字典值(`values`)数据的输出, 这里为方便就直接转换为`List`类型了, 如果不转换, 没办法在类外通过`list()`进行转换, 因为这样得到的数据不是可迭代对象, 通过直接输出值的类型, 可以得到`<class '__main__.mySL1'>`. 

---

然后是第二个类, 继承语法简洁明了, 直接调用父类的初始化方法, 但是这**里需要注意的**是, 继承`SortedList`类的代码这里就不能用了, 因为如果还是使用`SortedList`, 在`__init__`中修改`key`就会提示断言错误, `assert key is None`, 这个问题让我比较困惑, 甚至觉得可能继承的方法行不通... 后来查看源码[^2],(下面是模块的`__new__`方法的源码) 我知道了问题的所在. 

>   ```python
>       def __new__(cls, iterable=None, key=None):
>           """Create new sorted list or sorted-key list instance.
>           Optional `key`-function argument will return an instance of subtype
>           :class:`SortedKeyList`.
>           >>> sl = SortedList()
>           >>> isinstance(sl, SortedList)
>           True
>           >>> sl = SortedList(key=lambda x: -x)
>           >>> isinstance(sl, SortedList)
>           True
>           >>> isinstance(sl, SortedKeyList)
>           True
>           :param iterable: initial values (optional)
>           :param key: function used to extract comparison key (optional)
>           :return: sorted list or sorted-key list instance
>           """
>           # pylint: disable=unused-argument
>           if key is None:
>               return object.__new__(cls)
>           else:
>               if cls is SortedList:
>                   return object.__new__(SortedKeyList)
>               else:
>                   raise TypeError('inherit SortedKeyList for key argument')
>   ```

这里模块的作者提供了一个`SortedList`的子类, 叫做`SortedKeyList`, 顾名思义, 就是提供了一种可以写入`key`的类, 这时候继承这个类就不会有问题了.

>   其实在上面的函数调用那块, 就已经有所提示, 输出结果中的类型, 就显示是`SortedKeyList`, 这个类型就是修改了`key`(使得`key is not None`)之后得到的对象. 大家可以尝试一下, 如果不修改`key`, 就还是`SortedList`. 

```python
class mySL2(SKL):
    """use SortedKeyList instead SortedList,
    because SortedList cannot init argument `key`,
    `assert key is None` in its `__init__`"""

    def __init__(self, iterable=None):
        super().__init__(iterable=iterable, key=neg)

```

最后是创建`defaultdict`, 以及数据的读取:

```python
d3 = defaultdict(mySL1)
d4 = defaultdict(mySL2)


for i in [19, 11, 12, 123]:
    d3['x'].add(i)
    d4['y'].add(i)
# 或者直接通过列表初始化
d3['z'] = mySL1([1, 2])
d4['w'] = mySL2([1, 2])

print(d3)
print(d4)
print(d3['x'].get(), d3['z'].get())
print(list(d4['y']), list(d4['w']))
```

可以得到下面的结果:

```lua
defaultdict(<class '__main__.mySL1'>, {'x': SortedKeyList([123, 19, 12, 11], key=<function mySL1.__init__.<locals>.<lambda> at 0x1008e40d0>), 'z': SortedKeyList([2, 1], key=<function mySL1.__init__.<locals>.<lambda> at 0x100bebd30>)})
defaultdict(<class '__main__.mySL2'>, {'y': mySL2([123, 19, 12, 11], key=<built-in function neg>), 'w': mySL2([2, 1], key=<built-in function neg>)})
[123, 19, 12, 11] [2, 1]
[123, 19, 12, 11] [2, 1]
```

可以看出, 第一种类的创建, 其实最后还是用到了`SortedKeyList`这个子类. 

# 参考

[^1]:[python - How to use a specific data structure as the default_factory for a defaultdict? - Stack Overflow](https://stackoverflow.com/questions/31723719/how-to-use-a-specific-data-structure-as-the-default-factory-for-a-defaultdict);
[^2]:[python-sortedcontainers/sortedlist.py at master · grantjenks/python-sortedcontainers (github.com)](https://github.com/grantjenks/python-sortedcontainers/blob/master/sortedcontainers/sortedlist.py);