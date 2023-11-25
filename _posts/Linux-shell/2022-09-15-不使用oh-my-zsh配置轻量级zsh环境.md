---
categories: [Linux-Shell]
tags: Shell Tips
---

# 写在前面

之前一直在用一款名为oh-my-zsh的插件, 在我的MacOS上, 配置起来主题以及各种插件都比较方便, 但是, 最近在archlinux上面, 我用了omz之后, 速度下降了很多(archlinux虚拟机,还是采用架构虚拟化的方式,在arm上模拟出x86_64), 于是我就想着卸载omz然后直接安装代码补全和高亮插件, 这里参考了一篇国外开发者的博客[^1], 主要用到的插件是:

-   [zdharma-continuum/fast-syntax-highlighting: Feature-rich syntax highlighting for ZSH](https://github.com/zdharma-continuum/fast-syntax-highlighting);
-   [zsh-users/zsh-autosuggestions: Fish-like autosuggestions for zsh (github.com)](https://github.com/zsh-users/zsh-autosuggestions);
-   [zsh-users/zsh-completions: Additional completion definitions for Zsh. (github.com)](https://github.com/zsh-users/zsh-completions);

这里原文中还用到了一款主题插件, 但是我这里就不用了, 一切为了速度~(不过mac主机可以用, 看不出影响)

# 备份

首先就是卸载omz(如果有)

```bash
 uninstall_oh_my_zsh
```

然后查看一下你的`.zshrc`和`.zsh_history`, 这两个文件需要备份一下,稍后会用到. 注意, 如果卸载omz, 那么omz会帮你备份, 文件名类似这样`.zshrc.omz-uninstalled-2022-09-15_00-50-08`. 然后`.zshrc`会被替换为在安装omz之前的配置, 可能会有不同, 大家注意区分. 

```bash
cp .zshrc .zshrc_bak
```

# 创建配置文件夹

```bash
mkdir -p .zsh/plugins
cp .zshrc .zsh/
mv .zsh_history .zsh/
```

然后编辑`.zshrc`, 加上:

```bash
### ZSH HOME
export ZSH=$HOME/.zsh

### ---- history config ----------
export HISTFILE=$ZSH/.zsh_history

# How many commands zsh will load to memory.
export HISTSIZE=10000

# How maney commands history will save on file.
export SAVEHIST=10000

# History won't save duplicates.
setopt HIST_IGNORE_ALL_DUPS

# History won't show duplicates on search.
setopt HIST_FIND_NO_DUPS
```

# 安装插件

```bash
cd .zsh/plugins
git clone git@github.com:zdharma-continuum/fast-syntax-highlighting.git

git clone git@github.com:zsh-users/zsh-autosuggestions.git

git clone git@github.com:zsh-users/zsh-completions.git
```



在`.zshrc`中添加:

```bash
source $ZSH/plugins/fast-syntax-highlighting/fast-syntax-highlighting.plugin.zsh
fpath=($ZSH/plugins/zsh-completions/src $fpath)

# zsh-autosuggestions:config
source $ZSH/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#ff00ff,bg=cyan,bold,underline"
ZSH_AUTOSUGGEST_STRATEGY=(history completion)
ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE=20

# end config
```

# 链接

最后就是创建符号链接, 这样我们就可以通过更改`~/.zshrc`来同步更改`.zsh/.zshrc`配置文件了.

首先需要确认家目录下没有`.zshrc`文件, 如果有, 将所有内容复制到`.zsh/.zshrc`中, 然后`rm .zshrc`.

此时可以开始创建符号链接了. 

```bash
ln -s ~/.zsh/.zshrc ~/.zshrc

```

可以查看一下:

```bash
ls -la
.zshrc -> .zsh/.zshrc
```

然后:

```bash
source ~/.zshrc
```

即可完成~

# PROMPT配置

由于我没安装主题插件, 这里就通过一行命令配置提示符进行配置, 参考了[^2].

```bash
# prompt
ZSH_NEWLINE=$'\n'
export PROMPT=" %F{46}%F %(?.%F{green}√.%F{red}?%?)%f  %B%F{69}%~ ${ZSH_NEWLINE} %F{119}==>%f%b "

```

# 结果

```bash
√ ~/.zsh tree -L 2 -a
.
├── .zsh_history
├── .zshrc
└── plugins
    ├── fast-syntax-highlighting
    ├── zsh-autosuggestions
    └── zsh-completions
```

<img src="https://cdn.jsdelivr.net/gh/zorchp/blogimage/%E6%88%AA%E5%B1%8F2023-11-25%2012.06.39.png" alt="截屏2023-11-25 12.06.39" style="zoom:50%;" />



# ref

[^1]: [Using ZSH without OMZ - DEV Community 👩‍💻👨‍💻](https://dev.to/hbenvenutti/using-zsh-without-omz-4gch);
[^2]:[How Do I Change My ZSH Prompt Name (linuxhint.com)](https://linuxhint.com/change-zsh-prompt-name/);