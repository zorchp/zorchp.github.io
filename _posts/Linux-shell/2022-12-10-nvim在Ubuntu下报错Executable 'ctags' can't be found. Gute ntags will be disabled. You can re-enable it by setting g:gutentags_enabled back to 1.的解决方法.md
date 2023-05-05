---
categories: [Linux-Shell]
tags: Vim Server Debug
---

# 问题

最近在Ubuntu云服务器环境中部署了一下nvim, 用的大佬的配置[^1], 但是在Mac上没问题(指的是执行`:checkhealth`), 却在Ubuntu上有问题了, 具体信息为打开`.yaml`文件之后报错(其他文件没有此类问题):

```lua
Executable 'ctags' can't be found. Gutentags will be disabled. You can re-enable it by setting g:gutentags_enabled back to 1.
```

一开始我天真的以为加上`let g:gutentags_enabled=1`这句就行了, 没想到根本没有用, 翻看google发现, 原来解决方法竟然如此简单...

参考[^2],[^3]. 

# 解决

一开始我用了[^2]给出的方案:

```bash
sudo apt-get install global
sudo snap install universal-ctags
```

但是安装之后并没有完全解决, 报错当然是没有了, 但是会出现:

```bash
gutentags: ctags job failed, returned: 1
```

后来看到了[^3], 说是用`brew`来安装`ctags`:

```bash
brew install ctags
```

死马当活马医, 正好前阶段安装了LinuxBrew[^4], 侥幸心理试试, 结果还真成了!





# ref

[^1]:[ayamir/nvimdots: A well configured and structured Neovim. (github.com)](https://github.com/ayamir/nvimdots);
[^2]:[vim-gutentags插件异常问题解决 & gtags源码编译安装 - 小黑杂说 (wuruofan.com)](https://wuruofan.com/2020/07/07/ubuntu-vim-gutentags-work-abnormally-solved-with-universal-ctags-and-global-recompiled/);
[^3]:[ctags job failed, returned: 1 · Issue #169 · ludovicchabant/vim-gutentags (github.com)](https://github.com/ludovicchabant/vim-gutentags/issues/169#issuecomment-484460006);
[^4]:[在Ubuntu上安装最新的neovim(with LinuxBrew)\_zorchp的博客-CSDN博客\_ubuntu 安装neovim](https://zorchp.blog.csdn.net/article/details/128172332);