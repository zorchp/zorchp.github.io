---
categories: [Linux-Shell]
tags: Shell Linux
---

# 写在前面

总结Linux的Shell脚本中常见的分支控制流语句与基本实例. 环境为Ubuntu-jammy.

>   参考:Linux命令行与shell脚本编程大全

# 预备知识

## 条件判断: test命令

```bash
test 10 -gt 9
echo $? # 0
```

>   0表示真, 1表示假, 这里比较奇怪, 需要注意, 其实是延续了系统调用的状态码

我更喜欢下面的格式, 在if判断中比较常用:

```bash
[ 10 -gt 9 ]
echo $? # 0
```

### 数值(值大小)的比较

| 比较运算 | 运算符 |     注记      |
| :------: | :----: | :-----------: |
|   大于   | `-gt`  | greater than  |
|   小于   | `-lt`  |   less than   |
|   等于   | `-eq`  |     equal     |
| 大于等于 | `-ge`  | greater equal |
| 小于等于 | `-le`  |  less equal   |
|  不等于  | `-ne`  |   not equal   |

### 字符串(字典序)的比较

| 比较 | 描述 |
| :--: | :--: |
| str1 = str2 | 检查str1是否和str2相同 |
| str1 != str2 | 检查str1是否和str2不同 |
| str1 < str2 | 检查str1是否比str2小 |
| str1 > str2 | 检查str1是否比str2大 |
| -n str1 | 检查str1的长度是否非0  |
| -z str1 | 检查str1的长度是否为0 |

例子:

这种情况会把`>`解释为输出重定向, 所以需要转义.

```bash
[ "abb" \> "abc" ]
```

### 文件的判断

| 判断 | 描述 | 注记 |
| :--: | :--- | ---- |
| -d file | 检查file是否存在并是一个目录 | directory |
| -e file | 检查file是否存在 | exist |
| -f file | 检查file是否存在并是一个文件 | file |
| -r file | 检查file是否存在并可读 | read |
| -s file | 检查file是否存在并非空 | space |
| -w file | 检查file是否存在并可写 | write |
| -x file | 检查file是否存在并可执行 | execute |
| -O file | 检查file是否存在并属当前用户所有 | Owned |
| -G file | 检查file是否存在并且默认组与当前用户相同 | Group |
| file1 -nt file2 | 检查file1是否比file2新 | newer than |
| file1 -ot file2 | 检查file1是否比file2旧 | older than |

## 分支合并

-   `[ cond1 ] && [ cond2 ]`: 逻辑与
-   `[ cond1 ] || [ cond2 ]`: 逻辑或

## 高级括号

用于if判断/test测试

### 双方括号: [[  ]]

用于字符串比较的正则匹配

### 双圆括号: ((  ))

用于数值计算, C-style的for语句. 





## 命令行参数

直接以空格分隔传入, 与C类似, 采用一些特殊变量进行操作:

-   `$*`和`$@`变量可以用来轻松访问所有的参数。这两个变量都能够在单个变量中存储所有的命令行参数。
-   `$*`变量会将命令行上提供的所有参数当作一个单词保存。这个单词包含了命令行中出现的每 一个参数值。基本上`$*`变量会将这些参数视为一个整体，而不是多个个体。
-   另一方面，`$@`变量会将命令行上提供的所有参数当作同一字符串中的多个独立的单词。这样 你就能够遍历所有的参数值，得到每个参数。这通常通过for命令完成。
-   `$#`: 命令行参数个数
-   `$1`: 第一个参数









# 判断分支

## if-then

命令格式

```bash
if command
then 
    commands
fi
```

我喜欢下面这样:

```bash
if command; then 
    commands
fi
```

一个例子:

```bash
if [ 10 -gt 9 ]; then
    echo "10>9"
fi
```

## if-then-else

```bash
if command; then 
    commands
else 
    commands
fi 
```



## if-then-elif

```bash
if command1; then 
    commands
elif command2; then 
    more commands
fi 
```



## if-then-elif-else

```bash
if command1; then 
    commands
elif command2; then 
    more commands
...(more than elif)
else
    commands
fi 
```



## case 

上面的elif写多了比较复杂, 下面是case语句, 解决了elif的复杂嵌套问题, 对应C的switch-case:

```bash
case variable in 
    pattern1 | pattern2) 
        commands1;; 
    pattern3) 
        commands2;; 
    *) 
        default commands;; 
esac 
```

# 循环控制

## for: Shell-style

>   Python也是这样的, 不过没有do-done. 

```bash
for var in list 
do 
    commands 
done
```



## for: C-style

```bash
for (( variable assignment ; condition ; iteration process ))
do 
    commands 
done
```





## while: 为真循环

```bash
while test command 
do 
    other commands 
done 
```

### 使用shift传递参数

在使用`shift`命令时，默认情况下它会将每个参数变量向左移动一个位置。所以，变量`$3` 的值会移到`$2`中，变量`$2`的值会移到`$1`中，而变量`$1`的值则会被删除(注意，变量`$0`的值，也就是程序名，不会改变)。

>   使用shift命令的时候要小心。如果某个参数被移出，它的值就被丢弃了，无法再恢复。



## until: 为假循环

```bash
until test command 
do 
    other commands 
done 
```



## 控制语句

-   break
-   continue



# 函数

## 定义函数

两种方法: 带或者不带`function`关键字

```bash
function name { 
    commands
    return # 返回状态码
}

name() { commands }
```

## 函数内局部变量

>   函数内部使用的任何变量都可以被声明成局部变量
>
>   local关键字保证了变量只局限在该函数中。如果脚本中在该函数之外有同样名字的变量， 那么shell将会保持这两个变量的值是分离的

```bash
a() {
    local tmp=1
}
a
echo $tmp # 为空
```



