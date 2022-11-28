- #literal #[[string literal]]
- 使用单引号表示[[字符串]]：`'hello'`
- 使用双引号表示[[字符串]]：`"world"`
- 使用三个单引号表示[[字符串]]：#三引号字符串
	- ```python
	  '''this is a string'''
	  
	  '''this a very
	  very long string
	  it can have several lines.'''
	  ```
- 用三个双引号也可以创建[[字符串]]：#三引号字符串
	- ```python
	  """another string"""
	  
	  """Another
	  string with
	  several lines."""
	  ```
- 使用**单引号**表示的[[字符串]]中出现的**单引号**需要被 [[转义]] ：
	- ```python
	  >>> 'i\'m fine'
	  "i'm fine"
	  ```
	- [[Python]]中使用`\`作为[[转义字符]]，例如`\'`表示字符`'`而不是包裹在[[字符串]]起止两端的`'`
	- {{embed ((635d2344-fe09-4a23-93d1-d3a3ee09ea69))}}
- 使用双引号表示[[字符串]]时也需要被 [[转义]] ：
	- ```python
	  >>> "this is a \"sample\""
	  'this is a "sample"'
	  ```
	- {{embed ((635d2344-a289-4fb1-a080-746773231d9c))}}
- 使用`f`开头创建的[[字符串]]被称为[[f-字符串]]（[[f-string]]）
- 使用`r`开头表示的[[字符串]]被称为[[原始字符串]]（[[raw string]]）
-