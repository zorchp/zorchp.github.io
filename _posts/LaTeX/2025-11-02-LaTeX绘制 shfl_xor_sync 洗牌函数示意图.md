---
categories: [LaTeX]
tags: LaTeX TikZ
---

## 写在前面

学习 CUDA 的束内洗牌函数`__shfl_*_sync` 比较感兴趣这里面的示意图怎么绘制的. 下面是用 tikz 的一些方式



## __shfl_sync

```latex
\documentclass[tikz,border=10pt,convert={density=500,outext=.jpg}]{standalone}
\usepackage{tikz}
\usetikzlibrary{positioning, arrows.meta}

\begin{document}
\begin{tikzpicture}[
  thread/.style={rectangle,draw,minimum width=0.5cm,minimum height=0.5cm,
                 fill=blue!15,align=center,font=\tiny}
]
\def\height{-3}
\def\WrapWidth{32}
\def\subWrapWidth{16}

\node[anchor=west] at (-2,0) { Before: };
\foreach \i in {0,...,31} {
  \node[thread] (t\i) at (0.5*\i,0) {\i};
}

\node[anchor=west] at (-2,\height) { After: };
\foreach \i in {0,...,31} {
  \node[thread,fill=green!15] (s\i) at (0.5*\i,\height) {\i};
}

\pgfmathtruncatemacro{\NumGroups}{\WrapWidth/\subWrapWidth-1}

\foreach \i in {0,...,\NumGroups} {
  \pgfmathtruncatemacro{\firstElem}{\subWrapWidth * \i}
  \pgfmathtruncatemacro{\jStart}{\i * \subWrapWidth}
  \pgfmathtruncatemacro{\jEnd}{(\i+1)*\subWrapWidth-1}

  \foreach \j in {\jStart,...,\jEnd} {
    \draw[-{Stealth[length=2mm]},gray!60] (t\firstElem.south) -- (s\j.north);
  }
}


\end{tikzpicture}
\end{document}
```

> 语法真恶心, 没法直接在 for 里面求值



<figure>
    <img src="https://cdn.jsdelivr.net/gh/zorchp/blogimage@main//shfl.sync.jpg" alt="">
    <center><figcaption>__shfl_sync 执行情况  width=16</figcaption></center>
</figure>



## __shfl_xor_sync

这里绘制lane_mask 为 1,2,4,8,16 的示意图, 用一个模板来实现(有点元编程的意思)

```latex
\documentclass[tikz,border=10pt]{standalone}
\usepackage{tikz}
\usetikzlibrary{positioning, arrows.meta}

\begin{document}
\begin{tikzpicture}[
  thread/.style={rectangle,draw,minimum width=0.5cm,minimum height=0.5cm,
                 fill=blue!15,align=center,font=\tiny}
]
\def\height{-3}
\def\laneMask{LANE_MASK}  % 这里用字符串替换方式由外部控制

\node[anchor=west] at (-2,0) { Before: };
\foreach \i in {0,...,31} {
  \node[thread] (t\i) at (0.5*\i,0) {\i};
}

\node[anchor=west] at (-2,\height) { After: };
\foreach \i in {0,...,31} {
  \node[thread,fill=green!15] (s\i) at (0.5*\i,\height) {\i};
}
%% pgf 里面没有 xor 函数, 简单模拟一个
\pgfmathdeclarefunction{bitxor}{2}{%
  \pgfmathparse{int(mod(#1,#2*2) < #2 ? #1+#2 : #1-#2)}%
}

\foreach \i in {0,...,31} {
  \pgfmathtruncatemacro{\j}{bitxor(\i,\laneMask)} 
  \draw[-{Stealth[length=2mm]},gray!60] (t\i.south) -- (s\j.north);
}

\end{tikzpicture}
\end{document}
```

```bash
for i in {0..4}; do
	lane_mask=$((2 ** $i))
	new_file=shfl.$lane_mask.tex
	cat shfl.xor.tmpl.tex | sed "s#LANE_MASK#${lane_mask}#" >$new_file
	xelatex $new_file
done
## clear aux file 
latexmk -c
```

然后就有下面的一些示意图了

<figure>
    <img src="https://cdn.jsdelivr.net/gh/zorchp/blogimage@main//image-20251102113509105.png" alt="">
    <center><figcaption>__shfl_xor_sync 执行情况  laneMask=2</figcaption></center>
</figure>

<figure>
    <img src="https://cdn.jsdelivr.net/gh/zorchp/blogimage@main//image-20251103142825734.png" alt="">
    <center><figcaption>__shfl_xor_sync 执行情况  laneMask=16</figcaption></center>
</figure>


