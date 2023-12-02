[toc]

## 再看Galois基本定理

设$E$ 是域$F$的一个伽罗瓦扩张, $G=\text{Gal}(E/F)$. 记$\mathcal{H}=\{H\,|\,H\leqslant G\}$, $\mathcal{L}=\{L\,|\,F\subseteq L\subseteq E\}$是$F$与$E$的中间域所成集合, 那么存在如下两个映射:
$$
\text{Gal}:\,\mathcal{L}\to\mathcal{H},\,L\mapsto\text{Gal}(E/L),\quad\text{Inv}:\,\mathcal{H}\to\mathcal{L},\,H\mapsto\text{Inv}(H),
$$
满足如下的五条性质:

1.   $\text{Gal}$和$\text{Inv}$互为逆映射, 因而均为**一一映射**;

2.   上述一一映射存在反包含关系: 子群$H_1,H_2$分别与中间域$L_1,\,L_2$**一一对应**时,有
     $$
     H_1\supseteq H_2\iff L_1\subseteq L_2;
     $$
     (下面的描述均满足子群与中间域的一一对应)

3.   $[E:L]=|H|,\,[L:F]=[G:H]$; 

4.   $\forall\sigma\in G$, $H $的正规子群$\sigma H\sigma^{-1}$与$L$的共轭子域$\sigma(L)$一一对应, 即
     $$
     E^{\sigma H\sigma^{-1}}=\sigma(E^H);\text{Gal}(E/\sigma M)=\sigma\text{Gal}(E/M)\sigma^{-1}.
     $$

5.   $H\unlhd G$当且仅当$L$是$F$的伽罗瓦扩张, 这时有$\text{Gal}(L/F)\simeq G/H$. 

>   使用范畴的语言描述
>

>   证明(4):
>   $$
>   X=\{H|H<G\}\leftrightarrow Y=\{M|F\subset M\subset E\},
>   $$
>   tu
>
>   
>
>   $M=E^H=\text{Inv(H)}=\{x|h(x)=x,\forall h\in H\}$, $M'=\{x\in E|\sigma H\sigma^{-1}(x)=x,\forall h\in H\}$, 
>   $$
>   \sigma:E\to E\\
>   \qquad \ \  x\mapsto \sigma(s)
>   $$
>   其中$\sigma\in G_f$, 而$\forall y\in\sigma(M),y=\sigma(x),x\in M$, 有
>   $$
>   \sigma h\sigma^{-1}(y)=\sigma h\sigma^{-1}\sigma(x)=\sigma(x)=y
>   $$
>   所以可以得到$y\in M'$, 即$\sigma(M)\subseteq M'$, 反之, 直接令上述映射关系中的$H$换成$\sigma^{-1}H\sigma$, 可知$M'=\sigma(M)$.
>
>   >   或者由$|\sigma H\sigma^{-1}|=|H|$, 于是$|M'|=|\sigma (M)|$, 得到$M'=\sigma(M)$(通过子空间, 线性空间). 



>   证明(5):
>   $$
>   \forall \sigma\in G,\sigma H\sigma^{-1}=H\Rightarrow\sigma(M)=M,
>   $$
>   可以定义映射:
>   $$
>   \text{Aut}(E/F)=G\longrightarrow\text{Aut}(M/F)\\
>   \quad\qquad \sigma\longmapsto\sigma\big|_M
>   $$
>
>   1.   $\sigma$为群同态(映射复合, 运算保持)
>
>   2.   $\sigma$为满同态, $\sigma|_M$中每一个都能找到原象, (扩域链, 能找到一个域同构), 于是
>        $$
>        \text{Aut}(M/F)\cong G/\text{Ker}\rho=G/H.
>        $$





于是$f(x)=0$在$F$上求解, 可以得到
$$
\begin{cases}
F:&g(x)=0 \to M\\
M:&h(x)=0\to E
\end{cases}
$$
解方程的过程就可以化成先解一个域扩张维数($[M:F]$)小一些的方程, 再解其他方程($[E:M]$).
$$
[E:F]=[E:M][M:F]
$$

### 利用Galois基本定理解方程的核心思路

1.   先化简方程, 求解$G_f$;
2.   求$G_f$的正规子群;
3.   找正规子群对应的中间域;
4.   写出两个子域对应的多项式.

>   这里只考虑$f$为不可约的情况, 即对应了群论中的单群, 对于可约的情况直接因式分解即可. 



## 两个技巧

### 1. $G$在$\Omega$上传递$\iff f$在$F[x]$不可约

>   证明:
>
>   -   "$\Leftarrow$": $E=F(\alpha_1,\cdots,\alpha_n)$, $f$不可约, 所以$f$是$\alpha_i$的零化多项式, 也是极小多项式, 所以在$\alpha_i$和$\Omega$之间存在一一对应(是一条轨道), 所以传递(也称为可迁,`transitive`).
>   -   "$\Rightarrow$": 传递, 则$\alpha_i$可以映到$\Omega$中的任意一个元素, 而$\Omega$中的任何一个元素$\{\alpha_1,\cdots,\alpha_m\}$就是$\alpha_i$极小多项式的零点, 所以不可约.





### 2. $G\lesssim \mathcal{A}_n\iff\delta\in F$

其中
$$
\delta=\prod_{n\geqslant i>j\geqslant1}(\alpha_i-\alpha_j)
$$
> 证明:
    -   $g$是$G$中的奇置换, (有一个奇置换, 则逆序数多1, 符号相反)
        $$
        g(\delta)=-\delta=\prod\limits_{n\geqslant i>j\geqslant1}\big(g(\alpha_i)-g(\alpha_j)\big)\ne\delta\Rightarrow \delta\notin F.
        $$

  -   
  
  -   $g$为$G$中偶置换, 则$g(\delta)=\delta,\Rightarrow\delta\in F$. 







## 例子: 二次方程求解

$$
f(x)=x^2+ax+b=(x-\alpha_1)(x-\alpha_2),\quad E=F(\alpha_1,\alpha_2),
$$

于是$G_f\lesssim\mathcal{S}_2$, 于是$G_f=\{\text{id}\},or\ \mathcal{S}_2$, 其中, $G_f$为单位群时$f$可约, $G_f$为对称群时$f$不可约, 根据上述技巧, 令
$$
\delta=\alpha_2-\alpha_1,
$$
这时不容易得到$\delta$是否在$F$(基域)中, 于是
$$
\Delta=\delta^2=(\alpha_2-\alpha_1)^2=(\alpha_1+\alpha_2)^2-4\alpha_1\alpha_2=a^2-4b,
$$
由此我们只需判断$\sqrt\Delta\stackrel{?}{\in} F$, (是否能开根号), 如果$\sqrt\Delta\in F$, 则$f$可约. 





## 例子: 三次方程求解

对于三次方程:
$$
f(x)=x^3+ax^2+bx+c,
$$
$G_f\lesssim\mathcal{S}_3$子群, 有$\{\text{id}\},\langle(12)\rangle,\langle(13)\rangle,\langle(23)\rangle,\mathcal{A}_3,\mathcal{S}_3$六种情况, 这里只讨论$f$不可约的情况(若可约, 则直接因式分解即可求解).

而判断$f$不可约, 只需验证$\sqrt\Delta$是否在$F$中, 仅在$\mathcal{A}_3,\mathcal{S}_3$中$G_f$才是传递的. 

对于计算$\Delta$, 有下面的定理.(需要用到对称多项式的知识)



**定理**: 对于一般的首一**三次多项式方程**, 
$$
x^3+a_1x^2+a_2x+a_3=0,
$$
其判别式为:
$$
D=\Delta=a_1^2a_2^2-4a_1^3a_3-4a_2^3+18a_1a_2a_3-27a_3^2.
$$

>   证明: (核心思想: 待定系数法, 思路可见北大第四版高等代数)
>
>   由于下面的$6$次多项式
>   $$
>   D=\Delta=(\alpha_1-\alpha_2)^2(\alpha_1-\alpha_3)^2(\alpha_2-\alpha_3)^2
>   $$
>   是关于方程的根:$\alpha_1, \alpha_2,\alpha_3$的对称多项式, 所以一定可以写成*初等对称多项式*的多项式形式(对称多项式基本定理), 即
>   $$
>   \Delta=P(\sigma_1,\sigma_2,\sigma_3)=\sum_{i,j,k}c_I\alpha_1^i\alpha_2^j\alpha_3^k
>   $$
>   
>
>   其中: (根与系数的关系, Vieta定理)
>   $$
>   \begin{cases}
>   \sigma_1=\alpha_1+\alpha_2+\alpha_3\\
>   \sigma_2=\alpha_1\alpha_2+\alpha_1\alpha_3+\alpha_2\alpha_3\\
>   \sigma_3=\alpha_1\alpha_2\alpha_3
>   \end{cases}
>   $$
>   
>
>   于是$i+j+k=6,i\geqslant j\geqslant k$. 采用**降次**的字典序(针对**非齐次**多项式)进行排列, $(i,j,k)$, 
>
>   最高项为$(4,2,0)$, 于是排列$(4,2,0),(4,1,1),(3,3),(3,2,1),(2,2,2)$分别对应下面各项:
>   $$
>   \begin{aligned}
>   \Delta&=\sum\alpha_1^4\alpha_2^2+A\sum\alpha_1^4\alpha_2\alpha_3+B\sum\alpha_1^3\alpha_2^3+C\sum\alpha_1^3\alpha_2^2\alpha_3+D\sum\alpha_1^2\alpha_2^2\alpha_3^2
>   \end{aligned}
>   $$
>   
>   
>而
>   $$
>   \sigma_1^i\sigma_2^j\sigma_3^k=\sum\alpha_1^{i+j+k}\alpha_2^{j+k}\alpha_3^k+\cdots
>   $$
>   其最高项与$(4,2,0)$一一对应, 于是
>   $$
>   \begin{cases}
>   i+j+k=4\\
>   j+k=2\\
>   k=0\\
>   \end{cases}\Longrightarrow\begin{cases}
>   i=2\\
>   j=2\\
>   k=0\\
>   \end{cases}
>   $$
>   于是找到了$\sigma_1^2\sigma_2^2$展开式的首项$\alpha_1^4\alpha_2^2$,
>   
>即
>   $$
>   \Delta-\sigma_1^2\sigma_2^2=A'\sum\alpha_1^4\alpha_2\alpha_3+\cdots
>   $$
>   同理$\sigma_1^3\sigma_3=\sum \alpha_1^4\alpha_2\alpha_3+\cdots$ 
>   
>得到
>   $$
>   \Delta-\sigma_1^2\sigma_2^2-A'\sigma_1^3\sigma_3=B'\sum\alpha_1^3\alpha_2^3+\cdots
>   $$
>   这样一直做下去, 就得到:
>   $$
>   \Delta-\sigma_1^2\sigma_2^2-c_1\sigma_1^3\sigma_3-c_2\sigma_2^3-c_3\sigma_1\sigma_2\sigma_3-c_4\sigma_3^2=0
>   $$
>   即
>   $$
>   \Delta=\sigma_1^2\sigma_2^2+c_1\sigma_1^3\sigma_3+c_2\sigma_2^3+c_3\sigma_1\sigma_2\sigma_3+c_4\sigma_3^2,
>   $$
>   而且$c_1,c_2,c_3,c_4\in K$. 
>   
>此时令$\alpha_i=1,i=1,2,3$, 得到:
>   $$
>   \begin{cases}
>   \sigma_1=\alpha_1+\alpha_2+\alpha_3=3\\
>   \sigma_2=\alpha_1\alpha_2+\alpha_1\alpha_3+\alpha_2\alpha_3=3\\
>   \sigma_3=\alpha_1\alpha_2\alpha_3=1
>   \end{cases}
>   $$
>   于是
>   $$
>   0=81+27c_1+27c_2+9c_3+c_4,
>   $$
>   再取适当的$\alpha_i$,例如$\alpha_1=\alpha_2=1,\alpha_3=-2$, 得到$\sigma_1=0,\sigma_2=-3,\sigma_3=-2$,
>   $$
>   0=-27c_2+4c_4,
>   $$
>   取$\alpha_1=1,\alpha_2=-1,\alpha_3=0$, 得到$\sigma_1=0,\sigma_2=-1,\sigma_3=0$, 
>   $$
>   4=-c_2
>   $$
>   再取$\alpha_1=1,\alpha_2=1,\alpha_3=-1$, 得$\sigma_1=1,\sigma_2=-1,\sigma_3=-1$,
>   $$
>   1-c_1+c_2-c_3+c_4=0
>   $$
>   联立上面四个式子, 计算可得:
>   $$
>   c_1=-4,c_2=-4,c_3=18,c_4=-27,
>   $$
>   即:
>   $$
>   \Delta=\sigma_1^2\sigma_2^2-4\sigma_1^3\sigma_3-4\sigma_2^3+18\sigma_1\sigma_2\sigma_3-27\sigma_3^2.
>   $$
>   或者
>   $$
>   D=\Delta=a_1^2a_2^2-4a_2^3-4a_1^3a_3-27a_3^2+18a_1a_2a_3.
>   $$

#### 核心思想

1.   找到对称多项式各项的降次字典序排列;
2.   根据排列分别计算其对应的展开式首项(通过逐项求差的方法);
3.   利用待定系数法分别选择适当的根值联立方程组求解各系数.



例1 解三次方程
$$
f(x)=x^3-3x-1\in\mathbb{Q}[x].
$$

>   1.   $f(x)$在$\mathbb{Q}$上不可约, 即$G_f=\begin{cases}\mathcal{A}_3\\ \mathcal{S}_3\end{cases}$, 
>   2.   $\Delta=-4\cdot(-27)-27\cdot(-1)=81>0$, 于是$\delta=\pm9\in\mathbb{Q}$, 于是$G_f\cong \mathcal{A}_3$, 





例2 解三次方程
$$
f(x)=x^3+3x+1\in\mathbb{Q}[x].
$$

>   1.   $f(x)$在$\mathbb{Q}$上不可约, 即$G_f=\begin{cases}\mathcal{A}_3\\ \mathcal{S}_3\end{cases}$.
>   2.   $\Delta=-4\cdot27-27\cdot1=-135<0$, 于是$\delta=\sqrt{-135}\notin\mathbb{Q}$, 于是$G_f\cong \mathcal{S}_3$.





## 四次方程

设下述四次方程的四个根为$\alpha_1,\alpha_2,\alpha_3,\alpha_4$, 
$$
f(x)=x^4+a_3x^3+a_2x^2+a_1x+a_0,
$$

则有:
$$
\qquad f(x)=x^4+a_3x^3+a_2x^2+a_1x+a_0=(x-\alpha_1)(x-\alpha_2)(x-\alpha_3)(x-\alpha_4)\in\mathbb{F}[x],\qquad\qquad(*)
$$


构造扩域链
$$
\begin{aligned}
F\subset M\subset E(\alpha_1,\alpha_2,\alpha_3,\alpha_4)\\
\text{判断}\mathcal{S}_4\gtrsim G_f?\hspace{6em}
\end{aligned}
$$

不妨设$f$在$\mathbb{F}[x]$上不可约,  $\mathcal{S}_4$的子群在$\{1,2,3,4\}$上传递(可迁), 于是$G_f$有且仅有如下五种情况:(需要讨论$\mathcal{S}_4$的子群的构成情况)
$$
G_f=\mathcal{S}_4,\mathcal{A}_4,K_4,\langle(1234)\rangle,\langle(1234)K_4\rangle,\quad (\text{阶数分别为:}24,12,4,4,8).
$$

>   讨论:
>
>   根据Lagrange定理, $\mathcal{S}_4$的子群只有如下几种阶数:$1,2,3,4,6,8,12,24$, 传递子群(可迁子群)的阶数只能是$4,8,12,24$, 于是上述几种子群满足条件.





其中$M_2=\{x\in E\,|\,h(x)=x,\ \forall h\in K_4\}$, $K_4=\{(1),(12)(34),(13)(24),(14)(23)\}$, 
$$
\delta=\prod_{4\geqslant i>j\geqslant1}(\alpha_i-\alpha_j),
$$
$H<G$, 如何构造$\alpha$?

>   $\alpha\in E^H\iff \forall h\in H,h(\alpha)=\alpha$. 
>
>   任选$x\in E,W=\{x,h_1(x),...,h_{n-1}(x)\}$为$H$作用在$x$的一条轨道, 
>
>   $\sum\limits_{x\in W}x,\prod\limits_{x\in W}w$都是$E^H$上的元素, 此时$H=K_4$.

例如, 

-   取$x=\alpha_1,W=\{\alpha_1,\alpha_2,\alpha_3,\alpha_4\}$, $\sum_i\alpha_i$和$\prod_i\alpha_i$都在$F$中, 不成立.

-   取$x=\alpha_1\alpha_2,W=\{\alpha_1\alpha_2,\alpha_3\alpha_4\}$, 于是令
    $$
    \begin{aligned}
    \beta_1&=\alpha_1\alpha_2+\alpha_3\alpha_4\in E^H=M_2\\
    \beta_2&=(124)(\beta_1)=\alpha_1\alpha_3+\alpha_2\alpha_4\in E^H=M_2\\
    \beta_3&=(123)(\beta_2)=\alpha_1\alpha_4+\alpha_2\alpha_3\in E^H=M_2\\
    \end{aligned}
    $$

显然其中$\beta_i\ne\beta_j(\forall i\ne j)$, 因为$\beta_1-\beta_2=(\alpha_2-\alpha_4)(\alpha_1-\alpha_3)\ne 0$, (假设不可约, 且没有重根)

所以$\beta_1$的稳定子群(8阶子群,Sylow-2群)为  $\mathcal{S}_4$的一条轨道
$$
g(x)=(x-\beta_1)(x-\beta_2)(x-\beta_3)=x^3-\sum_{i}\beta_ix^2+\sum_{i\ne j}\beta_i\beta_jx-\prod_i\beta_i,
$$
于是: 

1.   $g(x)\in F[x]$; 
2.   $K_4$对应的域$M_2$就是$F(\beta_1,\beta_2,\beta_3)$, 即$F$关于$g$的分裂域.



>   于是解四次方程就等价于找中间域, 这一步骤对应于找Galois群的正规子群链(可解群链).

下面我们寻找如何计算三次预解式. 

-   至于为什么这样构造三次预解式, 是因为从原来的四次方程的根进行一定构造之后得到的$\beta_i$, 形成的三次方程$g(x)$和原来的四次方程具有相同的判别式. 

### 三次预解式(resolvent)

对于如下的四次方程:
$$
f(x)= x^4+a_3x^3+a_2x^2+a_1x+a_0,
$$
其三次预解式为:
$$
g(x)=X^3-a_2x^2+(a_1a_3-4a_0)x-a_0a_3^2+4a_0a_2-a_1^2.
$$

>   证明:
>
>   对下面的四次方程, 
>   $$
>   \qquad f(x)=x^4+a_3x^3+a_2x^2+a_1x+a_0=(x-\alpha_1)(x-\alpha_2)(x-\alpha_3)(x-\alpha_4)\in\mathbb{F}[x],\qquad\qquad(*)
>   $$
>   
>
>   由四次方程系数表达式(Vieta定理), 我们有:
>   $$
>   \begin{cases}
>   a_3=-\sum\limits_i\alpha_i\\
>   a_2=\sum\limits_{i\ne j}\alpha_i\alpha_j\\
>   a_1=-\sum\limits_{i\ne j,j\ne k,k\ne i}\alpha_i\alpha_j\alpha_k\\
>   a_0=\prod\limits_i\alpha_i
>   \end{cases}
>   $$
>   我们要计算下述三次预解式的三个系数, 
>   $$
>   g(x)=(x-\beta_1)(x-\beta_2)(x-\beta_3)=x^3-\sum_{i}\beta_ix^2+\sum_{i\ne j}\beta_i\beta_jx-\prod_i\beta_i,
>   $$
>   即计算:
>   $$
>   -\sum_{i}\beta_i,\ \sum_{i\ne j}\beta_i\beta_j, -\prod_i\beta_i,
>   $$
>   由上面的讨论, 我们有
>   $$
>   \begin{cases}
>   \beta_1=\alpha_1\alpha_2+\alpha_3\alpha_4\\
>   \beta_2=\alpha_1\alpha_4+\alpha_2\alpha_3\\
>   \beta_3=\alpha_1\alpha_3+\alpha_2\alpha_4\\
>   \end{cases}
>   $$
>
>   $$
>   \begin{cases}
>   \beta_1+\beta_2=(\alpha_1+\alpha_3)(\alpha_2+\alpha_4)\\
>   \beta_1+\beta_3=(\alpha_1+\alpha_4)(\alpha_2+\alpha_3)\\
>   \beta_2+\beta_3=(\alpha_1+\alpha_2)(\alpha_3+\alpha_4)
>   \end{cases}
>   $$
>
>   利用上述6个式子, 可以得到:
>
>   >   (这里部分内容使用了CAS, 即计算机代数系统, `Mathematica`的`SymmetricReduction`函数, 用于对称多项式的约化)
>
>   1.   **第一组式子左右两端分别相加**, 即可得到
>        $$
>        -\sum_{i}\beta_i=-\sum\limits_{i\ne j}\alpha_i\alpha_j=-a_2,
>        $$
>
>   2.   **第二组前两个式子**两端分别相乘得到
>        $$
>        \beta_1^2+\sum_{i\ne j}\beta_i\beta_j=(\alpha_1+\alpha_3)(\alpha_2+\alpha_4)(\alpha_1+\alpha_4)(\alpha_2+\alpha_3)
>        $$
>        于是我们得到:
>        $$
>        \begin{aligned}
>        \sum_{i\ne j}\beta_i\beta_j&=(\alpha_1+\alpha_3)(\alpha_2+\alpha_4)(\alpha_1+\alpha_4)(\alpha_2+\alpha_3)-\beta_1^2\\
>        &=(\alpha_1+\alpha_3)(\alpha_2+\alpha_4)(\alpha_1+\alpha_4)(\alpha_2+\alpha_3)-(\alpha_1\alpha_2+\alpha_3\alpha_4)^2\\
>        &=(\alpha_1 + \alpha_2 + \alpha_3 + \alpha_4) (\alpha_1 \alpha_2 \alpha_3 + \alpha_1 \alpha_2 \alpha_4 + \alpha_1 \alpha_3 \alpha_4 + \alpha_2 \alpha_3 \alpha_4) - 4 \alpha_1 \alpha_2 \alpha_3 \alpha_4 \\
>        &=\left(\sum_{i}\alpha_i\right)\left(\sum\limits_{i\ne j,j\ne k,k\ne i}\alpha_i\alpha_j\alpha_k\right)-4\prod_i\alpha_i=a_1a_3-4a_0
>        \end{aligned}
>        $$
>
>   3.   直接代入, 可以得到:
>        $$
>        \begin{aligned}
>        \prod_i\beta_i=&(\alpha_1\alpha_2+\alpha_3\alpha_4)(\alpha_1\alpha_3+\alpha_2\alpha_4)(\alpha_1\alpha_4+\alpha_2\alpha_3)\\
>        =&\alpha_1 \alpha_2 \alpha_3 \alpha_4 (\alpha_1 + \alpha_2 + \alpha_3 + \alpha_4)^2 \\
>        &-4 \alpha_1 \alpha_2 \alpha_3 \alpha_4 (\alpha_1 \alpha_2 + \alpha_1 \alpha_3 + \alpha_2 \alpha_3 + \alpha_1 \alpha_4 + \alpha_2 \alpha_4 + \alpha_3 \alpha_4) \\
>         &+ (\alpha_1 \alpha_2 \alpha_3 + \alpha_1 \alpha_2 \alpha_4+\alpha_1 \alpha_3 \alpha_4 + \alpha_2 \alpha_3 \alpha_4)^2\\
>        =&\prod_i\alpha_i\left(\sum_i\alpha_i\right)^2-4\left(\prod_i\alpha_i\right)\left(\sum_{i\ne j}\alpha_i\alpha_j\right)\\
>        &+\left(\sum\limits_{i\ne j,j\ne k,k\ne i}\alpha_i\alpha_j\alpha_k\right)^2\\
>        =&a_0a_3^2-4a_0a_2+a_1^2
>        \end{aligned}
>        $$
>        于是
>        $$
>        -\prod_i\beta_i=-(a_0a_3^2-4a_0a_2+a_1^2)=-a_0a_3^2+4a_0a_2-a_1^2.
>        $$
>
>   证毕.





### 四次方程的一般解法

1.   利用上述公式代入四次方程系数计算**三次预解式**;
2.   根据三次预解式的根来计算若干**二次方程**, 即得到四次方程的根.










## 参考

1.   高等代数北大版第四版. 
2.   代数学基础下(张英伯, 王恺顺).
3.   *Fields and Galois Theory* J.S. Milne.

