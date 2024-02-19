---
categories: Tips
tags: Tips Typora activation
---

## 写在前面

最近用 typora 写博客, 突然发现 typora 开始闪退了, ~~难道 TNT 软件被检测了??~~ 更新到最新也不行, 闪退依旧.

正好联想到之前看的一篇关于在 Windows 下伪激活 typora 的文章, ~~本质上是绕过激活检测~~, 反正就是能苟着先苟.

>   [Typora “伪”激活](https://mp.weixin.qq.com/s/XS_1bEbO-HNg2SXYRlP61Q);

这样操作一顿之后, 就不会闪退了, 但是有时候会提示出问题, 不要理会即可. 

## Windows 版怎么激活

>   经测试, 到 2024.2.7, 1.8.10 版可以使用

修改 Typora安装目录`\resources\page-dist\static\js\LicenseIndexchunk.js` （或者在目录中直接搜索`chunk.js` 文件）

```js
#查找
e.hasActivated="true"==e.hasActivated,
#替换为
e.hasActivated="true"=="true",
```

修改Typora 安装目录`\resources\page-dist\license.html`

```html
# 查找
</body></html>
# 替换
</body><script>window.onload=function(){setTimeout(()=>{window.close();},5);}</script></html>
```

修改 Typora 安装目录`\resources\locales\zh-Hans.lproj\Panel.json`

```json
#查找
"UNREGISTERED":"未激活",
#替换
"UNREGISTERED":" ",
```

## macOS 举一反三

>   其实难点在找目录. 

修改 Typora安装目录`/Applications/Typora.app/Contents/Resources/TypeMark/page-dist/static/js/LicenseIndex.180dd4c7.6d698c41.chunk.js` 

```js
#查找
e.hasActivated="true"==e.hasActivated,
#替换为
e.hasActivated="true"=="true",
```

修改Typora 安装目录 `/Applications/Typora.app/Contents/Resources/TypeMark/page-dist/license.html` 

```html
# 查找
</body></html>
# 替换
</body><script>window.onload=function(){setTimeout(()=>{window.close();},5);}</script></html>
```

修改 Typora 安装目录 `/Applications/Typora.app/Contents/Resources/zh-Hans.lproj/Panel.strings` 

```json
#查找
"UNREGISTERED":"未激活",
#替换
"UNREGISTERED":" ",
```

搞定. 
