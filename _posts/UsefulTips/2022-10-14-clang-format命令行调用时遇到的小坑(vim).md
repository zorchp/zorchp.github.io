---
categories: [Tips]
tags: C++ Vim Debug
---

# 写在前面

最近开始用neovim作为IDE了, 虽然参考了大佬的配置, 自己也学会了一些Lua语言的配置方法, 但是还是难免遇到一些奇奇怪怪的玄学问题, 不过,最终还是解决了.

>   问题描述: 
>
>   在vim调用``clang-format`时候, 总是不会正常的进行格式化, 也没有任何报错.格式化的代码如下(通过命令行进行调用)
>
>   ```json
>   clang-format -style='{BasedOnStyle: Google, IndentWidth: 4, SortIncludes: false, AccessModifierOffset: -4, ContinuationIndentWidth: 4, AlignAfterOpenBracket: true, AlignOperands: true, AlignTrailingComments: true, MaxEmptyLinesToKeep: 2, SpacesBeforeTrailingComments: 1, KeepEmptyLinesAtTheStartOfBlocks: true, AllowShortBlocksOnASingleLine:true}' test.cpp
>   ```
>
>   

# 解决方法

乍一看是没有任何问题的, 就是格式化套用指定格式, 但是通过终端运行时候会出现:

```lua
<command-line>:1:320: error: Found unexpected ':' while scanning a plain scalar
{BasedOnStyle: Google, IndentWidth: 4, SortIncludes: false, AccessModifierOffset: -4, ContinuationIndentWidth: 4, AlignAfterOpenBracket: true, AlignOperands: true, AlignTrailingComments: true, MaxEmptyLinesToKeep: 2, SpacesBeforeTrailingComments: 1, KeepEmptyLinesAtTheStartOfBlocks: true, AllowShortBlocksOnASingleLine:true}
```

这也就找到了问题所在, 在格式化选项指定的时候, 值前面的冒号不能不加空格! 就是这个问题使得vim调用时候补全失败, 但是vim又不会报错(因为是通过`efm`调用)..

改成下面这样, 就完美了:

```json
clang-format -style='{BasedOnStyle: Google, IndentWidth: 4, SortIncludes: false, AccessModifierOffset: -4, ContinuationIndentWidth: 4, AlignAfterOpenBracket: true, AlignOperands: true, AlignTrailingComments: true, MaxEmptyLinesToKeep: 2, SpacesBeforeTrailingComments: 1, KeepEmptyLinesAtTheStartOfBlocks: true, AllowShortBlocksOnASingleLine: true}'
```

