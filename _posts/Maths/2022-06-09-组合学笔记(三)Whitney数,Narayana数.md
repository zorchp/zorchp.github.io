---
categories: [Maths]
tags: Combinatorics
---

# 写在前面

总结一下组合中用到的惠特尼数(`Whitney`)和纳拉亚那数(`Narayana`), 以及德拉诺伊(`Delannoy`)数的常用定义与性质.

# Whitney 数

主要通过偏序集以及格的理想来定义, 指$2n$个元素的栅格(fence)的有$k$个元素的理想的个数.

- 栅格(fence): 通过偏序集来定义, 指形如`\/\/\`的偏序集, 即$\{ x_1 < x_2 > x_3 < x_4 > x_5 < x_6 \}$

  的偏序集,

例子:

> $a(3) = 5$ because the ideals of size$3$ of the fence $F(6) =\{ x_1 < x_2 > x_3 < x_4 > x_5 < x_6 \}$ are $x_1x_3x_5, x_1x_2x_3, x_3x_4x_5, x_1x_5x_6, x_3x_5x_6$.

定义式如下:

# Narayana 数

定义式如下:

$$
N(n,k)=\frac1n\binom nk\binom n{k-1},
$$

# Delannoy 数

# Franel 数

$$
F_n = \sum_{k = 0}^n \binom{n}{k}^3,
$$

[A000172 - OEIS](http://oeis.org/A000172),

# Apéry 数

$$
\begin{aligned}
A_n&=\sum_{k=0}^n\binom nk^2\binom{n+k}k^2=\sum_{k=0}^n\frac{[{(n+k)!}]^2}{(k!)^4[{(n-k)!}]^2},\\
B_n&=\sum_{k=0}^n\binom nk^2\binom{n+k}k=\sum_{k=0}^n\frac{(n+k)!}{(k!)^3[{(n-k)!}]^2},\\
\end{aligned}
$$

[A005259 - OEIS](http://oeis.org/A005259),
