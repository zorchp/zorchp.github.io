---
tags: C++
categories: C++
---

# 理解

一图胜千言



<img src="https://cdn.jsdelivr.net/gh/zorchp/blogimage/%E6%88%AA%E5%B1%8F2023-11-05%2018.18.51.jpg" alt="截屏2023-11-05 18.18.51" style="zoom:33%;" />







我愿称之为最强



[c - Difference between r+ and w+ in fopen() - Stack Overflow](https://stackoverflow.com/questions/21113919/difference-between-r-and-w-in-fopen/59193656#59193656);





需要注意里面的`a`和 `a+`, 区别在于 a 不可以读而 a+可以读. 



>   [c - Difference between r+ and w+ in fopen() - Stack Overflow](https://stackoverflow.com/questions/21113919/difference-between-r-and-w-in-fopen/21114091#21114091);

| Mode | Read | Write | Create New File<br /> if not exist | Truncate |
| :--: | :--: | :---: | :--------------------------------: | -------- |
|  r   |  ✅   |   ❌   |                 ❌                  | ❌        |
|  w   |  ❌   |   ✅   |                 ✅                  | ✅        |
|  a   |  ❌   |   ✅   |                 ✅                  | ❌        |
|  r+  |  ✅   |   ✅   |                 ❌                  | ❌        |
|  w+  |  ✅   |   ✅   |                 ✅                  | ✅        |
|  a+  |  ✅   |   ✅   |                 ✅                  | ❌        |

总结:

-   `+` 表示读写