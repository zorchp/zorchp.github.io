---
categories: [LaTeX]
tags: Vim LaTeX Tips Lua
---

# 写在前面

折腾一下在Mac上配置neovim写LaTeX的环境, 以及skim阅读器的配置. 这里参考了一位朋友的配置[^1], 我改成了在mac上使用的配置了.

# vimtex配置

```lua
function config.vimtex()
    vim.g.tex_flavor='latex' -- Default tex file format
    vim.g.vimtex_view_method = 'skim'
    -- allows forward search after every successful compilation
    vim.g.vimtex_view_skim_sync = 1
    -- allows change focus to skim after command `:VimtexView` is given
    vim.g.vimtex_view_skim_activate = 1

    vim.g.vimtex_indent_bib_enabled = 0
    vim.g.vimtex_indent_enabled = 0

    vim.g.vimtex_complete_enabled = 0
    -- Disable imaps (using Ultisnips)
    vim.g.vimtex_imaps_enabled = 0
    -- Do not open pdfviwer on compile
    vim.g.vimtex_view_automatic = 0
    -- Disable conceal
    vim.g.vimtex_syntax_conceal = {
        accents = 0,
        cites = 0,
        fancy = 0,
        greek = 0,
        math_bounds = 0,
        math_delimiters = 0,
        math_fracs = 0,
        math_super_sub = 0,
        math_symbols = 0,
        sections = 0,
        styles = 0,
    }
    -- Enable quickfix auto open
    -- vim.g.vimtex_quickfix_ignore_mode = 1
    vim.g.vimtex_compiler_progname = 'nvr'
    -- PDF viewer settings
    -- vim.g.vimtex_view_general_viewer = "skim"
    -- auto open quickfix on compile erros
    vim.g.vimtex_quickfix_mode = 1
    -- Latex warnings to ignore
    vim.g.vimtex_quickfix_ignore_filters = {
        "Command terminated with space",
        "LaTeX Font Warning: Font shape",
        "Package caption Warning: The option",
        [[Underfull \\hbox (badness [0-9]*) in]],
        "Package enumitem Warning: Negative labelwidth",
        [[Overfull \\hbox ([0-9]*.[0-9]*pt too wide) in]],
        [[Package caption Warning: Unused \\captionsetup]],
        "Package typearea Warning: Bad type area settings!",
        [[Package fancyhdr Warning: \\headheight is too small]],
        [[Underfull \\hbox (badness [0-9]*) in paragraph at lines]],
        "Package hyperref Warning: Token not allowed in a PDF string",
        [[Overfull \\hbox ([0-9]*.[0-9]*pt too wide) in paragraph at lines]],
    }
    vim.g.vimtex_fold_enabled = 0
    vim.g.vimtex_fold_manual = 0
    vim.g.vimtex_fold_types = {
        cmd_addplot = {
            cmds = { "addplot[+3]?" },
        },
        cmd_multi = {
            cmds = {
                "%(re)?new%(command|environment)",
                "providecommand",
                "presetkeys",
                "Declare%(Multi|Auto)?CiteCommand",
                "Declare%(Index)?%(Field|List|Name)%(Format|Alias)",
            },
        },
        cmd_single = {
            cmds = { "hypersetup", "tikzset", "pgfplotstableread", "lstset" },
        },
        cmd_single_opt = {
            cmds = { "usepackage", "includepdf" },
        },
        comments = {
            enabled = 0,
        },
        env_options = vim.empty_dict(),
        envs = {
            blacklist = {},
            whitelist = { "figure", "frame", "table", "example", "answer" },
        },
        items = {
            enabled = 0,
        },
        markers = vim.empty_dict(),
        preamble = {
            enabled = 0,
        },
        sections = {
            parse_levels = 0,
            parts = { "appendix", "frontmatter", "mainmatter", "backmatter" },
            sections = {
                "%(add)?part",
                "%(chapter|addchap)",
                "%(section|section\\*)",
                "%(subsection|subsection\\*)",
                "%(subsubsection|subsubsection\\*)",
                "paragraph",
            },
        },
    }
end

```

## 编译

```c
\ll
```



# skim的配置(方法1)

这个方法比较简单,无需配置nvim的服务器实例, 参考[^2].

同步选项, 命令是`custom`(自定), 然后参数为

```bash
--headless -c "VimtexInverseSearch %line '%file'"
```

当然前提是要在zsh默认的Python环境中安装:

```bash
python3 -m pip install neovim-remote
```

这样的话, 就能完成正反向搜索了, skim通过`command+shift+左键单击`反向跳转到vim, vim通过`\lv`跳转到skim的文章对应位置.

# skim配置(方法2, 弃用)

这个比较麻烦, 需要每次制定一个启动实例, 结果跟上面是一样的, 参考[^3]. 在今年1月份更新vimtex之后, 就不需要通过这样复杂的配置方法进行正反向搜索了.

>   2022-01-19: With the release of [VimTeX v2.8](https://github.com/lervag/vimtex/releases/tag/v2.8), all the hack here may not be needed anymore.

下面给出lua实现: 思路就是用一个临时文件`/tmp/vimtexserver.txt`保存`:echo v:servername`的内容, 然后通过skim读取这份文件的内容.

```lua
    vim.api.nvim_create_autocmd("FileType", {
        pattern = "tex",
        callback = function()
            vim.fn.writefile(
                {vim.fn.execute(":echo v:servername", "silent")}, 
                "/tmp/vimtexserver.txt")
        end,
    })
```

在skim中配置如下:

命令自定, `nvr`, 然后参数为

```bash
 --servername `cat /tmp/vimtexserver.txt` +"%line" "%file"
```

# latexmkrc配置文件

因为每次在文稿开头都要加上

```c
%!TEX program = xelatex
```

感觉还是比较麻烦, 这时候可以加上一个配置文件

```c
#
# Generel
#

# Needed for the dot2texi package which invokes GraphViz.
$latex = 'latex --shell-escape';
$xelatex = 'xelatex --shell-escape';

# 
# Mac OS
#
# $pdflatex = 'pdflatex -synctex=1 %O %S';
$xelatex = 'xelatex -synctex=1 %O %S';
$pdf_previewer = "open -a Skim";
$clean_ext = "paux lox pdfsync out";
$pdf_mode = 5;
$postscript_mode = $dvi_mode = 0;
```



# ref

[^1]:[jczhang02/nvim_dots (github.com)](https://github.com/jczhang02/nvim_dots);
[^2]:[Setup Skim PDF reader with VimTeX in Mac OS \| Deepak Ramani (dr563105.github.io)](https://dr563105.github.io/blog/skim-vimtex-setup/);
[^3]:[Set up Inverse Search for LaTeX with VimTeX and Neovim - jdhao's digital space](https://jdhao.github.io/2021/02/20/inverse_search_setup_neovim_vimtex/);