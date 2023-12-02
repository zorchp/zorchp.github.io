[toc]

# 第一章 组合分析概述

## 集合的计数

$$
有限集合N
\begin{cases}
    |N|&: 集合中元素的个数(N的基);\\
    \mathfrak{B}(N)&: N的所有子集构成的集合;\\
    \mathfrak{B}'(N)&: N的所有非空子集构成的集合(块,block).\\
\end{cases}
$$

- $N$ 的子集$\mathfrak{B}(N)$通过交/并/补运算构成一个布尔代数, 且其运算满足`De Morgan`公式.
- $N$的一个系$\mathscr{S}$(一称子集系)是指$N$的无重复块(_block_)构成的集合, 即$\mathscr{S}\in \mathfrak{B}'(\mathfrak{B}'(N))$;
- $k-$系是由$k$个块构成的系.

### 加法原理

设事件$A$有$m$种选取方式,事件$B$有$n$中选取方式, 则选$A$或$B$共有$m+n$种方式.

集合表示:

设$A,B$为有限集,且$A\cap B=\varnothing$,则$|A\cup B|=|A|+|B|$, $n$个有限集$A_1,...,A_n$满足$A_i\cap A_j=\varnothing(i\ne j)$,

$$
\Rightarrow \left|\bigcup_{i=1}^nA_i\right|=\sum_{i=1}^n|A_i|.
$$

### 乘法原理

设事件$A$有$m$种选取方式,事件$B$有$n$中选取方式, 则选$A$之后再选$B$共有$m\cdot n$种方式.

集合表示: 设$A,B$为有限集, $|A|=m,|B|=n$, 则$|A\times B|=|A|\cdot|B|=mn$.

乘积集合, $m$个有限集$N_i(1\leqslant i\leqslant m)$的笛卡尔积$N_1\times N_2\times\cdots\times N_m$,

其元素为$(y_1,y_2,...,y_m),\quad(y_i\in N_i)$

- 当$N_i=N(i\leqslant i\leqslant m)\Rightarrow N_1\times N_2\times\cdots\times N_m\triangleq N^m$;

定理: 有限个有限集的乘积集合的元素个数为

$$
\left|\prod_{i=1}^mN_i\right|=\prod_{i=1}^m|N_i|=|N_1||N_2|\cdots|N_m|.
$$

例子: 正整数$n$的素分解为$n=p_1^{\alpha_1}p_2^{\alpha_2}\cdots p_k^{\alpha_k}$($p_i$为素数), 则$n$的因子个数$d(n)=?$

> $n$的因子个数为$p_1^{\delta_1}p_2^{\delta_2}\cdots p_k^{\delta_k}$, 其中, $\delta_i\in A_i=\{0,1,2,...\alpha_i\}$,
> 则 $n$的一个因子对应一组 $(\delta_1,\delta_2, \ldots ,\delta_k)\in A_1\times
>   A_2\times\cdots \times A_k$,
>
> $$
> \begin{aligned}
>  \Rightarrow d(n)&= |A_1\times A_2\times \cdots \times A_k|\\
> & =  |A_1| |A_2| \cdots |A_k|\\
> &= (\alpha_1+1)(\alpha_2+1)\cdots (\alpha_k+1).
> \end{aligned}
> $$
>
> 一个具体的例子:
>
> $$
> 12=2^2\cdot3^1, \Rightarrow d(12)=3\times 2=6.
> $$

## 映射

有限集$M$到$N$的映射

$$
\begin{aligned}
    f: M&\to N\\
    x&\mapsto y=f(x)\\
\end{aligned}
$$

- $F(M,N), or \ N^M$表示集合$M$到$N$的全体映射$f$的集合.

定理A: 有限集$M$到$N$的映射个数为:

$$
|F(M,N)|=|N^M|=|N|^{|M|}
$$

> Proof:
> 设$|M|=m,|N|=n$, $M=\{x_1,x_2,...,x_m\}$.
> 则$\forall f\in F(M,N)$, 等价于给出$N$的以一个$m$元组$(y_1,y_2,...,y_m), (y_i\in N)$
> 即给定一个$f$等价于给出$N^m$的一个$m$元组, 于是有
>
> $$
> |F(M,N)=|N^m|=|N|^m=n^m=|N|^{ |M| }.
> $$
>
> 映射的分类:

$$
f:M\to N
\begin{cases}
    单射: \forall x_1,x_2\in M, x_1\ne x_2\Rightarrow f(x_1)\ne f(x_2);\\
    满射: \forall y\in N, \exist x\in M, 有y=f(x);\\
    双射: 既是单射又是满射(一一对应).\\
\end{cases}
$$

对于双射$f:M\to N$(一一对应), $\Rightarrow |M|=|N|$.

定理B: 有限集$M$的子集个数为: $|B(M)|=2^{|M|}$

> Proof:
> $\forall A\in B(M)$, 即$A\subset M$,
> 构造$f_A$(子集$A$的示性函数)
>
> $$
> f_A: M\to N=\{0,1\}\\
>  x\mapsto f_A(x)=\begin{cases}
> 1,x\in A\\
> 0,x\not\in A\\
>  \end{cases}
> $$
>
> 建立了$B(M)$与$F(M,N)$的一个一一对应.
> 于是$|B(M)|=|F(M,N)|=|N|^{|M|}=2^{|M|}$.

法二: 令$u_m=|B(M)|$
给定$x\in M$ 则< 的不含有$x $的子集与含有$x$的子集个数一样多, 且均为$u\_{m-1}$, 于是我们有如下的递推关系

$$
u_m=2u_{m-1}
$$

又由$u_0=1$,得到$u_m=2^m=2^{|M|}$.

例子: $n$元集合$N$的偶数元子集$E$,奇数元子集$F$, 则$|E|=?,|F|=?$.

解: 构造映射,

$$
\begin{aligned}
    f:E&\to F\\
    \forall A\in E, A&\mapsto f(A)=
\begin{cases}
    A\backslash\{x\},&x\in A\\
    A\cup \{x\}, &x\not\in A
\end{cases}
(x\in N)
\end{aligned}
$$

$f$为$E$到$F$的双射.

$\Rightarrow |E|=|F|=\frac12|B(N)|=2^{n-1}$.

## 集合的排列与组合

### 集合的排列

令$N$表示$n$元集合($|N|=n$), $[k]=\{1,2,...,k\}$

定义1: 集合$N$的一个$k$排列$\alpha(1\leqslant k\leqslant n)$就是一个从$[k]$到$N$的**单射**$\alpha$.

$$
\alpha([k])=(\alpha(1),\alpha(2),...\alpha(k)),\quad (\alpha(i)\in N,\alpha(i)\ne \alpha(j)).
$$

即$N$的一个有序的$k$元子集.

- $A_k(N)$表示$N$的所有的$k-$排列的集合.

定理1: 集合$N$的$k-$排列的个数$(1\leqslant k\leqslant n=|N|$)为

$$
|A_k(N)|=n(n-1)\cdots(n-k+1)\triangleq (n)_k \quad(n的降k阶乘)
$$

**球盒模型**:

$k$个不同的球放入$n$个不同的盒子, 每个盒子至多一个球的不同放法:$n$的降$k$阶乘.

一些记号:

- $(n)_k=n(n-1)\cdots(n-k+1)$, $(n)_0=1$. $n$的降$k$阶乘
- $\lang n\rang_k=n(n+1)\cdots(n+k-1)$, $\lang n\rang_0=1$. $n$的升$k$阶乘

(超几何级数中, $(n)_k$表示$n$的升$k$阶乘)

更一般地, 对于复数z,非负整数k,

- $(z)_k=z(z-1)\cdots(z-k+1)$, $(z)_0=1$. $z$的降$k$阶乘
- $\lang z\rang_k=z(z+1)\cdots(z+k-1)$, $\lang z\rang_0=1$. $z$的升$k$阶乘

引入$\Gamma-$函数$\Gamma(x+1)=x\Gamma(x)$

$$
(z)_k=\frac{\Gamma(z+1)}{\Gamma(z-k+1)}, \lang z\rang_k=\frac{\Gamma(z+k)}{\Gamma(z)}
$$

$k$可以不是非负整数

$\Gamma$函数的两种定义

$$
\begin{aligned}
\Gamma(x)&=\int_0^{+\infty}t^{x-1}e^{-t}\text{d}t\\
\Gamma(x)&=\lim_{n\to\infty}\frac{n!n^{x-1}}{\lang x\rang_n}\\
\end{aligned}
$$

$N$的置换, $\sigma: N\to N$(一一对应) (全排列)

定理2: $n$元集合$N$的所有置换的个数为$n!$.

### 集合的组合

定义2: 集合$N$的一个$k-$组合(or $k-block$)$B$就是$N$的一个$k$元非空子集(即: $B\subset N$, 且$1\leqslant k=|B|\leqslant n=|N|$)

- 若$k\geqslant0$, 称$N$的$k-$子集 用$B_k(N)$表示.

几种等价形式:

1.  令$\varphi:N\to\{0,1\})$, 且$\sum_{x\in N}\varphi(x)=k$, 这样映射的全体与$B_k(x)$一一对应;
    $$
    B\in B_k(N)\iff \varphi=\varphi_B=\begin{cases}
     1,x\in B\\
     0,x\not\in B\\
    \end{cases}(x\in N)
    $$
2.  不定方程$x_1+x_2+\cdots+x_n=k$, 其中$x_i=0or1$.
    方程的解集合与$B_k(N)$一一对应; ($N=\{y_1,y_2,...,y_n\}$)
3.  **球盒模型**:
    将$k$个相同的球放入$n$个不同的盒子, 且每个盒子至多一个球的不同放法.

定理3: $N$的$k-$子集的个数($0\leqslant k\leqslant n=|N|$)为:

$$
|B_k(N)|=\frac{n!}{(n-k)!k!}=\frac{(n)_k}{k!}\triangleq{n\choose k}(称为\textbf{二项式系数})
$$

> 证明:
> 用映射证明: $k!|B_k(N)|=|A_k(N)|=(n)_k$.
> 令
>
> $$
> \begin{aligned}
> f:A_k(N)&\to B_k(N)\\
> \alpha=(\alpha(1),\alpha(2),...,\alpha(k))&\mapsto f(\alpha)=\{\alpha(1),\alpha(2),..,\alpha(k)\}(由有序变为无序)
> \end{aligned}
> $$
>
> 则$\forall B\in B_k(N)\Rightarrow |f^{-1}(B)|=k!$,
> 当$B$选定$B_k(N)$, $f^{-1}(B)$互不相交且完全覆盖$A_k(N)$, 故
>
> $$
> \begin{aligned}
> (n)_k&=|A_k(N)|=\sum_{B\in B_k(N)}|f^{-1}(B)|=k!\,|B_k(N)|,\\
> &\Rightarrow |B_k(N)|=\frac{(n)_k}{k!}=\binom nk.
> \end{aligned}
> $$
>
> (牧羊人原理)

二项式系数满足的关系式:

1. $\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}$;(可以推出杨辉三角,Pascal三角)
2. $\binom{n}{k}=\frac{n}{k}\binom{n-1}{k-1}$;
3. $\binom{n+1}{k+1}=\binom{k}{k}+\binom{k+1}{k}+\cdots+\binom{n}{k}$;
4. $\binom{n+k+1}{k}=\binom{n+k}{k}+\binom{n+k-1}{k-1}+\cdots+\binom{n+1}{1}+\binom{n}{0}$;

其中1,2,4式的$n$可以推广到$z$(复数), 对于3则不能直接推广(由于3式右边的$n$是由$k$递增得到的, 需要满足$z$的降$k$阶乘)需要变成如下的递减形式(通过1式一步步递归得到下式):

$$
\binom{z+1}{k+1}=\binom{z}{k}+\binom{z-1}{k}+\cdots+\binom{z-s}{k}+\binom{z-s}{k+1}
$$

其中$s$为正整数, 最后一项保证了当$z-s=k+1$时, 能够和上面原来的3式中$\binom kk$保持一致.

代数证明:

直接展开之后再合并即可(代入验证等式成立), 这里不赘述.

组合证明:

(利用映射,双射以及相应的组合定义来证明)

可以直接从组合意义出发, 或者通过集合的计数方法.

### 其他计数方式--格路

1. $\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}$; (可以推出杨辉三角,Pascal三角)
2. $\binom{n}{k}=\frac{n}{k}\binom{n-1}{k-1}$;
3. $\binom{n+1}{k+1}=\binom{k}{k}+\binom{k+1}{k}+\cdots+\binom{n}{k}$;
4. $\binom{n+k+1}{k}=\binom{n+k}{k}+\binom{n+k-1}{k-1}+\cdots+\binom{n+1}{1}+\binom{n}{0}$;

从$(0,0)$到$(m,n)$点的格路数($\to,\uparrow$)
总步数为

$$
m+n \begin{cases}
向上走n步\\
向右走m步\\
\end{cases}
\Rightarrow
\binom{m+n}{m}=\binom{m+n}{n}
$$

① 上面的第一个式子. $\binom{n}{k}$是指从$O(0,0)$到$P(n-k,k)$的格路数, 分两种情况:

<div align="center"><img src="https://s2.loli.net/2021/12/15/kMcmiYntg7bTPEQ.png" style="zoom:33%;" ></img></div>

- $O$经过$A$ 到$P$ $:\binom{n-1}k$
- $O$经过$B$ 到$P$ $:\binom{n-1}{k-1}$

于是有$\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}$成立.

③ $\binom{n+1}{k+1}$是指从$O(0,0)$到$P(n-k,k+1)$的格路数. 分多种情况:

<div align="center"><img src="https://s2.loli.net/2021/12/15/AkKSpeUbmrf7nE6.png" style="zoom:33%;" /></div>

- $O$经过$A_1$到$P$ $:\binom nk$
- $O$经过$A_2$到$P$ $:\binom{n-1}k$
- $\vdots$
- $O$经过$A_{n-k+1}$到$P$ $:\binom kk$

于是③成立.

④同理,(只不过换成水平方向, 如图.) $\binom{n+k+1}{k}$是指从$O(0,0)$到$P(n+1,k)$的格路数.

<div align="center"><img src="https://s2.loli.net/2021/12/15/sZ5JPmzqUjtRHY3.png" alt="截屏2021-12-15 下午6.42.24" style="zoom:33%;" /></div>

- $O$经过$B_1$到$P$ $:\binom {n+k}k$
- $O$经过$B_2$到$P$ $:\binom{n+k-1}{k-1}$
- $\vdots$
- $O$经过$B_{k+1}$到$P$ $:\binom n0$

于是④式成立.

## 二项式恒等式

定理A (牛顿二项式定理)
若$xy=yx$, 则我们有

$$
(x+y)^n=\sum_{k=0}^n\binom{n}{k}x^ky^{n-k}
$$

> 证明:
>
> $$
> (x+y)^n=P_1P_2\cdots P_n=\sum_{k,l,k+l=n}c_{k,l}x^ky^l,\quad P_i=x+y
> $$
>
> 对展开式中$x^ky^{n-k}$的系数, 由$x^ky^{n-k}$的形成是从$P_i(i=1,2,...,n)$这$n$项中取其中$k$个项选$x$,剩余的$n-k$项中选$y$, 故共有$\binom{n}{k}$种方式, 于是有$c_{k,n-k}=\binom nk$.

推论1: $x=y=1.\Rightarrow 2^n=\sum_{k=0}^n\binom{n}{k}$.

$n$元集合$N$的所有子集数等于$k$元子集数之和$(k=0,1,2,...,n)$.

推论2: $x=-1, y=1\Rightarrow 0=\sum_{k=0}^n(-1)^k\binom nk\iff\sum_k\binom n{2k}=\sum_k\binom n{2k+1}=2^{n-1}$.

$n$元集合$N$的偶数元子集个数与奇数元子集个数相等.

推论3: $m,n$为正整数, $p=\min\{m,n\}$,则

$$
\sum_{k=0}^p\binom{m}{k}\binom{n}{p-k}=\binom{m+n}{p}(chu-Vandemonde卷积公式)
$$

> 证明:
>
> 直接通过下述等式
>
> $$
> (1+x)^m(1+x)^n=(1+x)^{m+n}
> $$
>
> 两端同时取$x^p$的系数, 可以得证.

**组合解释**:

从$m$个白球, $n$个黑球组成的$m+n$个球中选$p$个球, 共有$\binom{m+n}p$种方式. 这$p$个球可分成如下情况(根据白球数量分类)

含有$k$个白球$(k=0,1,2,...,p)$, 有$\binom mk\binom n{p-k}$种方式, 所以原式得证.

两个特例:

1. $$
   p=n,\Rightarrow \sum_{k=0}^n\binom{m}{k}\binom{n}{n-k}=\binom{m+n}{n}.
   $$

1. $$
   p=m=n,\Rightarrow \sum_{k=0}^n\binom{n}{k}^2=\binom{2n}{n}\to\text{\color{red}中心二项式系数}.
   $$

定理B: (差分公式)
设$\Delta$为差分算子, 即

$$
\begin{aligned}
    \Delta f(x)&=f(x+1)-f(x)&(对函数);\\
    \Delta u_m&=u_{m+1}-u_{m}&(对序列).
\end{aligned}
$$

二次差分:

$$
\begin{aligned}
    \Delta^2f(x)&=\Delta f(x+1)-\Delta f(x)\\
    &=f(x+2)-2f(x+1)+f(x)
\end{aligned}
$$

$n$次差分:$\Delta^n f=\Delta(\Delta^{n-1}f)$.

> 一次差分大于0: 函数(序列)是单增的; 二次差分大于0: 函数(序列)是凸的.

则有:

$$
\begin{aligned}
    \Delta^n f(x)&=\sum_{k=0}^n(-1)^{n-k}\binom nk f(x+k)&(n=0,1,2,...)\\
    \Delta^n u_m&=\sum_{k=0}^n(-1)^{n-k}\binom nk u_{m+k}&(n=0,1,2,...)
\end{aligned}
$$

> 证明:
> 由$\Delta f(x)=f(x+1)-f(x)$,
> 令移位算子$Ef(x)=f(x+1)$, 恒等算子$If(x)=f(x)$.
> 则$\Delta=E-I$, 且$E,I$可交换.
>
> $$
> \Rightarrow\ \Delta^n=(E-I)^n=\sum_{k=0}^n(-1)^{n-k}E^kI^{n-k}.
> $$
>
> 故有:
>
> $$
> \begin{aligned}
> \Delta^nf(x)
> &=\sum_{k=0}^n(-1)^{n-k}\binom nkE^kI^{n-k}f(x)\\
> &=\sum_{k=0}^n(-1)^{n-k}\binom nkf(x+k).
> \end{aligned}
> $$

$$
E^nf(x)=f(x+n)=(I+\Delta)^nf(x)=\sum_{k=0}^n\binom nk \Delta^kf(x).
$$

令$x=0\Rightarrow f(n)=\sum\limits_{k=0}^n\binom{n}{k}\Delta^k f(0)$.

> 差分算子例子:
>
> $$
> f(n)=n^4=\binom n1+14\binom n2+36\binom n3+24\binom n4.
> $$

例:

$$
\begin{aligned}
    f(x)&=x^n,\Delta f(x)=(x+1)^n-x^n\to n-1次多项式\\
    \Rightarrow&\Delta^n f(x)=n!=\sum_{k=0}^n(-1)^{n-k}\binom nk (x+k)^n\\
\end{aligned}
$$

令$x=0\Rightarrow n!=\sum\limits_{k=0}^n(-1)^{n-k}\binom nk k^n$.

- 差分$k$次:

$$
\Delta^k f(x)=\Delta^kx^n=\sum_{i=0}^k(-1)^{k-i}\binom ki (x+i)^n
$$

令$x=0\Rightarrow\Delta^k\dot{0}^n=\sum\limits_{i=0}^k(-1)^{k-i}\binom ki i^n=\sum\limits_{i=0}^k(-1)^{i}\binom ki (k-i)^n\to\color{red}\text{第二类Stirling数}(k!S(n,k))$.
($k!S(n,k)$: $n$个不同的球放入$k$个不同的盒子, 且每个盒子至少一个球的放法)

例子:

$$
\begin{aligned}
\Delta^k(x)_n&=(n)_k(x)_{n-k},&\Delta^k\lang x\rang_n=(n)_k\lang x+k\rang_{n-k},\\
\Delta^k\frac1{(x)_n}&=(-1)^k\frac{\lang n\rang_k}{(x+k)_{n+k}},&\Delta^k\frac1{\lang x\rang_n}=(-1)^k\frac{\lang n\rang_k}{\lang x\rang_{n+k}}.
\end{aligned}
$$

定理C: (二项式系数的同余性质)

$p$为素数, 则

$$
\binom{p}{k}\equiv0\pmod p \ \ or \ p\left|\binom pk\right.\quad (0<k<p),\ \binom p0=\binom pp=1,
$$

$$
\begin{aligned}
    \Rightarrow (1+x)^p&=\sum_{k=0}^p\binom pk x^k=1+\binom p1 x+\binom p2 x^2+\cdots+\binom p{p-1}x^{p-1}+x^p\\
    &\equiv 1+x^p\pmod p
\end{aligned}
$$

> 证明:
>
> 由$\binom pk=\frac{(p)_k}{k!}$为一整数, 即:$k!\,|\,(p)_k$.
>
> 而$(p)_k=p(p-1)_{k-1}$.
>
> 当$0<k<p$, $(k!,p)=1$, 于是$k!|(p-1)_{k-1}$.
>
> 令$(p-1)_{k-1}=h\cdot k!$($h$为整数).
>
> $\Rightarrow \binom pk =\dfrac{p\cdot h\cdot k!}{k!}=p\cdot h\equiv 0\pmod p$. 证毕.

## 重集的排列与组合

### 重集的排列

重集:

$$
\begin{aligned}
    N&=\{k_1a_1,k_2a_2,\cdots,k_na_n\}, &(有重数限制)\\
    M&=\{\infty\cdot a_1,\infty\cdot a_2,\cdots,\infty\cdot a_n\}, &(无重数限制)\\
\end{aligned}
$$

定义: 重集$M$的一个$k-$排列$\alpha$, 就是一个$M[k]$到$\{a_1,a_2,\cdots,a_n\}$的映射$\alpha$.

定理1: 重集$M$的$k-$排列总数为$n^k$.

**球盒模型**: $k$个不同的球放入$n$个不同的盒子里的不同放法.

定理2: 重集$N=\{n_1a_1,n_2a_2,\cdots,n_na_n\}$的全排列个数为:

$$
\frac{(n_1+n_2+\cdots+n_k)!}{n_1!n_2!\cdots n_k!},
$$

> 证明:
>
> 方法1: 对于重集$N$的$n$个元素的全排列, 直接选择,可以得到:
>
> $$
> \text{全排列个数}=\binom n{n_1}\binom{n-n_1}{n_2}\cdots\binom{n-n_1-n_2-\cdots-n_{k-1}}{n_k}=\frac{(n_1+n_2+\cdots+n_k)!}{n_1!n_2!\cdots n_k!},
> $$
>
> 方法2: 先选择,再除以重复的排列, 即得.

多项式系数:

$$
\begin{aligned}
\frac{(n_1+n_2+\cdots+n_k)!}{n_1!n_2!\cdots n_k!}&\triangleq\binom {n_1+n_2+\cdots+n_k}{n_1,n_2,\cdots,n_k}\\
(x_1+x_2+\cdots+x_k)^n&=\sum_{n_i}\binom{n}{n_1,n_2,\cdots,n_k}x_1^{n_1}x_2^{n_2}\cdots x_k^{n_k}\\
\end{aligned}
$$

球盒模型: $n$个不同的球放入$k$个不同的盒子, 其中第一个盒子有$n_1$个球, ... 第$k$个盒子有$n_k$个球的不同放法数.

考虑重集$N=\{n_1a_1,n_2a_2,\cdots,n_ka_k\}$的$r-$排列的计数, 其中$r<n,(n=n_1+n_2+\cdots+n_k), \exists n_i, \text{s.t.} r>n_i$.

### 重集的组合

$$
\begin{aligned}
    N&=\{k_1a_1,k_2a_2,\cdots,k_na_n\}, &(有重数限制)\\
    M&=\{\infty\cdot a_1,\infty\cdot a_2,\cdots,\infty\cdot a_n\}, &(无重数限制)\\
\end{aligned}
$$

定义: 重集$M$的一个$k-$组合$B$, 就是一个$M[k]$到$\{a_1,a_2,\cdots,a_n\}$的映射$B$.

几种等价形式:

1. $\varphi:\{a_1,a_2,\cdots,a_n\}\to\{0,1,2,\cdots\}$, 且$\sum_{i=1}^n\varphi(a_i)=k$.这样的映射全体与$M$ 的$k-$组合一一对应.
2. 不定方程$x_1+x_2+\cdots+x_n=k$, 其中$x_i$为非负整数. 方程的解集合与重集$M$的$k-$组合一一对应.
3. **球盒模型**, $k$个相同的球放入$n$个不同的盒子的不同放法数.

定理: 重集的$k-$组合数为

$$
\left\langle\begin{matrix}n\\k
\end{matrix}\right\rangle=\frac{\lang n\rang_k}{k!}=\binom{n+k-1}{k}.
$$

> 证明: (方法一: 用递推关系证明)
>
> 设$T(n,k)$表示不定方程$x_1+x_2+\cdots+x_n=k$的非负整数解的个数, 则方程的解可分为两种形式:
>
> 1.  $x_1=0$, 即$x_2+x_3+\cdots+x_n=k$的非负整数解, 共有$T(n-1,k)$个;
> 2.  $x_1\geqslant1$, 令$x_1'=x_1-1\geqslant0$, 方程的解等价于$x_1'+x_2+\cdots+x_n=k-1$的非负整数解, 共有$T(n, k-1)$个;
>
> 于是有$T(n,k)=T(n-1,k)+T(n, k-1)$.
>
> 又有初始值$T(n,0)=1, T(1, k)=1$(可以通过生成函数来求出$T(n,k)$
>
> 而$\left\langle\begin{matrix}n\\k
> \end{matrix}\right\rangle=\binom{n+k-1}{k}$也满足上述递推关系以及初值, 所以:
>
> $\Rightarrow T(n,k)=\binom{n-k+1}k$.

> 方法二: 从**球盒模型组合意义**出发证明, $k$个相同的球放入$n$个不同的盒子中.
>
> $n$个盒子并排放, 共有$n-1$条公共边.
>
> $n-1$条公共边和$k$个球共占用$n+k-1$个位置.
>
> 每一种放法对应于从$n+k-1$个位置中选$n-1$个位置作为盒子的公共边.
>
> 于是共有$\binom{n+k-1}{n-1}=\binom{n+k-1}k$种方法.

> 方法三:(用隔板法证明)
>
> $k$个相同的球放入$n$个不同的盒子, 且每个盒子至少1个球(隔板问题)
>
> 即从$k$个球中间的$k-1$个位置选择$n-1$位置中放置隔板,共有$\binom{k-1}{n-1}$种.
>
> 对应不定方程$x_1+x_2+\cdots+x_n=k$的**正整数解**的个数.
>
> 而所求为$x_1+x_2+\cdots+x_n=k$的非负整数解的个数, 转化为正整数解,等价于
>
> $$
> x_1'+x_2'+\cdots+x_n'=k+n\quad(x_i'=x_i+1)
> $$
>
> 的正整数解的个数:$\binom{n+k-1}{n-1}={n+k-1\choose k}$.

## 回顾

例题: 设$S$是由四种元素$a,b,c,d$组成的多重集$\{10\cdot a,10\cdot b,10\cdot c,10\cdot d\}$, 问$S$使得$a,c$至少出现1次, $b$至少出现两次, $d$至少出现3次的$9-$组合数是多少?

> 解: (考虑等价形式)
>
> 即考虑$x_1+x_2+x_3+x_4=9$,其中$\begin{cases}x_1\geq 1,\\x_2\geq 2,\\x_3\geq 1,\\x_4\geq 3,\end{cases}$,的整数解的个数. 令$y_1=x_1-1$, $y_2=x_2-2$, $y_3=x_3-1$, $y_4=x_4-3$.
>
> 则等价于$y_1+y_2+y_3+y_4=9-7=2$的非负整数解的个数.
>
> 由重集$M$的$k-$组合数$\Rightarrow {4+2-1\choose 2}={5\choose2}=10$.

<font color="red">注: </font>

重集$S=\{n_1a_1,n_2a_2,\cdots,n_ka_k\}$的$r-$组合.

1.  若$r\leq n_i(1\leq i\leq n)$则等价于无重复限制集合的$r-$组合,(有下界的情况较好处理)

    即$\iff S=\{\infty a_1,\infty a_2,\cdots,\infty a_k\}$的$r-$组合.

2.  若$r$大于其中一个或多个$n_i$时, 考虑$r-$组合.

    $\iff x_1+x_2+\cdots+x_k=r$(对于有上界的情况, 可以使用容斥原理, 生成函数方法求解)

    其中$0\leq x_i\leq n_i,i=1,2,...,k$.

例子: 证明不等式$x_1+x_2+\cdots+x_n\leq k$的非负整数解的个数为${n+k\choose k}$,并给出

$$
\sum_{j=0}^k{n+j-1\choose j}={n+k\choose k}
$$

的组合解释.

> 证明:
>
> $x_1+x_2+\cdots+x_n\leq k,x_i\geq0,1\leq i\leq n$,
>
> $\iff x_1+x_2+\cdots+x_n+x_{n+1}= k, x_i\geq 0,1\leq i \leq n+1$.
>
> 故非负整数解有$\binom{n+1+k-1}k=\binom{n+k}k$个.

> 另一方面, $x_1+x_2+\cdots+x_n\leq k,x_i\geq0,1\leq i\leq n$, 等价于
>
> $x_1+x_2+\cdots+x_n=j, 0\leq j\leq k$的解的并.
>
> 上述方程的解的个数为$\binom{n+j-1}j$, 由加法原理得到: $\sum\limits_{j=0}^k{n+j-1\choose j}={n+k\choose k}$.

考虑$\color{red}集合[n]=\{1,2,...,n\}上的两个计数问题$.

## 例子:(Gergonne, 1812)

- $[n]$的一个$k$元子集称为$l$间隔的, 若其中任意两个数之差大于$l$.

证明: $[n]$的$l$间隔的$k$ 元子集的个数为

$$
f_l(n,k)={n-l(k-1)\choose k}.
$$

> - $l=0$: $[n]$的$k$ 元子集个数为$n\choose k$.
> - $l=-1$: $[n]$的可重复$k$元子集个数为$n+k-1\choose k$.

> 证明:(方法一, 考虑方程组解和子集之间的一一对应)
>
> 考虑$[x]$的$l$间隔的$k$元子集$\{a_1,a_2,...,a_k\}_{(\leq)}$, 其中$1\leq a_1\leq a_2\leq \cdots\leq a_k\leq n,\quad(a_{i+1}-a_i>l)$.
>
> 即
>
> $$
> \underbrace{1,...,}_{x_1}\,a_1\underbrace{,...,}_{x_2}\,a_2\underbrace{,...,}_{x_3}\,a_3,...,a_k\underbrace{,...,n}_{x_{k+1}}
> $$
>
> 用$x_i$表示上图中元素的个数, 则由$a_1\geq1,a_{i+1}-a_i>l,a_k\leq n$.
>
> $\Rightarrow x_1\geq 0,x_i\geq l(i=2,...,k), x_{k+1}\geq0$.
>
> 且$x_1+x_2+\cdots+x_{k+1}= n-k$.
>
> 即建立了$[n]$的$l$间隔的$k$元子集与下述方程的解的一一对应
>
> $$
> x_1+x_2+\cdots+x_{k+1}= n-k, x_1\geq 0,x_i\geq l(i=2,...,k), x_{k+1}\geq0,
> $$
>
> (平移后去掉下界)令$y_1=x_1\geq0,y_i=x_i-l\geq0,\ (2\leq i\leq k),y_{k+1}=x_{k+1}\geq0$, 则原方程等价于
>
> $$
> y_1+\cdots+y_{k+1}=n-k-l(k-1)
> $$
>
> 的非负整数解的个数, 即为${n-k-l(k-1)+k+1-1\choose n-k-l(k-1)}={n-l(k-1)\choose k}$.

---

> 证明(方法二, 任意两数之差大于$l$, 通过插空的方法生成满足条件的间距)
>
> - $[n]$的$l$间隔的$k$元子集可由下列方法构成,
> - 先去掉$l(k-1)$个间隔, 再从剩余的$n-l(k-1)$个数中取$k$个, 故共有${n-l(k-1)\choose k}$种方法.

$l$间隔的$k-$排列问题直接乘以$k!$即可.

## 例子: 投票(选举)问题

(Bertrand, 1887提出) ($\text{Ardr}\acute{\text{e}}$, 1887解决)

设$p$和$q$满足$1\leq p<q$且 $ p+q=n$的整数, $f(p, q)$表示从$O(0,0)$到$M(p,q)$是除$O(0,0)$之外与直线$y=x$不交的格路数. 证明:

$$
f(p,q)=\frac{q-p}{q+p}\binom np.
$$

> 利用反射对应原理($\text{Ardr}\acute{\text{e}}$反射原理):
> $\text{Ardr}\acute{\text{e}}$反射:
> 从$A$到$M$**穿过**或**接触**$l$的格路数与$A$的对应点$A'$到$M$的格路数相等(存在一一对应).

> 证明: $f(p,q)$相当于从$A(0,1)$到$M(p,q)$是与直线$y=x$不交的格路数,
> 等于从$A(0,1)$到$M(p,q)$的所有格路数减去从$A(0,1)$到$M(p,q)$穿过或接触$y=x$的格路数.
>
>   <div align="center"><img src="https://s2.loli.net/2021/12/15/UNdEkrxL32TBuMW.png" style="zoom:33%;" /></div>
>
> 由$\text{Ardr}\acute{\text{e}}$反射,
>
> $$
> \Rightarrow f(p,q)=\binom{p+q-1}p-\binom{p+q-1}{p-1}=\frac{q-p}{q+p}\binom{p+q}p=\frac{q-p}{q+p}\binom np.
> $$

## 圈集的排列与组合

设$N$为置于一个圆圈上的$n$个点的有限集, 圈上的两个相邻点距离相等, 则集合等同于模$n$的剩余类集$[\overline{n}]=\{\bar{0},\bar{1},\bar{2},...,\overline{n-1}\}$.

定理1: 集合$N$的圈上的$k-$排列(即$[\bar{n}]$的$k-$排列)个数为$\frac{(n)_k}k$.

> 证明:
>
> 集合$N$的$k-$排列个数为$(n)_k$ ($a_1a_2...a_k$)
>
> 而$k$个球的排列有$k$种轮换, 这些轮换在圈上是一样的, 故集合$N$的圈上非$k-$排列个数为$\frac{(n)_k}k$.

例子:(Kaplamsky, 1943)

$[\bar{n}]$的一个$k$元子集称为$l$间隔的, 若其中任两个数在圈上之差大于$l$(圈上两点之间的任意一段弧上面至少有$l$个点). 证明: $[\bar{n}]$的$l$间隔的$k$元子集的个数为

$$
g_l(n,k)=\frac n{n-kl}\binom{n-kl}k.
$$

- $l=0$: 直接为$k-$组合.

直线上的$l$间隔$k$元子集个数为:

$$
f_l(n,k)=\binom{n-l(k-1)}{k}
$$

> $[\bar{10}]=\{\bar0,\bar1,...,\bar9\}$的$2$间隔的$3$元子集的个数为$10$. 分别如下
>
> $$
> \begin{aligned}
> A_0:&\ \ \bar0\bar3\bar6,\bar0\bar3\bar7,\bar0\bar4\bar7,\\
> A_1:&\ \ \bar1\bar4\bar7,\bar1\bar4\bar8,\bar1\bar5\bar8,\\
> A^*:&\begin{cases}
> \bar2\bar5\bar8,\bar2\bar5\bar9,\bar2\bar6\bar9,\\
> \bar3\bar6\bar9,
> \end{cases}
> \end{aligned}
> $$

> 证明:
>
> 设$A$表示$[\bar{n}]$的$l$间隔$k$元子集的集合, $g_l(n,k)=|A|$,
> 设
>
> $$
> \begin{cases}
> A_i=\{P\,|\,P\in A, P\cap[\bar l]\},\quad (i=0,1,2,...,l-1)\\[3pt]
> A^*=\{P\,|\,P\in A, P\cap [\bar{l}]=\varnothing\}
> \end{cases}
> $$
>
> $\Rightarrow A$为$A_i$与$A^*$的**不相交子集的并**. 于是有
>
> $$
> g_l(n,k)=|A|=|A^*|+\sum_{i=0}^{l-1}|A_i|.
> $$
>
> 由$P\in A_i$等价于从$n-2l-1$个元素的直线段$[i+l+1,\cdots,i+n-l-1]$的$l$间隔的$k-1$元子集$P'=P\backslash{\bar{i}}$, 其计数为$f_{l}(n-2l-1, k-1)$.
> 于是
>
> $$
> |A_i|=f_{l}(n-2l-1, k-1)={n-kl-1\choose k-1},\quad(0\leq i\leq l-1).
> $$
>
> 类似的, $P\in A^*\iff$从$n-l$个元素的直线段$[l,\cdots,n-1]$的$l$间隔的$k$元子集$P$, 其计数为$f_l(n-l,k)$,
>
> $$
> |A^*|=f_l(n-l, k)=\binom{n-kl}k,
> $$
>
> 于是
>
> $$
> \begin{aligned}
> g_l(n,k)&=|A^*| +\sum_{i=0}^{l-1}|A_i|\\
> &=f_L(n-l,k)+l\cdot f_l(n-2l-1,k-1)\\
> &=\binom{n-k-1}k+l\binom{n-kl-1}{k-1}=\frac{n}{n-kl}\binom{n-kl}k.
> \end{aligned}
> $$

## 生成函数(发生函数, 母函数,generating function)

又称为"**形式幂级数**", 其系数不一定收敛, 不关心是否收敛的问题.

### 分类

简单序列$\{a_n\}$

- 普通型生成函数:$\Phi(t)=\sum\limits_{n=0}^\infty a_nt^n\Rightarrow a_n=[t^n]\Phi(t)$.($a_n$是$\Phi(t)$中$t^n$的系数)
- 指数型生成函数: $\Psi(t)\sum\limits_{n=0}^{\infty}a_n\dfrac{t^n}{n!}\Rightarrow a_n=n![t^n]\Psi(t)$.

多重序列$\{a_{n,k}\}$:

- 普通生成函数: $\Phi(t,u)=\sum\limits_{n,k\geq0}a_{n,k}t^nu^k$.
- 指数生成函数: $\Psi(t,u)=\sum\limits_{n,k\geq0}a_{n,k}\dfrac{t^n}{n!}\dfrac{u^k}{k!}$.
- 混合生成函数: $\cdots$

例子:

序列$a_n=\binom xn=\frac{(x)_n}{n!}$.

$$
\Phi(t)=\sum\limits_{n=0}^\infty \binom xnt^n=\sum_{n\geq0}(x)_n\frac{t^n}{n!}=(1+t)^x
$$

于是

$$
\begin{aligned}
\sum_{n\geq0}(x+y)_n\frac{t^n}{n!}&=(1+t)^{x+y}=(1+t)^x(1+t)^y\\
&=\sum_{k\geq0}(x)_k\frac{t^k}{k!}\sum_{l\geq0}(y)_l\frac{t^l}{l!}
\end{aligned}
$$

比较两端$\dfrac{t^n}{n!}$的系数,有

$$
\begin{aligned}
(x+y)_n&=\sum_{k=0}^n\binom nk (x)_k(y)_{n-k}\\
\iff \binom {x+y}n&=\sum_{k=0}^n\binom xk\binom y{n-k}\quad {\color{red} \text{Chu-Vandemonde卷积公式}}
\end{aligned}
$$

类似, 由$\lang x\rang_n=x(x+1)\cdots(x+k-1)=(-1)^n(-x)_n$,

$$
\Rightarrow\sum\limits_{n=0}^\infty \lang x\rang_n \frac{t^n}{n!}=\sum_{n\geq0}(-x)_n\frac{(-t)^n}{n!}=(1-t)^{-x}
$$

$$
\begin{aligned}
\Rightarrow \lang x+y\rang_n&=\sum_{k=0}^n\binom nk \lang x\rang_k\lang y\rang_{n-k}\\
\iff \left\langle \begin{matrix}x+y\\n\end{matrix}\right\rangle&=\sum_{k=0}^n\left\langle \begin{matrix}x\\k\end{matrix}\right\rangle\left\langle \begin{matrix}y\\n-k\end{matrix}\right\rangle
\end{aligned}
$$

例子: (Fibonacci数)

$$
\left\{\begin{aligned}
F_n&=F_{n-1}+F_{n-2},\quad(n\geq2),\\
F_0&=0,\ F_1=1.
\end{aligned}\right.
$$

> 生成函数: 令
>
> $$
> \Phi =\Phi(t)=\sum_{n\geq0}F_nt^n.
> $$
>
> $$
> \begin{aligned}
> \Rightarrow\Phi&=t+\sum_{n\geq2}F_nt^n=t+\sum_{n\geq 2}(F_{n-1}+F_{n-2})t^n\\
> &=t+\sum_{n\geq2}F_{n-1}t^n+\sum_{n\geq2}F_{n-2}t^n\\
> &=t+t\Phi+t^2\Phi
> \end{aligned}
> $$
>
> 于是$\Phi=\sum\limits_{n\geq0}F_nt^n=\dfrac t{1-t-t^2}$, 由$1-t-t^2=(1-\alpha t)(1-\beta t)$, $\alpha=\dfrac{1-\sqrt5}2,\,\beta=\dfrac{1+\sqrt5}2$.
>
> $$
> \Rightarrow \Phi=\frac1{\beta-\alpha}\left(\frac1{1-\beta t}-\frac1{1-\alpha t}\right)=\frac1{\sqrt5}\sum_{n\geq0}(\beta^n-\alpha^n)t^n,
> $$
>
> 取$t^n$的系数, 有
>
> $$
> F_n=[t^n]\Phi(t)=\frac1{\sqrt5}(\beta^n-\alpha^n). \text{\color{red}(显式表达)}
> $$
>
> <font color="red">渐进表达:</font>
>
> $$
> n\to\infty ,F_n\sim\frac1{\sqrt{5}}\beta^n=\frac1{\sqrt5}\left(\frac{1+\sqrt5}2\right)^n.
> $$
>
> 另一方面,
>
> $$
> \begin{aligned}
> \Phi&=\frac t{1-t-t^2}=\frac t{1-t(1+t)}=t\sum_{k\geq0}t^k(1+t)^k\\
> &=\sum_{k\geq0}t^{k+1}\sum_{i=0}^k\binom kit^i
> \end{aligned}
> $$
>
> 再取$t^n$的系数,
>
> $$
> \Rightarrow F_n=[t^n]\Phi(t)=\sum_{i\geq0}\binom{n-i-1}i=\sum_{i=0}^{\left[\frac{n-1}2\right]}\binom{n-i-1}i.
> $$
>
> $$
> F_{n+2}= \sum_{i=0}^{\left[\frac{n+1}2\right]}\binom{n-i+1}i.
> $$
>
> $[n]$的$l$间隔的$k$子集个数为$\binom{n-l(k-1)}{k}$, 所以 $F_{n+2}$表示$[n]$的所有$1$间隔子集数.

例3:

二项式系数$a_{n,k}=\binom nk$.

$$
\begin{aligned}
\Phi(t, u)&=\sum_{n,k\geq0}a_{n,k}t^n u^k=\sum_{n,k\geq0}\binom nkt^nu^k=\sum_{n\geq0}t^n\left(\sum_{k\geq0}\binom nk u^k\right)\\
&=\sum_{n\geq0}t^n(1+u)^n=\frac1{1-t(1+u)}.
\end{aligned}
$$

特别地, 当$u=t$时,

$$
\sum_{n,k\geq0}\binom nk t^{n+k+1}=\frac t{1-t(1+t)}=\sum_{n\geq0}F_nt^n, \Rightarrow F_n=\sum_{i\geq0}\binom {n-i-1}i.
$$

混合型生成函数

$$
\varTheta (t,u)=\sum_{n,k\geq0}\binom nk\frac{t^n}{n!}u^k=\sum_{n\geq0}\frac{t^n}{n!}(1+u)^n=\exp\big(t(1+u)\big).
$$

$$
\begin{aligned}
\Psi(u,t)&=\sum_{n,k\geq0}\binom nk \frac{t^n}{n!}\frac{u^k}{k!}=\sum_{k\geq0}\sum_{n\geq k}\frac{t^{n-k}}{(n-k)!}\frac{(ut)^k}{(k!)^2}\\
&=\sum_{k\geq0}\frac{(ut)^k}{(k!)^2}\sum_{n\geq 0}\frac{t^n}{n!}=\mathrm{e}^t\sum_{k\geq0}\frac{(ut)^k}{(k!)^2}\\
&=\mathrm{e}^t I_0(2\sqrt{ut})
\end{aligned}
$$

其中

$$
I_0(z)=\sum_{k\geq0}\frac1{(k!)^2}\left(\frac z2\right)^{2k}
$$

称为**修正的$0$阶Bessel函数**.

其他类型的生成函数:

$$
\begin{aligned}
\Omega(t)&=\sum_{n\geq0}a_n\frac{n!}{\lang t\rang_{n+1}}\to\text{阶乘生成函数}\\
\Lambda(t)&=\sum_{n\geq1}a_n\frac{t^n}{1-t^n}\to\text{Lambert生成函数}\\
N(t)&=\sum_{n\geq0}a_n\frac{(t)_n}{n!}\to\text{Newton生成函数}
\end{aligned}
$$

## 常见的生成函数

### Bernoulli和Euler数及多项式

定义:

$$
\sum_{n\geq 0}B_n\frac{t^n}{n!}=\frac t{e^t-1},\quad \sum_{n\geq 0}B_n(x)\frac{t^n}{n!}=\frac {te^{tx}}{e^t-1},\\
\sum_{n\geq 0}E_n\frac{t^n}{n!}=\frac1{\cosh t}=\frac {2e^t}{1+e^{2t}},\quad \sum_{n\geq 0}E_n(x)\frac{t^n}{n!}=\frac {2e^{tx}}{1+e^t},
$$

一些展开项:

$$
\begin{aligned}
\Rightarrow &B_0=1,B_1=-\frac12,B_2=-\frac16,B_3=0,B_4=-\frac1{30},B_5=0,B_6=\frac1{42},\cdots\\
&E_0=1,E_1=0,E_2=-1,E_3=0,E_4=5,E_5=0,E_6=-61,\cdots\\[5pt]
\Rightarrow &B_0(x)=1,B_1(x)=x-\frac12,B_2(x)=x^2-x+\frac16,B_3(x)=x^3-\frac32x^2+\frac x2,\cdots\\
&E_0(x)=1,E_1(x)=x-\frac12,E_2(x)=x^2-x,E_2(x)=x^3-\frac32x^2+\frac14,\cdots
\end{aligned}
$$

而

$$
\sum\limits_{n\geq 0}B_n\frac{t^n}{n!}=\frac t{e^t-1}\Rightarrow (e^t-1)\sum_{n\geq0}B_n\frac{t^n}{n!}=t,
$$

即:

$$
\sum_{l\geq1}\frac{t^l}{l!}\cdot\sum_{k\geq0}B_k\frac{t^k}{k!}=t, 令k+l=n,\\
\Rightarrow \sum_{n\geq1}\frac{t^n}{n!}\cdot\sum_{k=0}^{n-1}\binom nkB_k=t,
$$

- 若两端取$t$的系数, 得到$B_0=1$,

- 取$t^n$的系数, 得到$\frac1{n!}\sum\limits_{k=0}^{n-1}\binom nkB_k=0$, ($n>1$),
  即$\sum\limits_{k=0}^n\binom{n+1}kB_k=0(n>0)$.
  $$
  \Rightarrow (n+1)B_n+\sum_{k=0}^{n-1}\binom{n+1}kB_k=0,\\
  \Rightarrow B_n=-\frac1{n+1}\sum_{k=0}^{n-1}\binom{n+1}kB_k.
  $$

注:

$$
\sum_{n\geq 0}B_n\frac{t^n}{n!}+\frac t2=\frac t{e^t-1}+\frac t2=\frac{te^t+t}{2e^t-2},
$$

右端为偶函数, 于是其展开项的奇数次幂都为0.

### 重要性质

1.  $B_n=B_n(0),\quad E_n=2^nE_n\left(\frac12\right)$;

2.  $B_{2k+1}=E_{2k-1}=0,\quad k=1,2,3,...$;

3.  $B'_n(x)=nB_{n-1}(x),\quad E_n'(x)=nE_{n-1}(x)$;

4.  $B_n(x+1)-B_n(x)=nx^{n-1},\quad E_n(x+1)+E_n(x)=2x^n$;

5.  $B_n(x+y)=\sum\limits_{k=0}^n\binom nk B_k(x)y^{n-k},\ E_n(x+y)=\sum\limits_{k=0}^n\binom nk E_k(x)y^{n-k}$; (函数的卷积公式)

    $$
    \sum_{n\geq 0}B_n(x+y)\frac{t^n}{n!}=\frac {te^{(x+y)t}}{e^t-1}=\frac {te^{xt}}{e^t-1}\cdot e^{yt}=\sum_{k\geq0}B_k(x)\frac{t^k}{k!}\cdot\sum_{l\geq0}\frac{y^l}{l!}t^l,
    $$

    比较两端$t^n$的系数, 得到上式成立.

6.  $E_n(x)=\sum\limits_{k=0}^n\binom nk \frac{E_k}{2^k}{(x-\frac12)}^{n-k}$;

7.  $B_n(1-x)=(-1)^nB_n(x),\ E_n(1-x)=(-1)^nE_n(x)$;

8.  $B_n(mx)=m^{n-1}\sum\limits_{k=0}^{m-1}B_k(x+\frac km)$;
    $$
    E_n(mx)=
    \begin{cases}
    m^n\sum\limits_{k=0}^{m-1}(-1)^kE_n\left(x+\frac mk \right),\quad(m=1,3,5,...)\\
    -\frac2{n+1}m^n\sum\limits_{k=0}^{m-1}(-1)^kB_{n+1}\left(x+\frac mk\right), \quad(m=2,4,6,...)
    \end{cases}
    $$

### 应用: 计算幂和

$$
S_k(n)=\sum_{i=0}^ni^k=1^k+2^k+\cdots+n^k.
$$

#### 交错幂和

$$
T_k(n)=\sum_{i=0}^n(-1)^ii^k.
$$

考虑形式级数$\sum\limits_{k\geq0}S_k(n)\dfrac{t^{k+1}}{k!}$, 化简得到

$$
\begin{aligned}
\sum\limits_{k\geq0}S_k(n)\dfrac{t^{k+1}}{k!}&=\sum_{k\ge0}\sum_{i=0}^k\frac{t^{k+1}}{k!}=\sum_{i=0}^nt\sum_{k\ge0}\frac{(it)^k}{k!}\\
&=\sum_{i=0}^nte^{it}=\sum_{i=0}^n(e^t-1)\cdot\sum_{m\ge0}B_m(i)\frac{t^m}{m!}\\
&=\sum_{m\ge0}\sum_{i=0}^nB_m(i)\frac{t^m}{m!}\cdot\sum_{p\ge0}\frac{t^p}{p!}-\sum_{m\ge0}\sum_{i=0}^nB_m(i)\frac{t^m}{m!}\\
&=\sum_{m\ge0}\sum_{j=0}^m\binom mj\sum_{i=0}^nB_j(i)\frac{t^m}{m!}-\sum_{m\ge0}\sum_{i=0}^nB_m(i)\frac{t^m}{m!}\\
\end{aligned}
$$

两边取$\left[\dfrac{t^{k+1}}{k!}\right]$, 并取$m=k+1$,

$$
\begin{aligned}
S_k(n)&=\frac1{k+1}\sum_{i=0}^n\left[\sum_{j=0}^{k+1}\binom{k+1}{j}B_j(i)-B_{k+1}(i)\right]\\
&=\frac1{k+1}\sum_{i=0}^n\big(B_{k+1}(i+1)-B_{k+1}(i)\big)\qquad(*)\\
&=\frac1{k+1}\big(B_{k+1}(n+1)-B_{k+1}(0)\big)
\end{aligned}
$$

其中, $(*)$应用了性质5.

$$
S_k(n)=\frac{B_{k+1}(n+1)-B_{k+1}}{k+1}=\frac1{k+1}\sum_{i=0}^k\binom{k+1}iB_i\cdot (n+1)^{k+1-i}
$$

于是我们得到:

$$
S_1(n)=\frac{n(n+1)}2,\quad S_2(n)=\frac{n(n+1)(2n+1)}6,\quad S_3=\frac{n^2(n+1)^2}4,\cdots
$$

类似,

$$
T_k(n)=\frac{(-1)^nE_k(n+1)+E_k(0)}2
$$

### Bernoulli多项式和Euler多项式的推广

高阶Bernoulli多项式$B_n^{(\alpha)}(x)$, 高阶Euler多项式$E_n^{(\alpha)}(x)$.

定义:

$$
\sum_{n\geq 0}B_n^{(\alpha)}(x)\frac{t^n}{n!}=e^{tx}\left(\frac {t}{e^t-1}\right)^\alpha,\quad\sum_{n\geq 0}E_n^{(\alpha)}(x)\frac{t^n}{n!}=e^{tx}\left(\frac {2}{1+e^t}\right)^\alpha,
$$

类似的性质:

1.  $B_{n}^{(\alpha)}(x+1)-B_n^{(\alpha)}(x)=nB_{n-1}^{(\alpha-1)}(x)$,

    $E_{n}^{(\alpha)}(x+1)+E_n^{(\alpha)}(x)=2E_{n}^{(\alpha-1)}(x)$;

2.  $B_n^{(\alpha+\beta)}(x+y)=\sum\limits_{k=0}^n\binom nkB_k^{(\alpha)}(x)B_{n-k}^{(\beta)}(y)$,
    $E_n^{(\alpha+\beta)}(x+y)=\sum\limits_{k=0}^n\binom nkE_k^{(\alpha)}(x)E_{n-k}^{(\beta)}(y)$;

    $\beta=0,\begin{cases}
     B_n^{(\alpha)}(x+y)=\sum\limits_{k=0}^n\binom nkB_k^{(\alpha)}(x)y^{n-k},\\
     E_n^{(\alpha)}(x+y)=\sum\limits_{k=0}^n\binom nkE_k^{(\alpha)}(x)y^{n-k},
     \end{cases}$

### Genocchi数$G_n$

定义:

$$
\sum_{n\geq1}G_n\frac{t^n}{n!}=\frac{2t}{e^t+1}
$$

$G_3=G_5=G_7=\cdots=0$, $G_{2m}=2(1-2^{2m})B_{2m}=2mE_{2m-1}(0)$.

## 生成函数在排列组合中的应用

- 普通生成函数:$f(x)=\sum\limits_{n\geq0}a_nx^n$, $g(x)=\sum\limits_{n\geq 0}b_nx^n$,

  $$
  h(x)=f(x)g(x)=\sum_{n\geq0}c_nx^n\iff c_n=\sum_{k=0}^na_kb_{n-k}.
  $$

  **特例**: 取$b_{k}=1$, 知$\sum\limits_{k=0}^na_k$ 的生成函数为$\frac1{1-x}f(x)$.

- 指数型生成函数: $f(x)=\sum\limits_{n\geq0}a_n\dfrac{x^n}{n!}$, $g(x)=\sum\limits_{n\geq0}b_n\dfrac{x^n}{n!}$.
  $$
  h(x)=f(x)g(x)=\sum_{n\geq0}c_n\frac{x^n}{n!}\iff c_n=\sum_{k=0}^n\binom nk a_kb_{n-k}.
  $$
  **特例**: 取$b_k=1$,知$\sum\limits_{k=0}^n\binom nka_k$的生成函数为$e^xf(x)$.

### 普通生成函数之应用: 组合

1.  $(1+x)(1+x)\cdots(1+x)=(1+x)^n=\sum\limits_{k=0}^n\binom nk x^k$,

    从$n$个不同的物体中不允许重复地选取$k$个物体的方法数为$\binom nk$.
    $k$个相同的球放入$n$个不同的盒子, 每个盒子**至多**有一个球的方法数. <font color="red">单射</font>

2.  允许重复:

    $$
    (1+x+x^2+\cdots)^n=\frac{1}{(1-x)^n}=\sum_{k\geq0}\binom {-n}k(-1)^{k}x^k\\
    =\sum_{k\geq0}\binom{n+k-1}kx^k=\sum_{k\geq0}\left\langle\begin{matrix}n\\k\end{matrix}\right\rangle x^k.
    $$

    $n$个不同的物体, 允许重复选取$k$个物体的方法数为$\binom{n+k-1}k$
    $k$个相同的球放入$n$个不同的盒子, 盒子中的球数量**不加限制**.<font color="red">映射(不加限制)</font>

3.  若每个物体至少选取一次.
    $$
    (x+x^2+\cdots)^n=x^n\frac1{(1-x)^n}=\sum_{k\geq0}\binom{n+k-1}kx^{n+k}\\(r=n+k)\qquad=\sum_{r\geq n}\binom{r-1}{r-n}x^r=\sum_{r\geq n}\binom{r-1}{n-1}x^r.
    $$
    从$n$个不同的物体中允许重复的选取$k$个, 且每个物体至少出现$k$次的方法数为$\binom{k-1}{n-1},\quad(k\geq n)$.
    $k$个相同的球放入$n$个不同的盒子, 且每个盒子**至少**有一个球. <font color="red">满射</font>

不定方程之解的个数也可以这样来求解.

### 指数生成函数之应用: 排列

1.  从$n$个不同物体中不允许重复的选取$k$物体进行排列的方法数为$(n)_k$, 即$(1+x)^n$展开式中$\frac{x^k}{k!}$的系数.
    $k$个不同的球放入$n$个不同的盒子里, 每个盒子至多一个球的方法数. <font color="red">单射</font>

2.  从$n$个不同物体中允许重复的选取$k$物体进行排列的方法数为$n^k$, $(1+x+\frac{x^2}{2!}+\cdots)^n$的展开式中$\frac{x^k}{k!}$的系数.
    $k$个不同的球放入$n$个不同的盒子里, 每个盒子中球不加限制的方法数.<font color="red">映射</font>

3.  $n$个不同物体中不允许重复的选取$k$物体, 且每个物体至少出现一次, 进行排列的方法数为 $(x+\frac{x^2}{2!}+\cdots)^n$的展开式中$\frac{x^k}{k!}$的系数.
    $$
    (e^x-1)^n=\sum_{k\geq0}\left(\sum_{i=0}^n (-1)^{n-i}\binom nii^k \right)\frac{x^k}{k!}.
    $$
    方法数为$\sum\limits_{i=0}^n (-1)^{n-i}\binom nii^k=n!S(k,n)$(第二类Stirling数).
    $k$个不同的球放入$n$个不同的盒子里, 每个盒子至少一个球的方法数. <font color="red">满射</font>

## 加括号问题(Catalan数)

### Catalan问题

考虑$n$个字母$x_1,x_2,...,x_n$的逐次乘积计算的不同方法数$a_n$. (假定乘积计算不适合结合律和交换律)

$a_2=1,a_3=2.a_4=5$.

可以用加括号方式表示, 或者二叉树表示(更加直观)

<img src="https://s2.loli.net/2021/12/15/B3nNu8smdopLZIO.png" style="zoom:50%;" />
$$
a_4=5,\quad (x_1x_2)(x_3x_4),\ ((x_1x_2)x_3)x_4),\ (x_1(x_2x_3))x_4,\
x_1((x_2x_3)x_4),\ x_1(x_2(x_3x_4))
$$

注意到$n$个字母的最后一次运算, 是在前$k$个字母的积与后$n-k$个字母的积之间进行的 ($1\leq k\leq n-1$).故有

$$
a_n=\sum_{k=1}^{n-1}a_ka_{n-k},(n\geq2)
$$

(Catalan数的其他组合解释)

### 凸多边形的三角剖分

<img src="https://s2.loli.net/2021/12/15/7tBvZFM8oSkmgWV.png" style="zoom:60%;" />

$c_3=5$,$c_n=\frac1{n+1}\binom {2n}n$表示正$n+2$边形的三角剖分数.

### 控制路径($\mathrm{Andr\acute{e}}$)

从$A(0,2)$到$B(n-2, n)$的路径, "$($"对应重垂直步, 任何不同于$x_{n-1}, x_n$的字母对应水平步.

- 从$A(0,2)$到$B(n-2,n)$且与直线$y=x$不交的路径的个数.

以$c_3=5$为例:

<img src="https://s2.loli.net/2021/12/15/pfiJCTjXMqmy6u2.png" style="zoom:45%;" />

### 投票问题的特例

$A(0,0)\to B(p,q)$除$A$外与$y=x$不交

$$
\frac{q-p}{q+p}\binom {p+q}p
$$

对应了$p=n-2,q=n$,

$$
\Rightarrow a_n=\frac2{2n-2}\binom{2n-2}n=\frac1{n-1}\binom{2n-2}n=\frac1n\binom {2n-2}{n-1}.
$$

### Dyck路径

从$(0,0)$到$(2n,0)$, 只能走斜上和斜下($\nearrow,\searrow$, 不穿过$x$轴)

<img src="https://s2.loli.net/2021/12/15/yQGHUvaLlDg3d4j.png" style="zoom:50%;" />

第一次接触$x$轴($0\leqslant k\leqslant n-1$), 于是

$$
c_n=\sum_{k=0}^{n-1}c_kc_{n-1-k}\iff c_{n+1}=\sum_{k=0}^nc_kc_{n-k},\\
c_n=\frac1{n+1}\binom{2n}n
$$

坐标系旋转$45^\circ$, 得到:

从$(0,0)$到$(n,n)$, $\longrightarrow, \uparrow$, 在$y=x$上方, 但不穿过$y=x$.

<img src="https://s2.loli.net/2021/12/15/jFDREA4pC5cKwnS.png" style="zoom:33%;" />

推广, 从$(0,0)$到$(p,q)$, $(q\geqslant p)$, 在$y=x$上方, 且不穿过$y=x$的路径数.

$$
f(p,q)=\frac{q-p+1}{q+1}\binom{p+q}p=\frac{q-p+1}{q+p+1}\binom{q+p+1}p,
$$

$p=q=n,f(n,n)=\frac1{n+1}\binom{2n}n\to$Catalan 数.

### Wedderburn-Etheringtan 可交换加括号问题

设$X\in E$, $E$可交换, $b_n$表示所有因子相乘都等于$X^n$的方法数.

$$
\begin{cases}
b_2=1&X\cdot X=X^2\\
b_3=1&(X\cdot X)\cdot X=X\cdot(X\cdot X)=X\cdot X^2\\
b_4=2&(X\cdot X)(X\cdot X),\\
&((X\cdot X)\cdot X)\cdot X
=(X\cdot(X\cdot X))\cdot X\\
&=X\cdot((X\cdot X)\cdot X)=X\cdot(X\cdot(X\cdot X))\\
&=X\cdot((X\cdot X^2))
\end{cases}
$$

(这里也可以使用二叉树表示, 只不过这里的二叉树相同$\iff$其中一棵可以经过这些点的垂直轴反射变换为另外一棵.)

通过观察最后一次运算, (根据$n$为奇数还是偶数分情况讨论)

偶数情况下最后一项为$b_p$的$2-$重复组合, 即$\binom{b_p+2-1}2=\binom{b_p+1}2$.

$$
\begin{cases}
b_{2p+1}=b_1b_{2p}+b_2b_{2p-1}+\cdots+b_pb_{p+1},&(p\geqslant1)\\
b_{2p}=b_1b_{2p-1}+b_2b_{2p-2}+\cdots+b_{p-1}b_{p+1}+\binom{b_p+1}2,&(p\geqslant1)\\
\end{cases}
$$

令$b_0=0,b_1=1$. 假定对于$x\notin N$, 有$b_k=0$.

$$
\Longrightarrow b_n=\sum_{\substack{0\leq i<j\leq n\\[3pt]i+j=n}}b_ib_j+\frac12b_{\frac n2}+\frac12b^2_{\frac n2}\quad(n\geqslant 2)
$$

令$B(t)=\sum\limits_{n\geq0}b_nt^n, (b_0=0,b_1=1)$,于是

$$
\begin{aligned}
\Longrightarrow B(t)=t+\underbrace{\sum_{n\geq2}\left(\sum_{\stackrel{0\leq i<j\leq n}{i+j=n}}b_ib_j\right)t^n}_{1}+\underbrace{\frac12\sum_{n\geq2}b_{\frac n2}t^n}_{2}+\underbrace{\frac12\sum_{n\geq2}b_{\frac n2}^2t^n}_{3}
\end{aligned}
$$

1.  $$
    \begin{aligned}
    =\sum_{j>i\geq0}b_ib_jt^{i+j}&=\frac12\left(\sum_{i,j\geqslant0}b_ib_jt^{i+j}-\sum_{i\geq0}b_i^2t^{2i}\right)\\
    &=\frac12\left(B^2(t)-\sum_{i\geq0}b_i^2t^{2i}\right).
    \end{aligned}
    $$

2.  $$
    \sum_{n\geq0}b_nt^{2n}=B(t^2).
    $$

3.  $$
    \sum_{n\geq0}b_n^2t^{2n}
    $$

所以:

$$
B(t)=t+\frac12B^2(t)+\frac12B(t^2)
$$

令$\beta(t)=1-B(t)$,

$$
\beta(t^2)=2t+\beta^2(t).
$$

具体数可见:[A001190 - OEIS](http://oeis.org/A001190).

### 广义$\mathrm{Schr\ddot{o}der}$加括号问题

计算$n$个字母的加括号数$c_n$,(不满足结合律, 交换律)

(允许每个括号中相邻因子的个数随意)

对于$n=4$,除了$a_4=5$, 还有下面6种, 于是:

$c_4=11$.

<img src="https://s2.loli.net/2021/12/15/A34bWQ2dLoOnYBR.png" style="zoom:67%;" />

对$c_n$分类, 最后一步恰好有$l(l\geq2)$个因子相乘, 其中$l_i$个因子有$i$个字母组成$(i=1,2,...,n)$, 于是有:

$$
\begin{cases}
l_1+l_2+\cdots+l_n=l\\
l_1+2l_2+\cdots+nl_n=n
\end{cases}\qquad
(l\geq2\Rightarrow l_n=0)
$$

对于恰好有$l$个因子这一类, $l=(l_1,l_2,\cdots,l_n)$相当于一个有序排列, $\sum\limits_{i=1}^nl_i=l$, 共有

$$
\frac{(l_1+l_2+\cdots+l_n)!}{l_1!l_2!\cdots l_n!}
$$

种不同的安排方法, 而对于每一种安排方法, 都有$c_1^{l_1}c_2^{l_2}\cdots c_n^{l_n}$种不同的方式, 于是:

$$
c_n=\sum_{\stackrel{\begin{cases}
l_1+l_2+\cdots+l_n=l\\
l_1+2l_2+\cdots+nl_n=n
\end{cases}}{}}\frac{l!}{l_1!l_2!\cdots l_n!}c_1^{l_1}c_2^{l_2}\cdots c_n^{l_n},\qquad (n\geq2,c_0=0,c_1=1).
$$

令

$$
\begin{aligned}
C(t)&=\sum_{n\geq0}c_nt^n=t+\sum_{n\geq2}c_nt^n\\
&=t+\sum_{\stackrel{l_1+\cdots+l_n=l}{l\geq2}}\frac{(l_1+l_2+\cdots+l_n)!}{l_1!l_2!\cdots l_n!}(c_1t)^{l_1}(c_2t^2)^{l_2}\cdots\\
&=t+\sum_{l\geq2}(c_1t+c_2t^2+\cdots)^{l}\\
&=t+\sum_{l\geq2}(C(t))^l=t+\frac{C^2(t)}{1-C(t)}
\end{aligned}
$$

于是:

$$
2C^2(t)-(1+t)C(t)+t=0,\quad C(0)=0
$$

得到:

$$
C(t)=\frac14\left(1+t-\sqrt{2-6t+t^2}\right).
$$

展开:

$$
\begin{cases}
c_0=0,\ c_1=1,\\
c_n=\sum\limits_{k=0}^{\left[\frac n2\right]}(-1)^k\frac{(2n-2k-3)!!}{k!(n-2k)!}3^{n-2k}2^{-k-2},\qquad(n\geq2)
\end{cases}
$$

递推关系:

$$
\begin{cases}
c_1=1,\ c_2=1,\\
(n+1)c_{n+1}=3(2n-1)c_n-(n-2)c_{n-1},(n\geq2),
\end{cases}
$$

序列信息可以看这里[A001003 - OEIS](http://oeis.org/A001003).

# 第二章 集合的划分与整数分拆

## 集合的划分

定义: $n$元集合$N$的一个$k$分类是指:$N=(A_1,\,\cdots,\,A_k)$**有序**, 其中

1.  $A_i\cap A_j=\varnothing,\,(i\ne j)$;
2.  $N=A_1\cup A_2\cdots\cup A_k$, $A_i$可以为空;

显然, 我们有:

$$
|N|=\sum_{i=1}^k|A_i|=|A_1|+\cdots+|A_k|.
$$

例题
证明:$2^{m+1}-1=1+2+2^2+\cdots+2^{m}$.

> 设$A=[m+1]=\{1,2,\cdots,m+1\}$, 令$E=\mathfrak{B}'(A)$, 即$A$的所有非空子集的全体(Block, 块), 则
>
> $$
> |E|=2^{m+1}-1,
> $$
>
> (减一为去掉了空集).
> 令$E_j$为$A$的最大元素为$j(j\geq1)$的子集的集合, 可以由$[j-1]$的全体子集并上$\{j\}$构成.
>
> 于是$|E_j|=2^{j-1}$.显然$E_i\cap E_j=\varnothing,E=\bigcup\limits_{j=1}^{m+1}E_j$,
> 所以$|E|=\sum\limits_{j=1}^{m+1}|E_j|$.

更一般, 得到:

$$
x^{m+1}-y^{m+1}=(x-y)(x^m+x^{m-1}y+\cdots+y^m).
$$

> 证明:
>
> 取$M=[m+1],N=A+B,|N|=x, |B|=y$.
>
>   <img src="https://s2.loli.net/2021/12/15/nxjsTRGDM38cmho.png" style="zoom:33%;" />
>
> 令$E$表示$M\to N$的映射中, $A$中元素有原像的映射的集合, 即$E=\{f\in F(M,N)\,|\,f^{-1}\ne \varnothing\}$.
>
> 于是$|E|=x^{m+1}-y^{m+1}$.
>
> 接下来进行分类:$E_j=\{f\in F(M,N)\,|\,f^{-1}\text{中最大元素为}j+1\}$.
>
> 于是
>
> $$
> |E_j|=(x-y)x^jy^{m-j},\quad (0\leq j\leq m).
> $$

例题2:

证明:

$$
\binom{x+y}n=\sum_{k=0}^n\binom xk\binom y{n-k}.
$$

> 设集合$Z=X+Y$. 令$E$表示$Z$的$n$元子集的集合, 即$E=\{A\subset Z\,\big|\,|A|=n\}$,
>
> 于是$|E|=\binom{x+y}n$.
>
> 令$E_k=\{B\in E\,\big|\,|B\cap X|=k\}$, 则$|E_k|=\binom xk\binom y{n-k}$.
>
> $$
> |E|=\sum_{k=0}^n|E_k|.
> $$

例题3:

证明:

$$
(x+y)^n=\sum_{k=0}^n\binom nk x^ky^{n-k}.
$$

> 令$N=[n]$, $Z=X+Y, |X|=x,|Y|=y$, 令$E=\mathcal{F}(N,Z)$, 则$|E|=(x+y)^n$.
>
> 令$E_k=\{f\in E\,\big|\,|f^{-1}(x)|=k\}$, 则$|E_k|=\binom nkx^ky^{n-k}$. 于是
>
> $$
> |E|=\sum_{k=0}^n|E_k|.
> $$

例题4:
证明:

$$
1^2+2^2+\cdots+n^2=\frac16n(n+1)(2n+1).
$$

> 令$M=\{x,y,z\},N=[n+1]$. $E=\{f\in\mathcal{F}(M,N)|f(x)<f(z), f(y)<f(z)\}$, 对$E$进行分类:
>
> 1.  令$E_k=\{f\in E|f(z)=k+1\}$, 则$|E_k|=k^2$. 于是$|E|=\sum\limits_{k=1}^n|E_k|=\sum\limits_{k=1}^nk^2$.
> 2.  另一方面, 令
>     $$
>     \begin{cases}
>     A=\{f\in E\,|\,f(x)=f(y)<f(z)\}&\Rightarrow |A|=\binom{n+1}{2}\\[5pt]
>     B=\{f\in E\,|\,f(x)<f(y)<f(z)\}&\Rightarrow |B|=\binom{n+1}{3}\\[5pt]
>     C=\{f\in E\,|\,f(y)<f(x)<f(z)\}&\Rightarrow |C|=\binom{n+1}{3}
>     \end{cases}
>     $$
>     可见$E=A\cup B\cup C$, 且$A,B,C$两两不交, 于是有
>     $$
>     |E|=|A|+|B|+|C|=\binom{n+1}2+2\binom{n+1}3=\frac16n(n+1)(2n+1).
>     $$

推广: 对于自然数的立方求和只需要将上题中的三个元素再添上一个即可证明.

## 集合的分类

定理: $n$元集合$N$的分类$\mu=(A_1,A_2,\cdots,A_m)$, ($|A_i|=a_i$)的个数为$\dfrac{n!}{a_1!\cdots a_m!}=\binom n{a_1,\cdots,a_m}$, $n=a_1+\cdots+a_m$.

> 证明: 依次选取进行组合即可.

## 集合的划分与第二类Stirling数

定义: $n$元集合$N$的一个$k-$划分:$N=N_1\cup\cdots\cup N_k$, 其中

1.  $N_i\ne\varnothing,\quad(1\leq i\leq k)$;($N_i$称为块)
2.  $N_i\cap N_j=\varnothing,\,(i\ne j)$.

定义: $S(n,k)$表示$n$元集合$N$的所有不同的$k-$划分数. ($S(n,k)$: 第二类Stirling数)

$$
\color{red}S(n,k)=0,(k>n),\mbox{规定}S(0,0)=1.
$$

<font color="red" size=4px>球盒模型:</font>

- $n$个不同的球放入$k$个相同的盒子, 且每个盒子至少有一个球的不同放法.

由于球不同, 其盒子加以区分, 则有$k!S(n,k)$种.

即$n$个不同的球放入$k$个不同的盒子, 且每个盒子至少有一个球的不同放法.

$$
f:n球(不同)\to k盒子(不同)
$$

- 若$f$为满射, 有$k!S(n,k)$种方式;
- 若$f$为不加限制的映射, 有$k^n$个.

对于不加限制的映射(右边的盒子可能有空的), 若有$i$个盒子有球, 其余为空盒子($1\leq i\leq k$), 则有$\binom kii!S(n,i)$种, 于是

$$
k^n=\sum_{i=0}^k\binom kii!S(n,i)=\sum_{i=0}^k(k)_iS(n,i).
$$

定理1: $S(n,0)=0,\quad S(n,1)=1,\quad S(n,2)=2^{n-1}-1,\quad S(n,n-1)=\binom n2,\quad S(n,n)=1$.

> 1.  $n$元集合$N$不能分成0块;
> 2.  $n$元集合$N$分成1块: 只有一种;
> 3.  $n$元集合$N$的所有子集$2^n$个, 去掉$\varnothing, N$之后有$2^n-2$个, 成对组合(两两组合为一个$2-$划分), 于是有$S(n,2)=(2^n-2)/2=2^{n-1}-1$;
> 4.  $n$元集合$N$分成$n-1$块, 则必有一块包含两个元素(鸽巢原理), 其余均含有1个元素, 所以$S(n,n-1)=\binom n2$;
> 5.  $n$元集合$N$分成$n$块, 则$S(n,n)=1$.

定理2:

$$
S(n,k)=S(n-1, k-1)+kS(n-1,k),\quad (n,k\geq1).
$$

> 证明:(递推关系可以类比二项式系数)
>
> - 当$k>n$, 两边均为0, 成立;
> - 当$k=n$, 两边均为1, 成立;
> - 当$1\leq k<n$, 由$S(n,k)$的意义, 令$N=\{a_1,\cdots,a_n\}$, 将其分成两类($k-$块的并):
>   - $\{a_n\}$为单独的一块, 所以其划分数为:$S(n-1,k-1)$;
>   - $\{a_n\}$不是单独的一块, 这时候需要考虑$\{a_n\}$与其他$k$个块的并(共同组成一块), $a_n$**可以并入其他**$n-1$个元素组成的$k$个块中的任意一块
>     $\Rightarrow kS(n-1,k)$.
>
> 于是:$S(n,k)=S(n-1, k-1)+kS(n-1,k),\quad (n,k\geq1)$.

### 杨辉三角(Pascal三角)

由二项式系数构成的一个矩阵

$$
(a_{nk})=\left(\!\!\left(\begin{matrix}n\\k\end{matrix}\right)\!\!\right)_{n,k\geq0}=
\begin{pmatrix}
1&&&&&\\
1&1&&&\Large0&\\
1&2&1&&\\
1&3&3&1&&\\
\vdots&\vdots&\vdots&\vdots&\ddots\\
&&&&&1
\end{pmatrix}
$$

其逆矩阵(两组多项式基的表示矩阵)

由$(1+x)^n=\sum\limits_{k=0}^n\binom nk x^k$, ($\beta=A\alpha$形式), 得到:

$$
x^n=((1+x)-1)^n=\sum_{k=0}^n(-1)^{n-k}\binom nk(1+x)^k,\quad(\alpha=B\beta形式)
$$

于是$\left(\!\!\left(\begin{matrix}n\\k\end{matrix}\right)\!\!\right)_{n,k\geq0}$的逆矩阵为$\left(\!\!(-1)^{n-k}\left(\begin{matrix}n\\k\end{matrix}\right)\!\!\right)_{n,k\geq0}$.

二项式反演公式(**Gould-Hsu**反演公式的一个特例)

$$
\begin{cases}
f_n=\sum\limits_{k=0}^n\binom nkg_k\\
g_n=\sum\limits_{k=0}^n(-1)^{n-k}\binom nkf_k
\end{cases}\iff
\begin{cases}
f_n=\sum\limits_{k=0}^n(-1)^{k}\binom nkg_k\\
g_n=\sum\limits_{k=0}^n(-1)^{k}\binom nkf_k.
\end{cases}(逆矩阵为其自身)
$$

### Stirling三角

$$
(S_{nk})=\left(S(n,k)\right)_{n,k\geq0}=
\begin{pmatrix}
1&&&&&\\
0&1&&&\Large0&\\
0&1&1&&\\
0&1&3&1&&\\
0&1&7&6&1&\\
\vdots&\vdots&\vdots&\vdots&&\ddots\\
&&&&&&1
\end{pmatrix}
$$

均为可逆的无穷下三角矩阵.

根据二项式的反演关系:

$$
\begin{cases}
f_k=\sum\limits_{i=0}^k\binom kig_i\\
g_k=\sum\limits_{i=0}^k(-1)^{k-i}\binom kif_i
\end{cases}
$$

以及上述式子:

$$
k^n=\sum_{i=0}^k\binom kii!S(n,i),
$$

取$f_k=k^n,g_i=i!S(n,i)$, 得到:(在差分公式中也遇到过)

$$
k!S(n,k)=\sum_{i=0}^k(-1)^{k-i}\binom kii^n=\sum_{i=0}^k(-1)^{i}\binom ki(k-i)^n,
$$

(利用容斥原理进行组合解释).

定理3: (第二类Stirling数的显式表达)

$$
S(n,k)=\frac1{k!}\sum_{i=0}^k(-1)^i\binom ki(k-i)^n.
$$

定理4: $S(n,k)$的解析定义

$$
x^n=\sum_{k=0}^nS(n,k)(x)_k.
$$

> 证明:
>
> $$
> m^n=\sum_{k=0}^nS(n,k)(m)_k, (1\leq m\leq n),
> $$
>
> 反证, 假设$x^n\ne\sum\limits_{k=0}^nS(n,k)(x)_k$, 即$x^n-\sum\limits_{k=0}^nS(n,k)(x)_k\ne0$. 而
>
> $$
> x^n-\sum\limits_{k=0}^nS(n,k)(x)_k=x^n-(x)_n-\sum\limits_{k=0}^{n-1}S(n,k)(x)_k
> $$
>
> 为至多$n-1$次多项式, 但是根据
>
> $$
> m^n=\sum_{k=0}^nS(n,k)(m)_k, (1\leq m\leq n),
> $$
>
> 上述多项式有$n$个零点:$x=1,2,\cdots,n$(代数学基本定理), 于是矛盾.

定理5: 第二类**Stirling**数$S(n,k)$的**有理生成函数**.

$$
\varphi_k(u)=\sum_{n\geq0}S(n,k)u^n=\frac{u^k}{(1-u)(1-2u)\cdots(1-ku)},\quad(k\geq1),
$$

> 证明:
>
> 从递推关系可以得到:
>
> $$
> \begin{aligned}
> \varphi_k(u)&=\sum_{n\geq0}S(n,k)u^n=\sum_{n\geq1}S(n-1,k-1)u^n+\sum_{n\geq1}kS(n-1,k)u^n\\
> &=u\varphi_{k-1}(u)+ku\varphi_k(u).
> \end{aligned}
> $$
>
> 于是:
>
> $$
> \varphi_k(u)=\frac{u}{1-ku}\varphi_{k-1}(u),\quad(k\geq1).
> $$
>
> 又因为
>
> $$
> \varphi_0(u)=\sum\limits_{n\geq0}S(n,0)u^n=1,
> $$
>
> 所以
>
> $$
> \varphi_k(u)=\frac{u^k}{(1-u)(1-2u)\cdots(1-ku)},\quad(k\geq1).
> $$

这里先插入一个小知识(参考[几种有理分式分解的方法 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/69471608)): (部分分式分解的方法)

> 形如
>
> $$
> \frac{P(x)}{(a_1x+b_1)(a_2x+b_2)...(a_nx+b_n)} = \frac{A_1}{(a_1x+b_1)} + \frac{A_2}{(a_2x+b_2)} +\cdots +\frac{A_n}{(a_nx+b_n)}
> $$
>
> 的有理多项式, 以$A_1$的计算为例, 两边同时乘以$(a_1x+b_1)$,
>
> $$
> \frac{P(x)(a_1x+b_1)}{(a_1x+b_1)(a_2x+b_2)...(a_nx+b_n)} = A_1+ \frac{A_2(a_1x+b_1)}{(a_2x+b_2)} +\cdots+\frac{A_n(a_1x+b_1)}{(a_nx+b_n)}
> $$
>
> $$
> A_1=\frac{P(x)}{(a_2x+b_2)...(a_nx+b_n)} -  \frac{A_2(a_1x+b_1)}{(a_2x+b_2)} +\cdots +\frac{A_n(a_1x+b_1)}{(a_nx+b_n)}
> $$
>
> 令$a_1x+b_1=0$, 则$x=-\frac{b_1}{a_1}$得到:
>
> $$
> A_1=\frac{P(-\frac{b_1}{a_1})}{(a_2\frac{-b_1}{a_1}+b_2)...(a_n\frac{-b_1}{a_1}+b_n)}.
> $$

定理6: (定理3) 采用生成函数证明

$$
\begin{aligned}
S(n,k)&=\frac1{k!}\sum_{i=0}^k(-1)^i\binom ki(k-i)^n\\
&=\frac1{k!}\sum_{i=0}^k(-1)^{k-i}\binom kii^n=\frac1{k!}\Delta^k\dot{0}^n
\end{aligned}
$$

其中最后一项为对$x^n$差分$k$次后取$x=0$得到的式子.

> 证明:
>
> 根据生成函数, 得到:
>
> $$
> \begin{aligned}
> S(n,k)&=[u^n]\varphi_k(u)=[u^n]\frac{u^k}{(1-u)(1-2u)\cdots(1-ku)}\\
> &=[u^{n-k}]\frac1{(1-u)(1-2u)\cdots(1-ku)}.
> \end{aligned}
> $$
>
> 由部分分式分解, 得
>
> $$
> \frac{1}{(1-u)(1-2u)\cdots(1-ku)}=\sum_{i=1}^k\frac{\alpha_i}{1-iu}=\frac{\alpha_1}{1-u}+\frac{\alpha_2}{1-2u}+\cdots+\frac{\alpha_k}{1-ku},
> $$
>
> 其中
>
> $$
> \begin{aligned}
> \alpha_i&=\lim_{u\to\frac1i}\frac{1-iu}{(1-u)(1-2u)\cdots(1-ku)}\\
> &=\lim_{u\to\frac1i}\frac{1}{(1-u)\cdots(1-(i-1)u)(1-(i+1)u)\cdots(1-ku)}\\
> &=\frac{1}{\left(1-\frac1i\right)\cdots\left(1-\frac{i-1}i\right)\left(1-\frac{i+1}i\right)\cdots\left(1-\frac ki\right)}\\
> &=\frac{i^{k-1}}{(i-1)(i-2)\cdots1(-1)\cdots(i-k)}\\
> &=(-1)^{k-i}\frac{i^k}{i!(k-i)!}
> \end{aligned}
> $$
>
> 于是
>
> $$
> \begin{aligned}
> S(n,k)&=[u^{n-k}]\sum_{i=1}^k\frac{\alpha_i}{1-iu}=\sum_{i=1}^k\alpha_i[u^{n-k}]\frac1{1-iu}\\
> &=\sum_{i=1}^k\alpha_i[u^{n-k}]\sum_{j\geq0}i^ju^j=\sum_{i=1}^k\alpha_ii^{n-k}\\
> &=\sum_{i=1}^k(-1)^{k-i}\frac{i^n}{i!(k-i)!}=\frac1{k!}\sum_{i=1}^k(-1)^{k-i}\binom kii^n.
> \end{aligned}
> $$
>
> 最后一项的求和下标可以改为$i=0$, 分类讨论:
>
> - $n=0$时, $k$只能为0, 其值为$S(0,0)=1$;
> - $n>0$时, $0^n=0$, 所以$S(n,0)=0$.
>
> 所以成立.

定理7: 第二类Stirling数$S(n,k)$的**垂直指数生成函数**

$$
\Phi_k(t)=\sum_{n\geq0}S(n,k)\frac{t^n}{n!}=\frac1{k!}(e^t-1)^k,\quad(k\geq0).
$$

进一步, $S(n,k)$的双变量混合生成函数为:

$$
\Phi(t,u)=\sum_{n,k\geq0}S(n,k)\frac{t^n}{n!}u^k=\exp\big(u(e^t-1)\big).
$$

> 证明:
>
> $$
> \begin{aligned}
> \Phi_k(t)&=\sum_{n=0}^{\infty} \frac{S(n, k)}{n !} t^{n}  \\
> &= \sum_{n=0}^{\infty} \frac{1}{k !} \sum_{j=0}^{k}\binom{k}{j} j^{n}(-1)^{k-j} \frac{t^{n}}{n !}\\
> & =\sum_{j=0}^{k}(-1)^{k-j} \frac{1}{k !}\binom{k}{j} \sum_{n=0}^{\infty} j^{n} \frac{t^{n}}{n !} \\
> & =\sum_{j=0}^{k}(-1)^{k-j} \frac{1}{k !}\binom{k}{j} \mathrm{e}^{jt} \\
> & =\frac{1}{k !} \sum_{j=0}^{k}\binom{k}{j}\left(\mathrm{e}^{t}\right)^{j}(-1)^{k-j} \\
> & =\frac{\left(\mathrm{e}^{t}-1\right)^{k}}{k !}
> \end{aligned}
> $$
>
> 进一步,
>
> $$
> \begin{aligned}
> \Phi(t,u)
> &=\sum_{n,k\geq0}S(n,k)\frac{t^n}{n!}u^k\\
> &=\sum_{k\geq0}\left(\sum_{n\geq0}S(n,k)\frac{t^n}{n!}\right)u^k\\
> &=\sum_{k\geq0}\left(\frac1{k!}(e^t-1)^k\right)u^k\\
> &=\exp\big(u(e^t-1)\big)
> \end{aligned}
> $$

定理8: (定理4) 第二类Stirling数$S(n,k)$的**水平生成函数**

$$
x^n=\sum_{k=0}^nS(n,k)(x)_k.
$$

> 证明:两端构造生成函数
>
> 由
>
> $$
> \begin{aligned}
> \sum_{n\geq0}x^n\frac{t^n}{n!}&=e^{xt}=\big(1+(e^t-1)\big)^x\\
> &=\sum_{k\geq0}\frac{(x)_k}{k!}(e^t-1)^k\\
> &=\sum_{k\geq0}(x)_k\frac{(e^t-1)}{k!}^k\\
> &=\sum_{k\geq0}(x)_k\sum_{n\geq0}S(n,k)\frac{t^n}{n!}\\
> &=\sum_{n\geq0}\left(\sum_{k\geq0}(x)_kS(n,k)\right)\frac{t^n}{n!}
> \end{aligned}
> $$
>
> 比较两端$\frac{t^n}{n!}$的系数$\left[\frac{t^n}{n!}\right]$, 即得.

定理9: 显式表达

$$
S(n,k)=\sum_{\stackrel{\large c_1+\cdots+c_k=n-k}{c_i\geq0}}1^{c_1}2^{c_2}\cdots k^{c_k},
$$

换言之, $S(n,k)$是$[k]$中所有$n-k$个**不必互异的**整数的乘积之和. 这种乘积项一共有$\binom{n-k+k-1}{k-1}=\binom{n-1}{k-1}$个.

> 例子:
>
> $$
> S(5,3)=1^2+2^2+3^2+1\cdot2+1\cdot3+2\cdot3=25.
> $$

> 证明: (由生成函数)
>
> $$
> \begin{aligned}
> \sum_{n\geq0}S(n,k)u^{n-k}&=\frac{1}{(1-u)(1-2u)\cdots(1-ku)}\\
> &=\prod_{i=1}^k\frac1{1-iu}\\
> &=\prod_{i=1}^k\left(\sum_{c_i\geq0}i^{c_i}u^{c_i}\right)\\
> &=\sum_{c_1,c_2,\cdots,c_k\geq0}1^{c_1}\cdots k^{c_k}u^{c_1+\cdots+c_k}.
> \end{aligned}
> $$
>
> 比较两端$[u^{n-k}]$, 即得.

定义3: $n$元集合$N$的一个划分$\mathscr{S}$具有类型$[\![c]\!]=[\![c_1,c_2,\cdots,c_n]\!]$, 当且仅当$\mathscr{S}$有$c_i$个$i$块, $i\in [n]$, 其中整数$c_i\geq0$, 且满足

$$
c_1+2c_2+\cdots+nc_n=n,(c_1+\cdots+c_n=|\mathscr{S}|).
$$

定理10: $n$元集合$N$的一个类型$[\![c]\!]$的划分数等于

$$
\frac{n!}{c_1!c_2!\cdots(1!)^{c_1}(2!)^{c_2}\cdots}.
$$

> 证明:
>
> 由于块与块之间的顺序不考虑, 而且块内元素的顺序也不计, 于是从有序排列中去掉$c_1!c_2!\cdots$ 即为无序.

定理11:

$$
S(n,k)=\sum_{\stackrel{c_1+2c_2+\cdots=n}{\stackrel{c_1+c_2+\cdots=k}{c_i\geq0}}}\frac{n!}{c_1!c_2!\cdots(1!)^{c_1}(2!)^{c_2}\cdots}.
$$

> 例子:
>
> $S(5,3)$,
>
> $$
> \begin{cases}
> c_1+2c_2+3c_3+4c_4+5c_5=5\\
> c_1+c_2+c_3+c_4+c_5=3
> \end{cases}
> (c_i\geq0)
> $$
>
> 两组解:
>
> 1.  $c_1=2,c_3=1$;
> 2.  $c_1=1,c_2=2$.

## Bell数

定义4: $n$元集合$N$ 的**所有划分**数$b(n)$, 称为$Bell$数, 即

$$
b(n)=\sum_{k=1}^nS(n,k),\quad(n\geq1).
$$

定理12: $Bell$数$b(n)$具有指数生成函数

$$
\sum_{n\geq0}b(n)\frac{t^n}{n!}=\exp(e^t-1),\ b(0)=1.
$$

且满足递推关系

$$
b(n+1)=\sum_{k=0}^n\binom{n}k b(k),\ (n\geq0).
$$

> 证明:
>
> 由于
>
> $$
> \Phi(t,u)=\sum_{n,k\geq0}S(n,k)\frac{t^n}{n!}u^k=\sum_{k\geq0}\left(\sum_{n\geq0}S(n,k)\frac{t^n}{n!}\right)u^k=\exp\big(u(e^t-1)\big)
> $$
>
> 所以我们得到:
>
> $$
> \Phi(t,1)=\sum_{n,k\geq0}S(n,k)\frac{t^n}{n!}=\sum_{k=0}^n\left(\sum_{n\geq0}S(n,k)\frac{t^n}{n!}\right)=\exp(e^t-1),
> $$
>
> 由指数生成函数
>
> $$
> \sum_{n\geq0}b(n)\frac{t^n}{n!}=\exp(e^t-1)
> $$
>
> 两边对$t$求导,得到:
>
> $$
> \sum_{n\geq0}b(n)\frac{t^{n-1}}{(n-1)!}=\exp(e^t-1)\cdot e^t,
> $$
>
> 于是
>
> $$
> \sum_{n\geq0}b(n+1)\frac{t^{n}}{n!}=\sum_{k\geq0}b(k)\frac{t^k}{k!}\cdot\sum_{j\geq0}\frac{t^j}{j!}=\sum_{k\geq0}b(k)\frac{t^k}{k!}\cdot\sum_{n-k\geq0}\frac{t^{n-k}}{(n-k)!},
> $$
>
> 比较两端$\dfrac{t^n}{n!}$的系数,得到:
>
> $$
> b(n+1)=\sum_{k=0}^n\binom{n}k b(k),\ (n\geq0).
> $$

**组合解释**:

$$
b(n+1)=\sum_{k=0}^n\binom{n}k b(k),\ (n\geq0).
$$

令$P=\{x_1,x_2,...,x_n,{\color{red} x}\}, N=\{x_1,...,x_n\}$, $b(n+1)$为集合$P$的所有划分数.

固定$x$, 将$P$的所有划分进行分类, 取$K\subset N$, $|K|=k$, $(0\leq k \leq n)$

$\{x\}\cup K$作为$P$的划分中的一块, 其余$N\backslash K$任意划分, 并在一起作为$P$的划分, 得到

$$
b(n+1)=\sum_{k=0}^n\binom{n}k b(n-k)=\sum_{k=0}^n\binom{n}k b(k),\ (n\geq0).
$$

此外, 我们有:

$$
\sum_{n\geq0}b(n)\frac{t^n}{n!}=\exp(e^t-1)=\frac{e^{e^t}}{e}=\frac1e\sum_{k\geq0}\frac{e^{tk}}{k!}=\frac1e\sum_{k\geq0}\frac{1}{k!}\sum_{n\geq0}\frac{t^nk^{n}}{n!},
$$

两边取$\left[\dfrac{t^n}{n!}\right]$, 得到:(Bell数的解析表示)

$$
b(n)=\frac1e\sum_{k\geq0}\frac{k^n}{k!}.
$$

定理13: 可以直接计算$Bell$数$b(n)$,

$$
b(n)=\Delta^nb(1), \ b(1)=1.
$$

> 证明:
>
> 根据
>
> $$
> \Delta^nb(m)=\sum_{k=0}^n(-1)^{n-k}\binom nkb(m+k),
> $$
>
> 令$m=1$, 得到:
>
> $$
> \begin{aligned}
> \Delta^nb(1)&=\sum_{k=0}^n(-1)^{n-k}\binom nkb(1+k)\\
> &=\sum_{k=0}^n(-1)^{n-k}\binom nk\sum_{i=0}^k\binom{k}i b(i)\\
> &=\sum_{i=0}^nb(i)\sum_{k=i}^n(-1)^{n-k}\binom nk\binom{k}i \\
> &=\sum_{i=0}^nb(i)\binom n{i}\sum_{k=i}^n(-1)^{n-k}\binom{n-i}{k-i} \\
> &=\sum_{i=0}^nb(i)\binom n{i}\sum_{j=0}^{n-i}(-1)^{j}\binom{n-i}{j} \\
> &=\sum_{i=0}^nb(i)\delta_{n,i}=b(n)
> \end{aligned}
> $$
>
> 其中:
>
> $$
> \delta_{n,i}=\begin{cases}1,&n=i\\0,&n\ne i\end{cases}
> $$
>
> 或者直接从差分定义式出发也可证明$\sum_{k=i}^n(-1)^{n-k}\binom nk\binom{k}i=\delta_{n,i}$.

利用差分公式计算Bell数:

$$
\begin{aligned}
\Delta^nb(1)&=b(n),\ b(1)=1\\
\Delta b(n)&=b(n+1)-b(n)\\
b(n+1)&=b(n)+\Delta b(n)\\
\Delta b(n+1)&=\Delta b(n)+\Delta^2b(n)
\end{aligned}
$$

绘制一个表格, 利用上述的递推关系即可依次得出, 具体请看[A000110 - OEIS](https://oeis.org/A000110).

```c
  1
  1 2
  2 3 5
  5 7 10 15
  15 20 27 37 52
```

## 第二类Stirling数的递推关系式

定理A:

$$
\begin{aligned}
S(n,k)&=S(n-1,k-1)+kS(n-1,k), (n\geq k\geq1)\\
S(n,0)&=S(0,k)=0, \ (n,k\geq1),\quad S(0,0)=1.
\end{aligned}
$$

> 证明: (分析方法)
>
> 根据
>
> $$
> \sum_{k=0}^nS(n,k)(x)_k=x^n=x^{n-1}\cdot x,
> $$
>
> 得到:
>
> $$
> \begin{aligned}
> \sum_{k=0}^nS(n,k)(x)_k&=x\cdot \sum_{k=0}^{n-1}S(n-1,k)(x)_k\\
> &=\sum_{k=0}^{n-1}S(n-1,k)(x)_{k}\big((x-k)+k\big)\\
> &=\sum_{k=0}^{n-1}S(n-1,k)(x)_{k+1}+\sum_{k=0}^{n-1}kS(n-1,k)(x)_k
> \end{aligned}
> $$
>
> 比较两端$[(x)_k]$, 即得.

定理B: $S(n,k)$满足"垂直"递推关系(对$n$计算, $k$不变)

1.  $$
    S(n,k)=\sum_{l=k-1}^{n-1}\binom{n-1}kS(l,k-1),
    $$

2.  $$
    S(n,k)=\sum_{l=k}^nS(l-1, k-1)k^{n-l}.
    $$

> 证明:
>
> 1.下式
>
> $$
> \sum_{n\geq0}S(n,k)\frac{t^n}{n!}=\frac1{k!}(e^t-1)^k
> $$
>
> 两端对$t$求导, 得到:
>
> $$
> \begin{aligned}
> \sum_{n\geq1}S(n,k)\frac{t^{n-1}}{(n-1)!}&=\frac1{(k-1)!}(e^t-1)^{k-1}e^t\\
> &=e^t\sum_{l\geq0}S(l,k-1)\frac{t^l}{l!}\\
> &=\sum_{m\geq0}\frac{t^m}{m!}\sum_{l\geq0}S(l,k-1)\frac{t^l}{l!}\qquad (let\ l+m=n-1)
> \end{aligned}
> $$
>
> 比较两端$\left[\frac{t^{m-1}}{(m-1)!}\right]$, 得.
>
> ---
>
> 2.根据有理生成函数, 得到:
>
> $$
> \begin{aligned}
> \sum_{n\geq0}S(n,k)u^n&=\frac{u^k}{(1-u)(1-2u)\cdots(1-ku)}=\frac{u}{1-ku}\cdot\frac{u^{k-1}}{(1-u)(1-2u)\cdots\big(1-(k-1)u\big)}\\
> &=\frac{u}{1-ku}\cdot \sum_{l\geq0}S(l,k-1)u^l\\
> &=\sum_{m\geq0}k^mu^{m+1}\cdot\sum_{l\geq0}S(l,k-1)u^l\qquad(let\ m+l+1=n)
> \end{aligned}
> $$
>
> 比较两端$[u^n]$, 得.
>
> 或者从$S(n,k)=S(n-1, k-1)+kS(n-1,k)$, 一直递归右端第二项得到.

定理C: $S(n,k)$满足"水平"递推关系(对$k$计算, $n$不变)

1.  $$
    S(n,k)=\sum_{j=0}^{n-k}(-1)^j\langle k+1\rangle_jS(n+1, k+j+1),
    $$

2.  $$
    k!S(n,k)=k^n-\sum_{j=0}^{k-1}(k)_jS(n,j).
    $$

> 证明:
>
> 1.  $S(n,k)=S(n+1, k+1)-(k+1)S(n,k+1)$一直递归右端第二项得.
> 2.  从$k^n=\sum_{i=0}^kS(n,i)(k)_i=k!S(n,k)+\sum_{i=0}^{k-1}(k)_iS(n,i)$, 得.

组合解释:

- $k!S(n,k)$表示$n$个不同的球放入$k$个不同的盒子, 且每个盒子至少一个球的不同放法数.

- $k^n$表示将$n$个不同的球放入$k$个不同的盒子, 盒子中球数不限
  $$
  k!S(n,k)=k^n-有空盒的放法数
  \begin{cases}
  1个空盒:\binom k1(k-1)!S(n,k-1)\\
  2个空盒:\binom k2(k-2)!S(n,k-2)\\
  \vdots
  \end{cases}
  $$

定理D: 第二类Stirling数满足"斜"递推关系

$$
S(n,k)=\delta_{n,k}+\sum_{i=0}^{k-1}(k-i)S(n-i-1,k-i).
$$

> 证明:
>
> $$
> S(n,k)=S(n-1, k-1)+kS(n-1,k)
> $$
>
> 重复迭代右端第一项, 得.

## 置换与第一类Stirling数

由第二类Stirling数构成的矩阵为一个Stirling三角$(S_{nk})=\big(S(n,k)\big)_{n,k\geq0}$.

$$
(S_{nk})=\left(S(n,k)\right)_{n,k\geq0}=
\begin{pmatrix}
1&&&&&\\
0&1&&&\Large0&\\
0&1&1&&\\
0&1&3&1&&\\
0&1&7&6&1&\\
\vdots&\vdots&\vdots&\vdots&&\ddots\\
&&&&&&1
\end{pmatrix}
$$

无穷可逆下三角矩阵,

且$x^n=\sum\limits_{k=0}^nS(n,k)(x)_k$, (两组多项式基的表示矩阵), 用$\big(s(n,k)\big)_{n,k\geq0}$表示$\big(S(n,k)\big)_{n,k\geq0}$的逆矩阵,即得到:

$$
(x)_n=\sum_{k=0}^ns(n,k)x^k.
$$

定义1: 第一类Stirling数$s(n,k)$由下述生成函数定义:

$$
(x)_n=\sum_{k=0}^ns(n,k)x^k.
$$

展开左端的下阶乘, 得到$s(n,k)$有符号, 称为第一类有符号Stirling数, 对应的还有第一类无符号Stirling数.

反演关系

$$
\begin{cases}
f_n=\sum\limits_{k=0}^nS(n,k)g_k\\
g_n=\sum\limits_{k=0}^ks(n,k)f_k
\end{cases}
$$

定义2: 第一类Stirling数的双变量生成函数

$$
\Psi(t,u)=\sum_{n,k\geq0}s(n,k)\frac{t^n}{n!}u^k=\sum_{n\geq0}\left(\sum_{k\geq0}s(n,k)u^k\right)\frac{t^n}{n!}\\
=\sum_{n\geq0}(u)_n\frac{t^n}{n!}=\sum_{n\geq0}\binom unt^n=(1+t)^u
$$

针对上式, 还可立即得出单变量指数型生成函数

$$
\sum_{n\geq0}\left(\sum_{k\geq0}s(n,k)u^k\right)\frac{t^n}{n!}=(1+t)^u=\exp\big(u\ln(1+u)\big)=\sum_{k\geq0}\frac{\ln^k(1+t)}{k!}u^k
$$

比较两端$[u^k]$, 得到:

$$
\Psi_k(t)=\sum_{n\geq0}s(n,k)\frac{t^n}{n!}=\frac{\ln^k(1+t)}{k!}.
$$

定义3: 第一类无符号Stirling数

$$
\bar{s}(n,k)=\big|s(n,k)\big|=(-1)^{n-k}s(n,k).
$$

定理1 第一类Stirling数具有水平生成函数

$$
(x)_n=\sum_{k=0}^ns(n,k)x^k\\
\ \langle x\rangle_n=\sum_{k=0}^n\bar{s}(n,k)x^k
$$

> 由于$(x)_n=(-1)^{n}\langle x\rangle_n$.

定理2 第一类Stirling数具有水平生成函数

$$
\ \ \Psi_n(u)=\sum_{k=1}^ns(n,k)u^{n-k}=(1-u)(1-2u)\cdots(1-(n-1)u)\\
\Psi_n(-u)=\sum_{k=1}^n\bar{s}(n,k)u^{n-k}=(1+u)(1+2u)\cdots(1+(n-1)u)
$$

> 证明: 在定理1中令$x=\frac1u$, 即证.

定理3 对固定的$n$和变量$k$, $\bar{s}(n+1,k+1)$是前$n$个正整数的**初等对称函数**, 即对于$l=1,2,...,n$, 有

$$
\bar s(n+1, n+1-l)=\sum_{1\leq i_1<i_2<\cdots<i_l\leq n}i_1i_2\cdots i_l,
$$

换言之, 第一类无符号Stirling数$\bar s(n,k)$是$[n-1]$中所有$n-k$个不同的整数的乘积之和(乘积共有$\binom{n-1}{k-1}$个).

> 证明:
>
> $$
> \langle x\rangle_n=\sum_{k=0}^n\bar{s}(n,k)x^k\Longrightarrow \langle x\rangle_{n+1}=\sum_{k=0}^{n+1}\bar{s}(n+1,k)x^k
> $$
>
> 右端两边同时除以$x$, 得到
>
> $$
> \langle x+1\rangle_{n}=(x+1)(x+2)\cdots(x+n)=\sum_{k=0}^{n}\bar{s}(n+1,k+1)x^k,
> $$
>
> 于是$\bar{s}(n+1,k+1)=[x^k]\langle x+1\rangle_n$为$[n]$中所有$n-k$个不同整数乘积之和.
>
> ---
>
> 又由
>
> $$
> \sum_{k=0}^n\bar{s}(n,k)u^{n-k}=(1+u)(1+2u)\cdots(1+(n-1)u)
> $$
>
> 得到
>
> $$
> \sum_{l=0}^{n+1}\bar{s}(n+1,n-l+1)u^{l}=(1+u)(1+2u)\cdots(1+nu)
> $$
>
> 得到
>
> $$
> \bar{s}(n+1,n-l+1)=[u^l](1+u)(1+2u)\cdots(1+nu)\\
> \qquad\qquad\quad=\sum_{1\leq i_1<i_2<\cdots<i_l\leq n}i_1i_2\cdots i_l,
> $$

第一类Stirling数的递推关系式

定理A:

1.  $$
    s(n,k)=s(n-1,k-1)-(n-1)s(n-1,k), (n,k\geq1),\\
    s(n,0)=s(0,k)=0, (n,k\geq1),s(0,0)=1
    $$

2.  $$
    \bar s(n,k)=\bar s(n-1,k-1)+(n-1)\bar s(n-1,k), (n,k\geq1),\\
    \bar s(n,0)=\bar s(0,k)=0, (n,k\geq1), \bar s(0,0)=1
    $$

> $\Rightarrow s(n,1)=(-1)^{n-1}(n-1)!,\quad s(n,n-1)=-\binom n2, s(n,n)=1$.
>
> $\Rightarrow \bar s(n,1)=(n-1)!,\quad \bar s(n,n-1)=\binom n2, \bar s(n,n)=1$.

> 证明: 用生成函数
>
> $$
> \sum_{k=0}^ns(n,k)x^k=(x)_n=(x)_{n-1}(x-n+1)\\
> =\sum_{k=0}^ns(n-1,k)x^k(x-(n-1))
> $$
>
> 比较$[x^k]$, 得.
>
> 无符号情况同理.

第一类Stirling数的组合解释:

令$\mathcal{S}_n$表示$[n]$到$[n]$所有双射构成的集合(置换群)

例如: 置换

$$
\pi=\binom{1\ 2\ 3\ 4\ 5\ 6\ 7}{4\ 2\ 7\ 1\ 3\ 6\ 5}\in\mathcal{S}_7,
$$

轮换表达式$\pi=(14)(2)(375)(6)$ $\Rightarrow$ 4个轮换的乘积.

第一类无符号Stirling数$\bar s(n,k)$表示的是$\mathcal{S}_n$中恰好有$k$个轮换的置换的个数.

例子:

1.  $\bar s(n,n)=1$, $\{(1)\}$.

2.  $\bar s(n,n-1)=\binom n2$, $n$个元素中任取两个构成一个2元轮换, 其余$n-2$为1元轮换.

3.  $\bar s(n,1)=(n-1)!$, 所有元素放在一起为一个轮换, 显然为$(n-1)!$.(圆排列)

4.  递推关系

    $$
    \bar{s}(n,k)=\bar s(n-1,k-1)+(n-1)\bar s(n-1,k),
    $$

    $\bar s(n,k)$表示$\mathcal{S}_n$中恰有$k$个轮换的置换的个数.

    1.  若1单独作为一个轮换, 共有$\bar s(n-1, k-1)$个;
    2.  若1在其他$n-1$个元素构成的$k$个轮换中(则1不单独作为一个轮换), 则1可以在其余$n-1$个元素前面形成不同的轮换, 共有$(n-1)\bar s(n-1,k)$个.

### 第一类Stirling数的递推关系式

定理A:

1.  $$
    s(n,k)=s(n-1,k-1)-(n-1)s(n-1,k), (n,k\geq1),\\
    s(n,0)=s(0,k)=0, (n,k\geq1),s(0,0)=1
    $$

2.  $$
    \bar s(n,k)=\bar s(n-1,k-1)+(n-1)\bar s(n-1,k), (n,k\geq1),\\
    \bar s(n,0)=\bar s(0,k)=0, (n,k\geq1), \bar s(0,0)=1
    $$

> $\Rightarrow s(n,1)=(-1)^{n-1}(n-1)!,\quad s(n,n-1)=-\binom n2, s(n,n)=1$.
>
> $\Rightarrow \bar s(n,1)=(n-1)!,\quad \bar s(n,n-1)=\binom n2, \bar s(n,n)=1$.

> 证明: 用生成函数
>
> $$
> \sum_{k=0}^ns(n,k)x^k=(x)_n=(x)_{n-1}(x-n+1)\\
> =\sum_{k=0}^ns(n-1,k)x^k(x-(n-1))
> $$
>
> 比较$[x^k]$, 得.
>
> 无符号情况同理.

定理B: 第一类Stirling数满足"垂直"递推关系

1.  $$
    ks(n,k)=\sum_{l=k-1}^{n-1}(-1)^{n-l-1}\frac{n!}{l!(n-l)}s(l,k-1),
    $$

2.  $$
    s(n+1,k+1)=\sum_{l=k}^n(-1)^{n-l}(l+1)(l+2)\cdots n s(l,k)=\sum_{l=k}^n(-1)^{n-l}\frac{n!}{l!} s(l,k).
    $$

对应的, 对第一类无符号Stirling数有

1.  $$
    k\bar s(n,k)=\sum_{l=k-1}^{n-1}\frac{n!}{l!(n-l)}\bar s(l,k-1),
    $$

2.  $$
    \bar s(n+1,k+1)=\sum_{l=k}^n(l+1)(l+2)\cdots n \bar s(l,k).
    $$

> 证明:
>
> 1.  由
>     $$
>     \sum_{n,k\geq0}s(n,k)\frac{t^n}{n!}u^k=(1+t)^u,
>     $$
>     两边关于$u$求导, 得到(利用$\ln(1+t)$展开式)
>     $$
>     \begin{aligned}
>     \sum_{n,k\geq0}k\cdot s(n,k)\frac{t^n}{n!}u^{k-1}&=(1+t)^u\ln(1+t)\\
>     &=\sum_{n,k\geq0}s(n,k)\frac{t^n}{n!}u^k\sum_{m\geq1}\frac{(-1)^{m-1}}{m}t^m
>     \end{aligned}
>     $$
>     比较两端$\left[\dfrac{t^n}{n!}u^{k-1}\right]$, 得. (右端$k$换成 $k-1$, $m+n$换成$n$)
> 2.  由
>
>     $$
>     \sum_{n,k\geq0}s(n,k)\frac{t^n}{n!}u^k=(1+t)^u,
>     $$
>
>     两边关于$t$求导, 得
>
>     $$
>     \begin{aligned}
>     \sum_{n,k\geq0}s(n,k)\frac{t^{n-1}}{(n-1)!}u^k&=u(1+t)^{u-1}=\frac{u}{1+t}(1+t)^u\\
>     &=\sum_{m\geq0}(-1)^mt^m\cdot \sum_{l,k\geq0}s(l,k)\frac{t^l}{l!}u^{k+1}
>     \end{aligned}
>     $$
>
>     比较两端$\left[\dfrac{t^n}{n!}u^{k+1}\right]$的系数, 得.
>
>     方法二: 直接通过原始递归式得到.

定理C: 第一类Stirling数满足"水平"递推关系

1.  $$
    (n-k)s(n,k)=\sum_{l=k+1}^n(-1)^{l-k}\binom{l}{k-1}s(n,l),
    $$

2.  $$
    s(n,k)=\sum_{l=k}^ns(n+1,l+1)n^{l-k}.
    $$

> 证明:
>
> 1.  根据$\sum\limits_{k=0}^ns(n,k)x^k=(x)_n$, 得到
>     $$
>     \begin{aligned}
>     (x)_{n+1}=x(x-1)_n&=x\sum_{l=0}^ns(n,l)(x-1)^l\\
>     &= x\sum_{l=0}^ns(n,l)\sum_{h\geq0}(-1)^{l-h}\binom lh x^h\\
>     &=\sum_{h,l\geq0}(-1)^{l-h}s(n,l)\binom lh x^{h+1}\\
>     (x)_{n+1}=(x-n)(x)_n&=(x-n)\sum_{j=0}^ns(n,j)x^j\\
>     &=\sum_{j=0}^ns(n,j)x^{j+1}-n\sum_{j=0}^ns(n,j)x^j
>     \end{aligned}
>     $$
>     比较上式两端$[x^k]$, 得到
>     $$
>     \sum_{l=k-1}^n(-1)^{l-k+1}s(n,l)\binom{l}{k-1}=s(n,k-1)-ns(n,k),
>     $$
>     整理
>     $$
>     \sum_{l=k+1}^n(-1)^{l-k}s(n,l)\binom{l}{k-1}+ks(n,k)-s(n,k-1)=ns(n,k)-s(n,k-1)
>     $$
>     得到:
>     $$
>     (n-k)s(n,k)=\sum_{l=k+1}^n(-1)^{l-k}\binom{l}{k-1}s(n,l).
>     $$
> 2.  由:
>
>     $$
>     \sum_{k=1}^ns(n,k)u^{n-k}=(1-u)(1-2u)\cdots(1-(n-1)u),
>     $$
>
>     得
>
>     $$
>     \sum_{k=1}^{n+1}s(n+1,k)u^{n+1-k}=(1-u)(1-2u)\cdots(1-nu)\\
>     \qquad\qquad\qquad\qquad=(1-nu)\sum_{k=1}^ns(n,k)u^{n-k}.
>     $$
>
>     于是
>
>     $$
>     \sum_{k=1}^ns(n,k)u^{n-k}=(1-u)(1-2u)\cdots(1-nu)\\
>     \qquad\qquad\qquad\qquad\!\!=\frac1{1-nu}\sum_{k=1}^{n+1}s(n+1,k)u^{n+1-k}\\
>     \qquad\qquad\qquad\qquad\!\,=\sum_{j\geq0}n^j\sum_{k=1}^{n+1}s(n+1,k)u^{n+1-k+j}
>     $$
>
>     比较两端$[u^{n-k}]$, 得. (取$k=l+1$, $j=l-k$)
>
>     方法二:
>     不断递推$s(n,k)=s(n+1,k+1)+ns(n,k+1)$, 右端最后一项, 得.

定理D: 斜递推关系

1.  $$
    s(n,k)=\delta_{n,k}-\sum_{i=1}^{k}(n-i)s(n-i,k-i+1).
    $$

> 证明:
>
> 逐次递推代入.

### 第一类Stirling数的同余问题

回顾二项式系数的同余关系:

$$
\binom{p}{k}\equiv0\pmod p,\quad(0<k<p)\Rightarrow (1+x)^p\equiv1+x^p\pmod p.
$$

定理1: 对每个素数$p$, $(x)_p=x(x-1)\cdots(x-p+1)\equiv x^p-x\pmod p$, 即: 第一类Stirling数$s(n,k)$满足:
除$s(p,p)=1$外, 有

1.  $s(p,k)\equiv 0\pmod p,\quad(1<k<p)$;
2.  $s(p,1)=(-1)^{p-1}(p-1)!\equiv -1\pmod p$.

> 证明:
>
> 1.  (数学归纳法)由$s(p,p-1)=-\binom p2\equiv0\pmod p$, 以及上述定理C:
>
>     $$
>     (n-k)s(n,k)=\sum_{l=k+1}^n(-1)^{l-k}\binom{l}{k-1}s(n,l),
>     $$
>
>     ($k\geq2$)假定对$(3\leqslant)k+1\leqslant l\leqslant p-1$, 有$s(p,l)\equiv0\pmod p$, 下面证明: $s(p,k)\equiv0\pmod p$.
>
>     对于$(p-k)s(p,k)=\sum\limits_{l=k+1}^p(-1)^{l-k}\binom l{k-1}s(p,l)$, 两端对$p$取余, 得到
>
>     $$
>     -ks(p,k)\equiv (-1)^{p-k}\binom p{k-1}s(p,p)\equiv0\pmod p
>     $$
>
>     由数学归纳法, 得到1成立.
>
> 2.  由
>     $$
>     \begin{aligned}
>     (p-1)s(p,1)=\sum_{l=2}^p(-1)^{l-1}\binom l1s(p,l)&\equiv (-1)^{p-1}s(p,p)\pmod{p}\\
>     &\equiv (-1)^{p-1}\pmod{p},
>     \end{aligned}
>     $$
>     两端对$p$取余, 得到
>
> $$
>   s(p,1)=(-1)^{p-1}(p-1)!\equiv (-1)^{p}\pmod{p}=-1\pmod p.
> $$

推论: ($Fermat$定理)

对所有整数$a\ne0$, 以及素数$p$, 有

$$
a^p\equiv a\pmod p.
$$

> 证明:
>
> 由$(x)_p\equiv x^p-x\pmod p$, 令$x=a$, 得到$(a)_p\equiv a^p-a\pmod p$, 而(连续$p$个整数中必定有一个是$p$的倍数)
>
> $$
> (a)_p=a(a-1)\cdots(a-p+1)\equiv 0\pmod p\Rightarrow a^p\equiv a\pmod p.
> $$

定理2: 对每个素数$p$, 第二类Stirling数满足: 除$S(p,1)=S(p,p)=1$外, 有

$$
S(p,k)\equiv 0\pmod p,\quad (1<k<p).
$$

> 证明:
>
> 对于$k\geq2$, 由$i^p\equiv i\pmod p$, 以及$\sum\limits_{i=0}^k(-1)^{k-i}\binom ki=0$(对$x$进行$k$次差分,$k\geq2$), 得到
>
> $$
> \begin{aligned}
> k!S(p,k)&=\sum\limits_{i=0}^k(-1)^{k-i}\binom kii^p\\
> &\equiv\sum\limits_{i=0}^k(-1)^{k-i}\binom ki i\pmod p\\
> &\equiv0\pmod p\\
> \end{aligned}
> $$
>
> 于是
>
> $$
> p\,|\,k!S(n,k),
> $$
>
> 而$1<k<p$, 得到$p\nmid k!$, 所以
>
> $$
> p\,|\,S(n,k),\quad S(n,k)\equiv0\pmod p,\,(1<k<p).
> $$

## 整数分拆

定义: 正整数$n$的一个$k$部分拆为

$$
n=\lambda_1+\cdots+\lambda_k,
$$

其中$\lambda_1\geqslant\cdots\geqslant\lambda_k\geqslant1$, $\lambda_i$称为**部分**, $k$称为**部分数**.

- 记作$n\vdash\lambda,\quad\lambda=(\lambda_1,\cdots,\lambda_k)_{\geqslant}$.
- $p(n,k)$表示$n$的所有$k$部分拆的个数.
- $p(n)$表示$n$的所有分拆的个数, 有$p(n)=\sum\limits_{k=0}^np(n,k)$.
- $p(n,n)=p(n,1)=p(n,n-1)=1$;
- $p(n,2)=\left[\frac n2\right],p(n,k)=0,(k>n)$.

定理1:

1.  $$
    p(n,k)=p(n-1,k-1)+p(n-k,k),
    $$

2.  $$
    p(n+k,k)=p(n,1)+p(n,2)+\cdots+p(n,k)=\sum_{i=1}^kp(n,i).
    $$

> 证明:
>
> 1.  对$n$的第$k$部分拆进行分类:
>
>     - $\lambda_k=1$: $n-1=\lambda_1+\cdots+\lambda_k$, 所以$p(n-1,k-1)$.
>     - $\lambda_k>1$: $\lambda_i>1,(1\leqslant i\leqslant k)$, 作变换$\lambda_i'=\lambda_i-1$, 得到
>       $$
>       \sum_{i=0}^k\lambda_i'=\sum_{i=0}^k\lambda_i-k=n-k,
>       $$
>       于是$p(n-k,k)$.
>
> 2.  由$p(n+k,k)$, 得到$n+k=\lambda_1+\cdots+\lambda_k,\ (\lambda_1\geqslant\cdots\geqslant\lambda_k\geqslant1)$,
>
>     - $\lambda_k>1$, 则作变换$\lambda_i'=\lambda_i+1$, 有$p(n,k)$.
>     - $\lambda_k=1\&\lambda_{k-1}>1$, 则$\sum\limits_{i=0}^{k-1}\lambda_{i}+0=n$, 有$p(n, k-1)$.
>     - $\vdots$
>
>     证毕.
>
>     或者直接利用1展开右端第一项得到.

从2, 令$k=n$得到

$$
p(2n,n)=\sum_{i=1}^np(n,i)=p(n).
$$

### 分拆的$Ferrers$图

- 转置后仍为分拆, 称为**共轭分拆**.
- 若$\lambda=\lambda'$, 称为**自共轭分拆**.

定理2

1.  $n$的$k$部分拆数$p(n,k)$等于$n$的最大部分数$k$的分拆数.
2.  $n$的至多$k$个部分的分拆数$\sum\limits_{j=1}^kp(n,j)$等于$n$的最大部分至多是$k$ 的分拆数.

> 证明:
>
> 直接从Ferrers图的转置即可看出.

利用Ferrers图重新证明分拆数的递推关系(定理1)

1.  $$
    p(n,k)=p(n-1,k-1)+p(n-k,k),
    $$

2.  $$
    p(n+k,k)=p(n,1)+p(n,2)+\cdots+p(n,k)=\sum_{i=1}^kp(n,i).
    $$

> 证明:
>
> 直接由Ferrers图.

定理3:

$n$ 的自共轭分拆的个数等于$n$的各部分都是奇数且两两不同非分拆的个数.

> 由Ferrers图易证.

对于$n$的一个分拆$\lambda=(\lambda_1,\lambda_2,...)_{\geqslant}$, 合并同类项, 则可以写成$\lambda=1^{k_1}2^{k_2}\cdots n^{k_n}$, 若$k_i=0$, 略去$i^{k_i}$项.

例:

$$
n=30,\ \lambda=(9,5,4,4,4,2,1,1),\Rightarrow, \lambda=1^22^14^35^19^1.
$$

定理4:

1.  $n$的所有分拆与方程$x_1+2x_2+\cdots+nx_n=n$的所有非负整数解一一对应.
2.  $n$的所有$k$部分拆与方程组$\begin{cases}x_1+2x_2+\cdots+nx_n=n\\x_1+x_2+\cdots+x_n=k\end{cases}$的所有非负整数解一一对应.

定理5:

$n$的各部分拆都是奇数的分拆的个数等于$n$的各部分两两不同的分拆的个数.

> 证明: 利用数字的二进制表示, 建立一一对应, 即可证明.
>
> 任取各分部都是奇数的一个分拆$\pi$, 例如$5^43^31^5$, 再把各分部的正的重数写成2的幂和, 即
>
> $$
> 4=2^2,3=2^1+2^0,5=2^2+2^0,
> $$
>
> 将其按展开的幂和中每一项幂$2^j$所对应的$2^j$个相同行($i2^j$个点)合并成一个新的分拆如下
>
> $$
> \pi_1=(20,6,4,3,1),
> $$
>
> 因为任一正整数写成$i2^j$, 其中$i$是奇数 的方式是唯一的, 所以$π_1$的各部分两两不同, 并且容易验证上述对应是一一的(从十进制到二进制的对应), 所以我们证明了定理.

分拆数的球盒模型:

$$
p(n,k): n=\lambda_1+\cdots+\lambda_k, (\lambda_1\geqslant\cdots\geqslant\lambda_k\geqslant1).
$$

将$n$个相同的球放入$k$个相同的盒子, 且每个盒子中至少有一个球的不同放法.

## 球盒模型的十二模式

$$
n球\stackrel{f}{\longrightarrow}k盒
$$

| $n$球 | $k$盒 | $f$单 | $f$满 | $f$不加限制 |
| :---: | :---: | :---: | :---: | :---------: |
| 不同  | 不同  |   ①   |   ②   |      ③      |
| 相同  | 不同  |   ④   |   ⑤   |      ⑥      |
| 不同  | 相同  |   ⑦   |   ⑧   |      ⑨      |
| 相同  | 相同  |   ⑩   |   ⑪   |      ⑫      |

1.  $n$不同球放入$k$不同盒子, 且每个盒子至多一个球, ($k\geq n$)

    $$
    k(k-1)\cdots(k-n+1)=(k)_n.
    $$

    对应**集合的排列问题**.

2.  $n$不同球放入$k$不同盒子, 每个盒子至少一个球, ($k\leq n$)
    $$
    k!S(n,k)\qquad\text{集合的划分:第二类Stirling数,(对应于⑧), 但是块之间有序(前面乘以}k!\text{)}
    $$
3.  $n$不同球放入$k$不同盒子, 球数不加限制.

    $$
    k\cdot k\cdots k=k^n.
    $$

    > 由2和3, (对第三种情况分类: 如果恰好有$i$个盒子有球) 可以得到第二类Stirling数的解析表达:
    >
    > $$
    > k^n=\sum_{i=1}^k\binom ki i!S(n,i)=\sum_{i=1}^nS(n,i)(k)_i
    > $$
    >
    > 当$i=0$时, 因为$S(n,0)=0$,于是上式仍然成立.

4.  $n$相同球放入$k$不同盒子, 且每个盒子至多一个球, ($k\geq n$), 即从$k$个不同的盒子中选取$n$个盒子放$n$个球

    $$
    \binom kn,\qquad x_1+x_2+\cdots+x_k=n, (x_i=0\ or\ 1).
    $$

5.  $n$相同球放入$k$不同盒子, 且每个盒子至少一个球, ($k\leq n$), **(插板问题)** $n-1$位置插入$k-1$板:

    $$
    \binom{n-1}{k-1},\qquad x_1+x_2+\cdots+x_k=n, (x_i=1,2,...)
    $$

6.  $n$相同球放入$k$不同盒子, 且每个盒子中球数不加限制 (**重集的组合**)

    $$
    \left(\!\!\left(\begin{matrix}k\\n\end{matrix}\right)\!\!\right)=\binom{k+n-1}{n},\qquad x_1+x_2+\cdots+x_k=n, (x_i=0,1,2,...)\\
    x_1'+x_2'+\cdots+x_k'=n+k,x_i'=x_i+1, (x_i'=1,2,...)
    $$

    > 从5,6可以得到(若恰好有$i$个盒子有球, 先取盒子, 再放球)
    >
    > $$
    > \binom{k+n-1}{n}=\sum_{i=1}^k\binom ki \binom {n-1}{i-1}=\sum_{i=1}^k\binom ki \binom{n-1}{n-i}
    > $$
    >
    > $\binom{n-1}{-1}=0$,所以$i=0$仍然成立.
    >
    > 为**Chu-Vandemonde卷积公式**:
    >
    > $$
    > \binom{m+n}k=\sum_{i=0}^k\binom mi\binom n{k-i}.
    > $$

7.  $n$不同球放入$k$相同盒子, 且每个盒子中至多一个球, (分成一元子集或空集)

    $$
    N=N_1\cup N_2\cup\cdots\cup N_k,\,(|N_i|=0\ or\ 1)\quad
    \begin{cases}
    1,&(k\geq n)\\
    0,&(k<n)
    \end{cases}
    $$

8.  $n$不同球放入$k$相同盒子, 且每个盒子中至少一个球($k\leq n$),
    集合划分问题(无序), 为第二类Stirling数$S(n,k)$, $N=N_1\cup N_2\cup\cdots\cup N_k,\,(N_i\ne\varnothing)$.

9.  $n$不同球放入$k$相同盒子, 且盒中球数不加限制.
    假设恰好有$i$个盒子有球, 则$\sum\limits_{i=1}^kS(n,i)$.

10. $n$相同球放入$k$相同盒子, 且每个盒子中至多一个球
    $$
    n=\lambda_1+\cdots+\lambda_k \ (\lambda_i=0\ or\ 1) \qquad\begin{cases}
    1,&(k\geq n)\\
    0,&(k<n)
    \end{cases}
    $$
11. $n$相同球放入$k$相同盒子, 且每个盒子中至少一个球($k\leq n$) 对应**整数分拆**问题

    $$
    n=\lambda_1+\cdots+\lambda_k (\lambda_i\geq1) \qquad p(n,k)
    $$

12. $n$相同球放入$k$相同盒子, 且每个盒子球数不加限制
    $$
    \sum_{i=1}^kp(n,i)=p(n,1)+p(n,2)+\cdots+p(n,k)=p(n+k,k).
    $$

## 分拆的生成函数

假定: $|q|<1$.

- $$
  (x:q)_\infty=\prod_{k\geq0}(1-q^kx)=(1-x)(1-qx)\cdots(1-q^kx)\cdots,
  $$

- $$
  (x:q)_n=\frac{(x:q)_\infty}{(q^nx:q)_\infty}=(1-x)(1-qx)\cdots(1-q^{n-1}x)=\prod_{k=0}^{n-1}(1-q^kx),
  $$

- $$
  \begin{aligned}
  (x:q)_0=1,\qquad\lim_{q\to1}\frac{(q^x:q)_n}{(1-q)^n}&=\lim_{q\to1}\frac{(1-q^x)(1-q^{x+1})\cdots(1-q^{x+n-1})}{(1-q)^n}\\
  &=x(x+1)\cdots(x+n-1)=(x)_n\qquad \text{(表示升阶乘)}
  \end{aligned}
  $$

定义1

- $P(n|S)$表示$n$的分拆部分属于$S$ 的分拆数;
- $P_l(n|S)$表示$n$的分拆部分属于$S$, 且部分数恰为$l$的分拆数;
- $Q(n|S)$表示$n$的分拆部分互异且属于$S$ 的分拆数;
- $Q_l(n|S)$表示$n$的分拆部分互异且属于$S$, 部分数恰好为$l$的分拆数.

定理1

1.  $$
    \sum_{n\geq0}P(n|S)q^n=\prod_{k\in S}\frac1{1-q^k},
    $$

2.  $$
    \sum_{l,n\geq0}P_l(n|S)x^lq^n=\prod_{k\in S}\frac1{1-q^kx}.
    $$

上述式子也被称为$q-$级数恒等式.

> 证明:
>
> 1.  $$
>     \prod_{k\in S}\frac1{1-q^k}=\prod_{k\in S}\sum_{m_k\geq0}q^{km_k}=\sum_{\stackrel{m_k\geq0}{k\in S}}q^{\sum\limits_{k\in S}km_k},
>     $$
>
>     于是
>
>     $$
>     \Large
>     \begin{aligned}
>     \ [q^n]\prod_{k\in S}\frac1{1-q^k}&=[q^n]\sum_{\stackrel{m_k\geq0}{k\in S}}q^{\sum\limits_{k\in S}km_k}\\
>     &=\sum_{\stackrel{\sum\limits_{k\in S}km_k=n}{m_k\geq0,\ k\in S}}1
>     \end{aligned}
>     $$
>
>     即$\sum\limits_{k\in S}km_k=n$的非负整数解的个数$\iff n=1^{m_1}2^{m_2}\cdots n^{m_n}$, 且部分属于$S$, 即$P(n|S)$.
>
> 2.  $$
>      \prod_{k\in S}\frac1{1-xq^k}=\prod_{k\in S}\sum_{m_k\geq0}x^{m_k}q^{km_k}=\sum_{\stackrel{m_k\geq0}{k\in S}}x^{\sum\limits_{k\in S}m_k}q^{\sum\limits_{k\in S}km_k},
>     $$
>
>     $$
>     \Large\begin{aligned}
>     \ [x^lq^n]\prod_{k\in S}\frac1{1-xq^k}&=[x^lq^n]\sum_{\stackrel{m_k\geq0}{k\in S}}x^{\sum\limits_{k\in S}m_k}q^{\sum\limits_{k\in S}km_k}\\
>     &=\sum_{\stackrel{\large\sum\limits_{k\in S}m_k=l}{\small\sum\limits_{k\in S}km_k=n}}1
>     \end{aligned}
>     $$
>
>     即方程组$\begin{cases}\sum\limits_{k\in S}m_k=l\\\sum\limits_{k\in S}km_k=n\end{cases}$的非负整数解的个数,
>
>     即$n=1^{m_1}\cdots n^{m_n}$且部分属于$S$, 部分数恰好为$l$的分拆$P_l(n|S)$.

定理2:

1.  $$
    \sum_{n\geq0}Q(n|S)q^n=\prod_{k\in S}{(1+q^k)},
    $$

2.  $$
    \sum_{l,n\geq0}Q_l(n|S)x^lq^n=\prod_{k\in S}{(1+xq^k)}.
    $$

> 对$m_k$, 要么不取, 要么取1次, 于是由定理1证明即得.

例题: 1,2,5,10能组成$n$ 的方法数$a_n$的方法数的生成函数为?

> 解:
>
> $$
> S=\{1,2,5,10\},\Rightarrow a_n=P(n|S).
> $$
>
> 于是
>
> $$
> \sum_{n\geq0}a_nq^n=\frac1{1-q}\cdot\frac1{1-q^2}\cdot\frac1{1-q^5}\cdot\frac1{1-q^{10}}=\prod_{k\in S}\frac1{1-q^k},
> $$
>
> 类比之前的生成函数:
>
> $$
> \sum_{n\geq0}a_nx^n=(1+x+x^2+\cdots)(1+x^2+x^4+\cdots)(1+x^5+x^{10}+\cdots)(1+x^{10}+x^{20}+\cdots)
> $$

定义2

- $P(n)$: $n$的所有分拆数:
- $P_l(n)$: $n$的$l$部分分拆数($P(n,l)$):
- $Q(n)$: $n$的所有部分互异的分拆数:
- $Q_l(n)$: $n$的所有部分互异的$l$部分拆数.

定理3

- $$
  \sum_{n\geq0}P(n)q^n=\prod_{k\geq1}\frac1{1-q^k}=\frac1{(q:q)_{\infty}};
  $$

- $$
  \sum_{n,l\geq0}P_l(n)x^lq^n=\prod_{k\geq1}\frac1{1-xq^k}=\frac1{(qx:q)_{\infty}};
  $$

- $$
  \sum_{n\geq0}Q(n)q^n=\prod_{k\geq1}({1+q^k})=(-q:q)_{\infty};
  $$

- $$
  \sum_{n,l\geq0}Q_l(n)x^lq^n=\prod_{k\geq1}({1+xq^k})={(-qx:q)_{\infty}}.
  $$

> 证明由定理2易得.
>
> 由前面定义:
>
> $$
> (x:q)_\infty=\prod_{k\geq0}(1-q^kx)=(1-x)(1-qx)\cdots(1-q^kx)\cdots,
> $$
>
> 我们可以化简:
>
> $$
> \begin{aligned}
> (-q:q)_{\infty}&=(1+q)(1+q^2)\cdots=\frac{1-q^2}{1-q}\cdot\frac{1-q^4}{1-q^2}\cdots=\frac{(q^2:q^2)_\infty}{(q:q)_\infty}\\
> &=\frac{(q^2:q^2)_\infty}{(q:q^2)_\infty(q^2:q^2)_\infty}=\frac{1}{(q:q^2)_\infty}=\frac1{(1-q)(1-q^3)\cdots}
> \end{aligned}
> $$
>
> 比较两端$[q^n]$,
>
> $$
> \Rightarrow n\text{部分互异的分拆数}=n\text{的部分为奇数的分拆数}.
> $$

定理4:

1.  $$
    \sum_{n\geq0}P_m(n)q^n=\frac{q^m}{(1-q)(1-q^2)\cdots(1-q^m)}=\frac{q^m}{(q:q)_m},
    $$

2.  $$
    \sum_{n\geq0}Q_m(n)q^n=\frac{q^{\binom {m+1}2}}{(1-q)(1-q^2)\cdots(1-q^m)}=\frac{q^{\binom {m+1}2}}{(q:q)_m}.
    $$

> 证明:
>
> 1.  根据
>     $$
>     \sum_{n,l\geq0}P_l(n)x^lq^n=\frac1{(qx:q)_{\infty}}=\sum_{l\geq0}x^l\sum_{n\geq0}P_l(n)q^n,
>     $$
>     比较两端$[x^m]$,
>     $$
>     \sum_{n\geq0}P_m(n)q^n=[x^m]\frac1{(qx:q)_{\infty}},
>     $$
>     令
>     $$
>     \frac1{(qx:q)_{\infty}}=\sum_{n\geq0}A_n(q)x^n,\quad (A_0(q)=1),
>     $$
>     于是
>     $$
>     (1-qx)\sum_{n\geq0}A_n(q)x^n=\frac1{(q^2x:q)_\infty}=\sum_{n\geq0}A_n(q)(qx)^n,
>     $$
>     比较两端$[x^n]$, 得到
>     $$
>     A_n(q)-qA_{n-1}(q)=q^nA_n(q),
>     $$
>     于是
>     $$
>     \begin{aligned}
>     A_n(q)&=\frac{q}{1-q^n}A_{n-1}(q)=\frac q{1-q^n}\cdot\frac{q}{1-q^{n-1}}\cdots\frac q{1-q}\cdot1\\
>     &=\frac{q^n}{(q:q)_n}
>     \end{aligned}
>     $$
>     所以:
>     $$
>     \sum_{n\geq0}P_m(n)q^n=\frac{q^m}{(1-q)(1-q^2)\cdots(1-q^m)}=\frac{q^m}{(q:q)_m}.
>     $$
> 2.  由:
>     $$
>     \sum_{n,l\geq0}Q_l(n)x^lq^n ={(-qx:q)_{\infty}}=\sum_{k\geq0}x^l\sum_{n\geq0}Q_l(n)q^n,
>     $$
>     于是
>     $$
>     \sum_{n\geq0}Q_m(n)q^n=[x^m](-qx:q)_\infty,
>     $$
>     令
>     $$
>     (-qx:q)_\infty=\sum_{n\geq0}B_n(q)x^n,\quad(B_0(q)=1),
>     $$
>     由
>     $$
>     \sum_{n\geq0}B_n(q)x^n=(1+qx)(-q^2x:q)_\infty=(1+qx)\sum_{n\geq0}B_n(q)(qx)^n,
>     $$
>     比较两端$[x^n]$, 得到
>     $$
>     B_n(q)=q^nB_n(q)+q^{n}B_{n-1}(q),
>     $$
>     于是
>     $$
>     B_n(q)=\frac{q^n}{1-q^n}B_{n-1}(q)=\frac{q^n}{1-q^n}\cdot\frac{q^{n-1}}{1-q^{n-1}}\cdots\frac q{1-q}=\frac{q^{\binom {n+1}2}}{(q:q)_n},
>     $$
>     所以:
>     $$
>     \sum_{n\geq0}Q_m(n)q^n=\frac{q^{\binom {m+1}2}}{(1-q)(1-q^2)\cdots(1-q^m)}=\frac{q^{\binom {m+1}2}}{(q:q)_m}.
>     $$

定义3

- $P^m(n)$: $n$的部分数$\leqslant m$的分拆数;
- $Q^m(n)$: $n$的部分数$\leqslant m$的互异分拆数.

定理5

$$
\sum_{n\geq0}P^m(n)q^n=\frac1{(q:q)_m}.
$$

进而, 有

$$
\frac1{(q:q)_m}=\sum_{k=0}^m\frac{q^k}{(q:q)_k},
$$

令$m\to\infty$, 有

$$
\frac1{(q:q)_\infty}=\sum_{k\geq0}\frac{q^k}{(q:q)_k}.
$$

> 证明:
>
> 因为$P^m(n)$表示$n$的部分数$\leqslant m$的分拆数, 根据共轭分拆, 其与$n$ 的最大部分$\leqslant m$的分拆数相同(分拆一一对应),
>
> $$
> P^m(n)=P(n|S),S=[m]=\{1,2,...,m\}
> $$
>
> 由
>
> $$
> \sum_{n\geq0}P(n|S)q^n=\prod_{k\in S}\frac1{1-q^k},\Rightarrow \sum_{n\geq0}P^m(n)q^n=\prod_{k=1}^m\frac1{1-q^k}=\frac1{(q:q)_m}.
> $$

或者也可以从Ferrers图中看定理4和5(利用共轭分拆的性质即可).

## 分拆数恒等式

定理6 : Gauss分拆恒等式

$$
\frac1{(x:q)_\infty}=\sum_{n\geq0}\frac{x^n}{(q:q)_n.}
$$

> 证明:
>
> 由
>
> $$
> \sum_{n,l\geq0}P_l(n)x^lq^n=\prod_{k\geq1}\frac1{1-xq^k}=\frac1{(qx:q)_{\infty}};
> $$
>
> 得到:
>
> $$
> \begin{aligned}
> \frac1{(qx:q)_{\infty}}&=\sum_{l\geq0}x^l\sum_{n\geq0}P_l(n)q^n\\
> &=\sum_{l\geq0}x^l\frac{q^l}{(q:q)_l}
> \end{aligned}
> $$
>
> 令$x\to \frac xq$, 得到
>
> $$
> \frac1{(x:q)_\infty}=\sum_{l\geq0}\frac{x^l}{(q:q)_l}.\quad\left(\frac1{(q:q)_\infty}=\sum_{k\geq0}\frac{q^k}{(q:q)_k}.\right)
> $$

定理7 (Euler分拆恒等式)

$$
(x:q)_\infty=\sum_{n\geq0}\frac{(-1)^nq^{\binom n2}}{(q:q)_n}x^n.
$$

> 证明:
>
> 根据
>
> $$
> \sum_{n,l\geq0}Q_l(n)x^lq^n=\prod_{k\geq1}({1+xq^k})={(-qx:q)_{\infty}},
> $$
>
> 得到:
>
> $$
> \begin{aligned}
> {(-qx:q)_{\infty}}&=\sum_{l\geq0}x^l\sum_{n\geq0}Q_l(n)q^n\\
> &=\sum_{l\geq0}x^l\frac{q^{\binom {l+1}2}}{(q:q)_l}
> \end{aligned}
> $$
>
> 令$x\to-\frac xq$, 得到
>
> $$
> (x:q)_\infty=\sum_{l\geq0}\frac{(-1)^lq^{\binom l2}}{(q:q)_n}x^l.
> $$

定理8: $n$的自共轭分拆的个数等于$n$的各部分都是奇数且两两不同分分拆的个数. (利用生成函数证明, Euler分拆恒等式)

<img src="https://s2.loli.net/2021/12/10/1bSQa8gvZWKUl3N.png" alt="截屏2021-12-08 下午6.20.00" style="zoom:30%;" />

> 证明:
>
> 由(Euler恒等式)
>
> $$
> (-qx:q^2)_\infty=\sum_{n\geq0}\frac{q^{n^2}x^n}{(q^2:q^2)_n},
> $$
>
> 令$x=1$,
>
> $$
> (-q:q^2)_\infty=\sum_{n\geq0}\frac{q^{n^2}}{(q^2:q^2)_n},
> $$
>
> 意义:
>
> - 左端: 各部分都是奇数的分拆.
>   $$
>   (-q:q^2)_\infty=(1+q)(1+q^3)\cdots
>   $$
> - 右端: 自共轭分拆, 利用上节定理5, 中间为$q^{n^2}$, 旁边为$\leqslant n$, 即$\frac1{(q^2:q^2)_\infty}$.

定义4:

- $P_l(n|\leqslant m)$: $n$的$l$部分拆, 且每部分$\leqslant m$的分拆数;
- $P^l(n|\leqslant m)$: $n$的部分数$\leqslant l$, 且每部分$\leqslant m$的分拆数;
- $Q_l(n|\leqslant m)$: $n$的$l$部互异分拆, 且每部分$\leqslant m$的分拆数.

定理9:

$$
\sum_{n,l\geq0}P_l(n|\leqslant m)x^lq^n=\frac1{(qx:q)_m}\\
\ \sum_{n,l\geq0}Q_l(n|\leqslant m)x^lq^n={(-qx:q)_m}
$$

类比:

- $$
  \sum_{n,l\geq0}P_l(n)x^lq^n=\prod_{k\geq1}\frac1{1-xq^k}=\frac1{(qx:q)_{\infty}};
  $$

- $$
  \sum_{n,l\geq0}Q_l(n)x^lq^n=\prod_{k\geq1}({1+xq^k})={(-qx:q)_{\infty}}.
  $$

以及:

- $$
  \sum_{l,n\geq0}P_l(n|S)x^lq^n=\prod_{k\in S}\frac1{1-q^kx}.
  $$

- $$
  \sum_{l,n\geq0}Q_l(n|S)x^lq^n=\prod_{k\in S}{(1+xq^k)}.
  $$

定理10 :Jacobi 三重积恒等式

$$
(q^2:q^2)_\infty(-qx:q^2)_\infty(-q/x:q^2)_\infty=\sum_{n}q^{n^2}x^n,\\
(q:q)_\infty(x:q)_\infty(q/x:q)_\infty=\sum_{n}(-1)^nq^{\binom n2}x^n\quad(-qx\to x,q^2\to q).
$$

> 证明:
> 根据Euler分拆恒等式, 以及$(x:q)_\infty=(x:q)_n(q^nx:q)_\infty\iff (q^2:q^2)_\infty=(q^2:q^2)_n(q^{2n+2}:q^2)_\infty$,
>
> $$
> \begin{aligned}
> (-qx:q^2)_\infty&=\sum_{n\geq0}\frac{q^{n^2}x^n}{(q^2:q^2)_n}\\
> &=\frac1{(q^2:q^2)_\infty}\sum_{n\geq0}q^{n^2}x^n(q^{2n+2}:q^2)_\infty\\
> &=\frac1{(q^2:q^2)_\infty}\sum_{n}q^{n^2}x^n(q^{2n+2}:q^2)_\infty \qquad\big(n<0,(q^{2n+2}:q^2)=0\big)\\
> &=\frac1{(q^2:q^2)_\infty}\sum_{n}q^{n^2}x^n\sum_{m\geq0}\frac{(-1)^mq^{m^2+m+2mn}}{(q^2:q^2)_m}\qquad(Euler)\\
> &=\frac1{(q^2:q^2)_\infty}\sum_{m\geq0}\frac{(-1)^mq^{m}x^{-m}}{(q^2:q^2)_m}\sum_{n}q^{(m+n)^2}x^{m+n}\\
> &=\frac1{(q^2:q^2)_\infty}\sum_{m\geq0}\frac{(-q/x)^m}{(q^2:q^2)_m}\sum_{n}q^{n^2}x^{n}\qquad(Gauss)\\
> &=\frac1{(q^2:q^2)_\infty}\frac1{(-q/x:q^2)_\infty}\sum_{n}q^{n^2}x^{n}\\
> \end{aligned}
> $$

定理11: Jacobi恒等式

$$
(q:q)_\infty^3=\sum_{n\geq0}(-1)^n(2n+1)q^{\binom {n+1}2}.
$$

> 证明:
>
> 由
>
> $$
> \begin{aligned}
> (q:q)_\infty(x:q)_\infty(q/x:q)_\infty&=\sum_{n}(-1)^nq^{\binom n2}x^n\\
> &=\sum_{n\geq1}(-1)^nq^{\binom n2}x^n+\sum_{n\geq0}(-1)^nq^{\binom {n+1}2}x^{-n}\\
> &=-\sum_{n\geq0}(-1)^nq^{\binom {n+1}2}x^{n+1}+\sum_{n\geq0}(-1)^nq^{\binom {n+1}2}x^{-n}\\
> &= \sum_{n\geq0}(-1)^n\big(x^{-n}-x^{n+1}\big)q^{\binom {n+1}2}\\
> \end{aligned}
> $$
>
> 两边同时除以$1-x$, 并令$x\to1$, 得到:
>
> $$
> (q:q)_\infty^3=\sum_{n\geq0}(-1)^n(2n+1)q^{\binom {n+1}2}.
> $$

定理12 Gauss三角数定理(Jacobi恒等式的特例)

$$
\frac{(q^2:q^2)_\infty}{(q:q^2)_\infty}=\sum_{n\geq0}q^{\binom {n+1}2}.
$$

> 三角形数:
>
> $$
> \binom{n+1}2=1,3,6,10,15,\cdots
> $$

> 证明:
>
> 由平方差公式以及$(q:q)_\infty=(q:q^2)_\infty(q^2:q^2)_\infty$, 得到
>
> $$
> \begin{aligned}
> \frac{(q^2:q^2)_\infty}{(q:q^2)_\infty}&=\frac{(q:q)_\infty(-q:q)_\infty}{(q:q^2)_\infty}\\
> &=\frac{(q:q^2)_\infty(q^2:q^2)_\infty(-q:q)_\infty}{(q:q^2)_\infty}\\
> &=(q^2:q^2)_\infty(-q:q)_\infty\\
> &=(q:q)_\infty(-q:q)_\infty(-q:q)_\infty\\
> &=\frac1{1+1}(q:q)_\infty(-1:q)_\infty(-q:q)_\infty\\
> &=\frac12\sum_n(-1)^nq^{\binom n2}(-1)^n\quad(Jacobi)\\
> &=\frac12\left(\sum_{n\geq1}q^{\binom n2}+\sum_{n\geq0}q^{\binom{n+1}2}\right)=\sum_{n\geq0}q^{\binom {n+1}2}.
> \end{aligned}
> $$

定理13 Euler五角数定理

$$
\begin{aligned}
(q:q)_\infty&=\sum_k(-1)^kq^{\frac{k(3k-1)}2}=\sum_k(-1)^kq^{\frac{k(3k+1)}2}\\
&=1+\sum_{k\geq1}(-1)^k\left(q^{\frac{k(3k-1)}2}+q^{\frac{k(3k+1)}2}\right)
\end{aligned}
$$

> 五角形数$\dfrac{n(3n-1)}2:1,5,12,22,\cdots$

> 证明:利用Jacobi三重积恒等式
>
> $$
> \begin{aligned}
> (q:q)_\infty&=(1-q)(1-q^2)(1-q^3)(1-q^4)(1-q^5)(1-q^6)\cdots\quad(间隔2项取)\\
> &=(q:q^3)_\infty(q^2:q^3)_\infty(q^3:q^3)_\infty\\
> &=(q^3:q^3)_\infty(q^2:q^3)_\infty(q:q^3)_\infty\quad(令x=q^2,或者x=q均可)\\
> &=\sum_n(-1)^nq^{3\binom n2}q^{2n}\\
> &=\sum_n(-1)^nq^{3\binom n2+2n}.
> \end{aligned}
> $$

定理14 Euler五角形数定理的组合证明

令$Q_e(n)\big($或$Q_o(n)\big)$为$n$分成偶数(或奇数)个部分互异的分拆数, 则

$$
Q_e(n)-Q_o(n)=
\begin{cases}
(-1)^k,&n=\dfrac{3k^2\pm k}2\\
0,&n\ne \dfrac{3k^2\pm k}2
\end{cases}
$$

> 证明:
>
> 对于$n$的部分互异的分拆: $\lambda=(\lambda_1,\cdots,\lambda_r)_{>}$,
>
> 定义:
>
> - $S(\lambda)$表示$n$ 的互异分拆$\lambda$的最小部分,($S(\lambda)=\lambda_r$).
> - $\sigma(\lambda)$表示从$\lambda_1$开始, 连续整数的长度.

例子:

<div align="center"><img src="https://s2.loli.net/2021/12/10/quvOf4gwtkHXphI.png" alt="66" style="zoom:55%;" /></div>

- 当$s(\lambda)\leq\sigma(\lambda)$, 对$\lambda=(7,6,4,3,2)$作变换:

  <div align="center"><img src="https://s2.loli.net/2021/12/11/XKd41C9zRNSTmIx.png" alt="截屏2021-12-11 上午12.33.48" style="zoom:25%;" /></div>

- 当$s(\lambda)>\sigma(\lambda)$, 对$\lambda'=(8,7,4,3)$作变换:

  <img src="https://s2.loli.net/2021/12/11/LvQoJscdNBUHaFG.png" alt="截屏2021-12-11 上午12.45.30" style="zoom:60%;" />

在上述两种变换下:

$$
Q_e(n)\rightleftarrows Q_o(n)
$$

但是当出现下述情况时, 无法执行:

1.  对于第一种变换, 若$n$的互异分拆部分数为$k$, 且$s(\lambda)=\sigma(\lambda)=k$, 即

    $$
    n=k+(k+1)+\cdots+(k+(k-1))=k^2+\binom k2=\frac{3k^2-k}2,
    $$

    于是

    $$
    Q_e(n)=Q_o(n)+(-1)^k.
    $$

2.  对于第二种变换, 若$n$的互异分拆部分数为$k$, 且$\sigma(\lambda)=k,s(\lambda)=k+1$, 即
    $$
    n=(k+1)+\cdots+2k=k^2+\binom {k+1}2=\frac{3k^2+k}2,
    $$
    于是
    $$
    Q_e(n)=Q_o(n)+(-1)^k.
    $$

综上:

- $n$不是五角形数: $Q_e(n)=Q_o(n)$.
- $n$是五角形数: $n=\dfrac12k(3k\pm1)$, $Q_e(n)=Q_o(n)+(-1)^k$.

推论: (Euler五角形数定理)

$$
\begin{aligned}
(q:q)_\infty&=\sum_k(-1)^kq^{\frac{k(3k-1)}2}=\sum_k(-1)^kq^{\frac{k(3k+1)}2}\\
&=1+\sum_{k\geq1}(-1)^k\left(q^{\frac{k(3k-1)}2}+q^{\frac{k(3k+1)}2}\right)
\end{aligned}
$$

> 证明: 根据
>
> $$
> 1+\sum_{k\geq1}(-1)^k\left(q^{\frac{k(3k-1)}2}+q^{\frac{k(3k+1)}2}\right)=1+\sum_{n\geq1}\big(Q_e(n)-Q_o(n)\big)q^n
> $$
>
> 而:
>
> $$
> \begin{aligned}
> (q:q)_\infty&=\prod_{k\geq1}(1-q^k)=\prod_{k\geq1}\sum_{a_k=0,1}(-1)^{a_k}q^{ka_k}\\
> &=\sum_{\stackrel{a_1,a_2,...,a_k=0,1}{k\geq1}}(-1)^{\sum_ka_k}q^{\sum_kka_k}\\
> &=\sum_{a_1=0,1}\sum_{a_2=0,1}\cdots(-1)^{a_1+a_2+\cdots}q^{1\cdot a_1+2\cdot a_2+\cdots}
> \end{aligned}
> $$
>
> 取$[q^n]$, 即
>
> $$
> n=1a_1+2a_2+\cdots=1^{a_1}2^{a_2}\cdots,\quad a_i=0\ or\ 1.
> $$
>
> 为一部分互异的分拆, 这里$\sum_ia_i$为$n$的部分互异分拆的部分数.

定理15 ($p(n)$的递推关系式)

$$
\begin{aligned}
p(n)&=p(n-1)+p(n-2)-p(n-5)-p(n-7)+\cdots\quad(n>0)\\
&=\sum_{k\geq1}(-1)^{k-1}\left(p\left(n-\frac{k(3k-1)}2\right)+p\left(n-\frac{k(3k+1)}2\right)\right)
\end{aligned}
$$

- $n<0$, 规定$p(n)=0$.

> 证明:
>
> 由分拆数生成函数, 得
>
> $$
> \sum_{n\geq0}P(n)q^n=\prod_{k\geq1}\frac1{1-q^k}=\frac1{(q:q)_{\infty}}\Rightarrow (q:q)_\infty\sum_{n\geq0}p(n)q^n=1
> $$
>
> 再由Euler五角数定理, 得到
>
> $$
> \Rightarrow \sum_{n\geq0}p(n)q^n\cdot\left(1+\sum_{k\geq1}(-1)^k\left(q^{\frac{k(3k-1)}2}+q^{\frac{k(3k+1)}2}\right)\right)=1,
> $$
>
> 比较两端$[q^n]$, ($n>0$)
>
> $$
> p(n)+\sum_{k\geq1}(-1)^k\left[p\left(n-\frac{k(3k-1)}2\right)+p\left(n-\frac{k(3k+1)}2\right)\right]=0,
> $$
>
> 即:
>
> $$
> p(n)=\sum_{k\geq1}(-1)^{k-1}\left(p\left(n-\frac{k(3k-1)}2\right)+p\left(n-\frac{k(3k+1)}2\right)\right).
> $$

### 分拆函数$p(n)$的同余性质

定理:

$$
\begin{aligned}
p(5n+4)&\equiv0\pmod5\\
p(7n+5)&\equiv0\pmod7\\
p(11n+6)&\equiv0\pmod{11}\\
\end{aligned}
$$

> 证明:
>
> $$
> \sum_{n\geq0}p(n)q^n=\prod_{k\geq1}\frac1{1-q^k}=\frac1{(q:q)_{\infty}},
> $$
>
> 得到:
>
> $$
> \sum_{n\geq0}p(m)q^{m+1}=\frac q{(q:q)_{\infty}}=\frac{q(q:q)_{\infty}^4}{(q:q)_\infty^5}\equiv\frac{q(q:q)_\infty^4}{(q^5:q^5)_\infty}\pmod5,\\
> \sum_{n\geq0}p(m)q^{m+2}=\frac {q^2}{(q:q)_{\infty}}=\frac{q^2(q:q)_{\infty}^6}{(q:q)_\infty^7}\equiv\frac{q^2(q:q)_\infty^6}{(q^7:q^7)_\infty}\pmod7.
> $$
>
> > 其中
> >
> > $$
> > (q:q)_\infty^5=(1-q)^5(1-q^2)^5(1-q^3)^5\cdots\equiv(1-q^5)(1-q^{10})(1-q^{15})\cdots\pmod5.
> > $$
> >
> > 由于
> >
> > $$
> > (1+x)^p\equiv1+x^p\pmod p,\quad \binom pk\equiv0\pmod p\quad(0<k<p).
> > $$
>
> 由Euler五角数定理以及Jacobi恒等式:
>
> $$
> (q:q)_\infty=\sum_k(-1)^kq^{\frac{k(3k-1)}2}=\sum_k(-1)^kq^{3\binom k2 +k},\\
> (q:q)_\infty^3=\sum_{n\geq0}(-1)^n(2n+1)q^{\binom {n+1}2}.
> $$
>
> $$
> \begin{aligned}
> q(q:q)_{\infty}^4&=q(q:q)_\infty(q:q)_\infty^3\\
> &=q\sum_k(-1)^kq^{3\binom k2 +k}\sum_{n\geq0}(-1)^n(2n+1)q^{\binom {n+1}2}\\
> &=\sum_{i\geq0}\sum_j(-1)^{i+j}(2i+1)q^{\binom{i+1}2+3\binom j2+2j+1}
> \end{aligned}
> $$
>
> 由于$(5,8)=1$, 我们有
>
> $$
> \begin{aligned}
> \binom{i+1}2+3\binom j2+2j+1&\equiv8\left\{\binom{i+1}2+3\binom j2+2j+1\right\}\pmod5\\
> &\equiv 4i^2+4i+12j^2-12j+16j+8\pmod5\\
> &\equiv 4i^2+4i+2j^2+4j+3\pmod5\\
> &\equiv(2i+1)^2+2(j+1)^2\pmod5
> \end{aligned}
> $$
>
> 又因为
>
> $$
> (2i+1)^2\equiv0,1,4\pmod5,\quad2(j+1)^2\equiv0,2,3\pmod5,
> $$
>
> 而
>
> $$
> \binom{i+1}2+3\binom j2+2j+1\equiv0\pmod5\iff\\[5pt]
> \begin{cases}
> (2i+1)^2\equiv0\pmod5\iff2i+1\equiv0\pmod5\\
> 2(j+1)^2\equiv0\pmod5
> \end{cases}
> $$
>
> $\iff p(5n+4)\equiv\pmod5$.

> 对于第二个式子:
> 由于
>
> $$
> q^2(q:q)_\infty^6=q^2(q:q)_\infty^3(q:q)_\infty^3=\sum_{i,j\geq0}(-1)^{i+j}(2i+1)(2j+1)q^{\binom{i+1}2+\binom{j+1}2+2},
> $$
>
> 而
>
> $$
> \binom{i+1}2+\binom{j+1}2+2\equiv8\left[\binom{i+1}2+\binom{j+1}2+2\right]\pmod7\\
> =(2i+1)^2+(2j+1)^2\pmod7,
> $$
>
> 又由
>
> $$
> (2n+1)^2\equiv0,1,2,4\pmod7,
> $$
>
> 当
>
> $$
> \binom{i+1}2+\binom{j+1}2+2\equiv0\pmod7\iff\\
> \begin{cases}
> (2i+1)^2\equiv0\pmod7\iff2i+1\equiv 0\pmod7\\
> (2j+1)^2\equiv0\pmod7\iff2j+1\equiv 0\pmod7\\
> \end{cases}
> $$
>
> $\iff p(7n+5)\equiv\pmod7$.

或者直接从生成函数方面进行考虑:

1.  $$
    \sum_{n\geq0}p(5n+4)q^n=5\frac{(q^5:q^5)_\infty^5}{(q:q)_\infty^6},
    $$

2.  $$
    \sum_{n\geq0}p(7n+5)q^n=7\frac{(q^7:q^7)_\infty^7}{(q:q)_\infty^4}+49q\frac{(q^7:q^7)_\infty^7}{(q:q)_\infty^8}.
    $$

### 分拆与Gauss二项式系数

定义:

- $P_l(n|\leqslant m)$: $n$的$l$部分拆, 且每部分$\leqslant m$的分拆数;
- $P^l(n|\leqslant m)$: $n$的部分数$\leqslant l$, 且每部分$\leqslant m$的分拆数;
- $Q_l(n|\leqslant m)$: $n$的$l$部互异分拆, 且每部分$\leqslant m$的分拆数.

定理1:

$$
\sum_{n,l\geq0}P_l(n|\leqslant m)x^lq^n=\frac1{(qx:q)_m}\\
\ \sum_{n,l\geq0}Q_l(n|\leqslant m)x^lq^n={(-qx:q)_m}
$$

定理2:

$$
\sum_{l,n\geq0}P^l(n|\leqslant m)x^lq^n=\frac1{(x:q)_{m+1}}.
$$

> 证明:
>
> 由于
>
> $$
> P^l(n|\leqslant m)=\sum_{k=0}^lP_k(n|\leqslant m),
> $$
>
> 以及
>
> $$
> \sum_{n,l\geq0}P_l(n|\leqslant m)x^lq^n=\frac1{(qx:q)_m},
> $$
>
> 得到:
>
> $$
> \begin{aligned}
> \sum_{l,n\geq0}P^l(n|\leqslant m)x^lq^n&=\sum_{l,n\geq0}\sum_{k=0}^lP_k(n|\leqslant m)x^lq^n\\
> &=\sum_{k,n\geq0}P_k(n|\leqslant m)q^n\sum_{l\geq k}x^l\\
> &=\sum_{k,n\geq0}P_k(n|\leqslant m)q^n\frac{x^k}{1-x}\\
> &=\frac1{1-x}\sum_{k,n\geq0}P_k(n|\leqslant m)x^kq^n\\
> &=\frac1{1-x}\cdot\frac1{(qx:q)_m}=\frac1{(x:q)_{m+1}}.
> \end{aligned}
> $$

定理3:

1.  $$
    \sum_{n\geq0}P_l(n|\leqslant m)q^n={\begin{bmatrix}l+m-1\\m-1\end{bmatrix}}q^l
    $$

2.  $$
    \sum_{n\geq0}P^l(n|\leqslant m)q^n={\begin{bmatrix}l+m\\l\end{bmatrix}}
    $$

> 其中:
>
> $$
> \begin{bmatrix}n\\k\end{bmatrix}=\frac{(q:q)_n}{(q:q)_k(q:q)_{n-k}},
> $$
>
> 称为Gauss二项式系数或者$q-$二项式系数, 当上式$q\to1$时, 得到:
>
> $$
> \lim_{q\to1}{\begin{bmatrix}n\\k\end{bmatrix}}=\lim_{q\to1}\frac{\dfrac{(q:q)_n}{(1-q)^n}}{\dfrac{(q:q)_k(q:q)_{n-k}}{(1-q)^k(1-q)^{n-k}}}=\frac{n!}{k!(n-k)!}=\binom nk.
> $$
>
> > 由于
> >
> > $$
> > \lim_{q\to1}\frac{(q:q)_n}{(1-q)^n}=n!.
> > $$

> 证明:
>
> 1.  由于$P_l(n|\leqslant m)=P^l(n|\leqslant m)-P^{l-1}(n|\leqslant m)$, 所以得到
>     $$
>     \begin{aligned}
>     \sum_{n\geq0}P_l(n|\leqslant m)q^n&=\sum_{l,n\geq0}P^l(n|\leqslant m)q^n-\sum_{n\geq0}P^{l-1}(n|\leqslant m)q^n\\
>     &={\begin{bmatrix}l+m\\l\end{bmatrix}}-{\begin{bmatrix}l-1+m\\l-1\end{bmatrix}},\quad(假定2式成立)\\
>     &={\begin{bmatrix}l+m-1\\m-1\end{bmatrix}}q^l
>     \end{aligned}
>     $$
>     故只需证明2成立, 即可.
> 2.  由
>     $$
>     \sum_{l,n\geq0}P^l(n|\leqslant m)x^lq^n=\frac1{(x:q)_{m+1}},
>     $$
>     得到:
>     $$
>     \sum_{n\geq0}P^l(n|\leqslant m)q^n=[x^l]\frac1{(x:q)_{m+1}},
>     $$
>     令
>     $$
>     \frac1{(x:q)_{m+1}}=\sum_{k\geq0}B_k(q)x^k,
>     $$
>     作代换$x\to xq$, 得到:
>     $$
>     \frac1{(xq:q)_{m+1}}=\sum_{k\geq0}B_k(q)x^kq^k,
>     $$
>     由
>     $$
>     (1-x)\frac1{(x:q)_{m+1}}=\frac1{(qx:q)_m}=\frac{1-q^{m+1}x}{(qx:q)_{m+1}},
>     $$
>     得到:
>     $$
>     (1-x)\sum_{k\geq0}B_k(q)x^k=(1-q^{m+1}x)\sum_{k\geq0}B_k(q)x^kq^k,
>     $$
>     比较两端$[x^k]$, 得到
>     $$
>     B_k(q)-B_{k-1}(q)=B_k(q)q^k-q^{m+k}B_{k-1}(q),
>     $$
>     整理得到:
>     $$
>     B_k(q)=\frac{1-q^{m+k}}{1-q^k}B_{k-1}(q),
>     $$
>     不断递推得到:(前面的式子取$x=0\Rightarrow B_0(q)=1$)
>     $$
>     B_k(q)=\frac{(q^{m+1}:q)_{k}}{(q:q)_k}B_0(q)=\frac{(q^{m+1}:q)_{k}}{(q:q)_k}\\
>     =\frac{(q:q)_{m+k}}{(q:q)_k(q:q)_{m}}={\begin{bmatrix}m+k\\k\end{bmatrix}},
>     $$
>     于是我们得到:
>     $$
>     \sum_{n\geq0}P^l(n|\leqslant m)q^n={\begin{bmatrix}l+m\\l\end{bmatrix}}={\begin{bmatrix}l+m\\m\end{bmatrix}}.
>     $$

通过Ferrers图也可以看出: 2和1的关系($2\Rightarrow1$).

定理4:

1.  $$
    \sum_{l=0}^n\begin{bmatrix}l+m\\m\end{bmatrix}q^l=\begin{bmatrix}m+n+1\\n\end{bmatrix},
    $$

2.  $$
    \sum_{l\geq0}\begin{bmatrix}l+m\\m\end{bmatrix}x^l=\frac1{(x:q)_{m+1}}.
    $$

    令$m\to\infty$, 得到

    $$
    \sum_{l\geq0}\frac{x^l}{(q:q)_l}=\frac1{(x:q)_\infty},
    $$

    即为Gauss分拆恒等式.

> 证明:
>
> 1.  利用Ferrers图证明.
> 2.  $$
>     \sum_{l\geq0}\begin{bmatrix}l+m\\m\end{bmatrix}x^l=\sum_{l\geq0}\left(\sum_{n\geq0}P^l(n|\leqslant m)q^n\right)x^l=\frac1{(x:q)_{m+1}},
>     $$

定理5:

$$
\sum_{n\geq0}Q_l(n|\leqslant m)q^n=\begin{bmatrix}m\\l\end{bmatrix}q^{\binom {l+1}2}.
$$

进而有:(双变量生成函数)

$$
(x:q)_{n}=\sum_{k=0}^n(-1)^k\begin{bmatrix}n\\k\end{bmatrix}q^{\binom k2}x^k, (\text{\color{red}Euler q-差分公式}),
$$

$$
n\to\infty\Rightarrow (x:q)_\infty=\sum_{k\geq0}\frac{(-1)^kq^{\binom k2}}{(q:q)_k}x^k,
$$

即Euler分拆恒等式.

> 证明:
>
> 从Ferrers图易得.
>
> 又由:
>
> $$
> \sum_{n,l\geq0}Q_l(n|\leqslant m)x^lq^n={(-qx:q)_m},
> $$
>
> 得到:
>
> $$
> {(-qx:q)_m}=\sum_{l\geq0}\left(\sum_{n\geq0}Q_l(n|\leqslant m)q^n\right)x^l=\sum_{l\geq0}{\begin{bmatrix}m\\l\end{bmatrix}}q^{\binom{l+1}{2}}x^l,
> $$
>
> 令$x\to -x/q$, 得到
>
> $$
> (x:q)_m=\sum_{l=0}^m(-1)^l{\begin{bmatrix}m\\l\end{bmatrix}}q^{\binom l2}x^l,
> $$
>
> 变换符号:
>
> $$
> (x:q)_n=\sum_{k=0}^n(-1)^k{\begin{bmatrix}n\\k\end{bmatrix}}q^{\binom k2}x^k,
> $$
>
> 上式令$x=q^{-m}$, 得到
>
> $$
> \sum_{k=0}^n(-1)^k{\begin{bmatrix}n\\k\end{bmatrix}}q^{\binom k2-km}=(q^{-m}:q)_n=\begin{cases}0,&0\leqslant m<n\\(-1)^nq^{-\binom{n+1}2}(q:q)_n,&m=n\end{cases}
> $$
>
> 即Euler分拆恒等式.

- 二项式系数$\binom nk$满足递推关系: $\binom nk=\binom{n-1}k+\binom{n-1}{k-1}$;

- $q-$二项式系数$\begin{bmatrix}n\\k\end{bmatrix}$满足递推关系式(通过Ferrers图):

  $$
  {\begin{bmatrix}n\\k\end{bmatrix}}=q^k{\begin{bmatrix}n-1\\k\end{bmatrix}}+{\begin{bmatrix}n-1\\k-1\end{bmatrix}}\stackrel{q\to1}{\longrightarrow}\binom nk=\binom{n-1}k+\binom{n-1}{k-1},
  $$

  或者:(通过Ferrers图另一种分法, 或者直接从上式令$k\to n-k$)

  $$
  {\begin{bmatrix}n\\k\end{bmatrix}}=q^{n-k}{\begin{bmatrix}n-1\\k-1\end{bmatrix}}+{\begin{bmatrix}n-1\\k\end{bmatrix}}\stackrel{q\to1}{\longrightarrow}\binom nk=\binom{n-1}k+\binom{n-1}{k-1}.
  $$

**Durfee矩**和分拆恒等式

定义: (Durfee方,(从左上角开始画的最大的正方形)) $\lambda=(7,6,4,2,1,1)$

<div align="center"><img src="https://s2.loli.net/2021/12/16/dq1BXgWoz3RST6E.png" style="zoom:25%;" /></div>

一般情况为Durfee矩(一个矩形)

定理6:

$$
\frac1{(qx:q)_n}=\sum_{k=0}^n{\begin{bmatrix}n\\k\end{bmatrix}}\frac{q^{k^2}x^k}{(qx:q)_k},
$$

$$
\left(n\to\infty\Rightarrow \frac1{(qx:q)_\infty}=\sum_{k\geq0}\frac{q^{k^2}x^k}{(q:q)_k(qx:q)_k}\right.\\
\left.x=1\Rightarrow\frac1{(q:q)_\infty}=\sum_{k\geq0}\frac{q^{k^2}}{(q:q)_k^2}\right)\quad\quad\!
$$

> 证明:
>
> $$
> \frac1{(qx:q)_m}=\sum_{n,l\geq0}P_l(n|\leqslant m)x^lq^n,
> $$
>
> 从Ferrers图中得出:
>
> - Durfee方($k\times k$): $q^{k^2}x^k$,(还需考虑双变量生成函数)
> - 方块右面: ${\begin{bmatrix}n\\k\end{bmatrix}}$,(只需考虑单变量生成函数, 因为方块已经考虑了部分数)
> - 方块下面: $\dfrac1{(qx:q)_m}$, (考虑双变量生成函数)

定理7: (q-Chu-Vandemende卷积公式)

1.  $$
    {\begin{bmatrix}\alpha+r\\n\end{bmatrix}}=\sum_{k=0}^n{\begin{bmatrix}\alpha\\k\end{bmatrix}}{\begin{bmatrix}r\\n-k\end{bmatrix}}q^{(\alpha-k)(n-k)}\\
    q\to1,\ \ \binom{\alpha+r}n=\sum_{k=0}^n\binom\alpha k\binom r{n-k}.
    $$

2.  $$
    {\begin{bmatrix}\alpha+r\\n\end{bmatrix}}=\sum_{k=0}^n{\begin{bmatrix}\alpha+k\\k\end{bmatrix}}{\begin{bmatrix}r-k-1\\n-k\end{bmatrix}}q^{k(r-n)}\\
    q\to1,\ \ \binom{\alpha+r}n=\sum_{k=0}^n\binom{\alpha+k} k\binom {r-k-1}{n-k}.
    $$

> 证明:
>
> 1.  取Durfee矩, $(n-k)\times(\alpha-k)$, 利用Ferrers图证明.
>
>     <div align="center"><img src="https://s2.loli.net/2021/12/17/R4pdsAJgMUcKlaG.png" style="zoom:35%;" /></div>
>
>     - ①: $q^{(\alpha-k)(n-k)}$,
>     - ②: ${\small\begin{bmatrix}r\\n-k\end{bmatrix}}$,
>     - ③: ${\small\begin{bmatrix}\alpha\\k\end{bmatrix}}$,
>
> 2.  同上, 类似可得到.(注意对于③块需要特别考虑, 即取到了最大的Durfee矩之后下面的块会变小)
>
>     <div align="center"><img src="https://s2.loli.net/2021/12/17/6jNsHdPvLO9QTfJ.png" style="zoom:35%;" /></div>
>
>     - ①: $q^{k(r-n)}$,
>     - ②: ${\small\begin{bmatrix}\alpha\\k\end{bmatrix}}$,
>     - ③: ${\small\begin{bmatrix}r-k-1\\n-k\end{bmatrix}}$.

# 第三章 恒等式与展开式

Newton二项式定理

$$
(x+y)^n=\sum_{k=0}^n\binom nk x^ky^{n-k}\iff\frac {(x+y)^n}{n!}=\sum_{k=0}^n\frac {x^k}{k!}\frac {y^{n-k}}{(n-k)!},
$$

Chu-Vandemonde卷积公式

$$
\begin{aligned}
(x+y)_n=\sum_{k=0}^n\binom nk (x)_k(y)_{n-k}
&\iff \frac{(x+y)_n}{n!}=\sum_{k=0}^n\frac{(x)_k}{k!}\cdot\frac{(y)_{n-k}}{(n-k)!}\\
&\iff\binom {x+y}n=\sum_{k=0}^n\binom xk\binom y{n-k}
\end{aligned}
$$

类似的也有:

$$
\begin{aligned}
\lang x+y\rang_n=\sum_{k=0}^n\binom nk \lang x\rang_k\lang y\rang_{n-k}
&\iff \frac{\langle x+y\rangle_n}{n!}=\sum_{k=0}^n\frac{\langle x\rangle_k}{k!}\cdot\frac{\langle y\rangle_{n-k}}{(n-k)!}\\
&\iff
\left\langle \begin{matrix}x+y\\n\end{matrix}\right\rangle=\sum_{k=0}^n\left\langle \begin{matrix}x\\k\end{matrix}\right\rangle\left\langle \begin{matrix}y\\n-k\end{matrix}\right\rangle
\end{aligned}
$$

定理1: (Abel恒等式)

1.  $$
    (x+y)^n=\sum_{k=0}^n\binom nk\frac x{x-kz}(x-kz)^k(y+kz)^{n-k},\\
    \iff\frac{(x+y)^n}{n!}=\sum_{k=0}^n\frac x{x-kz}\frac{(x-kz)^k}{k!}\frac{(y+kz)^{n-k}}{(n-k)!}.
    $$

    令$z=0$即得到二项式定理.

2.  $$
    (x+y)_n=\sum_{k=0}^n\binom nk\frac x{x-kz}(x-kz)_k(y+kz)_{n-k},\\
    \iff\binom{x+y}{n}=\sum_{k=0}^n\frac x{x-kz}\binom{x-kz}{k}\binom{y+kz}{n-k}.
    $$

    令$z=0$, 即得到Chu-Vandemonde卷积公式.

> 证明:(利用展开式证明, 1式求导,2式差分)
>
> 1.  令$a_k(x,z)=x(x-kz)^{k-1}/k!$, ($k\geqslant 1$) 令$a_0:=1$,
>
>     两边对$x$求偏导,得到:
>
>     $$
>     \begin{aligned}
>     \frac{\partial }{\partial x}a_k(x,z)&=\frac1{k!}\big[(x-kz)^{k-1}+(k-1)x(x-kz)^{k-2}\big]\\
>     &=\frac1{(k-1)!}(x-z)(x-kz)^{k-2}=\frac1{(k-1)!}(x-z)\big(x-z-(k-1)z\big)^{k-2}\\
>     &=a_{k-1}(x-z,z)
>     \end{aligned}
>     $$
>
>     再求一次偏导, 得到:
>
>     $$
>     \frac{\partial^2 }{\partial x^2}a_k(x,z)=a_{k-2}(x-2z,z)
>     $$
>
>     以此类推, 得到:
>
>     $$
>     \frac{\partial^i }{\partial x^i}a_k(x,z)=a_{k-i}(x-iz,z),
>     $$
>
>     由$a_k(x,z)$为$k$次多项式, 所以$a_k(x,z)$的$i$次偏导构成了多项式的一组基, 于是
>
>     $$
>     P(x)=\lambda_0a_0+\lambda_1a_1+\lambda_2a_2+\cdots,
>     $$
>
>     其中$\lambda_i$与$x$无关. 关于$x$求$i$次导, 得到:
>
>     $$
>     \begin{aligned}
>     P^{(i)}(x)&=\sum_{k\geq0}\lambda_k\frac{\partial^i}{\partial x^i}a_k(x,z)\\
>     &=\lambda_i+\lambda_{i+1}a_1(x-iz,z)+\cdots
>     \end{aligned}
>     $$
>
>     令$x=iz$, 得到$\lambda_i=P^{(i)}(iz)$, 所以有:
>
>     $$
>     P(x)=\sum_{k\geq0}a_k(x,z)P^{(k)}(kz),
>     $$
>
>     当$z=0$时, 上式为Taylor公式.
>     于是,令$P(x)=(x+y)^n\Rightarrow P^{(k)}(x)=(n)_k(x+y)^{n-k}$,
>
>     $$
>     \begin{aligned}
>     (x+y)^n&=\sum_{k=0}^na_k(x,z)(n)_k(y+kz)^{n-k}\\
>     &=\sum_{k=0}^n\frac x{x-kz}\cdot\frac{(n)_k}{k!}(x-kz)^k(y+kz)^{n-k}\\
>     &=\sum_{k=0}^n\binom nk\frac x{x-kz}(x-kz)^{k}(y+kz)^{n-k}
>     \end{aligned}
>     $$
>
> 2.  令$a_k(x,z)=x(x-kz-1)_{k-1}/k!$, ($k\geqslant1$) $a_0:=1$.
>     由于
>     $$
>     \begin{aligned}
>     \Delta_xa_k(x,z)&=a_k(x+1,z)-a_k(x,z)\\
>     &=\frac1{k!}\left[(x+1)(x-kz)_{k-1}-x(x-kz-1)_{k-1}\right]\\
>     &=\frac{(x-z)(x-kz-1)_{k-2}}{(k-1)!}\\
>     &=\frac{(x-z)(x-z-(k-1)z-1)_{k-2}}{(k-1)!}\\
>     &=a_{k-1}(x-z,z)
>     \end{aligned}
>     $$
>     再进行一次差分, 得到
>     $$
>     \Delta^2_xa_k(x,z)=\Delta_xa_{k-1}(x-z,z)=a_{k-2}(x-2z,z),
>     $$
>     以此类推, 有
>     $$
>     \Delta^i_xa_k(x,z)=a_{k-i}(x-iz,z),
>     $$
>     又因为$a_k(x,z)$为$k$次多项式, 故构成多项式的一组基,
>     $$
>     P(x)=\lambda_0a_0+\lambda_1a_1+\lambda_2a_2+\cdots,
>     $$
>     其中$\lambda_i$与$x$无关. 关于$x$求$i$次差分, 得到:
>     $$
>     \begin{aligned}
>     \Delta^i_xP(x)&=\sum_{k\geq0}\lambda_k\Delta^i_xa_k(x,z)\\
>     &=\lambda_i+\lambda_{i+1}a_1(x-iz,z)+\cdots
>     \end{aligned}
>     $$
>     令$x=iz$, 得到$\lambda_i=\Delta^i_xP(iz)$, 所以有:
>     $$
>     P(x)=\sum_{k\geq0}a_k(x,z)\Delta^k_xP(kz),
>     $$
>     令$P(x)=(x+y)_n$得到$\Delta^k_xP(x)=(n)_k(x+y)_{n-k}$,
>     $$
>     \begin{aligned}
>     (x+y)_n&=\sum_{k=0}^na_k(x,z)(n)_k(y+kz)_{n-k}\\
>     &=\sum_{k=0}^n\frac x{x-kz}\cdot\frac{(n)_k}{k!}(x-kz)_k(y+kz)_{n-k}\\
>     &=\sum_{k=0}^n\binom nk\frac x{x-kz}(x-kz)_{k}(y+kz)_{n-k}
>     \end{aligned}
>     $$

定理2: 对任意的形式级数$f(x)$有

$$
f(x)=\sum_{k\geq0}\frac{x(x-ku)^{k-1}}{k!}f^{(k)}(ku),
$$

当$u=0$, 有$f(x)=\sum\limits_{k\geq0}\dfrac{f^{(k)}(0)}{k!}x^k$, 为Taylor展开式.

> 证明:
> 由Abel恒等式, 令$y=0$得到
>
> $$
> \begin{aligned}
> f(x)&=\sum_{n\geq0}a_nx^n=\sum_{n\geq0}a_n(x+0)^n\\
> &=\sum_{n\geq0}a_n\sum_{k=0}^n\binom nkx(x-ku)^{k-1}(ku)^{n-k} \\
> &=\sum_{k\geq0}\frac{x(x-ku)^{k-1}}{k!}\sum_{n\geq k}(n)_ka_n(ku)^{n-k}\\
> &=\sum_{k\geq0}\frac{x(x-ku)^{k-1}}{k!}f^{(k)}(ku)
> \end{aligned}
> $$

> 类似的, 有
>
> $$
> f(x)=\sum_{k\geq0}\frac{x(x-ku-1)_{k-1}}{k!}\Delta^kf(ku),
> $$
>
> 令$u=0$, 得到
>
> $$
> f(x)=\sum_{k\geq0}\binom xk\Delta^kf(0),
> $$
>
> 取$f(x)=x^n$得到
>
> $$
> \begin{aligned}
> x^n&=\sum_{k\geq0}\binom xk\Delta^k\dot0^n=\sum_{k\geq0}\binom xkk!S(n,k)\\
> &=\sum_{k\geq0}(x)_kS(n,k)
> \end{aligned}
> $$

## Bell 多项式

定义1: 部分Bell多项式$B_{n,k}=B_{n,k}(x_1,x_2,\cdots,x_{n-k+1})$ (指数型)

$$
\Phi(t,u)=\sum_{n,k\geq0}B_{n,k}\frac{t^n}{n!}u^k=\exp\left(u\sum_{m\geq1}x_m\frac{t^m}{m!}\right),
$$

或者

$$
\Phi_k(t)=\sum_{n\geq k}B_{n,k}\frac{t^n}{n!}=\frac1{k!}\left(\sum_{m\geq1}x_m\frac{t^m}{m!}\right)^k.
$$

定义2: 完全Bell多项式$Y_n=Y_n(x_1,x_2,\cdots,x_{n})$

$$
Y_n=\sum_{k=1}^nB_{n,k},\ Y_0=1.
$$

$$
1+\sum_{n\geq1}Y_n(x_1,x_2,\cdots,x_{n})\frac{t^n}{n!}=\exp\left(\sum_{m\geq1}x_m\frac{t^m}{m!}\right).
$$

定理1: 部分Bell多项式为$k$次齐次整系数多项式, 且

$$
B_{n,k}(x_1,x_2,\cdots,x_{n-k+1})=\large\sum_{\huge\stackrel{\huge c_1,c_2,\cdots\geqslant0}{\large\begin{cases}c_1+c_2+\cdots+c_n=k\\
c_1+2c_2+\cdots+nc_n=n\end{cases}}}\frac{n!}{c_1!c_2!\cdots(1!)^{c_1}{(2!)}^{c_2}\cdots}x_1^{c_1}x_2^{c_2}\cdots
$$

共有$p(n,k)$项(方程组有$p(n,k)$个解).

> 证明:
>
> $$
> \begin{aligned}
> \sum_{n,k\geq0}B_{n,k}(x_1,x_2,\cdots,x_{n-k+1})\frac{t^n}{n!}u^k&=\exp\left(u\sum_{m\geq1}x_m\frac{t^m}{m!}\right)\\
> &=\sum_{k\geq0}\frac{u^k}{k!}\left(\sum_{m\geq1}x_m\frac{t^m}{m!}\right)^k\\
> &=\sum_{k\geq0}\frac{u^k}{k!}\left(\sum_{\stackrel{c_1+c_2+\cdots=k}{\small c_i\geq0}}\binom k{c_1,c_2,\cdots}\left(x_1\frac{t^1}{1!}\right)^{c_1}\left(x_2\frac{t^2}{2!}\right)^{c_2}\cdots\right)^k\\
> &=\sum_{c_1,c_2,\cdots\geq0}\frac{u^{c_1+c_2+\cdots}t^{c_1+2c_2+\cdots}}{c_1!c_2!\cdots(1!)^{c_1}(2!)^{c_2}\cdots}x_1^{c_1}x_2^{c_2}\cdots
> \end{aligned}
> $$
>
> 比较两端$\left[\dfrac{t^n}{n!}u^k\right]$, 得到
>
> $$
> B_{n,k}(x_1,x_2,\cdots,x_{n-k+1})=\large\sum_{\stackrel{\huge c_1,c_2,\cdots\geqslant0}{\large\begin{cases}c_1+c_2+\cdots+c_n=k\\
> c_1+2c_2+\cdots+nc_n=n\end{cases}}}\frac{n!}{c_1!c_2!\cdots(1!)^{c_1}{(2!)}^{c_2}\cdots}x_1^{c_1}x_2^{c_2}\cdots
> $$

从上述定理,可以得到:

$$
B_{n,k}(abx_1,ab^2x_2,\cdots)=a^kb^nB_{n,k}(x_1,x_2,\cdots),
$$

$B_{n,k}$的一些简单的值:

$$
\begin{aligned}
B_{0,0}=1,\quad B_{1,1}&=x_1,\quad B_{2,1}=x_2,\quad\cdots,\quad B_{n,1}=x_n,\\
B_{2,2}&=x_1^2,\quad B_{3,2}=3x_1x_2,\quad B_{3,3}=x_1^3,\quad\cdots,\quad B_{n,n}=x_1^n\\
B_{n,0}=0,\ (n>1&),\ B_{n,k}=0,\ (k>n)
\end{aligned}
$$

定理2 $B_{n,k}$满足的递推关系式:($n\geqslant1$)

1.  $$
    B_{n,k}=\sum_{l=k-1}^{n-1}\binom{n-1}{l}x_{n-l}B_{l,k-1},
    $$

2.  $$
    kB_{n,k}=\sum_{l=k-1}^{n-1}\binom nlx_{n-l}B_{l,k-1},
    $$

3.  $$
    \begin{aligned}
    B_{n,k}(x_1,x_2,\cdots)&=\sum_{l=0}^k\binom nkx_1^lB_{n-l,k-1}(0,x_2,x_3,\cdots)\\
    &=\sum_{l=0}^k\frac{n!}{(n-k)!l!}x_1^lB_{n-k,k-l}\left(\frac{x_2}2,\frac{x_3}3,\cdots\right)
    \end{aligned}
    $$

定义3 普通型Bell多项式$\hat B_{n,k}$,

$$
\sum_{n,k\geq0}\hat B_{n,k}t^n\frac{u^k}{k!}=\exp\left(u\sum_{m\geq1}x_m{t^m}\right),
$$

或者

$$
\sum_{n,k\geq0}\hat B_{n,k}t^n=\left(\sum_{m\geq1}x_m{t^m}\right)^k,
$$

定理2: $\hat B_{n,k}$也为$k$次齐次整系数多项式

$$
\hat B_{n,k}(x_1,x_2,\cdots)=\large\sum_{\stackrel{\huge {c_1,c_2,\cdots\geqslant0}}{\large\begin{cases}c_1+c_2+\cdots+c_n=k\\
c_1+2c_2+\cdots+nc_n=n\end{cases}}}\frac{k!}{c_1!c_2!\cdots}x_1^{c_1}x_2^{c_2}\cdots
$$

更一般地, 还有 $\omega_n$型Bell多项式:

$$
\sum_{n,k\geq0}\tilde B_{n,k}\frac{t^n}{\omega_n}=\frac1{\omega_k}\left(\sum_{m\geq1}x_m\frac{t^m}{\omega_m}\right)^k,
$$

特别地,

- $\omega_n=n!$: 指数型Bell多项式;
- $\omega_n=1$: 普通型Bell多项式.

定理1 : $B_{n,k}$的$n$个特殊值:

1.  $B_{n,k}(1,1,\cdots)=S(n,k)$(第二类Stirling数);
2.  $B_{n,k}(1!,2!,3!,\cdots)=\binom {n-1}{k-1}\dfrac{n!}{k!}$(Lah数);
3.  $B_{n,k}(0!,1!,2!,\cdots)=|s(n,k)|=|\bar s(n,k)|$(第一类无符号Stirling数);
4.  $B_{n,k}(1,2,3,\cdots)=\binom {n}{k}k^{n-k}$(幂等数);

> 证明: (通过$B_{n,k}$的生成函数证明)
>
> $$
> \sum_{n,k\geq0}B_{n,k}\frac{t^n}{n!}u^k=\exp\left(u\sum_{m\geq1}x_m\frac{t^m}{m!}\right),
> $$
>
> 1.  取$x_i=1$, 得到
>     $$
>     \sum_{n,k\geq0}B_{n,k}\frac{t^n}{n!}u^k=\exp\left(u(e^t-1)\right)\Rightarrow B_{n,k}(1,1,\cdots)=S(n,k).
>     $$
> 2.  $x_i=i!$, 得到
>     $$
>     \begin{aligned}
>     \sum_{n,k\geq0}B_{n,k}\frac{t^n}{n!}u^k&=\exp\left(\frac{ut}{1-t}\right)\\
>     &=\sum_{k\geq0}\frac{(ut)^k}{k!}(1-t)^{-k}\\
>     &=\sum_{k\geq0}\frac{(ut)^k}{k!}\sum_{l\geq0}\binom{-k}l(-t)^l\\
>     &=\sum_{k\geq0}\frac{(ut)^k}{k!}\sum_{l\geq0}\frac{\langle k\rangle_l}{l!}t^l\\
>     &=\sum_{k,l\geq0}\frac{\langle k\rangle_l}{k!l!}u^kt^{l+k}=\sum_{k,n\geq0}\frac{\langle k\rangle_n}{k!n!}u^kt^{n+k}
>     \end{aligned}
>     $$
>     比较$\left[\dfrac{t^n}{n!}u^k\right]$,
>     $$
>     B_{n,k}(1!,2!,3!,\cdots)=\frac{n!}{k!(n-k)!}\langle k\rangle_{n-k}=\binom {n-1}{k-1}\dfrac{n!}{k!}.
>     $$
> 3.  取$x_i=(i-1)!$,
>     $$
>     \begin{aligned}
>     \sum_{n,k\geq0}B_{n,k}\frac{t^n}{n!}u^k&=\exp\left(-u\ln{(1-t)}\right)\\
>     &=(1-t)^{-u}
>     \end{aligned}
>     $$
>     于是
>     $$
>     B_{n,k}(1!,2!,3!,\cdots)=|s(n,k)|=|\bar s(n,k)|.
>     $$
> 4.  $x_i=i$,
>     $$
>     \begin{aligned}
>     \sum_{n,k\geq0}B_{n,k}\frac{t^n}{n!}u^k&=\exp\left(ute^t\right)=\sum_{k\geq0}\frac{u^kt^k}{k!}e^{kt}\\
>     &=\sum_{k\geq0}\frac{u^kt^k}{k!}\sum_{l\geq0}\frac{k^lt^l}{l!}\\
>     &=\sum_{k,l\geq0}\frac{u^kt^{k+l}k^l}{k!l!}
>     \end{aligned}
>     $$
>     比较$\left[\dfrac{t^n}{n!}u^k\right]$, 取$l=n-k$, 得到
>     $$
>     B_{n,k}(1,2,3,\cdots)=\binom {n}{k}k^{n-k}.
>     $$

### 二项式型多项式序列

记为$\varphi_n(x)$, 通过下面的式子定义:

$$
\varphi_n(x+y)=\sum_{k=0}^n\binom nk\varphi_{k}(x)\varphi_{n-k}(y).
$$

例如:

$$
\varphi_n(x)=x^n,\quad\varphi_n(x)=(x)_n,\quad\varphi_n(x)=\langle x\rangle_n,
$$

- $$
  \circledast \qquad B_n(x)=\sum_{k=0}^nS(n,k)x^k \Rightarrow B_n(x+y)=\sum_{k=0}^n\binom nkB_k(x)B_{n-k}(y)
  $$

  计算生成函数:

  $$
  \sum_{n\geq0}B_{n}(x)\frac{t^n}{n!}=\exp\left(x(e^t-1)\right).
  $$

  其中$B_n(1)=b_n$(Bell数).

- $\circledast\circledast$Abel多项式 $A_n(x,z)=x(x-nz)^{n-1}$.

  $$
  A_n(x+y,z)=\sum_{k=0}^n\binom nkA_k(x,z)A_{n-k}(y,z),
  $$

  $$
  \sum_{n\geq0}A_n(x,z)\frac{t^n}{n!}=\exp{(x\bar f(t))},\qquad\bar f(t)=\sum_{k\geq1}(-kz)^{k-1}\frac{t^k}{k!}.
  $$

定理2 若$\varphi_n(x)$是一个二项式型多项式, 则

1.  $$
    B_{n,k}(\varphi_0(x),2\varphi_1(x),3\varphi_2(x),\cdots)=\binom nk\varphi_{n-k}(kx),
    $$

2.  $$
    B_{n,k}(\varphi_1(x),\varphi_2(x),\varphi_3(x),\cdots)=\frac1{k!}\sum_{j=0}^k(-1)^{k-j}\binom kj\varphi_{n}(jx),
    $$

> 证明:
> 因为$\varphi_n(x)$是一个二项式型多项式,
>
> $$
> \varPsi(x,t)=\sum_{m\geq0}\varphi_m(x)\frac{t^m}{m!}=e^{xf(t)}
> $$
>
> 于是
>
> $$
> \varPsi^k(x,t)=e^{kxf(t)}=\varPsi(kx,t),
> $$
>
> 1.  $$
>     \begin{aligned}
>     \frac1{k!}(t\varPsi(x,t))^k&=\frac1{k!}t^k\sum_{m\geq0}\varphi_m(kx)\frac{t^m}{m!}\\
>     &=\sum_{m\geq0}\varphi_m(kx)\frac{t^{m+k}}{k!m!}\\
>     &=\sum_{n\geq k}\binom nk\varphi_{n-k}(kx)\frac{t^n}{n!}
>     \end{aligned}
>     $$
>
>     另一方面,
>
>     $$
>     \begin{aligned}
>     \frac1{k!}(t\varPsi(x,t))^k&=\frac1{k!}\left(t\sum_{m\geq0}\varphi_m(kx)\frac{t^m}{m!}\right)^k\\
>     &=\frac1{k!}\left(\sum_{m\geq1}m\varphi_{m-1}(kx)\frac{t^m}{m!}\right)^k\\
>     &=\sum_{n\geq k}B_{n,k}\left(\varphi_0(x),2\varphi_1(x),\cdots\right)\frac{t^n}{n!}
>     \end{aligned}
>     $$
>
> 2.  由
>     $$
>     \begin{aligned}
>     \sum_{n\geq k}B_{n,k}(\varphi_1(x),\varphi_2(x),\varphi_3(x),\cdots)\frac{t^n}{n!}&=\frac1{k!}\left(\sum_{m\geq1}\varphi_m(x)\frac{t^m}{m!}\right)^k\\
>     &=\frac1{k!}(\varPsi(x,t)-1)^k\\
>     &=\frac1{k!}\sum_{j=0}^k(-1)^{k-j}\binom kj\varPsi(jx,t)\\
>     &=\frac1{k!}\sum_{j=0}^k(-1)^{k-j}\binom kj\sum_{n\geq0}\varphi_{n}(jx)\frac{t^n}{n!}\\
>     \end{aligned}
>     $$
>     比较两端$\left[\dfrac{t^n}{n!}\right]$, 得到
>     $$
>     B_{n,k}(\varphi_1(x),\varphi_2(x),\varphi_3(x),\cdots)=\frac1{k!}\sum_{j=0}^k(-1)^{k-j}\binom kj\varphi_{n}(jx).
>     $$

特殊的二项式型多项式序列, 代入上述定理验证.

1.  $\varphi_n(x)=x^n$,

    $$
    \begin{aligned}
    B_{n,k}(1,2x,3x^2,\cdots)&=\binom nk(kx)^{n-k}\\
    B_{n,k}(x,x^2,x^3,\cdots)&=\frac1{k!}\sum_{j=0}^k(-1)^{k-j}\binom kj(jx)^n
    \end{aligned}
    $$

    令$x=1$, 代入即得到定理1的①.

2.  $\varphi_n(x)=\langle x\rangle_n$,

    $$
    \begin{aligned}
    B_{n,k}(1,2x,3x(x+1),\cdots)&=\binom nk\langle kx\rangle_{n-k}\\
    B_{n,k}(x,x(x+1),x(x+1)(x+2),\cdots)&=\frac1{k!}\sum_{j=0}^k(-1)^{k-j}\binom kj\langle jx\rangle_n
    \end{aligned}
    $$

    令$x=1$得到定理1的②.

3.  $\varphi_n(x)=\sum\limits_{k=0}^nS(n,k)x^k$, 令$x=1$得到$\varphi_n(1)=b_n$,
    $$
    \begin{aligned}
    B_{n,k}(b_0,2b_1,3b_2,\cdots)&=\binom nk\sum_{j=0}^{n-k}S(n-k,j)k^j\\
    B_{n,k}(b_1,b_2,b_3,\cdots)&=\frac1{k!}\sum_{j=0}^k(-1)^{k-j}\binom kj\sum_{i=0}^nS(n,i)j^i\\
    &=\sum_{i=0}^nS(n,i)\cdot \frac1{k!}\sum_{j=0}^k(-1)^{k-j}\binom kj j^i\\
    &=\sum_{i=0}^nS(n,i)\cdot S(i,k)
    \end{aligned}
    $$

## Faà di Bruno公式

复合函数求导

定理1: (Faà di Bruno公式, 复合函数高阶求导公式)

设$f$和$g$为两个形式$Taylor$级数,

$$
f=\sum_{k\geq0}f_k\frac{u^k}{k!}, \quad g=\sum_{m\geq0}g_m\frac{t^m}{m!},(g_0=0).
$$

令$h$为$f$和$g$复合的形式级数,

$$
h=\sum_{n\geq0}h_n\frac{t^n}{n!}=f\circ g=f(g),
$$

则$h$的系数可由下式给出($B_{n,k}$为部分Bell多项式)

$$
h_0=f_0,\qquad h_n=\sum_{k=1}^nf_kB_{n,k}(g_1,g_2,\cdots,g_{n-k+1}).
$$

> 证明:
>
> 由
>
> $$
> h=\sum_{n\geq0}h_n\frac{t^n}{n!}=f(g)=\sum_{k\geq0}f_k\frac{g^k}{k!},
> $$
>
> 得到$h_n$是$f_k$的线性组合, 即
>
> $$
> h_n=\sum_{k=0}^nA_{n,k}f_k
> $$
>
> ($A_{n,k}$仅依赖于$g_1,g_2,...$, 与$f_k$无关)
>
> 选取特殊的$f_k$, 令
>
> $$
> f(u)=e^{au}=\sum_{k\geq0}a^k\frac{u^k}{k!},\qquad f_k=a^k,
> $$
>
> 得到
>
> $$
> \begin{aligned}
> h&=f{\small\circ}\, g=f(g)=e^{ag}=\exp(a\sum_{m\geq1}g_m\frac{t^m}{m!})\\
> &=\sum_{n,k\geq0}B_{n,k}(g_1,g_2,...)\frac{t^n}{n!}a^k
> \end{aligned}
> $$
>
> 又由
>
> $$
> h=\sum_{n\geq0}h_n\frac{t^n}{n!}=\sum_{n\geq0}\left(\sum_{k=0}^nA_{n,k}f_k\right)\frac{t^n}{n!}=\sum_{n,k\geq0}A_{n,k}\frac{t^n}{n!}a^k
> $$
>
> 比较$\left[\dfrac{t^n}{n!}a^k\right]$, 得到:
>
> $$
> A_{n,k}=B_{n,k}(g_1,g_2,...),
> $$
>
> 又因为$B_{0,0}=1$, 得到$h_0=f_0$, $B_{n,0}=0$,($n>1$) 得到$\sum_{k=1}^nB_{n,k}(g_1,g_2,...)f_k$.

$$
B_{n,k}(x_1,x_2,\cdots,x_{n-k+1})=\large\sum_{\huge\stackrel{\huge c_1,c_2,\cdots\geqslant0}{\large\begin{cases}c_1+c_2+\cdots+c_n=k\\
c_1+2c_2+\cdots+nc_n=n\end{cases}}}\frac{n!}{c_1!c_2!\cdots(1!)^{c_1}{(2!)}^{c_2}\cdots}x_1^{c_1}x_2^{c_2}\cdots
$$

得到:

$$
B_{0,0}=1, B_{n,1}=x_n,B_{n,n}=x_1^n.
$$

定理2:

设$F(y),G(x)$为给定的实函数, 且$G(x)$在$x=a$处具有任意阶导数, $F(y)$在$y=b=G(a)$处也有任意阶导数, 令$H(x)=F(G(x))$,若设

$$
g_m=\left.\frac{\text{d}^mG}{\text{d}x^m}\right|_{x=a}, \qquad f_k=\left.\frac{\text{d}^kF}{\text{d}y^k}\right|_{y=b},\qquad h_n=\left.\frac{\text{d}^nH}{\text{d}x^n}\right|_{x=a},
$$

其中:

$$
g_0=G(a),\qquad f_0=F(b)=F(G(a)),\qquad h_0=H(a)=F(G(a)),
$$

并定义相应的形式级数:

$$
g(t)=\sum_{m\geq1}g_m\frac{t^m}{m!},\quad f(u)=\sum_{k\geq0}f_k\frac{u^k}{k!}, \quad h(t)=\sum_{n\geq0}h_n\frac{t^n}{n!},
$$

则在形式上有$h=f{\small\circ}g$.

定理3: 对函数$F,G,H$, 其中$H=F(G)=F\cdot G$, 则$H$在$x=a$处的$n$阶导数为($n\geqslant1$)

$$
h_n=\left.\frac{\text{d}^nH}{\text{d}x^n}\right|_{x=a}=\sum_{k=1}^nf_kB_{n,k}(g_1,g_2,...,g_{n-k+1}).
$$

# 第四章 组合反演

二项式反演:

$$
\begin{cases}
f_n=\sum\limits_{k=0}^n\binom nkg_k\\
g_n=\sum\limits_{k=0}^n(-1)^{n-k}\binom nkf_k
\end{cases}\iff
\begin{cases}
f_n=\sum\limits_{k=0}^n(-1)^{k}\binom nkg_k\\
g_n=\sum\limits_{k=0}^n(-1)^{k}\binom nkf_k.
\end{cases}
$$

Stirling反演:

$$
\begin{cases}
f_n=\sum\limits_{k=0}^nS(n,k)g_k\\
g_n=\sum\limits_{k=0}^ks(n,k)f_k
\end{cases}
$$

## 经典Möbuis 反演公式

定义:(Möbius函数)

$$
\mu(n)=
\begin{cases}
1,&n=1\\
0,&p^2|n,\quad(p为素数)\\
(-1)^r,&n=p_1p_2\cdots p_r
\end{cases}
$$

定理1:

$$
\sum_{d|n}\mu(d)=\delta_{n,1}=\begin{cases}1,&n=1\\0,&n>1\end{cases}
$$

> $n=12, \quad d=1,2,3,4,6,12$, 于是
>
> $$
> \begin{array}{c|cccccc}
> d&1&2&3&4&6&12\\
> \hline
> \mu(d)&1&-1&-1&0&1&0
> \end{array}
> $$

> 证明:
>
> - $n=1$时, 由$\mu(1)=1$, 显然成立.
> - $n>1$时, 由$n$的素分解,
>   $$
>   n=p_1^{k_1}p_2^{k_2}\cdot p_r^{k_r},\quad k_i\geqslant1,
>   $$
>
> 令$n^*=p_1p_2\cdots p_r$, 则$d|n^*$得到$d|n$, 即$n^*$的因子一定是$n$的因子.
>
> 若$d|n$, 但$d\nmid n^*$, 于是我们得到$\mu(d)=0$,
>
> $$
> \sum_{d|n}\mu(d)=\sum_{d|n^*}\mu(d),
> $$
>
> 由于$n^*$的任一因子$d$必为几个不同素数的乘积, 若$d$为$k$个不同素数的乘积$(k=0,1,2,...,r)$, 该类型的因子共有$r\choose k$个, 此时$\mu(d)=(-1)^k$, 于是
>
> $$
> \sum_{d|n}\mu(d)=\sum_{d|n^*}\mu(d)=\sum_{k=0}^r(-1)^k\binom rk=(1-1)^r=0.
> $$

定理2: 经典的Möbius反演公式

设$f$和$g$定义在整数集上的函数, 则

$$
\begin{cases}
f(n)=\sum\limits_{d|n}g(d)&①\\
g(n)=\sum\limits_{d|n}\mu\left(\dfrac nd\right)f(d)&②
\end{cases}
$$

> 证明:
>
> - ①$\Rightarrow$②
>   若①成立, 则对$n$的任意因子$d$, 有
>   $$
>   f(d)=\sum_{d'|d}g(d'),
>   $$
>   代入②右端, 得到
>   $$
>   \begin{aligned}
>   \sum\limits_{d|n}\mu\left(\frac nd\right)f(d)&=\sum_{d|n}\mu\left(\frac nd\right)\sum_{d'|d}g(d')\\
>   &=\sum_{d'|n}g(d')\sum_{\frac nd\left|\frac n{d'}\right.}\mu\left(\frac nd\right)\\
>   &=\sum_{d'|n}g(d')\sum_{d:\,\frac nd\left|\frac n{d'}\right.}\mu\left(\frac nd\right)\\
>   &=\sum_{d'|n}g(d')\delta_{\frac n{d'},1}=g(n)
>   \end{aligned}
>   $$
> - ②$\Rightarrow$①
>   若②成立, 则
>   $$
>   \begin{aligned}
>   \sum_{d|n}g(d)&=\sum_{d|n}\sum\limits_{d'|d}\mu\left(\dfrac {d}{d'}\right)f(d')\\
>   &=\sum\limits_{d'|n}f(d')\sum_{d:\frac{d}{d'}\left|\frac{n}{d}\right.}\mu\left(\dfrac {d}{d'}\right)\\
>   &=\sum_{d'|n}f(d')\delta_{\frac n{d'},1}=f(n)
>   \end{aligned}
>   $$

例子: 考虑由$r$个字母组成的集合$S$上的$n$元环状字的计数问题. (穿珠子)

> Sol: 对一个环状字$\odot a_1a_2\cdots a_n$, 从任一字母开始展开成线排列, 得到$a_1a_2\cdots a_n$, 将其重复无穷次, 可以生成一个无限序列
>
> $$
> a_1a_2\cdots a_n a_{n+1}a_{n+2}\cdots a_{2n}\cdots
> $$
>
> 其中$a_{n+i}=a_i$, 所以可以推出该序列的周期为$n$(但是不一定为最小正周期), 设最小正周期为$d$, 则必有$d|n$.
>
> > 若$d\nmid n$, 令$n=qd+d'$($1\le d'<d$), 得到
> >
> > $$
> > a_i=a_{n+i}=a_{qd+d'+i}=a_{d'+i},
> > $$
> >
> > 于是$d'$也为周期, 与$d$为最小正周期矛盾.
>
> 于是$n$元环状字必有最小正周期$d$, 且 $d|n$.
>
> 最小正周期为$d$的$n$元环状字记为:
>
> $$
> \odot \underbrace{(a_1a_2\cdots a_d)(a_1a_2\cdots a_d)\cdots(a_1a_2\cdots a_d)}_{n个字母},
> $$
>
> 可以展成如下$d$个不同的线排列:
>
> $$
> d个\begin{cases}
> (a_1a_2\cdots a_d)\cdots(a_1a_2\cdots a_d)\\
> (a_2a_3\cdots a_{1})\cdots(a_2a_3\cdots a_1)\\
> \cdots\\
> (a_da_1\cdots a_{d-1})\cdots(a_da_1\cdots a_{d-1})\\
> \end{cases}
> $$
>
> 令$M(d)$表示最小正周期为$d$的$d$元环状字的个数, 则最小正周期为$d$的$n$元环状字可由其重复$n/d$次得到.
>
> 故最小正周期为$d$的$n$元环状字的个数也为$M(d)$, 而每种这样的环状字可以展成$d$个不同的线排列,
>
> 于是$n$元环状字展成的所有的线排列的个数为$\sum\limits_{d|n}dM(d)$.
>
> 另一方面, $S$上$n$元线状字的个数为$r^n$, 所以:
>
> $$
> \sum_{d|n}dM(d)=r^n,
> $$
>
> 通过Möbius反演公式
>
> $$
> \begin{cases}
> f(n)=\sum\limits_{d|n}g(d)&①\\
> g(n)=\sum\limits_{d|n}\mu\left(\dfrac nd\right)f(d)&②
> \end{cases}
> $$
>
> 令$f(n)=r^n,g(n)=nM(n)$, 得到
>
> $$
> nM(n)=\sum_{d|n}\mu\left(\frac nd\right)r^d,
> $$
>
> $$
> M(n)=\frac1n\sum_{d|n}\mu\left(\frac nd\right)r^d,
> $$
>
> 从而$S$上$n$元环状字的个数$C_r(n)$为
>
> $$
> C_r(n)=\sum_{d|n}M(d)=\sum_{d|n}\frac1d\sum_{d'|d}\mu\left(\frac d{d'}\right)r^{d'}.
> $$

> 例如, $C_2(4)=6$. $C_3(4)=24$.

## Gould-Hsu反演与Carlitz反演

二项式反演的推广

$$
\begin{cases}
f_n=\sum\limits_{k=0}^n(-1)^{k}\binom nkg_k\\
g_n=\sum\limits_{k=0}^n(-1)^{k}\binom nkf_k.
\end{cases}
$$

定理1 (Gould-Hsu反演, 1973)

$\{a_i\},\{b_i\}$为两任意的实数或复数序列, 使得

$$
\phi(x:n)=\prod_{i=0}^{n-1}(a_i+xb_i),\quad (n=1,2,\cdots)
$$

对任意的$x$以及$n$, $\phi(x:n)\ne0$, 规定$\phi(x:0)=1$. 有如下反演关系成立:

$$
\begin{cases}
f(n)=\sum\limits_{k=0}^n(-1)^{k}\binom nk\phi(k:n)g(k)&①\\
g(n)=\sum\limits_{k=0}^n(-1)^{k}\binom nk\dfrac{a_k+kb_k}{\phi(n:k+1)}f(k)&②
\end{cases}
$$

> 特别的, 取$a_i=1,b_i=0\Rightarrow \phi(x:n)=1$, 得到二项式反演.

> 证明:
>
> - ②$\Rightarrow$①
>   将②代入①右端, 得到
>
>   $$
>   \begin{aligned}
>   &\sum\limits_{k=0}^n(-1)^{k}\binom nk\phi(k:n)\sum\limits_{i=0}^k(-1)^{i}\binom ki\dfrac{a_i+ib_i}{\phi(k:i+1)}f(i)\\
>   =&\sum_{i=0}^n\binom ni(a_{i}+ib_i)f(i)\sum_{k=i}^n(-1)^{k+i}\binom {n-i}{k-i}\frac{\phi(k:n)}{\phi(k:i+1)}\\
>   =&\sum_{i=0}^n\binom  ni(a_i+ib_i)f(i)\sum_{j=0}^{n-i}(-1)^j\binom {n-i}j\frac{\phi(i+j:n)}{\phi(i+j:i+1)}\\
>   =&\sum_{i=0}^n\binom  ni(a_i+ib_i)f(i)(-1)^{n-i}\sum_{j=0}^{n-i}(-1)^{(n-i)-j}\binom {n-i}j\frac{\phi(i+j:n)}{\phi(i+j:i+1)}\\
>   \end{aligned}
>   $$
>
>   若能证明:
>
>   $$
>   \sum_{j=0}^{n-i}(-1)^{(n-i)-j}\binom {n-i}j\frac{\phi(i+j:n)}{\phi(i+j:i+1)}=\begin{cases}
>   0,&0\le i<n\\
>   \dfrac1{a_n+nb_n},&i=n.
>   \end{cases}
>   $$
>
>   即得到.
>
>   - 当$i=n$时, 上式为
>     $$
>     \frac{\phi(n:n)}{\phi(n:n+1)}=\frac1{a_n+nb_n},
>     $$
>     成立;
>   - 当$0\le i<n$时, 由$n$次差分公式
>     $$
>     \Delta^n f(x)=\sum_{k=0}^n(-1)^{n-k}\binom nk f(x+k),
>     $$
>     得到:
>     $$
>     \begin{aligned}
>     &\sum_{j=0}^{n-i}(-1)^{(n-i)-j}\binom {n-i}j\frac{\phi(i+j:n)}{\phi(i+j:i+1)}\\
>     =&\Delta^{n-i}\left.\frac{\phi(i+x:n)}{\phi(i+x:i+1)}\right|_{x=0}\\
>     =&\sum_{j=0}^{n-i}(-1)^{(n-i)-j}\binom {n-i}j\left.\frac{\phi(i+x+j:n)}{\phi(i+x+j:i+1)}\right|_{x=0}
>     \end{aligned}
>     $$
>     由$\dfrac{\phi(i+x:n)}{\phi(i+x:i+1)}$为$n-i-1$次多项式, 差分$n-i$次, 得到上式为0.
>
> - ①$\Rightarrow$②:
>   ①代入②右端, 得到
>
>   $$
>   \begin{aligned}
>   &\sum\limits_{k=0}^n(-1)^{k}\binom nk\dfrac{a_k+kb_k}{\phi(n:k+1)}\sum_{i=0}^k(-1)^i\binom ki \phi(i:k)g(i)\\
>   =&\sum_{i=0}^n\binom nig(i)\sum_{k=i}^n(-1)^{k+i}\binom {n-i}{k-i}\frac{a_k+kb_k}{\phi(n:k+1)}\phi(i:k)\\
>   \end{aligned}
>   $$
>
>   若能证明:
>
>   $$
>   \sum_{k=i}^{n}(-1)^{k+i}\binom {n-i}{k-i}\frac{a_k+kb_k}{\phi(n:k+1)}\phi(i:k)=\begin{cases}
>   0,&0\le i<n\\
>   1,&i=n.
>   \end{cases}
>   $$
>
>   即可.
>
>   - $i=n$时, 显然成立.
>   - $0\le i <n$时,
>
>     我们有
>
>     $$
>     \frac{\phi(i:k)}{\phi(n:k+1)}(a_k+kb_k)=\frac{n-k}{n-i}\frac{\phi(i:k+1)}{\phi(n:k+1)}+\frac{k-i}{n-i}\frac{\phi(i:k)}{\phi(n:k)},
>     $$
>
>     > 令
>     >
>     > $$
>     > a_k+kb_k=A(a_k+ib_k)+B(a_k+nb_k),
>     > $$
>     >
>     > 得到:
>     >
>     > $$
>     > \begin{cases}
>     > A+B=1\\
>     > Ai+Bn=k
>     > \end{cases}
>     > \Rightarrow
>     > \begin{cases}
>     > A=\dfrac{n-k}{n-i}\\
>     > B=\dfrac{k-i}{n-i}
>     > \end{cases}
>     > $$
>
>     将其代入
>
>     $$
>     \sum_{k=i}^n(-1)^{k+i}\binom {n-i}{k-i}\frac{a_k+kb_k}{\phi(n:k+1)}\phi(i:k),
>     $$
>
>     得到:
>
>     $$
>     \begin{aligned}
>     &\sum_{k=i}^n(-1)^{k+i}\binom {n-i-1}{k-i}\frac{\phi(i:k+1)}{\phi(n:k+1)}\\
>     &+\sum_{k=i}^n(-1)^{k+i}\binom {n-i-1}{k-i-1}\frac{\phi(i:k)}{\phi(n:k)}\\
>     =&-\sum_{k=i+1}^{n+1}(-1)^{k+i}\binom {n-i-1}{k-i-1}\frac{\phi(i:k)}{\phi(n:k)}\\
>     &+\sum_{k=i}^n(-1)^{k+i}\binom {n-i-1}{k-i-1}\frac{\phi(i:k)}{\phi(n:k)}\\
>     =&(-1)^{n+i}\binom {n-i-1}{k-i-1}\frac{\phi(i:n+1)}{\phi(n:n+1)}\\
>     &+(-1)^{2i}\binom {n-i-1}{-1}\frac{\phi(i:i)}{\phi(n:i)}\\
>     =&0+0=0
>     \end{aligned}
>     $$
>
>     证完.

例子: (Abel恒等式) 在原来的Abel恒等式中, 令$k\to n-k,x\to c-bn,z=-b,y\to a+bn$, 得到

1.  $$
    (a+c)^n=\sum_{k=0}^n\binom nk\frac{c-bn}{c-bk}(a+bk)^k(c-bk)^{n-k},
    $$

2.  $$
    (a+c)_n=\sum_{k=0}^n\binom nk\frac{c-bn}{c-bk}(a+bk)_k(c-bk)_{n-k}.
    $$

> 证明:
> 根据Gould-Hsu反演公式,
>
> $$
> \begin{cases}
> f(n)=\sum\limits_{k=0}^n(-1)^{k}\binom nk\phi(k:n)g(k)&①\\
> g(n)=\sum\limits_{k=0}^n(-1)^{k}\binom nk\dfrac{a_k+kb_k}{\phi(n:k+1)}f(k)&②
> \end{cases}
> $$
>
> 1.  改写为
>
>     $$
>     \underbrace{\frac{(a+c)^n}{c-bn}}_{f(n)}=\sum_{k=0}^n(-1)^k\binom nk\underbrace{(c-bk)^n}_{\phi(k:n)}\underbrace{\frac{(-a-bk)^k}{(c-bk)^{k+1}}}_{g(k)},
>     $$
>
>     其中,$\phi(x:n)=\prod\limits_{i=0}^{n-1}(a_i+xb_i),\quad (n=1,2,\cdots)$.
>
>     令$\phi(x:n)=(c-bx)^n$, 即$a_i=c, b_i=-b$.
>     对偶公式(反演)为:
>
>     $$
>     {\frac{(-a-bn)^n}{(c-bn)^{n+1}}}=\sum_{k=0}^n(-1)^k\binom nk\frac{c-bk}{(c-bn)^{k+1}}{\frac{(a+c)^k}{c-bk}},
>     $$
>
>     由于
>
>     $$
>     \sum_{k=0}^n(-1)^k\binom nkx^k=(1-x)^n,
>     $$
>
>     得到:
>
>     $$
>     \left(\frac{-a-bn}{c-bn}\right)^n=\left(1-\frac{a+c}{c-bn}\right)^n=\sum_{k=0}^n(-1)^k\binom nk\left(\frac{a+c}{c-bn}\right)^k.
>     $$
>
>     该式成立, 则证明1式成立.
>
> 2.  对于第二个式子
>
>     $$
>     (a+c)_n=\sum_{k=0}^n\binom nk\frac{c-bn}{c-bk}(a+bk)_k(c-bk)_{n-k},
>     $$
>
>     可以构造为:
>
>     $$
>     \underbrace{\frac{(a+c)_n}{c-bn}}_{f(n)}=\sum_{k=0}^n(-1)^{k}\binom nk \underbrace{(c-bk+k)_n}_{\phi(k:n)}\underbrace{\frac{(-1)^k(a+bk)_k}{(c-bk+k)_{k+1}}}_{g(k)},
>     $$
>
>     对偶公式:
>
>     $$
>     \frac{(-1)^n(a+bn)_n}{(c-bn+n)_{n+1}}=\sum_{k=0}^n(-1)^k\binom nk\frac{c-bk}{(c-bn+n)_{k+1}}\frac{(a+c)_k}{c-bk},
>     $$
>
>     化简得到:
>
>     $$
>     {(a+bn)_n}=\sum_{k=0}^n(-1)^{n-k}\binom nk{(a+c)_k}{(c-bn+n-k-1)_{n-k}},
>     $$
>
>     即:
>
>     $$
>     {(a+bn)_n}=\sum_{k=0}^n\binom nk{(a+c)_k}{(-c+bn)_{n-k}},
>     $$
>
>     于是成立, 由此得到2式成立.
>
>     ***
>
>     <font color="red">第二种方法</font>
>
>     - 将$(-1)^k$展开后代入, 这时候右端会多出一项$-1$, 为什么?
>     - 猜测可能是求和中放入$(-1)^k$之后当$k=0$时不满足反演关系
>
>     类似进行构造, 如下
>
>     $$
>     \underbrace{\frac{(a+c)_n}{c-bn}}_{f(n)}=\sum_{k=0}^n(-1)^k\binom nk \underbrace{(c-bk+k)_n}_{\phi(k:n)}\underbrace{\frac{(-a-bk+k-1)_k}{(c-bk+k)_{k+1}}}_{g(k)},
>     $$
>
>     其中, $\phi(x:n)=\prod\limits_{i=0}^{n-1}(a_i+xb_i),\quad (n=1,2,\cdots)$.
>
>     > 由于
>     >
>     > $$
>     > \frac{(x)_{n-k}}{x}=\frac{(x+k)_n}{(x+k)_{k+1}}.
>     > $$
>
>     令$\phi(x:n)=(c-bx+x)_n$, 即$a_i=c-i, b_i=1-b$.
>     对偶公式(反演)为:
>
>     $$
>     \frac{(-a-bn+n-1)_n}{(c-bn+n)_{n+1}}=\sum_{k=0}^n(-1)^k\binom nk\frac{c-bk}{(c-bn+n)_{k+1}}\frac{(a+c)_k}{c-bk},
>     $$
>
>     整理得到:
>
>     $$
>     {(-a-bn+n-1)_n}=\sum_{k=0}^n(-1)^k\binom nk{(a+c)_k}{(c-bn+n-k-1)_{n-k}},
>     $$
>
>     由于$(-1)^k(a+c)_k=(-a-c+k-1)_k$, 得到
>
>     $$
>     {(-a-bn+n-1)_n}=\sum_{k=0}^n\binom nk{(-a-c+k-1)_k}{(c-bn+n-k-1)_{n-k}},
>     $$
>
>     利用Chu-Vandemonde卷积公式:
>
>     $$
>     (x+y)_n=\sum_{k=0}^n\binom nk (x)_k(y)_{n-k},
>     $$
>
>     得到
>
>     $$
>     {(-a-bn+n-1)_n}=\sum_{k=0}^n\binom nk{(-a-c+k-1)_k}{(c-bn+n-k-1)_{n-k}},
>     $$
>
>     我们证明了对偶公式, 所以我们证明了2式成立.

定理2 (Carlitz反演)

$\{a_i\},\{b_i\}$为两任意的实数或复数序列, 使得

$$
\phi(x:n)=\prod_{i=0}^{n-1}(a_i+xb_i),\quad (n=1,2,\cdots)
$$

对任意的$x=q^n,\ (n\geqslant0)$以及$n$, $\phi(x:n)\ne0$, 规定$\phi(x:0)=1$. 有如下反演关系成立:

$$
\begin{cases}
f(n)=\sum\limits_{k=0}^n(-1)^{k}\begin{bmatrix} n\\k\end{bmatrix}q^{\binom{n-k}2}\phi(q^k:n)g(k)&①\\
g(n)=\sum\limits_{k=0}^n(-1)^{k}\begin{bmatrix} n\\k\end{bmatrix}\dfrac{a_k+q^kb_k}{\phi(q^n:k+1)}f(k)&②
\end{cases}
$$

> 例子:
>
> $$
> \underbrace{(x:q)_n}_{g(n)}=\sum_{k=0}^n(-1)^k\begin{bmatrix} n\\k\end{bmatrix}\underbrace{q^{\binom k2}x^k}_{f(k)},
> $$
>
> ($\phi(x:n)=1,a_i=1,b_i=0$),
>
> 对偶关系为:
>
> $$
> q^{\binom n2}x^n=\sum_{k=0}^n(-1)^k\begin{bmatrix} n\\k\end{bmatrix}q^{n-k\choose2}(x:q)_k.
> $$

## Lagrange反演公式

- 可以用来求反函数的各阶导数以及证明恒等式.

令$f=\sum\limits_{n\geq1}f_n\dfrac{t^n}{\omega_n}$, 则关于$\omega_n$的Bell多项式$\tilde B_{n,k}(f_1,f_2,\cdots)$定义为

$$
\sum_{n\geq k}\tilde B_{n,k}\frac{t^n}{\omega_n}=\frac1{\omega_k}f^k=\frac1{\omega_k}\left(\sum_{n\geq1}f_n\frac{t^n}{\omega_n}\right)^k.
$$

令$B_{n,k}=\tilde B_{n,k}(f_2,f_2,\cdots)$, 记($B$下三角矩阵)

$$
B=B(f)=\begin{pmatrix}
B_{1,1}&&&&\\
B_{2,1}&B_{2,2}&&\large0&\\
B_{3,1}&B_{3,2}&B_{3,3}&&\\
\vdots&\vdots&\vdots&\ddots
\end{pmatrix},
$$

例如:

- 二项式系数$\binom nk$构成的矩阵, 对应$f=\dfrac t{1-t},\omega_n=1$, 其中$B_{n,k}=\binom{n-1}{k-1}$.
- 第二类Stirling数$S(n,k)$构成的矩阵, 对应$f=e^t-1,\omega_n=n!$.

定理: 给定3个形式级数$f,g,h$, 均具有$f=\sum\limits_{n\ge1}f_n\dfrac{t^n}{\omega_n}$形式, 则$h=f{\small \circ}g$ 等价于矩阵等式$B(h)=B(g)\cdot B(f)$.(矩阵乘法)

> 证明:
>
> 由Bell多项式的生成函数定义
>
> $$
> \begin{aligned}
> \sum_{n\geq k}B_{n,k}(h_1,h_2,\cdots)\frac{t^n}{\omega_n}&=\frac1{\omega_n}h^k=\frac1\omega_k\big(f(g)\big)^k\\
> &=\frac1{\omega_k}\left(\sum_{n\ge1}f_n\frac{g^n}{\omega_n}\right)^k\\
> &=\sum_{l\ge k}B_{l,k}(f_1,f_2,\cdots)\frac{g^l}{\omega_k}\\
> &=\sum_{l\ge k}B_{l,k}(f_1,f_2,\cdots)\sum_{n\ge l}B_{n,l}(g_1,g_2,\cdots)\frac{t^n}{\omega_n}\\
> &=\sum_{n\ge l\ge k}B_{n,l}(g_1,g_2,\cdots)B_{n,l}(f_1,f_2,\cdots)\frac{t^n}{\omega_n}
> \end{aligned}
> $$
>
> 比较两端$\left[\dfrac{t^n}{\omega_n}\right]$, 得到
>
> $$
> B_{n,k}(h_1,h_2,\cdots)=\sum_{l=k}^nB_{n,l}(g_1,g_2,\cdots)B_{l,k}(f_1,f_2,\cdots),
> $$
>
> 即(矩阵相乘, 对应元素之间的关系)
>
> $$
> B(h)=B(g)\cdot B(f).
> $$

---

令$\omega_n=n!$, 仅考虑第一列$(k=1)$, 由$B_{n,1}(x_1,x_2,\cdots)=x_n$, 得到

$$
B_{n,1}(h_1,h_2,\cdots)=\sum_{l=1}^nB_{n,l}(g_1,g_2,\cdots)B_{l,1}(f_1,f_2,\cdots),
$$

即

$$
h_n=\sum_{l=1}^nB_{n,l}(g_1,g_2,\cdots)\,B_{l,1}(f_1,f_2,\cdots),\qquad(\text{Fa}{\acute{\text a}}\ \text{di Bruno公式}).
$$

---

令$f(t)=\sum\limits_{n\ge0}a_n{t^n}\quad(a_0=0,a_1\ne0)$, 即:$f(t)=\sum\limits_{n\ge1}a_n{t^n}$, 对应$\omega_n=1$, 于是$a_n=[t^n]f(t)$, 即$f(t)$中$[t^n]$.

令

$$
\bar f(t)=f^{\langle-1\rangle}(t)=\sum_{n\ge1}a_n^{\langle-1\rangle}t^n,
$$

其中:

$$
f{\small\circ}\bar f(t)=\bar f{\small\circ}f(t)=t.
$$

那么如何求解$a_n^{\langle-1\rangle}$? (利用Lagrange反演公式计算)

**定理1 Lagrange反演公式**

对所有整数$k$, $(1\leqslant k\leqslant n)$, 有

$$
\qquad \qquad B_{n,k}(\bar f)=[t^n](\bar f(t))^k=\frac kn[t^{n-k}]\left(\frac{f(t)}t\right)^{-n}.\qquad(*)
$$

另一种写法

$$
\begin{aligned}
f^k&=\sum_{n}b_{n,k}t^n,\\
\bar f^k&=\sum_{n}a_{n,k}t^n,
\end{aligned}
\quad\Longrightarrow\quad
a_{n,k}=\frac knb_{-k,-n}.
$$

> 证明:
>
> 由
>
> $$
> \bar f\circ f(t)=t\iff B(f)\cdot B(\bar f)=B(t),
> $$
>
> 又由
>
> $$
> \sum_{n\ge k}B_{n,k}(f)t^n=f^k,\quad\sum_{n\ge k}B_{n,k}(\bar f)t^n=\bar f^k,\quad \sum_{n\ge k}B_{n,k}(t)t^n=t^k,
> $$
>
> 得到
>
> $$
> B_{n,k}(f)=[t^n]f^k,\quad B_{n,k}(\bar f)=[t^n]\bar f^k,\quad B_{n,k}(t)=[t^n]t^k=\delta_{n,k},
> $$
>
> 分别对应矩阵形式:
>
> $$
> B_f=\left(B_{n,k}(f)\right)_{n,k},\quad B(\bar f)=(B_{n,k}(\bar f))_{n,k},\quad B(t)=(B_{n,k}(t))_{n,k}=I,
> $$
>
> 要证明$(*)$成立, 只需证明: $[t^n]f^k$构成的矩阵$B(f)$与$(*)$右端构成的矩阵相乘等于$I$.
>
> 记$\Pi_{n,k}$为相乘矩阵的元素, 则
>
> $$
> \Pi_{n,k}=\sum_{l=k}^n\left\{\frac ln[t^{n-l}]\left(\frac{f(t)}t\right)^{-n}\cdot[t^l]f^k\right\},
> $$
>
> 于是只需证$\Pi_{n,k}=\delta_{n,k}$,
>
> > 若
> >
> > $$
> > f(x)=\sum_{n\geq0}a_nx^n, \quad g(x)=\sum_{n\geq0}b_nx^n,\qquad h(x)=f(x)\cdot g(x)=\sum_{n\geq0}c_nx^n,
> > $$
> >
> > 则
> >
> > $$
> > c_n=[x^n]h(x)=\sum_{k=0}^na_kb_{n-k}=\sum_{k=0}^n[x^k]f(x)[x^{n-k}]g(x),
> > $$
> >
> > 上式为卷积公式.
>
> 对$f(x)=\sum\limits_{n\geq0}a_nx^n,$两端关于$x$求导, 得到
>
> $$
> f'(x)=\sum_{n\geq1}na_nx^{n-1},\iff xf'(x)=\sum_{n\ge1}na_nx^n,
> $$
>
> 得到
>
> $$
> na_n=[x^{n-1}]f'(x)=[x^{n}]xf'(x),
> $$
>
> 由
>
> $$
> l[t^l]f^k=[t^l]\left(t\cdot D(f^k)\right)=k[t^l](t\cdot f^{k-1}\cdot f'),
> $$
>
> 得到
>
> $$
> \begin{aligned}
> \Pi_{n,k}&=\frac kn\sum_{l=k}^n\left\{[t^{n-l}]\left(\frac{f(t)}t\right)^{-n}\cdot[t^l](tf^{k-1}f')\right\}\\
> &=\frac kn [t^n]\left\{\left(\frac{f(t)}t\right)^{-n}tf^{k-1}f'\right\}\\
> &=\frac kn [t^n]\left\{t^{n+1}f^{k-1-n}f'\right\}\\
> \end{aligned}
> $$
>
> 当$n=k$时,
>
> $$
> \Pi_{n,n}=[t^n](t^{n+1}f^{-1}f')=[t^{-1}]\frac{f'}f=1,
> $$
>
> > 由于$f(t)=\sum\limits_{n\ge1}a_n{t^n}$, 我们有
>
> $$
> \begin{aligned}
> \frac{f'}f&=(\ln f)'=\left(\ln(a_1t+a_2t^2+\cdots)\right)'\\
> &=\left(\ln t+\ln(a_1+a_2t+\cdots)\right)'\\
> &=\frac1t+\frac{a_2+2a_3t+\cdots}{a_1+a_2t+\cdots}\quad\Longrightarrow [t^{-1}]\frac{f'}f=1.
> \end{aligned}
> $$
>
> 当$n>k$时,
>
> $$
> \begin{aligned}
> \Pi_{n,k}
> &=\frac kn [t^n]\left\{t^{n+1}f^{k-1-n}f'\right\}\\
> &=\frac kn [t^0]\left\{tf^{k-1-n}f'\right\}\\
> &=\frac kn [t^0]\left\{t\cdot D\left(\frac{f^{-n+k}}{-n+k}\right)\right\}\\
> &=\frac kn [t^0]\left\{t\cdot \frac1{k-n}D\left(\frac1{f^{n-k}}\right)\right\}\\
> \end{aligned}
> $$
>
> 这时候$\dfrac1{f^{n-k}}$可以展开为Laurent级数的形式,
> 求导, 不可能出现$\dfrac1t$项, 于是$\Pi_{n,k}=0$, 所以我们证明了Lagrange反演公式.

定理2 Lagrange反演公式的等价形式之一

设$u=\bar f(t)$, 则对任意的形式级数$\Phi$,有

$$
\qquad\Phi(u)=\Phi(0)+\sum_{n\ge1}\frac{t^n}n[t^{n-1}]\left\{\Phi'(t)\left(\frac{f(t)}t\right)^{-n}\right\},\qquad (**)
$$

等价于

$$
n[t^n]\Phi(u)=[t^{n-1}]\left\{\Phi'(t)\left(\frac{f(t)}t\right)^{-n}\right\}.
$$

> 证明:
> 令$\Phi(v)=\sum\limits_{k\ge0}\varphi_kv^k$, 得到
>
> $$
> [t^n]\Phi(\bar f)=\sum_{k\ge0}\varphi_k[t^n]\bar f^k=\sum_{k\ge0}\frac kn \varphi_k[t^{n-k}]\left(\frac{f(t)}t\right)^{-n},
> $$
>
> 即:
>
> $$
> \begin{aligned}
> n[t^n]\Phi(\bar f)&=\sum_{k\ge0}k\varphi_k[t^{n-k}]\left(\frac{f}t\right)^{-n}\\
> &=\sum_{k\ge0}[t^{k-1}]\Phi'\cdot[t^{n-k}]\left(\frac{f}t\right)^{-n}\\
> &=[t^{n-1}]\Phi'(t)\left(\frac{f}t\right)^{-n}
> \end{aligned}
> $$

定理3:(Lagrange反演公式的等价形式之二, 应用于反函数求导)

设$u=\bar f(t)$, 则对任意的形式级数$\varPsi$, 有

$$
\frac{t\varPsi(u)}{uf'(u)}=\sum_{n\geq0}t^n[t^n]\left\{\varPsi(t)\left(\frac{f(t)}t\right)^{-n}\right\},
$$

等价于:

$$
[t^n]\frac{t\varPsi(u)}{uf'(u)}=[t^n]\left\{\varPsi(t)\left(\frac{f(t)}t\right)^{-n}\right\}.
$$

> 证明: 对下式关于$t$求导, 应用$t=f(u)$,以及$\dfrac{\text du}{\text d t}=\dfrac1{f'(u)}$, 得到:
>
> $$
> \qquad\Phi(u)=\Phi(0)+\sum_{n\ge1}\frac{t^n}n[t^{n-1}]\left\{\Phi'(t)\left(\frac{f(t)}t\right)^{-n}\right\},
> $$
>
> 得到:
>
> $$
> \begin{aligned}
> \Phi'(u)\frac{\text du}{\text dt}&=\frac{\Phi'(u)}{f'(u)}=\sum_{n\ge1}t^{n-1}\cdot [t^{n-1}]\left\{\Phi'(t)\left(\frac{f(t)}t\right)^{-n}\right\}\\
> &=\sum_{n\ge0}t^{n}\cdot [t^{n}]\left\{\Phi'(t)\left(\frac{f(t)}t\right)^{-n-1}\right\}\\
> \end{aligned}
> $$
>
> 令$\varPsi(u)=u\dfrac{\Phi'(u)}{f'(u)}=\dfrac{u\Phi'(u)}{t}$, 即$\Phi'(u)=\dfrac{t\varPsi(u)}u$, 代入上式, 即证.

---

例:设$f(t)=te^{-t}$ 计算复合逆$\bar f(t)$的系数, (反函数的系数)

> 解:(利用Lagrange反演公式, 取$k=1$)
>
> $$
> \begin{aligned}
> \ [t^n]\bar f(t)&=\frac1n[t^{n-1}]\left(\frac{f(t)}t\right)^{-n}=\frac1n[t^{n-1}]e^{nt}\\
> &=\frac1n[t^{n-1}]\sum_{l\ge0}\frac{n^l}{l!}t^l=\frac1n\frac{n^{n-1}}{(n-1)!}=\frac{n^{n-1}}{n!},
> \end{aligned}
> $$
>
> 得到
>
> $$
> \bar f(t)=\sum_{n\geq1}\frac{n^{n-1}}{n!}t^n.
> $$

例子: 给定整数$z$, 计算级数

$$
F(t)=\sum_{n\ge0}\binom{nz}nt^n
$$

的封闭形式. (表示)

> 解:
>
> 由于$(1+t)^{nz}=\sum\limits_{k=0}^{nz}\binom{nz}kt^k$, $[t^n](1+t)^{nz}=\binom{nz}nt^n$, 得到
>
> $$
> F(t)=\sum_{n\ge0}t^n\cdot[t^n](1+t)^{nz}
> $$
>
> 利用定理3,
>
> > 设$u=\bar f(t)$, 则对任意的形式级数$\varPsi$, 有
> >
> > $$
> > \frac{t\varPsi(u)}{uf'(u)}=\sum_{n\geq0}t^n[t^n]\left\{\varPsi(t)\left(\frac{f(t)}t\right)^{-n}\right\},
> > $$
>
> 构造函数, 令$\varPsi(t)=1$ , $f(t)=t(1+t)^{-z}$, $u=\bar f(t),\ t=f(u)$,
>
> $$
> F(t)=\sum_{n\ge0}t^n\cdot [t^n](1+t)^{nz}=\frac t{uf'(u)},
> $$
>
> 又由$t=f(u)=u(1+u)^{-z}$, 以及
>
> $$
> f'(u)=(1+u)^{-z}-zu(1+u)^{-z-1}=\frac{1+u-zu}{(1+u)^{z+1}},
> $$
>
> 于是
>
> $$
> F(t)=\frac{t(1+u)^{z+1}}{u+u^2-zu^2}=\frac{u(1+u)^{-z}(1+u)^{z+1}}{u+u^2-zu^2}=\frac{u+1}{1+u-zu}.
> $$

例子: 解方程

$$
y=x+x^py^{q+1},
$$

其中$p,q$为非负整数.

> 解:
>
> 由于$x=y(1-x^py^{q})=f(y)$, 得到$y=\bar f(x)$, 由Lagrange反演公式,
>
> $$
> \begin{aligned}
> \ [x^n]y&=[x^n]\bar f(x)=\frac1n[t^{n-1}]\left(\frac{f(t)}t\right)^{-n}\\
> &=\frac1n[t^{n-1}](1-x^pt^q)^{-n}\\
> &=\frac1n[t^{n-1}]\sum_{k\ge 0}\binom{-n}k(-x^pt^q)^k\\
> &=\frac1n[t^{n-1}]\sum_{k\ge0}\binom{n+k-1}{k}x^{pk}t^{qk}\qquad(let\ n=qk+1)\\
> &=\frac1{qk+1}\binom{qk+k}kx^{pk}
> \end{aligned}
> $$
>
> 于是
>
> $$
> \begin{aligned}
> y&=\sum_{k\ge0}\frac1{qk+1}\binom{qk+k}kx^{pk}x^{qk+1}\\
> &=x\sum_{k\ge0}\frac1{qk+1}\binom{qk+k}kx^{(p+q)k}
> \end{aligned}
> $$

例子: 证明Abel恒等式1(利用定理2)

$$
(x+y)^n=\sum_{k=0}^n\binom nk\frac x{x-kz}(x-kz)^k(y+kz)^{n-k}.
$$

> 定理2: 设$u=\bar f(t)$, 则对任意的形式级数$\Phi$,有
>
> $$
> \qquad\Phi(u)=\Phi(0)+\sum_{n\ge1}\frac{t^n}n[t^{n-1}]\left\{\Phi'(t)\left(\frac{f(t)}t\right)^{-n}\right\}.
> $$

> 证明:
>
> 令$f(t)=te^{zt}$, $\Phi(t)=e^{xt}$, 得到
> {% raw %}
>
> $$
> \begin{aligned}
> e^{xu}
> &=1+\sum_{k\geq1}\frac{t^k}k[t^{k-1}]\left\{x e^{xt}\cdot e^{-kzt}\right\}\\
> &=1+\sum_{k\geq1}\frac{t^k}k[t^{k-1}]x e^{(x-kz)t}\\
> &=1+\sum_{k\ge1}\frac{t^k}k[t^{k-1}]x \sum_{l\ge0}\frac{{(x-kz)^l}}{l!}t^l\\
> &=1+\sum_{k\ge1}x\frac{t^k}k\frac{(x-kz)^{k-1}}{(k-1)!}\\
> &=1+\sum_{k\ge1}\frac x{x-kz}{(x-kz)^{k}}\frac{t^k}{k!}\\
> &=\sum_{k\ge0}\frac x{x-kz}{(x-kz)^{k}}\frac{t^k}{k!}\\
> \end{aligned}
> $$
>
> {% endraw %}
> 即
>
> $$
> e^{xu}=\sum_{k\ge0}\frac x{x-kz}{(x-kz)^{k}}\frac{t^k}{k!},
> $$
>
> 两边同乘以$e^{yu}$, 将$t=f(u)=ue^{zu}$代入上式, 得到
>
> $$
> \begin{aligned}
> e^{(x+y)u}&=\sum_{k\ge0}\frac x{x-kz}{(x-kz)^{k}}\frac{1}{k!}u^ke^{kzu}\cdot e^{yu}\\
> &=\sum_{k\ge0}\frac x{x-kz}{(x-kz)^{k}}\frac{u^k}{k!}e^{(y+kz)u}
> \end{aligned}
> $$
>
> 由此得到
>
> $$
> \begin{aligned}
> \sum_{n\ge0}(x+y)^n\frac{u^n}{n!}&=\sum_{k\ge0}\frac x{x-kz}{(x-kz)^{k}}\frac{u^k}{k!}\sum_{l\ge0}\frac{(y+kz)^l}{l!}u^l
> \end{aligned}
> $$
>
> 比较两端$\left[\dfrac{u^n}{n!}\right]$, 得到
>
> $$
> (x+y)^n=\sum_{k=0}^n\binom nk\frac x{x-kz}(x-kz)^k(y+kz)^{n-k}.
> $$

对于Abel恒等式2,

$$
(x+y)_n=\sum_{k=0}^n\binom nk\frac x{x-kz}(x-kz)_k(y+kz)_{n-k}.
$$

可以类似证明如下.

> 由于最后要取两端$\left[\dfrac{u^n}{n!}\right]$, 所以一定要有
>
> $$
> \sum_{n\ge0}(x+y)_n\frac{u^n}{n!}=\sum_{n\ge0}\binom{x+y}nu^n=(1+u)^{x+y},
> $$
>
> 令$\Phi(t)=(1+t)^{x}$, $f(t)=t(1+t)^z$, $u=\bar f(t)\iff t=f(u)$, 可以得到:
>
> $$
> \begin{aligned}
> \Phi(u)&=(1+u)^x\\
> &=1+\sum_{k\geq1}\frac{t^k}k[t^{k-1}]\left\{x (1+t)^{x-1}\cdot (1+t)^{-kz}\right\}\\
> &=1+\sum_{k\geq1}\frac{t^k}k[t^{k-1}]x (1+t)^{x-1-kz}\\
> &=1+\sum_{k\ge1}\frac{t^k}k[t^{k-1}]x \sum_{l\ge0}\binom{x-kz-1}{l}t^l\\
> &=1+\sum_{k\ge1}x\frac{t^k}k\binom{x-kz-1}{k-1}\\
> &=1+\sum_{k\ge1}\frac x{x-kz}\frac{(x-kz)_{k}t^k}{k!}\\
> &=\sum_{k\ge0}\frac x{x-kz}\frac{(x-kz)_{k}t^k}{k!}
> \end{aligned}
> $$
>
> 即
>
> $$
> (1+u)^x=\sum_{k\ge0}\frac x{x-kz}\frac{(x-kz)_{k}}{k!}t^k,
> $$
>
> 两边同时乘以$(1+u)^y$, 将$t=f(u)=u(1+u)^z$代入, 得到
>
> $$
> \begin{aligned}
> (1+u)^{x+y}&=\sum_{k\ge0}\frac x{x-kz}\frac{(x-kz)_{k}}{k!}u^k(1+u)^{zk+y}\\
> \end{aligned}
> $$
>
> 由此得到
>
> $$
> \sum_{n\ge0}\frac{(x+y)_n}{n!}u^n=\sum_{k\ge0}\frac x{x-kz}\frac{(x-kz)_{k}}{k!}u^k\sum_{l\ge0}\frac{(y+zk)_l}{l!}u^l,
> $$
>
> 比较两端$\left[\dfrac{u^n}{n!}\right]$, 即得到:
>
> $$
> (x+y)_n=\sum_{k=0}^n\binom nk\frac x{x-kz}(x-kz)_k(y+kz)_{n-k}.
> $$

# 第五章 容斥原理

> 可以证明带有交错项的恒等式.

设$S$为一个有限集, $P_i(1\le i\le m)$为$m$个性质,

- $A_i=\{x|x\in S, x具有性质P_i\}$,
- $\bar A_i=\{x|x\in S, x不具有性质P_i\}$.

---

- $\bar A_1\cap\bar A_2\cap\cdots\cap\bar A_m=\{x|x\in S, 且x不具有P_i中任何性质\}$;
- $A_1\cup A_2\cup\cdots\cup A_m=\{x|x\in S, 且x具有全部性质\}$.

**定理(包含排除原理)**

$S$中**不具有任何性质**的元素个数为

$$
\begin{aligned}
|\bar A_1\cap\bar A_2\cap\cdots\cap\bar A_m|=|S|&-\sum_{1\leqslant i\leqslant m}|A_i|+\sum_{1\leqslant i<j\leqslant m}|A_i\cap A_j|\\
&-\sum_{1\leqslant i<j<k\leqslant m}|A_i\cap A_j\cap A_k|+\cdots\\
&+(-1)^m|A_1\cap A_2\cap\cdots\cap A_m|.
\end{aligned}
$$

> 证明:
>
> 要证明定理成立, 只需证明$S$中任意元素在等式两边被计算的次数相等.
>
> 1.  $x$不具有任何性质$(x\notin S)$, 则$1=1-0+0\cdots+(-1)^m0$,成立;
> 2.  $y$具有$t$个性质, $1\le t\le m$, $y\in S$, 则
>     $$
>     0=1-\binom t1+\binom t2-\binom t3+\cdots+(-1)^t\binom tt=(1-1)^t,
>     $$
>     显然成立. 证完.

例1: 设$n$为一正整数, Euler函数$\varphi(n)$表示所有不大于$n$且与$n$互素的正整数的个数, 证明

$$
\varphi(n)=n\left(1-\frac1{p_1}\right)\left(1-\frac1{p_2}\right)\cdots\left(1-\frac1{p_n}\right),
$$

其中, $n=p_1^{s_1}p_2^{s_2}\cdots p_m^{s_m}$.

> 证明:
>
> 设$A_i(1\le i\le m)$为集合$S=\{1,2,...,n\}$中能被$p_i$整除的素数的集合, 则
>
> $$
> |\varphi(n)|=|\bar A_1\cap\bar A_2\cap\cdots\cap\bar A_m|,
> $$
>
> 由容斥原理,
>
> $$
> \begin{aligned}
> \varphi(n)=&|S|-\sum_{1\leqslant i\leqslant m}|A_i|+\sum_{1\leqslant i<j\leqslant m}|A_i\cap A_j|\\
> &+\cdots+(-1)^m|A_1\cap A_2\cap\cdots\cap A_m|\\
> =&n-\left(\sum_{i}\frac{n}{p_i}\right)+\left(\sum_{i<j}\frac{n}{p_ip_j}\right)-\cdots\\
> &+(-1)^m\left(\frac{n}{\prod_i p_i}\right)\\
> =&n\left(1-\frac1{p_1}\right)\left(1-\frac1{p_2}\right)\cdots\left(1-\frac1{p_n}\right)
> \end{aligned}
> $$

例2: 求出1到100中不能被5整除, 也不能被6,8整除的整数 的个数.

> 令$S=\{1,2,...,100\}$, $A=\{n\in S\ |\ 5|n\}$, $B=\{n\in S\ |\ 6|n\}$, $C=\{n\in S\ |\ 8|n\}$,
>
> 于是所求的整数个数为$|\bar A\cap\bar B\cap \bar C|$, 且有$|S|=100$, $|A|=\left[\dfrac{100}5\right]=20$, $|B|=\left[\dfrac{100}6\right]=16$, $|C|=\left[\dfrac{100}8\right]=12$,
>
> $|A\cap B|=\left[\dfrac{100}{30}\right]=3$, $|A\cap C|=\left[\dfrac{100}{40}\right]=2$, $|B\cap C|=\left[\dfrac{100}{24}\right]=4$, $|A\cap B\cap C|=\left[\dfrac{100}{120}\right]=0$.
>
> 由容斥原理,
>
> $$
> \begin{aligned}
> |\bar A\cap\bar B\cap \bar C|
> =&|S|-(|A|+|B|+|C|)+(|A\cap B|\\
> &+|A\cap C|+B\cap C|)-|A\cap B\cap C|\\
> =&100-20-16-12+3+2+4-0\\
> =&61
> \end{aligned}
> $$

例3: 求不定方程

$$
x_1+x_2+x_3=9,\quad 1\le x_1\le3,2\le x_2\le 4,0\le x_3\le5,
$$

的整数解的个数.

> 解: 令$y_1=x_1-1,y_2=x_2-2,y_3=x_3$, 原不定方程可以等价于求解
>
> $$
> y_1+y_2+y_3=6,\quad 0\le y_1\le2,0\le y_2\le 2,0\le y_3\le5,
> $$
>
> 的整数解的个数, 令$S$为方程$y_1+y_2+y_3=6$的非负整数解, 则$|S|=\binom{3+6-1}{6}=\binom86=28$,
>
> 令$P_1$为性质$y_1\ge 3$, $P_2$为性质$y_2\ge3$, $P_3$为性质$y_3\ge6$, $A_i$表示满足性质$P_i$的解构成 的集合$i=1,2,3$,
>
> $$
> |\bar A_1\cap\bar A_2\cap\bar A_3|=28-\binom{3+3-1}3*2-1+1+0*2-0=8.
> $$

例4: (**错排问题**)

集合$\{1,2,...,n\}$的一个错位排列是指集合$\{1,2,...,n\}$的排列$a_1a_2...a_n$使得$a_i\ne i$, 令$D_n$表示集合$\{1,2,...,n\}$中错排个数, 则

$$
D_n=n!\left(1-\frac1{1!}+\frac1{2!}-\frac1{3!}+\cdots+(-1)^{n}\frac1{n!}\right).
$$

> 方法一, 利用容斥原理
>
> 设$S$为$\{1,2,...n\}$中所有排列构成的集合, 则$|S|=n!$, 令$P_i$为性质$a_i=i$, $A_i$表示$\{1,2,...n\}$中具有性质$P_i$的集合,
> 于是
>
> $$
> D_n=|\bar A_1\cap\bar A_2\cap\cdots\cap\bar A_n|,
> $$
>
> 于是
>
> $$
> \begin{aligned}
> D_n&=n!-\binom n1\cdot(n-1)!+\binom n2(n-2)!-\cdots+(-1)^n\binom nn(n-n)!\\
> &=n!-\frac{n!}{1!}+\frac{n!}{2!}-\cdots+(-1)^n\frac{n!}{n!}\\
> &=n!\left(1-\frac1{1!}+\frac1{2!}-\frac1{3!}+\cdots+(-1)^{n}\frac1{n!}\right)\\
> &=n!\left(\sum_{k=0}^n\frac{(-1)^k}{k!}\right)
> \end{aligned}
> $$
>
> 并且有:
>
> $$
> \frac{D_n}{n!}=\sum_{k=0}^n\frac{(-1)^k}{k!}\to e^{-1}\quad(n\to\infty),
> $$
>
> 也即$D_n$是与$\dfrac{n!}e$最接近的整数.

> 方法二, 组合解释
>
> 由$\{1,2,...,n\}$的所有排列的个数为$n!$个, $(a_1a_2...a_n)$,
>
> 分类, 恰有$k$个元素对应$a_i=i$, 其含错排, 共有$\binom nkD_{n-k}$, 于是
>
> $$
> n!=\sum_{k=0}^n\binom nkD_{n-k}=\sum_{k=0}^n\binom nkD_k,
> $$
>
> 由二项式反演,
>
> $$
> \begin{cases}
> f_n=\sum\limits_{k=0}^n\binom nkg_k\\
> g_n=\sum\limits_{k=0}^n(-1)^{n-k}\binom nkf_k
> \end{cases}
> $$
>
> 则
>
> $$
> \begin{aligned}
> D_n&=\sum_{k=0}^n(-1)^{n-k}\binom nkk!=\sum_{k=0}^n(-1)^{k}\binom nk(n-k)!\\
> &=n!\sum_{k=0}^n\frac{(-1)^{k}}{k!}
> \end{aligned}
> $$

---

> 或者取指数生成函数(不采用二项式反演):
>
> $$
>   D(x)=\sum_{n\ge0}D_n\frac{x^n}{n!},
> $$
>
> 两端取生成函数:
>
> $$
> n!=\sum_{k=0}^n\binom nkD_{n-k}=\sum_{k=0}^n\binom nkD_k,
> $$
>
> 得到
>
> $$
> \begin{aligned}
> \frac1{1-x}&=\sum_{n\ge0}\sum_{k=0}^n\binom nkD_{n-k}\frac{x^n}{n!}\\
> &=\sum_{k\ge0}\frac{x^k}{k!}\sum_{n\ge k}\frac{x^{n-k}}{(n-k)!} D_{n-k}\\
> &=\sum_{k\ge0}\frac{x^k}{k!}\cdot\sum_{m\ge0}\frac{x^m}{m!}D_{m}=D(x)\cdot e^x
> \end{aligned}
> $$
>
> 于是
>
> $$
> \sum_{n\ge0}D_n\frac{x^n}{n!}=D(x)=\frac1{1-x}e^{-x}=\sum_{n\ge0}n!\cdot\frac{x^n}{n!}\sum_{n\ge0}(-1)^n\frac{x^n}{n!}
> $$
>
> 两端取$\left[\dfrac{x^n}{n!}\right]$, 得到(并利用指数生成函数的乘法公式)
>
> $$
> D_n=\sum_{k=0}^n\binom nk{(-1)^k}{(n-k)!}=n!\sum_{k=0}^n\frac{(-1)^k}{k!}.
> $$

例5: 证明: (由于含有交错项, 可以使用容斥原理)

$$
k!S(n,k)=\sum_{i=0}^k(-1)^{k-i}\binom kii^n=\sum_{i=0}^k(-1)^i\binom ki(k-i)^n.
$$

> 证明: 由于$S(n,k)$表示$n$个不同的球放入$k$个相同的盒子, 且每个盒子中**至少一个球**的不同放法数
>
> $$
> S(n,k):\quad N=N_1\cup N_2\cup\cdots\cup N_k,\quad N_i\ne\varnothing, N_i\cap N_j=\varnothing.
> $$
>
> 若盒子加以区分, 则有$k!S(n,k)$种.
>
> 令$P_i$表示性质: 第$i$个盒子是空的, $A_i$表示满足性质$P_i$的所有放法的集合, (即第$i$个盒子为空的), 于是每个盒子至少一个球对应于$\bar A_1\cap \bar A_2\cap \cdots\cap \bar A_k$, 即$|\bar A_1\cap \bar A_2\cap \cdots\cap \bar A_k|=k!S(n,k)$, 并且
>
> $$
> \begin{aligned}
> k!S(n,k)&=|\bar A_1\cap \bar A_2\cap \cdots\cap \bar A_k|\\
> &=k^n-\binom k1(k-1)^n+\binom k2(k-2)^n-\cdots+(-1)^k\binom nk(k-k)^n\\
> &=\sum_{i=0}^k(-1)^i\binom ki(k-i)^n=\sum_{i=0}^k(-1)^{k-i}\binom kii^n
> \end{aligned}
> $$

例6: (**Eratosthenes筛法**, 用于计算$π (n)$, 即不超过$n$的素数的个数)

设$P_1(=2),P_2(=3), P_3(=5),\cdots$, 为递增的素数序列, 对实数$x>0$, 定义$π (x)$表示不超过$n$的素数的个数($π (5)=3,π (10)=4$), 可以通过容斥原理计算$π (n)$.

> 设$A_i$是$P_i$的倍数构成的集合, 其倍数属于$N=\{2,3,\cdots,n\}$, 若$q\in \bar A_1\cap\bar A_2\cap \cdots\cap\bar A_k$, ($k=π (\sqrt n)$)
>
> > 例如, 取$n=30$, $k=π (\sqrt {30})=π (5)=3$, $q\in \bar A_1\cap\bar A_2\cap\bar A_3$,
>
> 则$q$的素数因子大于$P_k$, 于是$q$为一个$\sqrt n<q\le n$的素数, 即
>
> $$
> |\bar A_1\cap \bar A_2\cap \cdots\cap \bar A_k|=\pi(n)-\pi(\sqrt n),
> $$
>
> 由容斥原理, 得到
>
> $$
> \begin{aligned}
> &\pi (n)-\pi(\sqrt n)\\
> &=n-1-\sum_{i=1}^k\left[{n\over P_i}\right]+\sum_{1\le i<j\le k}\left[{n\over P_iP_j}\right]-\cdots+(-1)^k\left[{n\over P_1P_2\cdots P_k}\right].
> \end{aligned}
> $$

于是, 根据上述公式, 可以计算$π (100)$,

$\pi (10)=4$, 则$P_i=2,3,5,7$, 于是

$$
\begin{aligned}
\pi(100)-\pi(10)=&(100-1)-\sum_{P_i=2,3,5,7}\left[{100\over P_i}\right]+\sum_{P_i,P_j=2,3,5,7}\left[{100\over P_iP_j}\right]\\
&-\sum_{P_i,P_j,P_k=2,3,5,7}\left[{100\over P_iP_jP_k}\right]+\left[{100\over 2\cdot3\cdot5\cdot7}\right]\\
=&99-(50+33+20+14)+(16+10+7+6+4+2)\\
&-(3+2+1+0)+0=21
\end{aligned}
$$

所以$π (100)=25$.

例7: 夫妇问题(Lucas于1891提出, 解决)

$n$对夫妇围桌而坐, 男女相间, 夫妇不相邻, 问有多少种可能的安排方式.

> 解: 假定女士已经就坐, 共有$2\cdot n!$种方式, (相当于线排列, 也可以坐男士的位置, 所以乘以2), 标号$1,2,...,n$,
>
> 女士左侧的空座位标号$1,2,...,n$, 则$n$位男士坐空座位等价于一个置换$\sigma$, 且$\sigma$满足
>
> - $\sigma(i)\ne i$, $\sigma\ne i+1$, $i\notin[n-1]$,
> - $\sigma(n)\ne n$, $\sigma(n)\ne1$,
>
> 设$\mu(n)$表示满足上述条件的置换的个数, 则所求的安排方式$\mu^*(n)=2\cdot n!\mu(n)$. 接下来计算$\mu(n)$,
>
> 令$A_{2i-1}=\{\sigma|\sigma(i)=i\}$, $i\in [n]=\{1,2,...,n\}$, $A_{2i}=\{\sigma|\sigma(i=i+1\}$, $i\in [n-1]$.
>
> $A_{2n}=\{\sigma|\sigma(n)=1\}$, (共有$2n$个集合)则
>
> $$
> \mu(n)=|\bar A_1\cap \bar A_2\cap \cdots\cap \bar A_{2n}|,
> $$
>
> 若$n_1,n_2,...,n_k$中含有圈集$(1,2,...,2n,1)$中相邻的两个元素, 则$|\bar A_{n_1}\cap \bar A_{n_2}\cap \cdots\cap \bar A_{n_k}|=0$, (不能同时存在于两个集合中).
>
> 若不含相邻的元素, 则$n_1,n_2,...,n_k$的选取方式为$g_1(2n,k)$, 其中
>
> $$
> g_l(n,k)=\frac n{n-kl}\binom{n-kl}k, \qquad(圈上的l间隔排列),
> $$
>
> (指定了$k$个($n_1,n_2,...,n_k$), 则$n-k$个随便取)
>
> 另一方面, 满足$\bar A_{n_1}\cap \bar A_{n_2}\cap \cdots\cap \bar A_{n_k}$的置换个数为$(n-k)!$, 故有
>
> $$
> \begin{aligned}
> \mu(n)&=\sum_{k=0}^{2n}(-1)^kg_1(2n,k)(n-k)!\quad(超过n的均为0)\\
> &=\sum_{k=0}^n(-1)^k\frac{2n}{2n-k}\binom{2n-k}{k}(n-k)!
> \end{aligned}
> $$
>
> (由Touchard 1953给出. )
>
> 所以最后所求为
>
> $$
> \mu^*(n)=2\cdot n!\mu(n)=2\cdot n!\sum_{k=0}^n(-1)^k\frac{2n}{2n-k}\binom{2n-k}{k}(n-k)!.
> $$
