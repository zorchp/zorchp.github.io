---
categories: [Linux-Shell]
tags: Linux Shell sed awk
---

# 写在前面

来总结一下Shell编程中常用的文本处理工具, 用好这些工具, 什么辅助的GUI界面都不想用了. 

当然了, 要想用好三剑客(grep, sed, awk), 首先得学一下文本处理的基本命令, 下面会以例子的形式给出, 方便大家加深理解. 

>   测试环境:
>   MacOS下multipass-Ubuntu22.04虚拟机
>
>   由于很多Shell工具在MacOS和Linux中存在区别, 这里还是以Linux为主了. 

# 预备知识

## I/O类命令

下面是一些输入输出类命令



### echo



### cat



### tac





## 统计类命令

下面列出一些进行字符统计的命令

### wc: 统计字符数

也可以统计行数



### 



## 操作类命令

### sort: 行排序

>   sort - sort lines of text files



### uniq: 去重

>   uniq - report or omit repeated lines



### tr: 操作字符串

>   tr - translate or delete characters

















## `grep`







## `sed`





提取IP地址

```bash
❯ ifconfig en0 | sed -n '5p' | sed -e 's/^.*inet//g' -e 's/net.*$//g'
 192.168.0.103
```



```bash
❯ ifconfig en0 | sed -e '5s/^.*inet//' -e "5s/netmask.*$//p" -n
 192.168.0.103
```





## `awk`命令



提取IP地址

```bash
❯ ifconfig en0 | awk 'NR==5{print $2}'
192.168.0.103
```





输入分隔符和输出分隔符的修改

```bash
❯ echo {1..50}pyyu | xargs -n 5 > awk-test.txt
❯ cat awk-test.txt
1pyyu 2pyyu 3pyyu 4pyyu 5pyyu
6pyyu 7pyyu 8pyyu 9pyyu 10pyyu
11pyyu 12pyyu 13pyyu 14pyyu 15pyyu
16pyyu 17pyyu 18pyyu 19pyyu 20pyyu
21pyyu 22pyyu 23pyyu 24pyyu 25pyyu
26pyyu 27pyyu 28pyyu 29pyyu 30pyyu
31pyyu 32pyyu 33pyyu 34pyyu 35pyyu
36pyyu 37pyyu 38pyyu 39pyyu 40pyyu
41pyyu 42pyyu 43pyyu 44pyyu 45pyyu
46pyyu 47pyyu 48pyyu 49pyyu 50pyyu
❯ awk -F "py" -v OFS="----" '{print $1,$NF}' awk-test.txt
1----yu
6----yu
11----yu
16----yu
21----yu
26----yu
31----yu
36----yu
41----yu
46----yu
❯ awk  -v FS="py" -v OFS="----" '{print $1,$NF}' awk-test.txt
1----yu
6----yu
11----yu
16----yu
21----yu
26----yu
31----yu
36----yu
41----yu
46----yu
❯ awk  -v FS="py" -v OFS="----" -v RS=" " '{print $1,$NF}' awk-test.txt
1----yu
2----yu
3----yu
4----yu
5----yu
7----yu
8----yu
9----yu
10----yu
12----yu
13----yu
14----yu
15----yu
17----yu
18----yu
19----yu
20----yu
22----yu
23----yu
24----yu
25----yu
27----yu
28----yu
29----yu
30----yu
32----yu
33----yu
34----yu
35----yu
37----yu
38----yu
39----yu
40----yu
42----yu
43----yu
44----yu
45----yu
47----yu
48----yu
49----yu
50----yu
❯ awk  -v FS="py" -v OFS="----" -v ORS="py" '{print $1,$NF}' awk-test.txt
1----yupy6----yupy11----yupy16----yupy21----yupy26----yupy31----yupy36----yupy41----yupy46----yupy%

```





