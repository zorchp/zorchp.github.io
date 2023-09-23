---
categories: [C_C++]
tags: C++ Debug
---

# 问题与解决

最近看看C++11标准, 准备用用新的`range-based for`语法, 但是一个例子让我有点困惑, 就是下面这段代码:

```cpp
#include <bits/stdc++.h>
using namespace std;


void t1() {
    vector<string> vs{'a', "abc"};
    for (int i = 0; i < vs.size(); i++) {
        cout << vs[i] << " ";
    } cout << endl;
}

int main(int argc, char const *argv[]) {
    t1();
    return 0;
}
```

乍看起来, 应该只输出两个值, 就是字符串`a`和`abc`, 但是结果却让我有点意外:

```lua
abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc 
```

一开始我以为是语法的问题, 将其改为:

```cpp
    for (int i = 0; i < vs.size(); i++) {
        cout << vs[i] << " ";
    } cout << endl;

```

但是还是一样的情况, 这时候我就想起来之前写的一篇文章, 就是关于C风格字符串的, 用单引号得到的是字符数组, 那么为什么会直接将第一个元素作为数字然后循环呢?

查看`vector`源码(Mac位于`/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/c++/v1/vector`)我才知晓了原理:

```cpp
vector(size_type __n, const value_type& __x);
vector(size_type __n, const value_type& __x, const allocator_type& __a);
```

上面是部分的`vector`构造函数, 不难看出通过初始化列表的方式进行赋值, 其实就是用到了这个构造函数, 即`a个b`这样的形式, 这里应该还蕴含着隐式类型转换, 直接把C字符`'a'`转成了`97`了, 这才导致输出了97次的`abc`..

同样地, 使用下面的两个初始化方法也得到一样的结果:

```cpp
// vector<string> vs = {97, "abc"};
// vector<string> vs('a', "abc");
```

