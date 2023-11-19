---

---



# 写在前面

通过 ghidra 工具, 但是只能用命令行启动, 不太舒服, 写个脚本生成 MacOS 的 app 格式并导入启动台. 

不算复杂, 主要是解析包的一些元信息还有裁剪软件图标(通过 MacOS 自带的 API)

# 脚本



<script src="https://gist.github.com/zorchp/2f5cba673d7d4e92259f286cdc2174da.js"></script>

可以放在任意位置, 执行之后应该就会出现火龙的标志了:

<img src="../../../../../Desktop/%E6%88%AA%E5%B1%8F2023-11-18%2010.04.57.jpg" alt="截屏2023-11-18 10.04.57" style="zoom:50%;" />