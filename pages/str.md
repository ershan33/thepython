tags:: built-in, builtins, 类, 基础类型, 基础笔记
alias:: 字符串, 字符串类型, 文本序列类型
title:: str

- ## 定义
	- [[字符串]]是[[python]]中用于**存储和处理**文本的基础 [[数据类型]]
	- 可以把 [[字符串]] 理解成我们真实世界中的文字，例如：
		- 今天天气真好（文字） -> "今天天气真好" （ [[字符串]] ）
		- What is your name? （文字）-> 'What is your name?' （单引号也能创建 [[字符串]] ）
	- 我们可以使用[[python/type]]查看[[python]]中 [[字符串]] 的类型：
		- ```python
		  >>> type('app')
		  <class 'str'>
		  >>> type("abc")
		  <class 'str'>
		  >>> type("""a
		  ... b
		  ... c""")
		  <class 'str'>
		  ```
- ## 为什么需要字符串
	- 我们在写程序的时候可能会进行人机交互，需要用[[字符串]]作为提示或者展示信息。
	- 文本是我们日常生活中重要的信息载体，**存储和处理**文本是常见的编程需求。
- ## 如何
	- ### 表示字符串：[[字符串的表示方法]]
	- ### 操作字符串：[[字符串的操作符]]
	  id:: 635d5ce2-dd4f-4e80-9949-e80563fbf5c4
	- ### 使用字符串：[[字符串的方法]]
- ## [[exception]]
	- 使用**中文引号**创建 [[字符串]] 会造成 [[语法错误]] 。#SyntaxError #beginner
	  id:: 6384dc36-19fe-4c08-a7b1-2c2ade9cc85f
		- ```python
		  >>> print(“hello world”)
		  SyntaxError: invalid character '“' (U+201C)
		  ```
	- 在单引号表示的[[字符串]]中使用**未[[转义]]的单引号**会造成 [[语法错误]] 。#SyntaxError #escape #beginner
	  id:: 635d2344-fe09-4a23-93d1-d3a3ee09ea69
		- ```python
		  >>> 'i'm fine'
		    File "<stdin>", line 1
		      'i'm fine'
		         ^
		  SyntaxError: invalid syntax
		  ```
	- 在双引号表示的[[字符串]]中使用**未转义的双引号**会造成[[语法错误]] 。#SyntaxError #escape #beginner
	  id:: 635d2344-a289-4fb1-a080-746773231d9c
		- ```python
		  >>> "a wrong "usage" of string representation"
		    File "<stdin>", line 1
		      "a wrong "usage" of string representation"
		                ^
		  SyntaxError: invalid syntax
		  ```
	- 把[[字符串]]和[[数字]]相加会造成[[类型错误]]。#TypeError #beginner #python/input
	  id:: 635d38de-5a49-4999-9f97-3b2bad3b0670
		- ```python
		  >>> '1' + 1
		  Traceback (most recent call last):
		    File "<stdin>", line 1, in <module>
		  TypeError: can only concatenate str (not "int") to str
		  >>> '1' + 1.1
		  Traceback (most recent call last):
		    File "<stdin>", line 1, in <module>
		  TypeError: can only concatenate str (not "float") to str
		  ```
	- 把[[字符串]]和**非[[整数]]**相乘会造成[[类型错误]]。#typeerror #beginner #python/input
	  id:: 635d3d5f-496d-40c0-ab55-ff95719df531
		- ```python
		  >>> 'a' * '3'
		  Traceback (most recent call last):
		    File "<stdin>", line 1, in <module>
		  TypeError: can't multiply sequence by non-int of type 'str'
		  ```
	-
-