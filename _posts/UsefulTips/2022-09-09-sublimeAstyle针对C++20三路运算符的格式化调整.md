---
categories: [Tips]
tags: Sublime Tips C++
---

# 写在前面

之前文章介绍过关于在sublime编辑器中格式化C/C++ 代码的最佳方式, 但是昨天尝试用C++20新增的三路运算符时候突然被格式化掉了, 具体例子如下:

```cpp
auto ans1 = a <=> b;
// 被格式化为
auto ans1 = a <= > b;
```



这就成了一个显然的语法错误了, 一开始我想通过更新插件或者看issue的方式解决, 但是这个项目已经不活跃了, 没办法,只能靠自己了.

# 配置方法

首先进入官方文档[^1], 但是选项太多了, 找起来不方便... 后来参考的gist[^2], 还是不错的, 通过在家目录下配置`.astylerc`文件完成配置, 这里除了复制全部的内容并新建文件, 还需要修改一个选项, 如下:

```bash
cd ~
vim .astylerc
```

注释掉`pad-oper`选项, 使得不进行操作符之间空格的填充:

```lua
# Insert space padding around operators. Any end of line comments will remain
# in the original column, if possible. Note that there is no option to unpad.
# Once padded, they stay padded.
#
# if (foo==2)
#     a=bar((b-c)*a,d--);
#
# becomes:
#
# if (foo == 2)
#      a = bar((b - c) * a, d--);
#
#pad-oper
```

然后, 还需要进行一个sublime选项的配置, 进入`sublimeAstyleformatter`的user-settings界面, 修改使用外部选项, 如下:

```json
    // Language-specific for C++
    "options_c++": {
        "use_only_additional_options": true,
        "additional_options_file": "/Users/xxx/.astylerc",//your astylerc file dir
    },
```

保存之后再进行格式化, 就不会影响三路运算符了. 这里其实直接改sublime本身的配置也可以, 但是我更喜欢使用配置文件, 管理起来比较方便, 如果直接在sublime中改就是:

```json
        // Insert space padding around operators. Any end of line comments
        // will remain in the original column, if possible. Note that there
        // is no option to unpad. Once padded, they stay padded.
        "pad-oper": false,
```





# ref

[^1]:[Artistic Style (sourceforge.net)](http://astyle.sourceforge.net/astyle.html);
[^2]:[Astyle code automatic formatting settings (github.com)](https://gist.github.com/derofim/49a1d0eea566230567ac36f0f386f27b);