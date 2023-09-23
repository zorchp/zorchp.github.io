---
categories: [C_C++]
tags: C++ Interview
---

# 写在前面

最近做一个华为机试的模拟题, 发现看起来一样的输出就是不给过, 后来发现可能是字符串末尾的空格导致, 一开始没想到别的好办法, 直接存数组做了. 后来发现, 用字符串流 (`stringstream`) 非常方便, 于是就顺便总结下. 

>   这个题是这样的:
>
>   Tom从小就对英文字母非常感兴趣，尤其是元音字母(a,e,i,o,u,A,E,I,O,U)，他在写作文的时候都会把元音字母写成大写的，辅音字母则都写成小写, 你试试把一个句子翻译成他写作文的习惯吧。
>
>   ###### 输入
>
>   输入一个字符串S(长度不超过100，只包含大小写的英文字母和空格)。
>
>   ###### 输出
>
>   按照习惯输出翻译后的字符串S。
>
>   ###### 样例1
>
>   复制输入：
>
>   `Who Love Solo`
>
>   复制输出：
>
>   `whO lOvE sOlO`

注意这个用例, 末尾是不含有空格的, 但是如果每次处理之后不判断, 就一定会带着一个空格, 这就是麻烦的地方了. 

下面就以这个题为一个引子, 讲讲 C++高效读取字符串的方法. 

# 题外话

这题肯定是要构建一个哈希表存元音字母了, 但是这里我给出两种方法, 如果刷题追求速度的话, 大家可以看一下哪种方法更快一些. 

```cpp
#include <bits/stdc++.h>
using namespace std;

// version 1
// unordered_set<char> dic{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

// version 2
static const string dc = "aeiouAEIOU"s;
static unordered_set<char> dic(dc.begin(), dc.end());
```



# 几种方法

## 一般的循环读取

用一般的循环可以读取, 但是**没办法记录是否遍历到了最后一个单词**, 所以就只能存数组(我一开始的想法, 后来才发现可以用输出字符串流).

```cpp
void t0() {
    string s;
    vector<string> vs;
    // 可以通过的写法, 但是需要额外空间
    while (cin >> s) {
        if (cin.get() == '\n') break; // 事实上并没有读取到换行
        vs.emplace_back(s);
    }

    auto N = vs.size();
    for (int i{}; i < N; ++i) {
        for (auto& c : vs[i]) {
            if (dic.count(c))
                c = toupper(c);
            else
                c = tolower(c);
        }
        cout << vs[i] << (i == N - 1 ? "" : " ");
    }
}
```

>   注意, 这种写法在本地测试时候会阻塞 cin 读取, 但是在 oj 不会.

## getline 读取一行

另外就是仅读取一行, 采用`getline()`. 剩余的逻辑不变. 这种方法不会阻塞, 读取完一行之后就停了. 

```cpp
void t1() {
    string s, t;
    vector<string> vs;
    getline(cin, s);
    stringstream ss(s);
    // 可以通过的写法, 但是需要额外空间
    while (ss >> t) {
        vs.emplace_back(t);
    }

    auto N = vs.size();
    for (int i{}; i < N; ++i) {
        for (auto& c : vs[i]) {
            if (dic.count(c))
                c = toupper(c);
            else
                c = tolower(c);
        }
        cout << vs[i] << (i == N - 1 ? "" : " ");
    }
}
```

## 用字符流构建输出字符串

我认为的最佳(最有 C++ 味道)的解法. 

```cpp
void t2() {
    string s, t;
    getline(cin, s);
    stringstream ss(s);
    ostringstream oss;
    while (ss >> t) {
        for (auto& c : t) {
            if (dic.count(c))
                c = toupper(c);
            else
                c = tolower(c);
        }
        oss << t << " ";
    }
    auto ans = oss.str();
    ans.pop_back(); // 删除末尾的空格
    cout << ans;
}
```



# C++字符串流



## 单行读取

两种写法, 推荐第一种. 

```cpp
void t1() {
    string s;
    getline(cin, s);
    stringstream ss(s);
    string t;
    // 单行读取, 空格分隔的字符串
    while (ss >> t) {
        cout << "==>" << t << "<==\n";
    }
    cout << "over...\n";
}
```

判断条件是字符流是否为空, 这时候需要进行字符串的判空. 

```cpp
void t2() {
    string s;
    getline(cin, s);
    stringstream ss(s);
    // 另一种写法, 需要注意结尾的空格, 也会被读取
    while (ss) {
        string t;
        ss >> t;
        if (t.empty()) break;
        cout << "==>" << t << "<==\n";
    }
    cout << "over...\n";
}
```

非常好用, 并且在二叉树的序列化和反序列化中也可以用来简化代码. 

## 多行读取

把 `getline` 放在 `while` 中就可以了. 这里给出一个读取未知维数矩阵的例子

```cpp
vector<vector<int>> ans;

template <typename T>
ostream &operator<<(ostream &os, const vector<T> &v) {
    for (auto i : v) os << i << " ";
    return os << endl;
}

template <typename T>
ostream &operator<<(ostream &os, const vector<vector<T>> &v) {
    for (auto i : v) os << i;
    return os << endl;
}

void t1() {
    string row;
    std::ios::sync_with_stdio(false); // 取消 cin 和 stdin 的同步

    while (getline(cin, row)) {
        vector<int> tmp;
        int item;
        istringstream ss(row);
        while (ss >> item) {
            tmp.emplace_back(item);
        }
        ans.emplace_back(tmp);
        if (row.empty()) break; // 换行时结束
    }
    cout << ans;
}

int main(int argc, char *argv[]) {
    t1();
    return 0;
}
```



### 传统的 C scanf 读取

由于C++的字符流在读取**大矩阵**时候往往要比 scanf 慢很多, 为了不超时, 应该学习一下 scanf 的读取方法(竞赛常见). 

>   这里仅针对数字, 如果是字符串, 由于 C-style 的字符串和 C++的 string 之间还需要转换, 还是建议用 C++ 的方法读取. 

可以参考:  [探寻C++最快的读取文件的方案](https://byvoid.com/zhs/blog/fast-readfile/). 

```cpp
void t2() {
    // 容器还是用 vector, 但是 IO 采用 C 风格
    char buf[10]{};
    auto atoi = [](char *buf) {
        int ans{};
        for (int i{}; buf[i] != '\0'; ++i) ans = ans * 10 + (buf[i] - '0');
        return ans;
    };
    vector<int> tmp;
    while (~scanf("%[^ \n]", buf)) {
        tmp.emplace_back(atoi(buf));
        if (getchar() == '\n') {
            ans.emplace_back(tmp);
            cout << tmp;
            tmp.clear();
            // if (getchar() == '\n') break;
        }
    }
    cout << ans;
}
```

但是这里就有一个问题, 第 16 行不能加, 加上之后会吃掉开头的字符(因为 scanf 的忽略列表中指定了空格和回车)

>   这就导致不能在本地测试时候读取结束正常退出. 

另外, 用于分隔的空格数量只能是一个, 多了的话也会由于忽略字符导致数组变化. 
