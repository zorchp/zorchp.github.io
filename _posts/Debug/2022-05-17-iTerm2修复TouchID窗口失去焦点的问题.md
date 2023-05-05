---
categories: [Debug]
tags: MacOS Debug Tips
---

# 发现问题



最近一直困扰我的一个问题, 就是在`iTerm2`中每次采用`sudo`命令时候都不能直接用指纹输入, 而是要点击一下指纹那个窗口才能输入指纹, 之前我已经设置了`sudo`命令采用指纹输入了. 

这个问题不是很好描述, 在Google中也搜索了好久, 今天突然想起来, 觉得这是一个必须解决的问题, 当然也是碰巧了(遇到问题就要多尝试). 

一个一模一样的问题就是[^1], 这里面也有我用蹩脚的英文做的回答..

# 解决

上面说我这算是凑巧了, 因为尝试过各种的配置, 都没有丝毫的效果, 但是在系统自带的终端中就没有这个问题, 后来我灵机一动, 想着看看选项卡种有没有什么可以用的选项, 终于找到了`iTerm2`->`Secure Keyboard Entry`这个选项! 这也是问题的根源所在, 我以前不知道为什么直接手残点了这个选项, 但是却并没注意到这个选项带来的效果...(就是禁止别的应用读取输入)反而影响了TouchID的快捷操作了..

>   When this is enabled, the operating system will prevent other programs running on your computer from being able to see what you are typing. If you're concerned that untrusted programs might try to steal your passwords, you can turn this on, but it may disable global hotkeys in other programs.[^2]
>
>   启用此操作后，操作系统将阻止计算机上运行的其他程序能够查看您的键入内容。如果您担心不受信任的程序可能会尝试窃取密码，则可以打开此密码，但是它可能会禁用其他程序中的全局热键。



# 后记

不懂的选项别乱用, 设置过的任何东西都要有个印象, 或者认真查配置文档.

[^1]:[Touch ID window for sudo doesn't get focus when opened from iTerm - Ask Different (stackexchange.com)](https://apple.stackexchange.com/questions/440516/touch-id-window-for-sudo-doesnt-get-focus-when-opened-from-iterm);
[^2]: [Menu Items - Documentation - iTerm2 - Mac OS Terminal Replacement](https://iterm2.com/documentation/2.1/documentation-menu-items.html);