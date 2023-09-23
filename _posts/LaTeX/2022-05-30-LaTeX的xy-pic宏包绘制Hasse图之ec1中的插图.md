---
categories: [LaTeX]
tags: LaTeX xy-pic
---



最近抽时间绘制了一下下面这个图[^1]:

<img src="https://s2.loli.net/2022/05/30/t61XYCSNQfG3gKW.png"/>

这是我绘制的图: (有点丑, 但是这不重要了)

![截屏2022-05-31 00.01.19](https://s2.loli.net/2022/05/31/ix1BKDvOPWo8tnc.png)

部分代码如下:

```latex
{% raw  %}
\documentclass[border=3pt]{standalone}
% \input xypic
\usepackage[all,pdf]{xy}
\newcommand{\B}{{\dir{*}}}
\begin{document}
    \begin{xy}\drop[*1]\xybox{
            (0,0)="A" *{\B}*\cir{},
            (5,8.66)="B" *{\B}*\cir{},
            (10,0)="C" *{\B}*\cir{},
            (20,0)="D" *{\B}*\cir{},
            {"A";"B":"C";"B",x} ="I" *{},
            "I";"A"**{}  **@{-},
            "I";"C"**{}  **@{-}}
        \end{xy}
\end{document}
{% endraw  %}
```



```latex
{% raw  %}
\documentclass[border=3pt]{standalone}
% \input xypic
\usepackage[all,pdf]{xy}
\newcommand{\B}{{\dir{*}}}
\newcommand{\C}{\circ}
\def\al{\ar@{-}}
\def\xyy{\xymatrix@1}

\begin{document}
    \xyy{*=0{\B}\al[d]\al[dr]&*=0{\B}\al[d]\\*=0{\B}&*=0{\B}}
\end{document}
{% endraw  %}
```

其他代码我放在[latexstudio](https://www.latexstudio.net/index/details/index/ids/2691)了. 

费了不少功夫, 之后再抽空讲解一下代码吧. 主要就是参考了xypic-guide和xypic-refer[^2][^3].

[^1]: [Enumerative Combinatorics: Volume 1 (Cambridge Studies in Advanced Mathematics, Series Number 49): Stanley, Richard P.: 9781107602625: Amazon.com: Books](https://www.amazon.com/Enumerative-Combinatorics-Cambridge-Advanced-Mathematics/dp/1107602629);
[^2]:[XY-pic Reference Manual - TeXDochttp://texdoc.net › doc › generic › xypic › xyrefer](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwib9r3QzIf4AhVutlYBHR95BBoQFnoECAcQAQ&url=http%3A%2F%2Ftexdoc.net%2Ftexmf-dist%2Fdoc%2Fgeneric%2Fxypic%2Fxyrefer.pdf&usg=AOvVaw3WI0d708nftp7XfsXusFd1);
[^3]:[XY-pic User's Guide - TeXDochttps://texdoc.org › serve › xyguide.pdf](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj5scLyzIf4AhXum1YBHZBTDwoQFnoECAUQAQ&url=https%3A%2F%2Ftexdoc.org%2Fserve%2Fxyguide.pdf%2F0&usg=AOvVaw0iLS2DBDcMUkQzkN26piZj);