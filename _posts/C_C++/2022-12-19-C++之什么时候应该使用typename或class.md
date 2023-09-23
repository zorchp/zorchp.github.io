---
categories: [C_C++]
tags: C++
---

# 写在前面

对于C++模版元编程, 使用关键字`typename`还是`class`显然是不重要的, 除了在模版模版参数中使用类类型一定要用`class`声明类外, 例如下面这个例子, 为容器给出泛型函数, 虽然这样事实上只针对序列式容器:

```cpp
template <typename T, template <typename> class Container>
ostream &operator<<(ostream &os, Container<T> v) {
    for (auto i : v) os << i << " ";
    return os << endl;
}
```

在模版中, 一般情况下二者都可以混用, 但是也有例外...

>   参考effective STL 引言部分

# 从属类型前使用`typename`

为了避免潜在的语法解析二义性问题, 需要在从属于(`dependent`)形式类型参数的类型名前面加上`typename`, 下面是一个例子, 输入是一个容器, 返回值是容器中的最后一个元素是否大于第一个元素, 其实现通过函数模板的方法:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

template <typename C>
bool lastGreaterThanFirst(const C &container) {
    if (container.empty()) return false;
    typename C::const_iterator begin(container.begin()), end(container.end());
    return *--end > *begin;
}

void t1() {
    vector<int> v{1, 3, 5};
    cout << lastGreaterThanFirst(v); // 1
    reverse(v.begin(), v.end());
    cout << lastGreaterThanFirst(v); // 0
}
int main(int argc, char *argv[]) {
    t1();
    return 0;
}
```

这个例子中, 局部变量`begin`以及`end`的类型为`C::const_iterator`, 而`const_iterator`是从属类型(dependent type), 于是就要在这种类型声明符前面加上`typename`. 

>   为了解析C++程序，编译器需要知道某些名称是否为类型[^1]。
>
>   C++编译器基本上将模板的文本复制到内部缓冲区中，只有当需要实例化时，它们才解析模板，并可能检测定义中的错误。但是，其他实现不会因为模板作者的错误而打扰模板的用户，而是选择在早期检查模板，并在实例化发生之前尽快在定义中给出错误。所以必须有一种方法告诉编译器某些名称是类型，而某些名称不是。

# ref

[^1]:[c++ - 为什么必须在哪里以及为什么必须放置“模板”和“类型名”关键字？- 堆栈溢出 (stackoverflow.com)](https://stackoverflow.com/questions/610245/where-and-why-do-i-have-to-put-the-template-and-typename-keywords);