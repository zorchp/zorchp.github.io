---
categories: [Tips]
tags: R Debug
---

# 写在前面

安装R语言读取Excel文件的一个包`xlsx`, 需要用到java环境, 所以配置起来比较麻烦一些, 喜爱按分别在两个平台上进行配置的详细说明. 

# macOS上的解决方案

这里需要进行如下的操作, 主要参考[^2]:

```bash
$ /usr/libexec/java_home -V
Matching Java Virtual Machines (1):
    1.8.0_162, x86_64:	"Java SE 8"	/Library/Java/JavaVirtualMachines/jdk1.8.0_162.jdk/Contents/Home

$ export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_162.jdk/Contents/Home

$ export PATH=$JAVA_HOME/bin:$PATH

$ R CMD javareconf

$ R --quiet -e 'install.packages("rJava", type="source", repos="http://cran.us.r-project.org")'
```

这里我安装时候用到的java在`/opt/homebrew/`中, 其他均不变, 一套流程走下来就完美解决了~





# win10的解决方案

首先下载jdk18 的最新安装包, 这里推荐用msi格式的安装包, 直接安装即可, 注意路径一会要用到. 

找到安装路径, 在资源管理器的地址栏后面输入(前面的东西类似于`D:\JAVA\jdk-18.0.1`, 保留)

```bash
bin\jlink.exe --module-path jmods --add-modules java.desktop --output jre
```

执行完毕之后就会有jre文件夹, 这个文件夹的路径之后也会用到. 

然后设置环境变量, 在**系统变量**->**Path**–>**编辑**–>**编辑文本**，在变量值最后输入`;%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin`

新建系统变量`JAVA_HOME`, 值为`D:\JAVA\jdk-18.0.1`, 类似这样. 

然后回到Rstudio, 执行安装即可, `install.packages('xlsx')`, 就可以愉快使用啦~

## 一个小插曲

在环境为Windows10, R版本为4.2.0, Java为jdk18的电脑上, RStudio一执行`library('xlsx')`就会报错, `RSession Aborted`, 然后莫名其妙退出. 这里我也是百思不得解, 后来在官方的帖子[^1] 上找到了答案, 最新版R和RStudio之间有某种冲突关系, 解决办法是安装一个patched版本的R包, 安装地址为[Download the R-4.2.0 Patched build for Windows. The R-project for statistical computing.](https://cran.r-project.org/bin/windows/base/rpatched.html); 

# 小结





[^1]:[R session aborted when loading "xlsx" package - RStudio IDE - RStudio Community](https://community.rstudio.com/t/r-session-aborted-when-loading-xlsx-package/135572/4);
[^2]:[Compiling rJava macOS, java8 · Issue #153 · s-u/rJava (github.com)](https://github.com/s-u/rJava/issues/153);