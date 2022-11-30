- {{embed [[pip]]}}
- 安装好 Python 以后可以用下面的方法确认你的 `pip` 是正常工作的：
	- ```sh
	  > pip --version  # linux example
	  pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
	  
	  > pip --version  # windows example
	  pip 21.2.4 from C:\Program Files\Python310\lib\site-packages\pip (python 3.10)
	  ```
- 接下来我们使用 `pip` 安装一个第三方库 [[rich]]:
	- ```sh
	  > pip install rich
	  ```
- 可以通过下面的方式验证一个库是否安装成果了：
	- ```sh
	  > python -c "import rich"
	  ```
	- 如果按下回车运行没有任何反应则说明安装成功了。
	- 如果安装失败或者尚未安装会显示如下内容：
	- ```sh
	  > python -c "import notexists"
	  Traceback (most recent call last):
	    File "<string>", line 1, in <module>
	  ModuleNotFoundError: No module named 'notexists'
	  ```
- LATER 整理有关 `pip` 环境变量缺失引发的错误