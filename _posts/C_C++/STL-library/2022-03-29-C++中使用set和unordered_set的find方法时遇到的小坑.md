---
categories: [C_C++]
tags: C++ STL Debug
---

# 写在前面

最近想尝试着使用C++重新写一下图论中的经典算法, 深度优先搜索和广度优先搜索, 因为C++新版本中的STL越来越完善, 使用起来也是相当方便, 但是在使用集合(`set`)和无序集合(`unordered_set`)的时候还是出现了一些小小的问题. 下面来记录一下, 也是对初学STL的一个总结.

>   环境:
>
>   CLion gcc C++17
>
>   cmake 3.21

# 集合/无序集合中查找的区别

集合作为一种单键的容器, 其内置了查找方法, 用于查找集合中的元素, 如果存在则使迭代器指向找到的元素, 如果不存在则指向`.end()`迭代器位置. 看下面的一个例子:

```cpp
#include <iostream>
#include <set>
#include <unordered_set>

using namespace std;


int main(int argc, char const *argv[]) {
    // unordered_set<int> ret = {20, 1, 2, 3};
    set<int> ret = {20, 1, 2, 3};
    for (auto &i: ret)
        cout << i << " ";
    cout << endl;
    int item = 10;
    cout << "查询" << item << "迭代器指向: " << *ret.find(item)<<endl;
    int item1 = 1;
    cout << "查询" << item1 << "迭代器指向: " << *ret.find(item1)<<endl;
    for (auto &i: ret)
        cout << i << " ";
    cout << endl;
    return 0;
}
/*
 * 1 2 3 20 
 * 查询10迭代器指向: 0
 * 查询1迭代器指向: 1
 * 1 2 3 20 
 */
```

当使用`set`容器的时候, 查找容器中不存在的元素, 迭代器默认会指向**0**, 但是,当你使用无序集合, 就会发生分段错误, 即迭代器指向了一个空的元素, 在实际使用的时候, 还是应该先采用`ret.find(item) != ret.end() `, 判断元素是否存在, 如果单纯对迭代器进行解引用操作就会出现问题. 但是在`set`中不会出现类似的问题, 只会使迭代器指向的元素为0, 即使容器中没有0这个元素. 