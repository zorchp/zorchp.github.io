---
tags: MacOS Tips Sublime
---

# 写在前面

最近又开始折腾编辑器了, 当然还是一个历史遗留问题, 我最爱的Sublime还是不能通过终端执行C/C++程序, 或者就是执行完之后直接退出了, 绕了一圈, 从每一个程序中加上`system(read);`算是一个折中的方案, 但是终归有点麻烦, 采用AppleScript(命令行中使用`osascript -e`)的方法当然可以, 但是我找了半天也没一个能跑明白... 只能说自己功力不够

# 针对Terminal

下面倒是一个可以通过applescript跑起来的例子, 就是对`iTerm`不行, 只能对系统默认的终端(`Terminal.app`)来操作.. 还是有点鸡肋的. 这个命令我参考了[^1], 并做了一些改动.

```bash
# double `-e`
osascript -e 'tell application "Terminal" to activate' -e 'tell application "Terminal" to do script "/Users/xxx/Desktop/main && read -n && exit"'
# single `-e`
osascript -e 'tell application "Terminal" to activate do script "clear && /Users/xxx/Desktop/main && read -n && exit"'
```

稍加配置就可以直接在sublime中运行了, 这里的配置就不详细说了. 其实万变不离其宗, 都是通过修改后缀为`.sublime-build`的JSON文件实现的编译系统的配置. 下面主要以主流的iTerm为例进行配置. 



# 针对iTerm

这里借鉴一位印度开发者的gist[^2], 这里我修改成直接能运行的配置, 如下:

```json
{
    "shell_cmd": "g++ $file_name -o ${file_base_name}.out && \"/Users/xxx/Library/Application Support/Sublime Text 3/Packages/User/run-in-iTerm.sh\" ${file_path}/${file_base_name}.out",
    "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
    "working_dir": "${file_path}",
    "selector": "source.c, source.c++, source.cxx, source.cpp",
}
```

其中的`run-in-iTerm.sh`如下(其实还是Apple脚本):

```lua
#!/bin/bash

################################################
# https://stackoverflow.com/questions/32675804/how-do-i-execute-a-command-in-an-iterm-window-from-the-command-line
# https://www.iterm2.com/documentation-scripting.html
# Better Examples @ https://gitlab.com/gnachman/iterm2/wikis/Applescript
################################################

osascript - "$@" <<EOF
on run argv
tell application "iTerm"
    activate
    set new_term to (create window with default profile)
    tell new_term
        tell the current session
            repeat with arg in argv
               write text arg
            end repeat
        end tell
    end tell
end tell
end run
EOF

```

但是我后来发现, 这个appleScript脚本还是有一些不方便的地方, 就比如每次执行之后都会创建一个新的iTerm窗口, 需要自己关闭, 我需要的是按下enter之后就销毁窗口(这点在vs或者dev-c++上就做得很好).

于是我又找到另外一种脚本[^3], 如下:

```lua
#!/bin/bash

osascript - "$@" <<EOF
on run argv
    tell application "iTerm"
        if (window count) is equal to 0 then
            reopen
        end if
        tell current session of current window
            repeat with arg in argv
                write text arg
            end repeat
        end tell
    end tell
end run
EOF

```

上面脚本的意思是通过现有的窗口完成程序的运行, 但是这个也有一个问题, 就是必须要有一个已经打开的iTerm窗口, 否则就会报错说找不到打开的iTerm窗口, 这个还是有点烦, 接着找..

后来接连看了几篇回答和对应的外链(其实就是gist代码段和iTerm官方给出的代码), 分别是[^4],[^5], 发现Applescript已经被iTerm弃用了, 取而代之的是Python-API, 但是配置起来还是比较麻烦(其实就是因为自己没学过`async`)

后来几经摸索, 我想出来了一个方案, 就是在前面给出的json的基础上, 设置一些参数, 使得`Press ENTER to exit`得以实现, 下面是最后的配置, 当然, 这里也参考了sublime的build system的主要配置参数[^6], 比较简单, 这里我直接贴出来代码了:

```json
{
    "shell_cmd": "g++ -std=c++20 $file_name -o ${file_base_name}.out && \"/Users/xxx/Library/Application Support/Sublime Text 3/Packages/User/run-in-iTerm.sh\" \"clear && ${file_path}/${file_base_name}.out && read 'word?Press ENTER to exit!' && exit\"",
    "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
    "working_dir": "${file_path}",
    "selector": "source.c, source.c++, source.cxx, source.cpp",
}
```

通过捕获`read`命令的方式进行配置[^7], 这里也有一个坑, 就是之前的`read -p "xxx"`的方式在`zsh`上面失效了, 就必须采用`read "name?what's your name?"`的方式进行读取, 一个测试的例子如下:

```bash
❯ read "name?what's your name?"
what's your name?paul
❯ echo $name
paul

# another format
❯ read name\?"what's your name?"
what's your name?paul
❯ echo $name
paul
```

这里当然就是随便选取一个别名即可, 我取的就是`Press ENTER to exit!` 

>   这里有一个小插曲, 就是看第一段applescript中的代码, 里面的
>
>   ```lua
>   repeat with arg in argv
>      write text arg
>   end repeat
>   ```
>
>   部分是不是很像Python的`for i in range()`呢? 其实就是逐参数读取的命令, 这里我设置了一连串的命令, 就是方便其在iTerm中执行:
>
>   ```bash
>   \"clear && ${file_path}/${file_base_name}.out && read 'word?Press ENTER to exit!' && exit\"
>   ```
>



总体效果还是很不错的, 如下:



![aa](https://s2.loli.net/2022/08/09/iOktVLa3xYMhbfs.gif)



# 参考

[^1]:[macos - How to use osascript to open the Terminal App in a new window and make sure it's on the top of all other windows? - Ask Different (stackexchange.com)](https://apple.stackexchange.com/questions/205143/how-to-use-osascript-to-open-the-terminal-app-in-a-new-window-and-make-sure-its);
[^2]:[Sublime Text 3 CPP Basic Setup (on Mac). (github.com)](https://gist.github.com/phoenisx/f8c866b7c66f3af05b00d4db9c676fcc);
[^3]:[iterm_cmd.sh (github.com)](https://gist.github.com/LeoUfimtsev/82e7e827b6bfb1000f422a98f2008cc3);

[^4]:[How do I execute a command in an iTerm window from the command line? - Stack Overflow](https://stackoverflow.com/questions/32675804/how-do-i-execute-a-command-in-an-iterm-window-from-the-command-line);
[^5]:[Scripting - Documentation - iTerm2 - macOS Terminal Replacement](https://iterm2.com/documentation-scripting.html);

[^6]:[Build Systems — Sublime Text Unofficial Documentation (sublime-text-unofficial-documentation.readthedocs.io)](https://sublime-text-unofficial-documentation.readthedocs.io/en/sublime-text-2/reference/build_systems.html);
[^7]:[bash - zsh: read:-p: no coprocess error while using read command with -p flag - Ask Ubuntu](https://askubuntu.com/questions/1246576/zsh-read-p-no-coprocess-error-while-using-read-command-with-p-flag);
