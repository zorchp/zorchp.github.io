---
categories: [Tips]
tags: MATLAB Windows MacOS Tips
---

# 写在前面

11月的最后一天了, 总结一下支持MATLAB的一个jupyter的插件, 有了这个你就可以在`jupyter notebook`或者`jupyter lab`上面使用MATLAB语句了, 还是很不错的, 虽然我安装了好久......

下面来说一下我在我的电脑以及朋友的电脑(Win11)上面安装这个插件的具体方法. 环境配置如下:

>   MacOS 12.6 arm64 M1
>   MATLAB 2022a update 1
>   Python3.8 with ibrew(Intel brew by Rosetta2)

以及:

>   Windows11 amd64
>   MATLAB 2017a
>   Python3.5 with mini-conda

主要的安装方法我参考了MATLAB-proxy的GitHub主页[^1],(用的人真的少, 所以支持也不算很好, 比较慢), 哈佛的课程主页[^2], 以及MATLAB官方answer[^3], 最后给出我之前配置Intel brew的链接[^4],(下面简称`ibrew`).



# Win11安装MATLAB-jupyter

这里还是走了一些弯路的, 因为Win11中已经安装的MATLAB版本是2017a, 应该是最后一个支持jupyter插件的MATLAB版本了, 我一开始用的是之前电脑里面就有的Python3.9, 但是后来发现MATLAB里面的Python engine只支持2.6, 2.7, 3.5这三个Python版本, 没办法, 那就用Conda来安装一个Python3.5吧..

先从官网下载最新版miniconda(至于Python版本并不重要, 直接用3.9即可), 然后一路确定安装即可. 

>   需要注意的是你的电脑中如果已经存在Python或者不想让Conda成为默认的Python环境的话, 一定要取消勾选安装前的最后一步, 有红色字体提示.

安装完之后, 创建Python3.5虚拟环境, 直接在Conda的prompt(cmd/powershell都可以)中输入

```python
conda create -n py35 python=3.5
```

>   如果你的MATLAB是很新的版本(2017a往后), 那么用Python3.8或许也可以, 这里没有测试过(因为MATLAB安装一次实在是太久了)

然后进入虚拟环境, 输入:

```python
conda activate py35
```

切换到MATLAB的安装目录:(下面均在powershell中操作)

```powershell
# 切换盘符
d:
# 切换到MATLAB目录
cd d:\matlab2017a\extern\engines\python
python setup.py install
```

安装完成之后就可以发现目录下多了一个`dist`文件夹, 这就是MATLAB提供的Python接口文件, 相当于一个Python的包, 只不过是在MATLAB的目录下.

这时候仍然在prompt下, 安装`matlab_kernel`:

```bash
pip install matlab_kernel
python -m matlab_kernel install
```

安装之后可以通过下面的命令查看一下引擎的支持情况:

```python
jupyter kernelspec list
```

最后在虚拟环境中安装`jupyter`, (需要注意, python3.5不支持jupyter lab, 所以这里只能以notebook为例了)

```python
pip install jupyter
```

>   安装完成之后, 如果需要使用`jupyter lab`, 那就还需要安装一下MATLAB-proxy插件(**前提是你的MATLAB版本高于2017a**)
>
>   这个插件的安装首先需要node.js环境(直接官网下载安装即可, 需要最后勾选添加到环境变量)
>
>   设置一下国内镜像:
>
>   ```powershell
>   npm config set registry=https://registry.npmmirror.com
>   ```
>
>   下面安装这个插件:(参考GitHub主页[^1])
>
>   ```python
>   python -m pip install jupyter-matlab-proxy
>   ```
>
>   然后:
>
>   ```bash
>   python -m pip install jupyterlab
>   ```
>
>   最后安装jupyterlab的扩展插件:
>
>   ```python
>   jupyter labextension install @jupyterlab/server-proxy
>   ```
>
>   安完之后就可以用jupyter lab了. 

使用MATLAB2017a可以用jupyter插件, 但是第一次启动可能很慢(可能是电脑的问题), 建议还是尽量用高一些版本的MATLAB. 

使用方法的话, 大家应该都轻车熟路了:

```bash
# For Jupyter Notebook
jupyter notebook

# For Jupyter Lab
jupyter lab 
```

jupyter lab的效果见下[^1]:(注意默认内核仍为Python, 需要替换成MATLAB, 不是MATLAB(connection))

![](https://github.com/mathworks/jupyter-matlab-proxy/raw/main/img/combined_launchers.png)

当然, 使用jupyter lab的前提是你有MATLAB正版授权, 因为之后会需要提供注册账户. (这里建议使用pojie的朋友用notebook)

# MacOS(M1)安装MATLAB-jupyter

这里主要参考了一个回答[^3], 专门解决Mac M1的MATLAB问题, 主要技术点就是通过Rosetta2转译的brew安装Python, 然后剩下的操作都在该Python下进行(如果不这样的话会提示架构不同, 原因是MATLAB现在还不是原生支持M1芯片的, 所以对应的Python插件需要使用Rosetta2安装转译版). 关于安装ibrew的方法, 可以看我之前的文章[^4].

首先安装Python:

```bash
ibrew install python@3.8
```

这里Python默认安装在`/usr/local/bin`下, 名为`python3.8`, (前提是添加了`/usr/local/bin`环境变量)

然后到MATLAB的安装目录:

```bash
cd /Applications/MATLAB_R2022a.app/extern/engines/python
python3.8 setup.py install
```

安装完成后, 再通过该Python安装一些包:

```bash
python3.8 -m pip install matlab_kernel
python3.8 -m matlab_kernel install
python3.8 -m pip install jupyter
```

最后:

```bash
python3.8 -m  jupyter notebook
```

效果如下:

<img src="https://s2.loli.net/2022/11/30/mTpC5u7jaMBfNSi.gif" alt="bb" style="zoom:33%;" />

如果想使用jupyterlab, 仍然需要通过win的那套方法安装jupyterlab-proxy-Server, 下面给出命令:

```bash
python3.8 -m pip install jupyter-matlab-proxy
python3.8 -m pip install jupyterlab
jupyter labextension install @jupyterlab/server-proxy
```

效果:(登录后)

![1](https://s2.loli.net/2022/11/30/hxEm1RnHQ6FXjKA.png)





# ref

[^1]:[mathworks/jupyter-matlab-proxy: MATLAB Integration for Jupyter (github.com)](https://github.com/mathworks/jupyter-matlab-proxy);
[^2]:[Install Jupyter-MATLAB — AM111 0.1 documentation](https://am111.readthedocs.io/en/latest/jmatlab_install.html);
[^3]:[Install Matlab engine for Python on MacBook M1 - MATLAB Answers - MATLAB Central (mathworks.cn)](https://ww2.mathworks.cn/matlabcentral/answers/1735700-install-matlab-engine-for-python-on-macbook-m1);
[^4]:[m1 MBA配置Homebrew环境+国内源配置\_zorchp的博客-CSDN博客\_brew查看源](https://zorchp.blog.csdn.net/article/details/112435816);