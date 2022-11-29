- 按照惯例，我们学习编程写下的第一个程序是打印 `hello world`。在 Python 中实现这个需求非常简单，只需要一行语句即可实现：
	- ```python
	  print('hello world')
	  ```
	- 我们可以直接在 [[python shell]] 中运行：
	- ![hello world](../assets/image_1669739193303_0.png)
- 还记得我们之前安装过的 `rich` 吗？现在我们来实现一个炫彩款的 `hello world`:
	- ```python
	  from rich import print
	  
	  print('[red]hello[/red] [blue]world[/blue]')
	  ```
	- 运行结果：
	- ![colorful hello world](../assets/image_1669738961075_0.png)
	- 第 1 行我们从 `rich` 中引入了 `print` 函数
	- 第 3 行我们使用 `print` 打印了一个字符串，这个字符串里面使用了一个简单的标记语法给对应的单词添加颜色属性，然后运行程序的时候会显示对应的彩色输出。