---
tags: GoLang
categories: GoLang
---

## 写在前面

```bash
brew install go
```



最近新安装的 go 突然不能用了, 很奇怪, 后来发现需要设置一下

```bash
# vi ~/.zshrc
# Set the GOPROXY environment variable
export GOPROXY=https://goproxy.io,direct
export GOROOT=/opt/homebrew/Cellar/go/1.21.4/libexec/
export GOPATH=$HOME/go/
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
```

>   坑点就在 libexec, 之前好像是不需要的, 不加的话就会找不到 go 的执行文件, 报错:
>
>   ```c
>   package fmt is not in std (/opt/homebrew/Cellar/go/1.21.4/src/fmt)
>   package command-line-arguments: cannot find package
>   ```



在 nvim 里面开启 gopls 支持

```bash
brew install gopls
go get golang.org/x/tools/gopls@latest
# vim-go: could not find 'gopls'. Run :GoInstallBinaries to fix it
```



测试一下

```bash
go run hello.go
```

