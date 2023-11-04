---
categories: [Tips]
tags: MacOS
---



一直想写一下这个问题, 因为每次 nvim 卡死之后执行 `pkill -9 nvim` , 就会出现这个问题, 并且网上并没有解决方案...



>   环境:
>
>   MacOS 13.4
>
>   iterm 3.4.20
>
>   
>
>   bash/zsh 均测试出现问题
>
>   程序: 
>
>   nvim/ ssh 等异常退出之后会导致模式改变, Ctrl+ <> 回显而不是执行. 





>   其他信息:
>
>   [Iterm2 Ctrl-C Not Working](https://groups.google.com/g/iterm2-discuss/c/-7OLeFUHvlA);
>
>   [启用 `CSI u` 模式时移动空格会向终端发出 `;2u` (#9770) · 西雅图 · George Nachman / iterm2 · GitLab](https://gitlab.com/gnachman/iterm2/-/issues/9770);
>
>   [TUI: Enable/disable modifyOtherKeys automatically · Issue #15352 · neovim/neovim](https://github.com/neovim/neovim/issues/15352);



猜测, nvim 的异常退出导致某些变量未能重置, 从而改变了 iterm 的键位 report 行为 

事实就是如此. 

CSI u mode 会导致这个问题. 



但是没办法这样