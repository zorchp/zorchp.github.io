---
categories: [Tips]
tags: Tips iTerm Sublime
---

# 写在前面

最近在medium[^1]看到一款不错的字体, 名叫FiraCode, 其主要特色功能就是能够将诸如大于等于号`>=`, 箭头符号`->`这样的复合符号连接起来,产生一种很棒的效果, 具体效果这里就不展示了, 可以看官方GitHub主页[^2].

下面主要讲一下如何在macOS中配置这个字体, 主要展示在sublime和iTerm中进行字体配置.

# 安装字体

```bash
brew tap homebrew/cask-fonts
brew install --cask font-fira-code
```



# sublime配置字体

在settings文件里面写入:

```json
"font_face": "fira code",
```

保存即可生效.

# iTerm配置字体

这里面有一点小的不同,需要在advanced选项中关闭`ligature`, 具体参考[^3], 下两图为具体配置.

![截屏2022-09-10 00.09.42](https://img-blog.csdnimg.cn/4b3ad7ba996143579dc7b2eb0d2a06de.jpeg#pic_center)![截屏2022-09-10 00.10.08](https://img-blog.csdnimg.cn/38266abccbc34f7daf1a79a4925fac27.jpeg#pic_center)



# ref

[^1]:[11 Best Programming Fonts. There are many posts and sites… | by Charlee Li | ITNEXT](https://itnext.io/11-best-programming-fonts-724283a9ed57);
[^2]:[tonsky/FiraCode: Free monospaced font with programming ligatures (github.com)](https://github.com/tonsky/FiraCode);
[^3]:[vim - firacode ligatures not working in iterm 2 - Stack Overflow](https://stackoverflow.com/questions/59128426/firacode-ligatures-not-working-in-iterm-2);