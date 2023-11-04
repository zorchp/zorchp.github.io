---
tags: Java Vim
categories: Java
---



# 写在前面

秋招基本上结束了, C++算是告一段落, 但是学习之路才刚刚开始. 

下面写一下 Nvim 上 Java 开发的一些基本配置, 还是延续了以往的轻量级开发环境搭建方法, Nvim 的配置可以看我之前的文章.

>   光会 C++不行, 后端语言还得看 Java/Go

下面的配置主要针对 Java 开发的代码补全, 代码格式化等操作, 用到的插件是 

-   clang-format(没错, 这个万能插件可以格式化 Java)
-   nvim-jdtls(相当于是对 eclipse-jdtls 的一层封装, 比较好用的, 之所以不用 java-language-server 是因为这个插件的维护还是差点意思)

参考了 GitHub 的一些文档:

-   [mfussenegger/nvim-jdtls: Extensions for the built-in LSP support in Neovim for eclipse.jdt.ls](https://github.com/mfussenegger/nvim-jdtls);
-   [eclipse-jdtls/eclipse.jdt.ls: Java language server](https://github.com/eclipse-jdtls/eclipse.jdt.ls#installation);

# 安装 jdtls

不能通过 Mason 安装 jdtls, 只能自己下载压缩包, 因为通过 mason 安装的 jdtls 只有可执行文件而没有 jar 等配置包.

>   用 brew 可以安装, 配置包在 libexec 内

首先下载压缩包, 这里就下载最新版了:

-   [Project download area | The Eclipse Foundation](https://www.eclipse.org/downloads/download.php?file=/jdtls/snapshots/jdt-language-server-latest.tar.gz);

然后解压, 随便找一个目录

我这里的目录在:

```c
 ==> pwd
/Users/xxx/code/java_code/tools/jdtls
  √  ~/code/java_code/tools/jdtls
 ==> ls
bin                 config_mac          config_ss_linux_arm config_ss_win       log_data
config_linux        config_mac_arm      config_ss_mac       config_win          plugins
config_linux_arm    config_ss_linux     config_ss_mac_arm   features
```

然后就是配置**代码检查**插件了, 这里有几个坑点:

-   主要修改的几个路径

    >   -- 💀 标记出来的

    必须用绝对路径, 使用`$HOME/`都不行

-   data 路径可以指定在 jdtls 的安装路径下, 但是像这样的缓存最好每一个项目独立一份比较好, 我这里是在安装路径下 mkdir 了`log_data`目录

-   



# 代码检查插件

配置:

plugins:

```lua
lang["mfussenegger/nvim-jdtls"] = {
	lazy = true,
	ft = "java",
	config = require("lang.nvim-jdtls"),
}
```

config:

```lua
return function()
	-- See `:help vim.lsp.start_client` for an overview of the supported `config` options.
	local config = {
		-- The command that starts the language server
		-- See: https://github.com/eclipse/eclipse.jdt.ls#running-from-the-command-line
		cmd = {

			-- 💀
			"java", -- or '/path/to/java17_or_newer/bin/java'
			-- depends on if `java` is in your $PATH env variable and if it points to the right version.

			"-Declipse.application=org.eclipse.jdt.ls.core.id1",
			"-Dosgi.bundles.defaultStartLevel=4",
			"-Declipse.product=org.eclipse.jdt.ls.core.product",
			"-Dlog.protocol=true",
			"-Dlog.level=ALL",
			"-Xmx1g",
			"--add-modules=ALL-SYSTEM",
			"--add-opens",
			"java.base/java.util=ALL-UNNAMED",
			"--add-opens",
			"java.base/java.lang=ALL-UNNAMED",

			-- 💀
			"-jar",
			"/Users/xxx/code/java_code/tools/jdtls/plugins/org.eclipse.equinox.launcher_1.6.500.v20230717-2134.jar",
			-- "/path/to/jdtls_install_location/plugins/org.eclipse.equinox.launcher_VERSION_NUMBER.jar",
			-- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                                       ^^^^^^^^^^^^^^
			-- Must point to the                                                     Change this to
			-- eclipse.jdt.ls installation                                           the actual version

			-- 💀
			"-configuration",
			"/Users/xxx/code/java_code/tools/jdtls/config_mac",
			-- "/path/to/jdtls_install_location/config_SYSTEM",
			-- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        ^^^^^^
			-- Must point to the                      Change to one of `linux`, `win` or `mac`
			-- eclipse.jdt.ls installation            Depending on your system.

			-- 💀
			-- See `data directory configuration` section in the README
			"-data",
			"/Users/xxx/code/java_code/tools/jdtls/log_data/",
			-- "/path/to/unique/per/project/workspace/folder",
		},

		-- 💀
		-- This is the default if not provided, you can remove it. Or adjust as needed.
		-- One dedicated LSP server & client will be started per unique root_dir

		root_dir = require("jdtls.setup").find_root({ ".git", "mvnw", "gradlew" }),

		-- Here you can configure eclipse.jdt.ls specific settings
		-- See https://github.com/eclipse/eclipse.jdt.ls/wiki/Running-the-JAVA-LS-server-from-the-command-line#initialize-request
		-- for a list of options
		settings = {
			java = {},
		},

		-- Language server `initializationOptions`
		-- You need to extend the `bundles` with paths to jar files
		-- if you want to use additional eclipse.jdt.ls plugins.
		--
		-- See https://github.com/mfussenegger/nvim-jdtls#java-debug-installation
		--
		-- If you don't plan on using the debugger or other eclipse.jdt.ls plugins you can remove this
		init_options = {
			bundles = {},
		},
	}
	-- This starts a new client & server,
	-- or attaches to an existing client & server depending on the `root_dir`.
	require("jdtls").start_or_attach(config)
end
```





# 格式化插件

改一下clang-format 的配置, 加上支持 Java 即可, 注意 config 也有相应改动

```lua
return function()
	local null_ls = require("null-ls")
	local btns = null_ls.builtins

	-- Please set additional flags for the supported servers here
	-- Don't specify any config here if you are using the default one.
	local sources = {
		btns.formatting.clang_format.with({
			filetypes = { "c", "cpp", "java" }, -- change this
			extra_args = require("completion.formatters.clang_format"),
		}),

```



针对单项目设置: `.clang-format` 文件

```yaml
BasedOnStyle: Google
---
Language: Java
IndentWidth: 4
ColumnLimit: 100
BreakStringLiterals: true
BreakAfterJavaFieldAnnotations: false
BraceWrapping:
  AfterCaseLabel: true
  AfterClass: true
  AfterControlStatement: true
  AfterEnum: true
  AfterFunction: true
  AfterNamespace: true
  AfterObjCDeclaration: true
  AfterStruct: true
  AfterUnion: true
  AfterExternBlock: true
  BeforeCatch: true
  BeforeElse: true
  IndentBraces: true
  SplitEmptyFunction: false
  SplitEmptyRecord: false
  SplitEmptyNamespace: false
```

# 使用小结



单文件可以支持, 但是 gradle 项目不能跳转, 很多时候也不能读取其他类, 还是不如 idea 方便的..

针对多文件项目, 我推荐用 NetBeans.
