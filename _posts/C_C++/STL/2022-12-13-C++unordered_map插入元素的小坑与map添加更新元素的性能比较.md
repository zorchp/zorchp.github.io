---
categories: [C_C++]
tags: C++ STL
---

# 坑

来看这样一个例子:

```cpp
#include <iostream>
#include <unordered_map>
using namespace std;

void t1() {
    unordered_map<int, int> m1{};
    for (auto &i : {1, 2, 3, 1}) m1[i]++;
    cout << "m1[4]=" << m1[4] << endl;
    cout << "m1.count(4)=" << m1.count(4) << endl;
    for (auto &[k, v] : m1) cout << k << " : " << v << endl;
}


int main(int argc, char const *argv[]) {
    t1();
    return 0;
}
/*
m1[4]=0
m1.count(4)=1
4 : 0
3 : 1
2 : 1
1 : 2
*/
```

默认的`m1[4]`当然是`0`没错, 但是奇怪的是只是输出了一下, 就不知不觉给map中输入了一个键值对, 还是非常离谱的. 

# 补充

后来拜读了*effective STL*一书, 才算是理解了为什么无序列表会是这样.

>   参考: 第24条, 当效率至关重要时, 请在`map::operator[]`与`map::insert`之间谨慎做出选择.
>
>   当然, 也适用于`unordered_map`. 

## 用于更新元素`operator[]`

重载的`[]`取值运算符的作用是`添加和更新元素`, 也就是说对于

```cpp
map<k, v> m;
```

表达式`m[k]=v`(也等价于`m.operator[](k)=v`)会首先检查键`k`在不在`map`中, 

-   如果不在就被加入, 并以`v`作为相应的值;
-   如果在, 则与之关联的值被更新为`v`.

具体来说, `operator[]`返回的是引用, 指向与`k`相关联的值对象, 然后`v`被赋给该(`operator[]`返回的)引用所指向的对象. 所以, 

-   如果键`k`已经有了相关联的值, 则该值被更新
-   如果`k`还没有存在于映射表中, 那就没有`operator[]`可以指向的值对象, 于是就是用值类型的默认构造函数创建一个新的对象, 然后`operator[]`就能返回一个指向该新对象的引用了. 

一个例子:

>   ```cpp
>   map<int, Widget> m;
>   m[1] = 1.50;
>   ```
>
>   等价于:
>
>   ```cpp
>   typedef map<int, Widget> IntWidgetMap;
>   pair<IntWidgetMap::iterator, bool> result = m.insert(IntWidgetMap::value_type(1, Widget()));
>   result.first->second = 1.50;
>   ```
>
>   具体流程为:
>
>   1.   默认构造临时对象`Widget`, 
>   2.   调用赋值操作符
>   3.   析构临时对象

这也就不难理解上面我们的代码为什么出现问题了, 仅仅调用了`m1[4]`就会使键值对`4:0`被写入映射表.

## 用于添加新的元素`.insert()`

直接使用`insert()`函数(方法)就不会有上面的开销:

```cpp
m.insert(IntWidgetMap::value_type(1, 1.50));
```

但是在更新元素的时候, 使用`operator[]`反而要好一些, 看下面的代码:

```cpp
m[k]=v;
m.insert(IntWidgetMap::value_type(k, v)).first->second = v;
```

当然不仅是在代码的简洁程度方面, 对于程序运行的开销也是如此:

使用`insert()`更新元素的时候, 需要经历下面的步骤:

1.   构造`IntWidgetMap::value_type`类型(`pair<int, Widget>`类型)的临时对象;
2.   构造`Widget`临时对象;
3.   更新元素;
4.   析构`Widget`临时对象;
5.   析构`IntWidgetMap::value_type`临时对象;

## 结论

-   添加元素用`insert`;
-   更新元素用`operator[]`;
