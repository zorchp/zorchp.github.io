---
tags: Sublime
categories: [Tips]
---



# 基本配置

## 字体

```json
    "font_size": 20,
    "font_face": "JetBrainsMono Nerd Font Mono",
```

## 自动保存

```json
    "save_on_focus_lost": true,
```

## 光标显示样式

```json
    "caret_style": "smooth",
```



## Vintage

```json
    "ignored_packages":
    [
        "Vintage",
    ],
    "vintage_use_clipboard": true,
    "vintage_ctrl_keys": true,
    "relative_line_numbers": true,
```



## 空格和缩进(制表位)

```json
    "tab_size": 4,
    "use_tab_stops": true,
    "translate_tabs_to_spaces": true,
    "draw_white_space":
    [
        "all",
        "selection"
    ],
    "word_wrap": true,
```

## 更新检查

```json
    "update_check": false
```

## 主题

```json
    "color_scheme": "Packages/Agila Theme/Agila Neon Monocyanide.tmTheme",
    "theme": "Agila Neon.sublime-theme",
```





# 快捷键部分

## 构建

```json
    {
        "command": "build",
        "keys": [
            "f10"
        ]
    }
```



## Vintage

Vim, 但是不太好用.. 

```json
    {
        "command": "exit_insert_mode",
        "context": [
            {
                "key": "setting.command_mode",
                "operand": false
            },
            {
                "key": "setting.is_widget",
                "operand": false
            }
        ],
        "keys": [
            "j",
            "k"
        ]
    }
```



## 块注释

```json
    {
        "args": {
            "block": true
        },
        "command": "toggle_comment",
        "keys": [
            "super+shift+forward_slash"
        ]
    }
```





## format code

未配置 format on save, 因为可能导致一些问题(阅读源码时).

### C/C++ and js

>   [SublimeClangFormat](https://github.com/rosshemsley/SublimeClangFormat);

```cpp
    {
        "command": "clang_format",
        "context": [
            {
                "key": "selector",
                "operand": "source.c++",
                "operator": "equal"
            }
        ],
        "keys": [
            "super+option+l"
        ]
    },
    {
        "command": "clang_format",
        "context": [
            {
                "key": "selector",
                "operand": "source.c",
                "operator": "equal"
            }
        ],
        "keys": [
            "super+option+l"
        ]
    },
    {
        "command": "clang_format",
        "context": [
            {
                "key": "selector",
                "operand": "source.js",
                "operator": "equal"
            }
        ],
        "keys": [
            "super+option+l"
        ]
    },
```



### python

```json
    {
        "command": "anaconda_auto_format",
        "context": [
            {
                "key": "selector",
                "operand": "source.python",
                "operator": "equal"
            }
        ],
        "keys": [
            "super+alt+l"
        ]
    }
```



### json and xml

by [indent_xml](https://github.com/alek-sys/sublimetext_indentxml).

```json
    {
        "command": "auto_indent",
        "keys": [
            "super+alt+l"
        ]
    }
```



