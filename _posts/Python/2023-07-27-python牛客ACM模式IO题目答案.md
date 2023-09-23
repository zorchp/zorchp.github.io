---
categories: [Python]
tags: Python
---





>   [牛客竞赛_ACM/NOI/CSP/CCPC/ICPC算法编程高难度练习赛_牛客竞赛OJ](https://ac.nowcoder.com/acm/contest/5657);



## 1

```python
import sys

for l in sys.stdin:
    a, b = l.split()
    print(int(a) + int(b))
```



## 2



```python
import sys

n = input()
for l in sys.stdin:
    a, b = l.split()
    print(int(a) + int(b))
```



## 3



```python
import sys

for l in sys.stdin:
    a, b = l.split()
    if a != '0' or b != '0':
        print(int(a) + int(b))        
```



## 4



```python
import sys

for l in sys.stdin:
    a = l.split()
    ans = 0
    n = int(a[0])
    if  n == 0:
        break
    arr = [int(i) for i in a[1:]]
    print(sum(arr))
```





## 5



```python
# import sys

t = int(input())
for _ in range(t):
    l = input().split()
    print(sum([int(i) for i in l[1:]] ))
```





## 6

```python
import sys

for l in sys.stdin:
    print(sum([int(i) for i in l.split()[1:]]))
```



## 7

```python
import sys

for l in sys.stdin:
    print(sum([int(i) for i in l.split()]))
```





## 8



```python
n = input()

a = sorted(input().split())

print(" ".join(a))
```



## 9

```python
import sys

for l in sys.stdin:
    print(' '.join(sorted(l.split())))
```



## 10

```python
import sys

for l in sys.stdin:
    ll = sorted(l.strip().split(','))
    print(','.join(ll))
```

注意换行符



## 11

```python
print(sum([int(i) for i in input().split()]))
```

不需要注意溢出真的爽... 

# 加餐: 链表的输入输出



## 输入



```python
# 用于模拟 stdin
s = "9->0->4->5->1"

lists = s.split("->")
lists = lists.split("->")
lists = [int(i) for i in lists]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(lists[0])
cur = head
for i in range(1, len(lists)):
    cur.next = ListNode(lists[i])
    cur = cur.next
```



## 输出

```python
cur = head
while cur and cur.next:
    print(cur.val, end="")
    print("->", end="")
    cur = cur.next
print(cur.val)
```

# 总结

1.   Python 刷题真的爽 (前提是数据范围小, 大了还得上 C++)
2.   stdin 本质上就使用了`strip`, `split`, 之类的 API, 用起来非常方便. 