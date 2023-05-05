---
categories: [Python]
tags: Python Tips
---

# 写在前面

今天刷几道关于数的运算的题, 我发现了一个很匪夷所思的问题:

两段几乎完全一样的代码, 其运行时间差异怎么会如此之大呢?(题目:[415. 字符串相加 - 力扣（LeetCode）](https://leetcode.cn/problems/add-strings/))

```python
# 我的代码
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        na,nb=len(num1)-1,len(num2)-1
        add=0
        ans=''
        while na>=0 or nb>=0 or add:
            a=eval(num1[na]) if na>=0 else 0
            b=eval(num2[nb]) if nb>=0 else 0
            tmp=a+b+add
            ans+=str(tmp%10)
            add=tmp//10
            na-=1
            nb-=1
        return ans[::-1]
```

下面是官方代码:

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        na,nb=len(num1)-1,len(num2)-1
        add=0
        ans=''
        while na>=0 or nb>=0:
            a=int(num1[na]) if na>=0 else 0
            b=int(num2[nb]) if nb>=0 else 0
            tmp=a+b+add
            ans=str(tmp%10)+ans
            add=tmp//10
            na-=1
            nb-=1
        return '1'+ans if add else ans
```

乍一看没什么问题, 但是我的代码就是`188ms`, 而官方的是`36ms`, 这就很奇怪了..

# 分析

后来一番对比发现, 真正的罪魁祸首并不在代码逻辑方面, 而在于一个小小的API函数`eval()`, 这个函数虽然也能将字符串转换为整数, 但是其效率非常低...

其实从力扣的判题就能看出来了, 但是我还是想在本地试试:

```python
from time import time 
st=time()
ans=[]
for i in range(10000000):
    ans.append(eval(str(i)))
print("ok")
print("time :", time()-st)

```

上面的代码运行时间为:`34.3s`, 而将`eval`换成`int`之后程序运行时间只有`3.6s`, 足可见其对运行效率的影响.

那么, 到底是什么原因导致差异的呢?

# eval()与int()比较

这里参考了一些stack的回答[^1].

1.   `int()`函数只能对**仅含有整数**的字符串做处理, 而并不进行字符串的检查, 当然, 这里一个额外的情况如下:

     ```python
     In [1]: int('01')
     Out[1]: 1
     
     In [2]: eval('01')
       File <string>:1
         01
          ^
     SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
     
     ```

     可以看到前导零并不会影响`int`, 但是`eval`会首先将前导零认为是八进制数字, 这也是`int()`和`eval()`在整数转换时候不一样的地方(int更胜一筹);

2.   对于浮点数, 只能使用`eval()`, 看下面的例子:

     ```python
     In [3]: int('1.1')
     ---------------------------------------------------------------------------
     ValueError                                Traceback (most recent call last)
     Input In [3], in <cell line: 1>()
     ----> 1 int('1.1')
     
     ValueError: invalid literal for int() with base 10: '1.1'
     
     In [4]: eval('1.1')
     Out[4]: 1.1
     ```

3.   在与`eval()`搭配使用`input()`的时候需要注意, 由于`eval()`会执行Python中的表达式, 那就会有下面的一个问题. 

     一般的Python入门书中对于用户输入都是这样写的:

     ```python
     x=eval(input("Enter a number:"))
     ```

     这样当然可以得到一个完整的数字, 但是也有一定的安全风险, 这里的安全风险指的是: 在并没有输入类型检查的情况下, 如果用户输入了一段代码, 那么这段代码将会被`eval`函数执行. 看下面的例子:

     ```python
     x=eval(input("Enter a number:"))
     # 此时输入下面的内容
     __import__('os').system("rm -rf *")
     ```

     如果你使用的是类Unix系统, 并且此时工作目录下有一些源文件, 那么当你使用了这个程序的时候, 此时目录中的内容就消失了(谨慎操作). 



# ref

[^1]:[python - “eval”和“int”有什么区别 - Stack Overflow](https://stackoverflow.com/questions/45881547/what-is-the-difference-between-eval-and-int);