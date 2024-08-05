---
categories: [Frontend]
tags: Frontend
---



## 写在前面

在新的 Mac 上配置jekyll博客. 

> M1 芯片 mbp Sonoma14.5
>
> brew 



## 环境配置

```bash
## 新版 Ruby
brew install ruby
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
ruby -v
which gem

# 换源
sudo gem sources --remove https://rubygems.org/
sudo gem sources -a http://gems.ruby-china.com/
gem sources -l


## 安装博客插件
sudo gem install --user-install bundler jekyll
# Fetching bundler-2.5.17.gem
# WARNING:  You don't have /Users/xx/.local/share/gem/ruby/3.3.0/bin in your PATH,
#	  gem executables will not run.
## 加入user的环境变量
echo 'export PATH="$HOME/.local/share/gem/ruby/3.3.0/bin:$PATH"' >> ~/.zshrc # 注意你的版本. 
## 相关依赖
sudo gem install --user-install webrick
bundle config set path 'vendor/bundle'
bundle exec jekyll serve
#enjoy~  http://127.0.0.1:4000/
```

