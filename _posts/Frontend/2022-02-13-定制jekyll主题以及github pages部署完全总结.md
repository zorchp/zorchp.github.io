---
categories: [Frontend]
tags: [Frontend HTML]
---



# 写在前面

去年就已经开始折腾了jekyll+GitHub Pages的个人站点搭建, 一直以来的想法是自己从零开始进行前端网页的配置, 出发点是好的, 但是我发现最近已经没有时间让我折腾这些了.

恰好前阶段看到网上有人使用jekyll的主题进行博客的配置, 正好省去了自己写css的复杂手续. 下面来看看如何一步步使用主题进行配置, 以及一些实现的小细节, 希望能帮到准备采用jekyll/GitHub pages进行博客搭建的你~



>   虽然依旧走了很多弯路, 但是已经逐渐熟悉了jekyll主页的配置方法. 真是应了那句老话, "纸上谈来终觉浅, 绝知此事要躬行"..



本文不列出具体的配置方法, 具体方法都在对应的参考文献中, 非常详细. 

# 主题的搭建与配置(通过`gem`)

这里我选择了jekyll-TeXt-theme这个主题, 主要是从这篇博客[^1]中获得了灵感, (这是一款低代码的主题), 话不多数, 当然是先找这个主题的官方文档[^2] (这个主题项目还是一位国内开发者贡献的, 在github上有2k+的star)



接下来就是一步一步顺着文档的思路往下走, 这里我想体验一下采用`ruby`的`gem`进行编译和发布的方法, 感觉实现起来不算难, 但是这却成了我折腾到晚上三点的一大绊脚石...

下面主要说通过`gem`以及`bundle`的方式进行主题配置与发布的方法. 

看过我之前文章的话, 配置这个主题应该就很简单了, 需要注意的一点就是最后关于主题的选择方面, 直接通过官方文档中的改写`_config.yml_`文件的方法并不成功, 每次都会显示github action 编译失败(但是在本地的执行不会出现问题), 总是提示找不到主题, 我再三确认, 往上各种找解决方案都是不行.. 最后我通过修改主题为远程主题成功解决了这个问题.

这里先修改`_config.yml`文件, 

```yaml
## !USE TEXT THEME
# theme: jekyll-text-theme # Gem-based Jekyll Themes
remote_theme: kitian616/jekyll-TeXt-theme # Jekyll Remote Theme, see https://github.com/benbalter/jekyll-remote-theme for more information.
```

最后加上一行:(提示使用远程主题插件)

```yaml
plugins:
  - jekyll-feed
  - jekyll-paginate
  - jekyll-sitemap
  - jemoji
  - jekyll-remote-theme # 添加这一行
```



这样配置的话还需要在`gemfile`里面加上对应的插件, 具体gemfile如下:

```ruby
source "https://rubygems.org"

# gem "jekyll-text-theme", path: "../"
gem "jekyll-text-theme"

gem "tzinfo-data"
gem "wdm", "~> 0.1.0" if Gem.win_platform?

gem "webrick", "~> 1.7"
gem "jekyll-remote-theme"

```

改好之后先在同级目录下执行

```bash
bundle install --path vendor/bundle
```

然后就能通过

```bash
bundle exec jekyll serve
```

运行起本地jekyll服务, 在浏览器输入`localhost:4000`就能看到自己的站点了.



# 给网页添加图标

终于搭建好了网站并发布在了github上, 但是这时候却出现了一个小小的问题, 网页标签页左边的小图标不见了, 取而代之的是一个默认的图标.. 这让有强迫症的我十分不爽, 于是接下来我们继续研究如何添加图标. 

同样地, 我们先进入官方文档[^3]找找, 在这里面还真有很多有价值的信息~

大致配置方法就是先进入一个生成ico的网站([RealFaviconGenerator](https://realfavicongenerator.net/)), 然后新建`_includes/head/favicon.html`文件, 里面写入

```html
<!-- start favicons snippet, use https://realfavicongenerator.net/ -->
<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16x16.png">
<link rel="manifest" href="/assets/site.webmanifest">
<link rel="mask-icon" href="/assets/safari-pinned-tab.svg" color="#5bbad5">

<!-- 下面两行用于生成主页标签页以及子网页标签页上面的小图标 -->
<link rel="shortcut icon" href="/assets/favicon.ico" type="image/x-icon"/>
<link rel="bookmark" href="/assets/favicon.ico"/>

<meta name="msapplication-TileColor" content="#da532c">
<meta name="theme-color" content="#ffffff">
<!-- end favicons snippet -->
```

注意这里我在博客站点的根目录新建了一个`src/`目录, 在里面存放了有上述网站生成的所有icon文件(png,svg等). 



# 一点小问题

页面中每次都要在`yaml`头部中添加作者信息, 而不能每次默认添加. 

解决方案是修改`_config.yml`配置文件, 如下:

```yaml
defaults:
  - scope:
      path: ""
      type: posts
    values:
      layout: article
      author: zorchp # 添加这一行
      sharing: true
      license: true
      aside:
        toc: true
      show_edit_on_github: true
      show_subscribe: true
      pageview: true
```

在本地预览的时候需要重启一下本地服务, 才能刷新该配置文件的更改.

# 关于数学公式

对于数学公式的支持来自`mathjax`, 这款渲染引擎可以对整篇文章进行公式渲染(参考了博客[^7], 但是美中不足的一点就是其在行内公式中反斜杠仍然表示转义字符, 这就使内公式中使用诸如`\\`这样的字符的话, 其HTML页面就只会显示一个`\`, 这个问题现在也没有得到解决, 只能采用折中办法, 即采用`\\\\`来表示换行. 当然, 不在行内公式中写矩阵之类的大符号其实也是一个办法. 



>   其实不仅是在数学行内公式中, 对于一般的md文件, 如果写入字符`|`, 其渲染引擎会将其自动识别为表格分隔符, 要解决这个问题只需在`|`前面加上一个`\`.



另外, 这个主题的数学支持还有一个问题, 就是行间公式和文字之间一定要加上**空行**, 如果不加就仍然显示为行内公式..

# 从github迁移镜像到gitee

又是很大的一块内容.. 这里主要的技术支持是`GitHub Actions`, 以及`gitee pages`.

这里我主要参考了[^4], 里面的方法真的是非常详细, 但是最后我还是没有采用这个方法, 有以下两个原因:

1.   这个action的作用是将github所有的库都同步到gitee的, 但是由于github pages的库名称是`xxx.github.io`, 而gitee的是与用户名同名的仓库, 这就导致其同步之后不能达到完全自动化的目的. 
2.   之后推出新版本能够通过构建两个仓库之间的mapping来实现不同名称仓库的同步, 但是新的问题又出现了, gitee pages在同步之后不能自动更新页面, 反而还得自己手动进入`服务`-> `gitee pages`->点击`更新`才行, 这就是个很大的麻烦事了. 

遇到了这样的问题, 当然是接着寻求搜索引擎的帮助. 

一开始看到的一些网上的方法, 大多采用的是一个名为[puppeteer](https://github.com/puppeteer/puppeteer)的前端自动化模块, 但是这样的方法还不是很方便, 毕竟网页结构发生变化的话又要重新debug, 随后在一篇文章的评论下面看到了一个github项目, 名为`gitee-pages-action`[^6], 通过其官方readme文件, 一步一步配置, 我就完成了博客同步的最后一步了, 即镜像同步到gitee并更新gitee pages. 

具体的方法请见[^6]或者action主页[^8].

这个方法虽然是通过模拟登陆的方式进行更新的, 但是也已经相当好用了, 成功更新之后会有gitee公众号的登陆提示. 在提交之后会进行事件触发, 然后进行同步更新, 在此期间(大约2分钟)gitee的站点会显示404.

# 文件结构

(这里是上传github仓库的文件结构,不是本地配置的)

```c
.
├── .github
│   └── workflows
│       └── gitee-mirror-pages.yml // 配置actions
├── 404.html // 404时候显示的页面
├── Gemfile // 用于安装gem的配置文件
├── _config.yml // 主配置文件
├── _data //一些配置文件
│   └── locale.yml 
│   └── ...
├── _includes // 这里可以修改网页结构
│   └── head
│       └── favicon.html  // 用于修改图标的显示
├── _posts // 博客的Markdown源文件存放目录
│   └── ...
├── src // 博客的图标,音频,图片等资源文件
│   └── ...
├── about.md // `关于`页面
├── archive.html // 归档页
└── index.html // 站点主页
```



# 最后的总结

经过了差不多一个礼拜的各种折腾, 我终于完美地实现了博客的搭建配置与同步, 即实现了如下的功能: 

1.   通过`gem`部署github pages, 采用jekyll的主题;
2.   (在原有的TeXt主题的基础上, 进行了一些小的修改);
3.   实现了github pages到gitee pages的同步推送与刷新;

为了完成个人站点的配置, 我经历了下面的几个阶段:

从一开始的想要自己从零开始配置博客主题, 到开始使用jekyll的官方主题, 在配置过程中采用了轻量化的部署方式(采用ruby gem), 但是这也花费了不少时间, 最后才用**远程主题**的方式成功build了github pages. 当然, 这其中也包括很多小细节的实现, 如文件目录的写法, 网页标签页的图标显示等.

后来进入博客的过程中发现github的页面速度有点慢, 于是我想通过gitee的同步来加速, 这里用到了github actions的技术(依旧, 从直接导入, 慢慢转变成指定映射关系之后进行的同步, 省去了很大的功夫). 

然后因为推送到gitee的gitee pages没办法自动同步(只能每次推送之后手动点击更新, 自动更新是企业版的功能), 就去寻找网上大佬们的解决方案, 一开始看到的是通过`js`脚本的方式每次提交之后就进行点击更新(这个方法可以, 但是稳定性会差点), 后来我开始采用gitee-pages-actions的方法(也是github上面的一个开源项目, 本质上还是github actions), 一点一点完善了自己的博客. 

>   gitee pages在页面渲染方面还是不如github pages的, 一些HTML语法就不能正常显示(如图片).



最后, 引用一篇博客[^4]中提到的: 

>   通过发现问题也借此了解了很多知识，github竟然还有Action这么神奇的功能，感觉很有趣。回想起之前只会git clone就太狭隘了。有时间还是要多多了解这些东西，以及背后的原理。任何事物的出现和发展都是有其必然原因和规律。就像伟大的git诞生一样。（这样说突然想学习一下程序的历史，给自己挖个坑有空了解一下，也可以用自己的语言写一篇历史故事，感觉会蛮有趣。 - - ）
>
>   一个产品的本质就是有需求才会推动实现，而为了实现需要尝试很多方法，学习很多知识。
>
>   我料想，人生也应如是。

```不断突破不断超越, 这才是人生的意义所在吧. ```

希望大家在看到这篇文章后也能配置自己喜欢的个人站点, 技术之路永不止步~

# 主要参考

[^1]:[我的Jekyll博客 \| 开放笔记 (goooooouwa.fun)](https://goooooouwa.fun/productivity/2021/03/29/blog-setup.html#博客配置一览);
[^2]:[快速开始 - TeXt Theme (tianqi.name)](https://tianqi.name/jekyll-TeXt-theme/docs/zh/quick-start);
[^3]:[Logo 和 Favicon - TeXt Theme (tianqi.name)](https://tianqi.name/jekyll-TeXt-theme/docs/zh/logo-and-favicon);

[^4]: [github博客自动同步到gitee（保姆级教程）_李梨同学的博客-CSDN博客_github同步到gitee](https://blog.csdn.net/outman_1921/article/details/115454572?spm=1001.2014.3001.5506);
[^5]:[巧用Github Action同步代码到Gitee \| Yikun](https://yikun.github.io/2020/01/17/巧用Github-Action同步代码到Gitee/);
[^6]:[yanglbme/gitee-pages-action: 🤖 Auto Deploy Gitee Pages With GitHub Actions \| 无须人为干预，由 GitHub Actions 自动部署 Gitee Pages](https://github.com/yanglbme/gitee-pages-action);
[^7]:[关于博客搭建过程的一些总结和吐槽 \| Sharzy](https://sharzy.in/posts/2019-08-08-pitfall/);
[^8]:[Gitee Pages Action · Actions · GitHub Marketplace](https://github.com/marketplace/actions/gitee-pages-action); 

