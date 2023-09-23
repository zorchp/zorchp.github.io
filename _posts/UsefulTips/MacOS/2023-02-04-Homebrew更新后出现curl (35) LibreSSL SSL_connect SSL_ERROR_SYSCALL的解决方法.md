---
categories: [Tips]
tags: MacOS Brew Debug
---

# 问题

brew更新之后, 使用`brew outdated --cask`会出现下面的错误:

```c
curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to formulae.brew.sh:443
```

或者说应该是一个警告, 那么怎么解决呢? 

一开始以为是代理的问题, 关掉之后也不行, 后来看到了Stack Overflow的方案, 很不错, 在此记录一下. 



# 解决方案

>   -   [networking - Homebrew gives SSL error (SSL_ERROR_SYSCALL) on home network - Super User](https://superuser.com/questions/1264498/homebrew-gives-ssl-error-ssl-error-syscall-on-home-network/1654685#1654685);
>   -   [brew update fails if there are unstashed changes in homebrew core · Issue #3410 · Homebrew/brew (github.com)](https://github.com/Homebrew/brew/issues/3410#issuecomment-343922422);

首先使用下面的命令重置brew到最新版:

```bash
brew update-reset
```

这个过程可能要持续一段时间, 因为要拉取最新版的brew. 

然后更新:

```bash
brew update
```

这个过程中我都是开启代理的, 就算有了ustc源还是慢. 再试试:

```bash
 ==> brew update
HOMEBREW_BREW_GIT_REMOTE set: using https://mirrors.ustc.edu.cn/brew.git for Homebrew/brew Git remote.
HOMEBREW_CORE_GIT_REMOTE set: using https://mirrors.ustc.edu.cn/homebrew-core.git for Homebrew/core Git remote.
Already up-to-date.
√  ~
 ==> brew outdated --cask
calibre (6.8.0) != 6.12.0
dosbox-x (2022.12.26,20201226002957) != 2022.12.26,20221226183221
geogebra (6.0.722.0) != 6.0.755.0
keycastr (0.9.12) != 0.9.13
prince (15) != 15.0.1
rstudio (2022.07.2,576) != 2022.12.0,353
```

OK了. 
