---
categories: [Linux-Shell]
tags: git Tips
---

# 写在前面

近期更新了一下自己的GitHub Pages博客, 但是发现上传到GitHub上面的文件中有很多奇奇怪怪的文件, 并且无关于博客的构建与生成. 之前倒是在阮一峰老师的技术周刊上面看到一篇文章[^1]通过`.gitignore`文件去除MacOS下独有的索引文件`.DS_Store`文件, 但是感觉写的太简略了, 实在是没有到我心坎里, 下面根据另外几篇不错的文章[^2][^3], 加上官方文档中的解释/示例[^4]与自己的实践, 总结出本文, 校网能对同样热爱技术的大家有所帮助. 

>   测试环境: MacOS

# .gitignore能干什么

>   通常，在项目上使用Git的工作时，您会希望排除将特定文件或目录推送到远程仓库库中的情况。`.gitignore`文件可以指定Git应该忽略的未跟踪文件。

例如jetbrains系列IDE项目生成的`.idea`目录, vscode生成的`.vscode`目录, 或者C项目编译的目标文件等, 这些文件都不是项目的源码, 并且没有这些内容会让源代码更加清爽, 这时候就要有一个`.gitignore`文件来大显身手了. 



# 基本用法

gitignore文件采用`#`作为注释符号, 空行用来分隔不同模式, 一行表示一个模式, 在GitHub中每次创建仓库会问项目是否需要gitignore以及语言类型, 不同语言类型对应不同的gitignore模板.

## 通配符规则

`.gitignore`文件是纯文本文件，其中每行包含一个模式，用于忽略文件或目录。`.gitignore`使用全局匹配模式来匹配带通配符的文件名。如果文件或目录包含在通配符，则可以使用单个反斜杠（`\`）来转义字。

### 斜杠符

斜杠符号（`/`）是目录的分隔符。斜杠开头模式相对于`.gitignore`所在的目录。如果模式以斜杠开头，则仅从仓库的根目录中开始匹配文件和目录。如果模式不是以斜杠开头，则它将匹配任何目录或子目录中的文件和目录。

如果模式以斜杠结尾，则仅匹配目录。当目录被忽略时，其所有文件和子目录也将被忽略。

### 文件名

最直接的模式是没有任何特殊字符的文件名。例如/access.log仅匹配access.log。而access.log将会匹配当前目录与子目录 access.log，logs/access.log ，var/logs/access.log。当以/斜杠符号结束时则匹配目录。例如build/匹配build目录。

### 通配符

**`*`**星号符号匹配零个或多个字符。例如`*.log`模式将匹配error.log，logs/debug.log，build/logs/error.log等所有目录下以.log作为扩展名的文件。

`**`两个相邻的星号符号匹配任何文件或零个或多个目录。当后跟斜杠（`/`）时，它仅与目录匹配。例如，logs/**将会匹配logs目录中所有文件与目录。**/build将匹配所有目录中出现以build命名目录与文件var/build，pub/build。

模式foo/**/bar将匹配foo/bar，foo/a/bar，foo/a/b/c/bar。

`?`问号匹配单个任意字符。例如模式access?.log将会匹配access0.log，access1.log，accessA.log 。

### 方括号

**[...]**方括号匹配方括号中包含的字符。当两个字符之间用连字符`-`隔开时，表示一个字符范围。该范围包括这两个字符之间的所有字符。范围可以是字母或数字。如果`[`之后的第一个字符是感叹号（`!`），则该模式匹配除指定集合中的字符以外的任何字符。

例如模式`*.[oa]`将匹配文件file.o，file.a。模式*.[!oa]将匹配file.s，file.1但不匹配file.0与file.a。

### 反模式

以感叹号（`!`）开头的模式将否定先前模式。此规则的例外是，如果排除了其父目录，则重新包含文件。例如模式 `*.log`与`!error.log`这将会匹配所有以.log作为扩展名文件，但不匹配error.log。



# 全局生效

可以创建一个全局的忽略文件, 用来设置所有本地项目提交时候的忽略规则.

例如，要将`~/.gitignore_global`设置为全局Git忽略文件，您可以执行以下操作。首先创建文件：

```bash
touch ~/.gitignore_global
```

将文件添加到Git配置：

```bash
git config --global core.excludesfile ~/.gitignore_global
```

这里我的全局规则为:

```lua
# ~/.gitignore_global
# Symlinked into ~/ as .gitignore

# Compiled source
*.dll
*.exe

# Packages/ Archives
*.7z
*.dmg
*.gz
*.iso
*.tar
*.zip
*.pkg

# Databases
*.sql
*.sqlite

# Logs
*.log

# project files
.idea/
.vscode/

# OS generated files
**/*.app
**/CmakeCache.txt
**/build/*
**/CmakeFiles/*
**/.DS_Store
.DS_Store
**/.Spotlight-V100
**/.Trashes
**/Thumbs.db
```



# 测试与调整

## 显示所有被忽略的文件

带有`--ignored`选项的`git status`命令显示所有被忽略文件的列表：

```bash
git status --ignored
```

在调试过程中比较常用, 可以看到被添加到gitignore忽略列表的文件. 



## 忽略以前提交的文件

您的工作副本中的文件可以被追踪，也可以不被追踪。要忽略先前提交的文件，需要取消暂存并从索引中删除该文件，然后在`.gitignore`中添加该文件模式.

`--cached`选项告诉git不要从工作树中删除文件，而只是从索引中删除它。要递归删除目录，请使用`-r`选项：

```bash
git rm --cached filename
```

如果要从索引和本地文件系统中删除文件，请忽略`--cached`选项。以递归方式删除文件时，使用`-n`选项将执行“空运行”(dry-run, 不运行, 只显示待删除的文件)并显示要删除的文件：

```bash
# 会删除本地路径
git rm -r directory 
```

然后进行递归删除(并不会删除本地路径)

```bash
# 只会删除索引
git rm --cached -r directory
```



# ref

[^1]:[Eradicating .DS_Store from Git (0xmachos.com)](https://0xmachos.com/2020-01-22-Eradicating-.DS_Store-From-Git/);
[^2]:[忽略Git中的文件和目录.gitignore | myfreax](https://www.myfreax.com/gitignore-ignoring-files-in-git/);
[^3]:[Git - gitignore Documentation (git-scm.com)](https://git-scm.com/docs/gitignore);
[^4]:[github/gitignore: A collection of useful .gitignore templates](https://github.com/github/gitignore);

