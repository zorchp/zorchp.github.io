---
categories: [Linux-Shell]
tags: Linux Tips Config
---



## 写在前面

在 xhs 看到了一个有意思的图片, 想试试能不能把内容反解出来. (后来还是求助了大模型 hh)

<img src="https://cdn.jsdelivr.net/gh/zorchp/blogimage@main//17ACC7378187B02BA8071341D20AE00C.jpg" alt="img" style="zoom: 33%;" />

## shell 源码

> Linux/MacOS 下运行良好. 

```bash
#!/bin/bash

text=" PEACE  FOR  ALL  PEACE  FOR  ALL "

# 获取终端尺寸
cols=$(tput cols)
lines=$(tput lines)
text_length=${#text}

# 频率和幅度控制
freq=0.3
amplitude=10

# 隐藏光标，恢复时清屏
tput civis
trap "tput cnorm; clear; exit" SIGINT

# 无限动画循环
for (( t = 0; ; t++ )); do
    clear

    for (( i = 0; i < lines; i++ )); do
        # 用 bc 替代 awk 计算 offset（macOS 通常默认没有 awk 的 BEGIN 块浮点能力）
        offset=$(echo "$amplitude * c($freq * ($t + $i))" | bc -l | awk '{printf "%d", $1}')

        # 计算水平起始列
        col=$(( (cols - text_length) / 2 + offset ))

        # 颜色渐变计算（256 色）
        base_color=12
        color_range=180
        color=$(( (base_color + i * color_range / lines + t) % 256 ))

        # 移动光标并打印字符（使用 printf 兼容性更好）
        tput cup $i $col
        char="${text:i % text_length:1}"
        printf "\033[38;5;%sm%s\033[0m" "$color" "$char"
    done

    sleep 0.03
done
```

### 转码 base64

```json
$ base64 print.sh -w 0
IyEvYmluL2Jhc2gKCnRleHQ9IiBQRUFDRSAgRk9SICBBTEwgIFBFQUNFICBGT1IgIEFMTCAiCgojIOiOt+WPlue7iOerr+WwuuWvuApjb2xzPSQodHB1dCBjb2xzKQpsaW5lcz0kKHRwdXQgbGluZXMpCnRleHRfbGVuZ3RoPSR7I3RleHR9CgojIOmikeeOh+WSjOW5heW6puaOp+WItgpmcmVxPTAuMwphbXBsaXR1ZGU9MTAKCiMg6ZqQ6JeP5YWJ5qCH77yM5oGi5aSN5pe25riF5bGPCnRwdXQgY2l2aXMKdHJhcCAidHB1dCBjbm9ybTsgY2xlYXI7IGV4aXQiIFNJR0lOVAoKIyDml6DpmZDliqjnlLvlvqrnjq8KZm9yICgoIHQgPSAwOyA7IHQrKyApKTsgZG8KICAgIGNsZWFyCgogICAgZm9yICgoIGkgPSAwOyBpIDwgbGluZXM7IGkrKyApKTsgZG8KICAgICAgICAjIOeUqCBiYyDmm7/ku6MgYXdrIOiuoeeulyBvZmZzZXTvvIhtYWNPUyDpgJrluLjpu5jorqTmsqHmnIkgYXdrIOeahCBCRUdJTiDlnZfmta7ngrnog73lipvvvIkKICAgICAgICBvZmZzZXQ9JChlY2hvICIkYW1wbGl0dWRlICogYygkZnJlcSAqICgkdCArICRpKSkiIHwgYmMgLWwgfCBhd2sgJ3twcmludGYgIiVkIiwgJDF9JykKCiAgICAgICAgIyDorqHnrpfmsLTlubPotbflp4vliJcKICAgICAgICBjb2w9JCgoIChjb2xzIC0gdGV4dF9sZW5ndGgpIC8gMiArIG9mZnNldCApKQoKICAgICAgICAjIOminOiJsua4kOWPmOiuoeeul++8iDI1NiDoibLvvIkKICAgICAgICBiYXNlX2NvbG9yPTEyCiAgICAgICAgY29sb3JfcmFuZ2U9MTgwCiAgICAgICAgY29sb3I9JCgoIChiYXNlX2NvbG9yICsgaSAqIGNvbG9yX3JhbmdlIC8gbGluZXMgKyB0KSAlIDI1NiApKQoKICAgICAgICAjIOenu+WKqOWFieagh+W5tuaJk+WNsOWtl+espu+8iOS9v+eUqCBwcmludGYg5YW85a655oCn5pu05aW977yJCiAgICAgICAgdHB1dCBjdXAgJGkgJGNvbAogICAgICAgIGNoYXI9IiR7dGV4dDppICUgdGV4dF9sZW5ndGg6MX0iCiAgICAgICAgcHJpbnRmICJcMDMzWzM4OzU7JXNtJXNcMDMzWzBtIiAiJGNvbG9yIiAiJGNoYXIiCiAgICBkb25lCgogICAgc2xlZXAgMC4wMwpkb25lCg==
```



## 最终效果



<img src="https://cdn.jsdelivr.net/gh/zorchp/blogimage@main//output.gif" alt="output" style="zoom:150%;" />