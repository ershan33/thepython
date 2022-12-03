tags:: 基础笔记
title:: Python Shell

- ## What
	- > It’s an [[interactive environment]] where you [[type]] some [[Python]] code and press ENTER, and [[Python]] shows you the result.
	- 交互式的 [[Python]] 编程环境，输入 [[Python]] 语句按下回车，立刻就可以得到计算的结果。
## Why
	- 方便学习，可以快速的对新的知识点进行试验。但是不太好用，推荐安装使用 [[IPython]]。
## How
	- 安装好 [[Python]] 以后（确保 [[python]] 在 [[环境变量]] 中），使用 [[cmd]] 输入 [[python]] 即可。
	- 或者在桌面找到 [[idle]] 的图标（使用开始菜单搜索 [[idle]]）也可以，点击打开即可。
	- 当执行 [[简单语句]] [[simple statement]] 时，输入一行语句按下回车后会马上执行：
		- ```python
		  >>> age = 10
		  >>> age
		  10
		  >>> print('hello')
		  hello
		  >>> age = 10; name = 'ershan'
		  >>> age, name
		  (10, 'ershan')
		  ```
	- 当执行 [[复合语句]] 时，需要输入连续的两次回车才会执行：
		- ```python
		  >>> for i in range(3):
		  ...     print(i)
		  ...
		  0
		  1
		  2
		  ```
		- 在交互时环境中`>>>`被称为 [[提示符]]，提示用户后面可以进行输入。`...`表示当前行之后还有后续语句，除非用户输入两次连续的回车。
- ## 常见 [[exception]]
	- 在 [[交互式环境]] 下编写 [[python 的复合语句]] 忘记 [[缩进]] 将会造 [[缩进错误]]。#IndentationError #初学者避坑指南
		- ```python
		  >>> for i in range(3):
		  ... print(i)
		    File "<stdin>", line 2
		      print(i)
		      ^
		  IndentationError: expected an indented block
		  ```
	- 在 [[交互式环境]] 下一次执行多个语句将会造成 [[语法错误]]。#SyntaxError #初学者避坑指南
		- ```python
		  >>> for i in range(3):
		  ...     print(i)
		  ... print('end')
		    File "<stdin>", line 3
		      print('end')
		      ^
		  SyntaxError: invalid syntax
		  ```
-