tags:: built-in, builtins, 类, 基础类型, 基础笔记
alias:: 字符串, 字符串类型, 文本序列类型
title:: str

- ## What
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
- ## Why
	- 我们在写程序的时候可能会进行人机交互，需要用[[字符串]]作为提示或者展示信息。
	- 文本是我们日常生活中重要的信息载体，**存储和处理**文本是常见的编程需求。
- ## How
	- ### [[字符串的表示方法]]
	- ### [[字符串的操作符]]
	  id:: 635d5ce2-dd4f-4e80-9949-e80563fbf5c4
	- ### [[字符串的方法]]
- ## Exception
	- {{query (and [[exception]] [[str]])}}
	  query-table:: false