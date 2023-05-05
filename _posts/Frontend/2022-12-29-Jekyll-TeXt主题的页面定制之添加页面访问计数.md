---
categories: [Frontend]
tags: HTML 
---

# 写在前面

突然想起来之前的GitHub Pages博客还没有添加访问量统计, 后来发现可以通过`不蒜子`来设置, 还是集免费的接口, 那当然可以拿来用用了.

官网: [不蒜子 - 极简网页计数器 (ibruce.info)](http://busuanzi.ibruce.info/);

# 方法

由于我之前设置了TeXt主题, 所以需要定制文章页面与index界面的话, 就需要改一下网页的模板, 一开始没找到方法, 后来发现应该在`./_includes/`新建一个文件, 名为`article-footer.html`, 然后复制[jekyll-TeXt-theme/article-footer.html at master · kitian616/jekyll-TeXt-theme (github.com)](https://github.com/kitian616/jekyll-TeXt-theme/blob/master/_includes/article-footer.html);内容进入, 倒数第二行加上:

```html
<script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>

Total <span id="busuanzi_value_site_pv"></span> views.<br />
您是xxx的第<span id="busuanzi_value_site_uv"></span>个小伙伴<br />
<span id="busuanzi_value_page_pv"></span> Hits
```

然后就是`index.html`, 加入上述内容即可, `commit`一下, 刷新页面就可以啦!

显示:

![截屏2022-12-29 13.12.08](https://s2.loli.net/2022/12/29/svXWhS17uKBq3Y2.jpg)