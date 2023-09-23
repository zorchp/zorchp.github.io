---
categories: [C_C++]
tags: C++ String
---

# 写在前面

刷力扣([415. 字符串相加](https://leetcode.cn/problems/add-strings/))时候发现这样一个现象:

使用

```cpp
s1 = static_cast<char>(c) + s1;
```

要比先push_back, 然后reverse慢很多:

```cpp
s2.push_back(static_cast<char>(c));
// .. 
reverse(s2.begin(), s2.end());
```

那么问题出在哪呢?

猜测: 第一种方法应该是等号右边先通过重载的加法运算符创建了一份字符串的临时对象, 然后(调用拷贝赋值运算符)赋值给s1, 最后还要销毁临时对象, 这就导致每次都要进行赋值和销毁, 时间成本就上来了..

而第二种都只是原地操作, 对内存的影响应该也只局限于动态扩容了. 

# 测试

```cpp
#include <algorithm>
#include <cassert>
#include <chrono>
#include <iostream>
#include <string>
using namespace std;
using namespace std::chrono;
#define MAX 100000
string s1{}, s2{};


void t1() {
    for (int i{}; i < MAX; ++i) s1 = static_cast<char>(i % 127) + s1;
}

void t2() {
    for (int i{}; i < MAX; ++i) s2.push_back(static_cast<char>(i % 127));
    reverse(s2.begin(), s2.end());
}

int main() {
    //
    assert(s1 == s2);
    auto start = system_clock::now();
    t1(); // Time spent: 2.48452s
    // t2(); // Time spent: 0.006175s
    auto end = system_clock::now();
    auto duration = duration_cast<microseconds>(end - start);
    cout << "Time spent: "
         << double(duration.count()) * microseconds::period::num /
                microseconds::period::den
         << "s" << endl;


    assert(s1 == s2);
}

```



# 结论

还是使用push_back吧, 老老实实. 

虽然`s = tmp + s;`这样的写法很方便(特别是数字字符串时候不需要反向遍历), 但是鉴于性能不好还是少用了. 