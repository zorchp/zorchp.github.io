---

---

## 写在前面







## 网络

上回说到, 代理会被自动导入到 lima 的实例中, 怎么取消这个设置呢?看下面的操作

### 默认配置 yaml

>   [lima/examples/default.yaml at master · lima-vm/lima](https://github.com/lima-vm/lima/blob/master/examples/default.yaml);

```yaml
# Extra environment variables that will be loaded into the VM at start up.
# These variables are consumed by internal init scripts, and also added
# to /etc/environment.
# If you set any of "ftp_proxy", "http_proxy", "https_proxy", or "no_proxy", then
# Lima will automatically set an uppercase variant to the same value as well.
# 🟢 Builtin default: null
# env:
#   KEY: value

# Lima will override the proxy environment variables with values from the current process
# environment (the environment in effect when you run `limactl start`). It will automatically
# replace the strings "localhost" and "127.0.0.1" with the host gateway address from inside
# the VM, so it stays routable. Use of the process environment can be disabled by setting
# propagateProxyEnv to false.
# 🟢 Builtn default: true
propagateProxyEnv: null
```

>   结果这样设置还是没用, 还是老老实实 unset 吧. 
>
>   ```bash
>   unset HTTP_PROXY https_proxy HTTPS_PROXY https_proxy
>   ```
>
>   >   难道文档我理解错了?

### 安装/配置虚拟网络管理

```bash
brew install socket_vmnet
```

配置

```bash
# Set up the sudoers file for launching socket_vmnet from Lima
limactl sudoers >etc_sudoers.d_lima
sudo install -o root etc_sudoers.d_lima /etc/sudoers.d/lima
```

加入环境变量

```bash
echo 'export PATH="/opt/homebrew/opt/socket_vmnet/bin:$PATH"' >> ~/.zshrc
```

看来没啥用

