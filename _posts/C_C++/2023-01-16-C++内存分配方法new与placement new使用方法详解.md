---
categories: [C_C++]
tags: C++  Interview
---

# 写在前面

总结一下C++内存分配中的`new`/`delete`方法, 以及一个很有意思的工具: `placement new`. 

>   参考:
>
>   1.   cppprimer5ed, pp409, pp726(19.1).
>   2.   侯捷C++ video



# new的基本使用

## 编译器角度

在使用`new`分配内存的时候, 例如下面这样:

```cpp
string *sp = new string("abc"); // 分配并初始化一个string对象
string *sa = new string[10];    // 分配10个默认初始化的string对象
```

上面的`new`内存分配, 本质上进行了三个步骤:

1.   `new`表达式调用一个名为`operator new`(或`operator new[]`)的标准库函数, 这个函数分配了一块足够大的/原始的/未命名的内存空间, 以便存储特定类型的对象(或对象构成的数组);
2.   编译器运行相应的构造函数以构造这些对象, 传入初始值;
3.   对象被分配空间, 并且构造完成, 返回指向该对象的指针. 

对于`delete`, 同理:(两个步骤)

```cpp
delete sp;   // 销毁*sp, 释放sp所指向的内存空间
delete[] sa; // 销毁数组中的元素, 然后释放对应的内存空间
```

步骤:

1.   对`sp`所指向的对象或者`arr`所指的数组中的元素执行相应的析构函数;
2.   编译器调用`operator delete`(或`operator delete[]`)释放内存.

## operator new/operator delete调用规则

>   当重载了全局的operator new和operator delete之后, 内存分配就不是系统默认的了, 所以这两个函数一定要保证正确. 

分配内存/析构内存时, 编译器首先在被分配内存类(及其基类)的作用域中查找, 是否有定义operator new和operator delete成员函数. 若未找到, 则在全局作用域内查找, 最后, 会调用标准库定义的版本. 

其中, 若在定义了/重载了operator new和operator delete之后, 还想使用全局的operator new和operator delete, 那么应该使用`作用域运算符`, 即:

```cpp
::new
::delete
```



## 标准库定义的版本

>   书上写错了, `operator delete`返回值类型应该是`void`而不是`void*`.

下面的版本可能会抛出`std::bad_alloc`异常:

```cpp
void *operator new(size_t);   // 分配一个对象
void *operator new[](size_t); // 分配一个数组
void operator delete(void*) noexcept;   // 释放一个对象
void operator delete[](void*) noexcept; // 释放一个数组
```

下面的版本承诺不会抛出异常:

```cpp
#include <new> // struct nothrow_t, nothrow
void *operator new(size_t, nothrow_t&) noexcept;    // 分配一个对象
void *operator new[](size_t, nothrow_t&) noexcept;  // 分配一个数组
void operator delete(void*, nothrow_t&) noexcept;   // 释放一个对象
void operator delete[](void*, nothrow_t&) noexcept; // 释放一个数组
```

>   注意:
>
>   1.   重载上述运算符函数时, 必须使用`noexcept`异常说明符指定其不抛出异常. 
>
>   2.   应用程序可以自定义上述函数中任意一个, 前提是自定义的版本必须位于全局作用域或者类作用域中. 
>
>   3.   将上述运算符函数定义成类的成员函数时, 其默认就是隐式静态的(implicit, static), 这是因为`operator new`用在对象构造之前, 而`operator delete`用在对象销毁之后, 所以这两个成员必须静态, 并且**不能操纵类的任何数据成员**. 
>
>   4.   在类中定义时, 无需显式声明`static`.(声明了也不会报错)
>
>   5.   $\bigstar$对`operator new`或`operator new[]`来说, 其返回值类型必须是`void*`, 第一个形参**必须**是`size_t`且该形参不能含有默认实参. 
>
>   6.   当编译器调用`operator new`时, 把存储**指定类型对象所需的字节数**传给`size_t`形参; 当调用`operator new[]`时, 传入函数的是存储**数组中所有元素**所需的空间. 
>
>   7.   如果要自定义`operator new`, 可以为其提供额外形参, 这就用到了后面会提到的`placement new`, 将实参传给新增的形参.
>
>   8.   下面这个**全局函数**不能被重载: (在类中作为成员函数可以被重载)
>        ```cpp
>        void *operator new(size_t, void*);
>        ```
>
>        这个函数只能供标准库使用. 
>
>        下面是一个测试:
>        
>        ```cpp
>        // error: redefinition of 'void* operator new(size_t, void*)'
>        void* operator new(size_t size, void* start) {
>            cout << "operator new(size_t size, void* start), size=" << size
>                 << ", start=" << start << endl;
>            return start;
>        }
>        ```
>        
>   8.   
>        



## 重载operator new/operator delete

```cpp
#include <iostream>
using namespace std;

class Foo {
public:
    int _id;
    long _data;
    string _str;

public:
    Foo() : _id(0) {
        cout << "default ctor.this=" << this << " id=" << _id << endl;
    }
    Foo(int i) : _id(i) {
        cout << "ctor.this=" << this << " id=" << _id << endl;
    }

    // virtual or not
    // ~Foo() { cout << "dtor.this=" << this << " id=" << _id << endl; }
    virtual ~Foo() { cout << "dtor.this=" << this << " id=" << _id << endl; }

    static void* operator new(size_t size);
    static void operator delete(void* pdead, size_t size);
    static void* operator new[](size_t size);
    static void operator delete[](void* pdead, size_t size);
};

void* Foo::operator new(size_t size) {
    Foo* p = (Foo*)malloc(size);
    cout << "Foo::new, size=" << size << endl;
    return p;
}

void Foo::operator delete(void* pdead, size_t size) {
    cout << "Foo::delete" << endl;
    free(pdead);
}

void* Foo::operator new[](size_t size) {
    Foo* p = (Foo*)malloc(size);
    cout << "Foo::new[], size=" << size << endl;
    return p;
}

void Foo::operator delete[](void* pdead, size_t size) {
    cout << "Foo::delete[]" << endl;
    free(pdead);
}
```

接下来是测试函数:

1.   调用全局的new/delete:
     ```cpp
     void t1() {
         Foo* pf = new Foo;
         delete pf;
         /*
         Foo::new, size=48
         default ctor.this=0x600003388270 id=0
         dtor.this=0x600003388270 id=0
         Foo::delete, size=48
         */
     
         Foo* pf1 = ::new Foo;
         ::delete pf1;
         // if not overload new and delete: call system new and delete
         /*
         default ctor.this=0x600003388270 id=0
         dtor.this=0x600003388270 id=0
         */
     }
     ```

2.   调用自定义的new/delete:
     ```cpp
     void t2() { // 验证内存大小
         cout << "sizeof(int)=" << sizeof(int) << endl;
         cout << "sizeof(long)=" << sizeof(long) << endl;
         cout << "sizeof(string)=" << sizeof(string) << endl;
         cout << "sizeof(Foo)=" << sizeof(Foo) << endl;
         /*clang++
         sizeof(int)=4
         sizeof(long)=8
         sizeof(string)=24
         sizeof(Foo)=40
         */
         /*g++
         sizeof(int)=4
         sizeof(long)=8
         sizeof(string)=32
         sizeof(Foo)=48
         */
     }
     // 然后是内存分配测试:
     void t3() {
         cout << "sizeof(Foo)=" << sizeof(Foo) << endl; // g++: 48
         Foo* p = new Foo(7);
         cout << "sizeof(new Foo)=" << sizeof(*p) << endl;
         delete p;
     
         Foo* pArr = new Foo[5];
         cout << "sizeof(new Foo[5])=" << sizeof(*pArr) << endl;
         delete[] pArr;
         /*
         sizeof(Foo)=48
         Foo::new, size=48
         ctor.this=0x600000f18000 id=7
         sizeof(new Foo)=48
         dtor.this=0x600000f18000 id=7
         Foo::delete
         Foo::new[], size=248 
         default ctor.this=0x600003d1c008 id=0
         default ctor.this=0x600003d1c038 id=0
         default ctor.this=0x600003d1c068 id=0
         default ctor.this=0x600003d1c098 id=0
         default ctor.this=0x600003d1c0c8 id=0
         sizeof(new Foo[5])=48
         dtor.this=0x600003d1c0c8 id=0
         dtor.this=0x600003d1c098 id=0
         dtor.this=0x600003d1c068 id=0
         dtor.this=0x600003d1c038 id=0
         dtor.this=0x600003d1c008 id=0
         Foo::delete[]
         */
     }
     ```

     这里要注意, 为什么对象数组的大小不是`48*5=240`, 反而还多了一个8呢? 248=48*5+8

     >   因为8就是size_t也就是unsigned long在64位机器下的大小, 保存了对象数组长度. 
     >
     >   下面是分别在64位机器和32位(使用`g++ -m32`选项, 仅支持x86_64)机器下测试的情况:
     >
     >   ```cpp
     >   // 64bit:
     >   cout << sizeof(size_t) << endl;               // 8
     >   cout << sizeof(long) << endl;                 // 8
     >   cout << sizeof(unsigned long) << endl;        // 8
     >   cout << sizeof(unsigned) << endl;             // 4
     >   cout << typeid(unsigned).name() << endl;      // j
     >   cout << typeid(unsigned int).name() << endl;  // j
     >   cout << typeid(unsigned long).name() << endl; // m
     >   cout << typeid(size_t).name() << endl;        // m
     >   // 32bit:
     >   4
     >   4
     >   4
     >   4
     >   j
     >   j
     >   m
     >   j
     >   ```

     

3.   类中含有虚析构函数的情况:
     ```cpp
     // 析构函数为:
     virtual ~Foo() {cout << "dtor.this=" << this << " id=" << _id << endl;}
     ```

     此时`t3()`函数执行情况如下:

     ```cpp
         sizeof(Foo)=56
         Foo::new, size=56 // has a vptr: 48+8
         ctor.this=0x6000039701c0 id=7
         sizeof(new Foo)=56
         dtor.this=0x6000039701c0 id=7
         Foo::delete
         Foo::new[], size=288 // 288=56*5+8
         default ctor.this=0x139e04588 id=0
         default ctor.this=0x139e045c0 id=0
         default ctor.this=0x139e045f8 id=0
         default ctor.this=0x139e04630 id=0
         default ctor.this=0x139e04668 id=0
         sizeof(new Foo[5])=56
         dtor.this=0x139e04668 id=0
         dtor.this=0x139e04630 id=0
         dtor.this=0x139e045f8 id=0
         dtor.this=0x139e045c0 id=0
         dtor.this=0x139e04588 id=0
         Foo::delete[]
     ```



## 一个小坑

来说一个奇怪的情况:

首先看下面的例子:(算是上面例子的一个简化)

```cpp
#include <iostream>
using namespace std;

class P {
public:
    int a; // 4bytes
    void* operator new(size_t size) {
        P* p = (P*)malloc(size);
        cout << "P::new, size=" << size << endl;
        return p;
    }
    void* operator new[](size_t size) {
        P* p = (P*)malloc(size);
        cout << "P::new[], size=" << size << endl;
        return p;
    }
    // virtual
    // ~P() {}
};
```

这里面为了省事我直接把成员函数定义也放在类中了. 

然后是测试函数:

```cpp
void t1() {
    P* p = new P;
    // 4 (无析构函数)
    // 4 (无虚析构, 仅有析构)
    // 16 (虚析构)
    delete p;
    P* p1 = new P[5]();
    // 20 (无析构函数) 因为没设置析构函数,
    // 这时候就不会记录之后delete时候要释放的大小, 所以没有size_t信息,
    // 也就只有4*5=20大小 28 (无虚析构, 仅有析构) 88 (虚析构)
    delete[] p1;
}
int main(int argc, char const* argv[]) {
    t1();
    return 0;
}
```

思考一下输出是多少(运行环境:64bit机器, g++-12)

如果你的答案是:

```cpp
P::new, size=4
P::new[], size=20
```

并且你知道为什么, 那么就要恭喜你, 可以不用往后看了. 

想知道为什么注释掉析构函数之后就不会多出来`size_t`类型的记录数组大小的cookie的话, 就接着往下看吧. 

下面我做了一个表格, 就是关于上面这个例子有析构函数, 没有析构函数以及有虚析构函数三种情况得到的内存大小数据. 

|    析构行为    | 单个对象大小 | 对象数组大小 |
| :------------: | :----------: | :----------: |
|   无析构函数   |      4       |    20=4*5    |
| 有非虚析构函数 |      4       |   28=4*5+8   |
|  有虚析构函数  |   16=4+8+4   |  88=16*5+8   |

并且, `clang++ -cc1 -fdump-record-layouts test.cpp`查看内存布局发现:

```cpp
*** Dumping AST Record Layout
         0 | class P
         0 |   (P vtable pointer)
         8 |   int a
           | [sizeof=16, dsize=12, align=8,
           |  nvsize=12, nvalign=8]
```

>   发现存在内存对齐, 所以就变成了16而不是12了. 

并且, 没有析构函数的时候并不会占用多余的内存来记录数组大小, 这是因为没有析构动作, 那么也不会去记录析构的数组大小, 换句话说, 只有在调用用户的析构函数的时候, 才会申请额外的内存`size_t`来存储数组大小, 这就是`8`的由来. 

**但是**, 类中包含指针对象(例如`string`)的话就**一定**会产生`size_t`大小的一个变量来保存数组长度信息. 

>   [c++ - 成员运算符 new[\] 的参数“大小”增加，如果类具有析构函数/删除[] - 堆栈溢出 (stackoverflow.com)](https://stackoverflow.com/questions/45781692/parameter-size-of-member-operator-new-increases-if-class-has-destructor-dele);

# placement new(定位 new)

## 定义

cppprimer的定义是:

>   通过改变使用`new`的方式来阻止其抛出异常. 
>
>   ```cpp
>   int *p1 = new int; //分配失败, new throw `std::bad_alloc`
>   int *p2 = new (nothorw) int; //分配失败, new返回空指针
>   ```
>
>   这种形式(第二行)的`new`称为`placement new`(定位`new`)表达式, 这种写法允许我们向`new`传递额外的参数. 

侯捷老师的PPT:

>   placement-new 允许我们将对象建构在allocated memory(已分配好的内存)中,
>   但是没有placement-delete, 因为**并没有额外分配内存空间**,
>   或者可以称呼与placement-new对应的是placement-delete.
>   placement-new:等同于调用构造函数.

## 基本使用

```cpp
#include <complex>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <new>
using namespace std;

void t1() {
    char* buf = new char[sizeof(complex<int>) * 3];
    complex<int>* pc = new (buf) complex<int>(1, 2);
    // 这里其实调用了下面的:
    // static void* operator new(size_t size, void* start);
    printf("buf=%p\n", buf);
    printf("pc=%p\n", pc);
    /* buf=0x600001bc1100 */
    /* pc=0x600001bc1100 */

    cout << pc->real() << " " << pc->imag() << endl; // 1 2
    // 标准库提供的placement new()重载
    delete[] pc;
}
int main(int argc, char const* argv[]) {
    t1();
    return 0;
}
```

直接使用, 原地重新分配, 可以看到地址是相同的. 



## 重载placement new/placement delete

```cpp
#include <iostream>

using namespace std;
/*placement-new*/
class Bad {}; // 稍后会作为异常抛出
class Foo {
public:
    Foo() { cout << "Foo::Foo()" << endl; }
    Foo(int) {
        cout << "Foo::Foo(int)" << endl;
        throw Bad(); // 这里给出一个异常的例子
    }
    // new
    static void* operator new(size_t size); // 一般的重载
    static void* operator new(size_t size,
                              void* start); // 标准库提供的placement new()重载
    static void* operator new(size_t size, long extra); // 新的placement new()
    static void* operator new(size_t size, long extra,
                              char init); // 另一个新的placement new()
    // static void* operator new(long extra, char init);
    // error, 第一参数必须是size_t类型

    /*可以重载对应版本的placement delete(), 但是不会被调用,
    只有当placement new()调用的ctor抛出异常时候, 才会调用这些重载版本的delete(),
    也只可能被这样调用, 用途是归还未能完全创建成功的object占用的内存memory*/
    static void operator delete(void*, size_t);
    static void operator delete(void*, void*);
    static void operator delete(void*, long);
    static void operator delete(void*, long, char);

private:
    int m_i;
};


void* Foo::operator new(size_t size) {
    cout << "operator new(size_t size), size=" << size << endl;
    return malloc(size);
}

void* Foo::operator new(size_t size, void* start) {
    cout << "operator new(size_t size, void* start), size=" << size
         << ", start=" << start << endl;
    return start;
}

void* Foo::operator new(size_t size, long extra) {
    cout << "operator new(size_t size, long extra), size=" << size
         << ", extra=" << extra << endl;
    return malloc(size + extra);
}

void* Foo::operator new(size_t size, long extra, char init) {
    cout << "operator new(size_t size, long extra, char init), size=" << size
         << ", extra=" << extra << ", init=" << init << endl;
    return malloc(size + extra);
}

// void* Foo::operator new(long extra, char init) {
//     //error: 'operator new' takes type size_t ('unsigned long') as first
//     parameter return malloc(extra);
// }

void Foo::operator delete(void*, size_t) {
    cout << "operator delete(void*, size_t)" << endl;
}

void Foo::operator delete(void*, void*) {
    cout << "operator delete(void*, size_t)" << endl;
}

void Foo::operator delete(void*, long) {
    cout << "operator delete(void*, long)" << endl;
}

void Foo::operator delete(void*, long, char) {
    cout << "operator delete(void*, long, char)" << endl;
}
```

下面是测试函数:

```cpp
// 基本调用方式, 与析构
void t1() {
    Foo* pf = new (300, 'c') Foo;
    delete pf;
    /*
    Foo::Foo()
    operator delete(void*, size_t)
    */
}
// 全部调用方式
void t2() {
    Foo start;
    Foo* p1 = new Foo;
    Foo* p2 = new (&start) Foo;
    Foo* p3 = new (100) Foo;
    Foo* p4 = new (100, 'a') Foo;
    delete p1;
    delete p2;
    delete p3;
    delete p4;
    /*
    Foo::Foo()
    operator new(size_t size), size=4
    Foo::Foo()
    operator new(size_t size, void* start), size=4, start=0x16f35b04c
    Foo::Foo()
    operator new(size_t size, long extra), size=4, extra=100
    Foo::Foo()
    operator new(size_t size, long extra, char init), size=4, extra=100, init=a
    Foo::Foo()
    operator delete(void*, size_t)
    operator delete(void*, size_t)
    operator delete(void*, size_t)
    operator delete(void*, size_t)
    */
}
// 调用重载的operator delete的情况(bad_alloc)
void t3() {
    Foo start;

    Foo* p5 = new (100) Foo(1);
    delete p5;
    /*
    Foo::Foo()
    operator new(size_t size, long extra), size=4, extra=100
    Foo::Foo(int)
    libc++abi: terminating with uncaught exception of type Bad
    [1]    10066 abort
    */
    // Foo* p6 = new(100, 'a') Foo(1);
    // Foo* p7 = new(&start) Foo(1);
    // Foo* p8 = new Foo(1);
}
int main(int argc, char const* argv[]) {
    // t1();
    // t2();
    t3();
    return 0;
}
```



## 应用1: 委托构造

在C++11的委托构造函数出现之前, 可以使用placement new原地调用构造函数来完成构造. 

```cpp
#include <iostream>
using namespace std;

class P {
public:
    P() {
        new (this) P(1, 1.2);
        cout << "call P()\n";
    }
    P(int a) {
        new (this) P(a, 1.2);
        cout << "call P(int)\n";
    }
    // 使用委托构造
    //  P() : P(1, 1.2) { cout << "call P()\n"; }
    //  P(int a) : P(a, 1.2) { cout << "call P(int)\n"; }

private:
    // target ctor
    P(int a, double b) : m_a(a), m_b(b) { cout << "call P(int, double)\n"; }

    int m_a;
    double m_b;
};

void t1() {
    // 使用placement new
    P p1;
    // call P(int, double)
    // call P()

    P p2(10);
    // call P(int, double)
    // call P(int)
}

void t2() {
    // C++11: 使用委托构造
    P p1;
    // call P(int, double)
    // call P()

    P p2(10);
    // call P(int, double)
    // call P(int)
}

int main(int argc, char const *argv[]) {
    t1();
    // t2();
    return 0;
}
```

## 应用2: 显式调用构造函数

还可以这样在实例化的对象上通过placement new显式调用构造函数: (C++黑科技)

```cpp
#include <iostream>
#include <string>
using namespace std;

void t1() {
    string* ps = new string;
    cout << "strs: " << *ps << endl;
    // ps->string::string("1");//error,不能直接调用, 但是编译器可以
    // error: 'class std::__cxx11::basic_string<char>' has no member named
    // 'string'
    // ps->string::~string;
}
class A {
public:
    int id;
    A(int i) : id(i) { cout << "ctor. this=" << this << ' ' << id << endl; }
    ~A() { cout << "dtor. this=" << this << endl; }
};

void t2() {
    A* pA = new A(1);
    // vc can build successfully
    // pA->A::A(3); // error: cannot call constructor 'A::A' directly
    delete pA;
    // ctor. this=0x600001d14040 1
    // dtor. this=0x600001d14040
}

void t3() {
    // 采用placement new 调用构造函数
    A* pA = new A(1);
    new (pA) A(2);
    // ctor. this=0x600000578040 1
    // ctor. this=0x600000578040 2
}

int main(int argc, char const* argv[]) {
    // t1();
    t2();
    // t3();
    return 0;
}

```

