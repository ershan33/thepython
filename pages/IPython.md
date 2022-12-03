- 原生的 [[Python Shell]] 实在太过简陋，并不是学习的好工具。这里推荐大家使用增强版的 IPython。
- ## 安装 IPython
	- 使用 `pip` 直接安装即可：
		- ```sh
		  pip install ipython
		  ```
- ## 使用 IPython
	- 在终端里直接输入 `ipython` 运行即可：
		- ```sh
		  > ipython
		  Python 3.9.13 (main, Oct 13 2022, 21:15:33)
		  Type 'copyright', 'credits' or 'license' for more information
		  IPython 8.6.0 -- An enhanced Interactive Python. Type '?' for help.
		  
		  In [1]:
		  ```
	- ### 获取帮助
		- 在 `ipython` 中可以使用 `?object` 的方式获取 `object` 的帮助文档：
			- ![ipython 获取帮助文档](../assets/ipython_ex1.gif)
		- 使用 `??object` 可以获取更详细的文档
	- ### 执行命令行命令
		- 在 `ipython` 中可以使用 `!command` 的形式运行命令行命令，例如 `!echo`：
			- ```python
			  In [1]: !echo hello
			  hello
			  ```
	- ### 自动补全
		- 可以使用 `tab` 键进行自动补全：
			- ![](../assets/ipython_ex2.gif)
	- ### 获取历史语句
		- 使用 `ctrl + r` 搜索获取历史语句
			- ![获取历史](../assets/ipython_ex3.gif)
	-