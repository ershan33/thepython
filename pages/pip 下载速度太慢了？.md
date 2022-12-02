- 有时候因为网络问题 `pip` 的下载速度非常缓慢，这个时候我们可以把 `pip` 的下载地址替换成国内的镜像地址。
- ## 常用国内景象
-
- ## 更改 `pip` 镜像源
	- 使用如下命令查看 `pip` 配置文件的调试信息：
		- ```sh
		  > pip config debug
		  env_var:
		  env:
		  global:
		    C:\ProgramData\pip\pip.ini, exists: False
		  site:
		    C:\Program Files\Python310\pip.ini, exists: False
		  user:
		    C:\Users\ershan\pip\pip.ini, exists: True
		      global.index-url: https://pypi.douban.com/simple/
		    C:\Users\ershan\AppData\Roaming\pip\pip.ini, exists: False
		  ```
	- ### Linux
		- ```sh
		  cd ~ && mkdir .pip
		  vim pip.conf
		  # content
		  # [global]
		  # index-url = https://pypi.douban.com/simple/
		  ```
	- ### Windows
		- ```bat
		  # path is %APPDATA\pip\pip.ini
		  # content
		  # [global]
		  # index-url = https://pypi.douban.com/simple/
		  ```