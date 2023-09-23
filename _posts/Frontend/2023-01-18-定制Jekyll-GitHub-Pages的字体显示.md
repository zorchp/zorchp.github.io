---
categories: [Frontend]
tags: Frontend CSS
---

# 写在前面

改一下博客的字体显示, 默认的不好看, 这里改成`JetBrainsMono Nerd Font Mono`, 连字字体. 

官方GitHub:

[JetBrainsMono Nerd Font Mono](https://github.com/ryanoasis/nerd-fonts/blob/master/patched-fonts/JetBrainsMono/Ligatures/Regular/complete/JetBrains%20Mono%20Regular%20Nerd%20Font%20Complete%20Mono.ttf);

这里我的主题的TeXt, 官方主页:[kitian616/jekyll-TeXt-theme: 💎 🐳 A super customizable Jekyll theme for personal site, team site, blog, project, documentation, etc. (github.com)](https://github.com/kitian616/jekyll-TeXt-theme);

# 更改方法

>   参考了:
>
>   [动态加载字体 - Tate & Snow (tate-young.github.io)](https://tate-young.github.io/2020/08/26/css-font-face.html);

在本地项目的目录下, 也就是你的`xxx.github.io`这个仓库下, 新建目录:

```bash
cd ~/code/xxx.github.io
mkdir _sass/
```



然后新建文件:

```bash
vi custom.scss
```

写入如下内容:(内容是从[google webfonts helper (mranftl.com)](https://gwfh.mranftl.com/fonts/jetbrains-mono?subsets=latin)来的)

```scss
/* start custom scss snippet */

/* jetbrains-mono-regular - latin */
@font-face {
  font-family: 'JetBrains Mono';
  font-style: normal;
  font-weight: 400;
  src: url('/assets/fonts/jetbrains-mono-v13-latin-regular.eot'); /* IE9 Compat Modes */
  src: local(''),
  url('/assets/fonts/jetbrains-mono-v13-latin-regular.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
  url('/assets/fonts/jetbrains-mono-v13-latin-regular.woff2') format('woff2'), /* Super Modern Browsers */
  url('/assets/fonts/jetbrains-mono-v13-latin-regular.woff') format('woff'), /* Modern Browsers */
  url('/assets/fonts/jetbrains-mono-v13-latin-regular.ttf') format('truetype'), /* Safari, Android, iOS */
  url('/assets/fonts/jetbrains-mono-v13-latin-regular.svg#JetBrainsMono') format('svg'); /* Legacy iOS */
}

body {
  /* 更改正文字体 */
  font-family: 'JetBrains Mono', Times, Menlo, Monaco, Consolas, Andale Mono, lucida console, Courier New, monospace;
  font-size: 1.2rem;
}

code {
  /* 更改code字体 */
  font-family: 'JetBrains Mono', Times, Menlo, Monaco, Consolas, Andale Mono, lucida console, Courier New, monospace;
  font-size: 1.05rem;
}

/* end custom scss snippet */
```

然后从上面提到的网站[google webfonts helper (mranftl.com)](https://gwfh.mranftl.com/fonts/jetbrains-mono?subsets=latin)下载字体, 解压到指定目录, 这里就是`/assets/fonts`目录了, 注意不是系统根目录, 而是项目的根目录. 



# 本地测试

```bash
bundle exec jekyll serve
```

实际效果的话, 可以看我的主页了:

[Home - Zorch's Blog (zorchp.github.io)](https://zorchp.github.io/);

