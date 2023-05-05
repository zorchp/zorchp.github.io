---
categories: [Frontend]
tags: Frontend
---



# 问题描述

最近写关于博客配置的文章中出现了这样一个问题, `如果页面是通过Jekyll引擎进行渲染的, 那么如果在文章中写了Liquid代码, 引擎也会将其解析` 写配置类博客的目的当然是展示代码, 那么如何只展示Liquid代码而并不使引擎解析呢? 



不同于块注释

```html
{{ "{% comment " }}%}
This is a comment in Liquid 
{{ "{% endcomment " }}%}
```



如果写上块注释的话其实Liquid是不会显示的, 要让其完整显示命令语句, 只能进行一种类似于转义的方法. 

之后通过Google我得到了完美的答案, 主要参考了Stack Overflow里面的回答[^1][^2], 下面来详细介绍一下具体的方法与各自的使用场景. 





# 方法一: 针对块

(非常推荐)

```html
{{ "{% raw " }}%}
{{ "{% this " }}%}
{{ "{% endraw " }}%}
```

显示效果:

```html
{% raw  %}
{% this %}
{% endraw  %}
```



# 方法二: 针对行

(较为复杂, 推荐)

```html
{% raw  %}{{ "{% this " }}%}{% endraw  %}
```

显示为

```html
{{ "{% this " }}%}
```

或者

```html
{% raw  %} {{ "{{ this " }}}} {% endraw %}
```

显示为:

```html
{{ "{{ this " }}}}
```

---

当然, 如果需要显示下面的命令: 

```html
{% raw %} {{ "{% this " }}%} {% endraw %}
```

则需要这样来写:

```html
{% raw  %} {{ "{{ " }}"{{ "{% this" }} " }}{{ }}%} {% endraw %}
```

同理, 如果要显示下面的命令:

```html
{% raw %} {{ "{{ this " }}}} {% endraw %}
```

就要这样来写:

```html
{% raw  %}{{ "{{ " }}"{{ "{{ this" }} " }}{{ }}}}{% endraw  %}
```



# 方法三: 使用特殊字符

(需要记忆HTML特殊字符, 不推荐)

代码:

```html
&#123;&#123; this &#125;&#125;
```

显示效果:

&#123;&#123; this &#125;&#125;



代码: 

```html
&#123;% this %&#125;
```

显示效果:

&#123;% this %&#125;



# 方法四: 使用变量

代码:

```html
{% raw %}{% assign var = "{{ sth }}" %} {{ var }}{% endraw %}
```

显示效果: 

```html
{% assign var = "{{ sth }}" %} {{ var }}
```





# 主要参考

[^1]:[How to escape liquid template tags? - Stack Overflow](https://stackoverflow.com/questions/3426182/how-to-escape-liquid-template-tags/13582517#13582517?newreg=ac585e721bad49e8860c8d4c78709404);
[^2]:[Include Jekyll/Liquid code without rendering it - Stack Overflow](https://stackoverflow.com/questions/37688226/include-jekyll-liquid-code-without-rendering-it);
