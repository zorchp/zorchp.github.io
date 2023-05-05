---
categories: [Tips]
tags: Python MacOS
---

# 写在前面

>   好久没写博客, 因为最近一直忙着看Effective系列, 终于告一段落了. 

看到微软出的Visual-chatgpt, 想试试(后来失败了), 在这里记录一下吧.



>   参考:
>
>   1.   [https://github.com/microsoft/visual-chatgpt](https://github.com/microsoft/visual-chatgpt);
>   2.   [Unable to run Visual ChatGPT 4 on Mac : SSLError : SSLCertVerificationError( ](https://github.com/microsoft/visual-chatgpt/issues/246);
>   3.   [https://github.com/microsoft/visual-chatgpt/issues/187](https://github.com/microsoft/visual-chatgpt/issues/187);





# 方法

## MacOS下的准备工作

```bash
# 安装xcode集成
xcode-select --install
# 安装 brew, 用 brew 安装 cmake
brew install cmake
brew install miniforge # Conda
```



## 环境配置

换源: pip以及Conda(不赘述了)

```bash
conda create -n visgpt python=3.8
conda activate visgpt
```

安装包:

```bash
python -m pip install -r requirements.txt
```

改端口, 去掉https验证, 添加全局网络(magic):

```python
# python源码文件中修改

if __name__ == "__main__":
    os.environ["CURL_CA_BUNDLE"] = ""


# 最后一行: 
        # demo.launch(server_name="0.0.0.0", server_port=1015)
        demo.launch(server_name="0.0.0.0", server_port=7868, share=True)

```



## 网络配置

```bash
export https_proxy=http://127.0.0.1:9090
```

magic global, 然后就可以愉快的运行了



## 跑起来

```bash
python visual_chatgpt.py --load ImageCaptioning_cpu,ImageEditing_cpu,Text2Image_cpu
```

首先会下载6GB左右的模型参数, 然后就可以跑模型了

# 各种坑

## 网络

>   SSLError: HTTPSConnectionPool(host='huggingface.co', port=443)

首先当然是网络问题, 使用magic上网之后依然存在, 后来发现只使用`export https_proxy=xxx`即可

## MacOS

训练到结束, 结果直接来一个`zsh bus error`, 实在离谱. 

后来看issue(参考链接3), Mac上确实要多尝试很多次才能跑, 鉴于自己电脑内存不行, 还是算了

# 结论

>   既然用 MacOS 还是别玩深度学习了...

显卡是集显, CPU拉满也还是很慢, 针对m系列芯片做了优化, 问题价钱就太高了..

真的想试试, 感觉可以用Google的TPU或者租GPU的服务器.
