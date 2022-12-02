- 有时候因为网络问题 `pip` 的下载速度非常缓慢，这个时候我们可以把 `pip` 的下载地址替换成国内的镜像地址。
- ## 常用国内镜像源
	- ### 豆瓣源
		- ```plaintext
		  https://pypi.douban.com/simple/
		  ```
	- ### 阿里源
		- ```plaintext
		  https://mirrors.aliyun.com/pypi/simple/
		  ```
	- ### 清华源
		- ```plaintext
		  https://pypi.tuna.tsinghua.edu.cn/simple
		  ```
- ## 直接使用
	- 可以通过 `-i` 选项直接使用国内镜像：
		- ```sh
		  > pip install -i https://pypi.douban.com/simple/ numpy
		  ```
	- 如果不想每次输入可以把镜像地址写入 `pip` 的配置文件。
- ## 更改 `pip` 镜像源
	- ### Linux
		- 使用如下命令查看 `pip` 配置文件的调试信息
			- ```sh
			  > pip config debug
			  env_var:
			  env:
			  global:
			    /etc/xdg/pip/pip.conf, exists: False
			    /etc/pip.conf, exists: False
			  site:
			    /home/ershan/miniconda3/pip.conf, exists: False
			  user:
			    /home/ershan/.pip/pip.conf, exists: False
			    /home/ershan/.config/pip/pip.conf, exists: False
			  ```
		- 上面几个路径是 `pip` 搜索配置的顺序，用户可以按需创建配置文件，例如在 `user` 的 `$HOME` 目录下面新建文件：
			- ```sh
			  cd ~ && mkdir .pip
			  vim pip.conf # 不熟悉 vim 可以使用 nano pip.conf
			  ```
		- 写入如下内容即可：
			- ```plaintext
			  [global]
			  index-url = https://pypi.douban.com/simple/
			  ```
	- ### Windows
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
		- 找到合适的路径新建文件配置即可：
			- ```bat
			  # 例如 %APPDATA%\pip\pip.ini
			  # %APPDATA% 会展开成 C:\Users\ershan\AppData\Roaming\
			  # content
			  [global]
			  index-url = https://pypi.douban.com/simple/
			  ```
-