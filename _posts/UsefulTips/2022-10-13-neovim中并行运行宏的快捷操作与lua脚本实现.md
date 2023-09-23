---
categories: [Tips]
tags: Vim Lua
---

# 写在前面

最近入坑vim了, 主要是想整一个纯键盘操作的编辑器, 用sublime当然方便, 但是还是需要鼠标点点点, 不知不觉中降低了效率. (但是过渡阶段还是得先用sublime的) 

之前一个朋友就推荐过neovim, 并且帮我配置了在Mac的iTerm上的nvim环境, 当时没学过lua感觉配置起来bug很多, 为了稳定还是一直用的sublime, 直到后来我发现sublime的编译以及运行一些代码的时候需要很繁琐的配置, 格式化代码的插件也几乎都是8~9年前的了, 用起来很不方便, 于是还是想转入vim阵营((我是一直追求轻量级的)). 

>   最近也一直在研究lua的一些基本语法, 不得不说lua脚本的语法真的是一股清流, 我以前就以为Python就是相当简洁明了的脚本了, 后来学了lua发现类与面向对象竟然还能这么写(通过Table), 真是大开眼界, 并且由于有了Python基础, 学起来lua配置nvim还是得心应手的, 只是对于一些vim时代留下来的API调用还是不熟悉, 这时候就要靠`:h`了.

除了lua基本语法的学习, 我还看了一本书, 名为《practical Vim》, 中译版在微信读书中有, 叫做《vim使用技巧》, 如果你熟悉了一些基本的vim技巧, 那么看起这本书肯定是爱不释手. 

话不多说, 下面来看一个具体的配置应用, 就是关于上面介绍的书中说的一个技巧(其实书中并未提及相关实现, 但是作者提供的vimrc文件[^1]中有说明), 是关于并行执行自定义宏的, 有了这个快捷操作, 你的vim用起来一定更加如虎添翼.

>   环境:
>
>   1.   MacOS arm64(M1)
>   2.   NeoVim 0.8.0 (with brew) config: ref[^2]
>   3.   ...

# 并行执行宏

下面先来看看自定义宏, 假设有下面这些文本:

```c
one
two
three
four
```

现在要给每一行前面加上一个行序号, 变成下面这样:

```c
1) one
2) two
3) three
4) four
```

那么应该如何用宏解决这个问题呢?

1.   光标跳转到第一行(`gg`)
2.   进入命令模式设置变量`i=1`(`:let i=1`)
3.   按下`qa`开始录制宏(保存在寄存器`a`中)
4.   按下`I`将光标移到行首进行编辑
5.   按下`<C-R>`(Ctrl+R)然后输入`=i`并回车(此时会显示出变量`i`的值`1`)
6.   输入`) `(右半括号以及空格)
7.   按下`ESC`(或者`<C-[>`), 然后按下`q`停止录制宏

上面一套流程之后, 文本变成了下面这样:

```c
1) one
two
three
four
```

接下来开始执行宏, 即:

1.   按下`j`, 光标跳到下一行(第二行)
2.   按下`V`(shift+V)进入行可视模式
3.   按下`G`(shift+G)选中直到最后一行的文本
4.   输入`:`, 此时命令提示框会变成`:'<,'>`
5.   后面接着输入`normal @a`, 并回车

这样就用并行模式执行了宏, 可以看到文本变成了如下:

```c
1) one
2) two
3) three
4) four
```

这就是我们想要的结果~

为便于使用, 下面我录制了一个GIF动画: 

![aa](https://s2.loli.net/2022/10/13/gT3R2AqHSBp5ltW.gif)

# 快速执行宏操作

下面我参考了[^1]的vimrc配置, 其中有一个快捷操作, 就是说不用输入`:'<,'>normal @a`, 直接选中指定行之后输入`@a`即可完成宏的操作. 下面是我为了在`nvim`上使用vim的函数配置, 加上了`vim.cmd`.

```lua
vim.cmd([[
    xnoremap @ :<C-u>call ExecuteMacroOverVisualRange()<CR>
    function! ExecuteMacroOverVisualRange()
    echo "@".getcmdline()
    execute ":'<,'>normal @".nr2char(getchar())
	endfunction
]])
```



但是这不是一个很`lua`的写法, 下面我用lua以及nvim提供的API函数重写了上面的快捷配置函数:

```lua
{% raw %}
function vim.fn.ExecuteMacroOverVisualRange()
    vim.api.nvim_echo({{"@" .. vim.fn.getcmdline()}},false,{})
    vim.fn.execute(":'<,'>normal @" .. vim.fn.nr2char(vim.fn.getchar()))
end

["x|@"] = map_cu("lua vim.fn.ExecuteMacroOverVisualRange()"),
{% endraw %}
```

参考[^2].

```lua
-- 这里我参考了大佬的配置, 直接定义函数即可, 注意这里用的函数原型为
function rhs_options:map_cu(cmd_string)
    -- <C-u> to eliminate the automatically inserted range in visual mode
    self.cmd = (":<C-u>%s<CR>"):format(cmd_string)
    return self
end
```



可以达到一样的效果.

# Ref

[^1]:[dotfiles/vimrc at master · nelstrom/dotfiles (github.com)](https://github.com/nelstrom/dotfiles/blob/master/vimrc#L172);
[^2]:[ayamir/nvimdots: A well configured and structured Neovim. (github.com)](https://github.com/ayamir/nvimdots);
