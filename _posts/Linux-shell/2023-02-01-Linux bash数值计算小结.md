---
categories: [Linux-Shell]
tags: Linux Shell
---



# 双小括号



>   测试环境: 
>
>   Ubuntu jammy

只支持整数

```bash
❯ echo $((9>8 && 78<9))
0
❯ echo $((9>8 && 78>9))
1
❯ echo $((9>8 || 78>9))
1
❯ echo $((123**9))
6443858614676334363
```



```bash
❯ num=5
❯ ((num*=3))
❯ echo $num
15
❯ a=$((2+3**92%2))
❯ echo $a
1
```



```bash
❯ a=5
❯ echo $((++a))
6
❯ echo $a
6
❯ echo $((a++))
6
❯ echo $a
7
```





```bash
echo $(($1))
```







## $[]数值计算

```bash
❯ res=$[1-22]
❯ echo $res
-21
```





## let命令对变量的数值计算







## bc计算器

```bash

```







### 计算1加到100的方法

1.   ```bash
     ❯ seq -s "+" 100| sed "s/\+$/\n/g" |bc
     5050
     ```

2.   ```bash
     ❯ echo {1..100} |tr " " "+"|bc
     5050
     ```

3.   ```bash
     ❯ seq -s " + " 100 | sed "s/..$/\n/g" | xargs expr
     5050
     ```

4.   

