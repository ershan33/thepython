tags:: python/oop, python/method
alias:: python/静态方法

- ## What
	- 静态方法是定义在类里面但是不和任何对象（类对象和实例对象）绑定的方法。
	- 在python中使用`@staticmethod`定义静态方法。
	- ```python
	  class Dog:
	    @staticmethod
	    def info():
	      return 'dog class'
	  ```
	- ```python
	  >>> d = Dog()
	  >>> type(d.info)
	  <class 'function'>
	  >>> d.info
	  <function Dog.info at 0x7fde580489d0>
	  >>> d.info()
	  'dog class'
	  ```
## Why
	- 静态方法用来表示一个和类有所关联但是又没用使用任何类或者成员属性的方法
## How
-