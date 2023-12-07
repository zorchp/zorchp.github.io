---

---



## conda常用命令

下面给出一些conda管理的常用命令:

-   刷新镜像缓存`conda clean -i`; (i表示索引)

-   更新conda: `conda update -n base -c defaults conda`;

    或者更新全部: `conda update --all`.

    >   注意, 如果提示`conda`有更新却无法更新, 可以用Install指定最新版本的方法完成更新. 
    >
    >   或者在执行 `conda update --all` 时候指定 `-c conda-forge` 

-   删除虚拟环境: `conda env remove --name your_env_name`;

-   查看虚拟环境:`conda info -e`;

-   创建虚拟环境: `conda create -n py39 python==3.9`;

-   查看conda的镜像配置: `conda info`;

-   激活环境: `conda activate tf27`;

-   取消激活: `conda deactivate`;

-   查看版本: `conda -V` 或者`conda --version`;

-   删除缓存(以及下载好的包文件, 不会删除已安装的包): `conda clean --all`.

## 配合zshrc

```bash
####  python  and conda  ###
alias ipy=ipython
alias py=python
alias de='conda deactivate'
alias py3x='conda activate py3x'
alias py3xi='conda activate py3xi'

```

## 镜像

### Condarc

```yaml
channels:
  - defaults
show_channel_urls: true
auto_activate_base: false
ssl-verify: false
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  deepmodeling: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/

```

### pypi.conf

```python
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

等价于在 `~/.config/pip/pip.conf` 文件写入

```yaml
# ==> cat .config/pip/pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

