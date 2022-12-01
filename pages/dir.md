tags:: builtins, builtin_function_or_method

- ```python
  Docstring:
  dir([object]) -> list of strings
  
  If called without an argument, return the names in the current scope.
  Else, return an alphabetized list of names comprising (some of) the attributes
  of the given object, and of attributes reachable from it.
  If the object supplies a method named __dir__, it will be used; otherwise
  the default dir() logic is used and returns:
    for a module object: the module's attributes.
    for a class object:  its attributes, and recursively the attributes
      of its bases.
    for any other object: its attributes, its class's attributes, and
      recursively the attributes of its class's base classes.
  Type:      builtin_function_or_method
  ```
-
- `dir` 用于查看当前[[作用域]]（scope）下的 [[命名空间]] ，可以接收一个[[参数]]`dir(obj)`，作用是查看指定[[参数]][[对象]]的命名空间。
- 可以通过实现 `__dir__`特殊方法定制调用它时的行为。否则将会使用默认的 `dir()` 调用逻辑：
	- 对于一个[[模块]]对象来说：放回模块的属性。
	- 对于一个[[类]]对象来说：返回类的属性，然后递归获取到的它的基类的属性。
	- 对于任何其它的[[对象]]：放回对象的属性，它所属类的属性，以及递归获取的该类基类的属性。
-
- #例子
	- 查看 `dir` 自身的命名空间：
		- ```python
		  >>> dir(dir)
		  ['__call__', '__class__', '__delattr__',
		   '__dir__', '__doc__', '__eq__', '__format__',
		   '__ge__', '__getattribute__', '__gt__',
		   '__hash__', '__init__', '__init_subclass__',
		   '__le__', '__lt__', '__module__', '__name__',
		   '__ne__', '__new__', '__qualname__', '__reduce__',
		   '__reduce_ex__', '__repr__', '__self__',
		   '__setattr__', '__sizeof__', '__str__',
		   '__subclasshook__', '__text_signature__']
		  ```
	- 查看[[类]]的命名空间：
		- ```python
		  >>> dir(int)
		  ['__abs__', '__add__', '__and__',
		   '__bool__', '__ceil__', '__class__',
		   '__delattr__', '__dir__', '__divmod__',
		   '__doc__', '__eq__', '__float__',
		   '__floor__', '__floordiv__', '__format__',
		   '__ge__', '__getattribute__',
		   '__getnewargs__', '__gt__', '__hash__',
		   '__index__', '__init__', '__init_subclass__',
		   '__int__', '__invert__', '__le__',
		   '__lshift__', '__lt__', '__mod__',
		   '__mul__', '__ne__', '__neg__', '__new__',
		   '__or__', '__pos__', '__pow__', '__radd__',
		   '__rand__', '__rdivmod__', '__reduce__',
		   '__reduce_ex__', '__repr__', '__rfloordiv__',
		   '__rlshift__', '__rmod__', '__rmul__',
		   '__ror__', '__round__', '__rpow__',
		   '__rrshift__', '__rshift__', '__rsub__',
		   '__rtruediv__', '__rxor__', '__setattr__',
		   '__sizeof__', '__str__', '__sub__',
		   '__subclasshook__', '__truediv__',
		   '__trunc__', '__xor__', 'as_integer_ratio',
		   'bit_count', 'bit_length', 'conjugate',
		   'denominator', 'from_bytes', 'imag',
		   'numerator', 'real', 'to_bytes']
		  ```
	- 查看[[对象]]的命名空间：
		- ```python
		  >>> dir('hello world')
		  ['__add__', '__class__', '__contains__',
		   '__delattr__', '__dir__', '__doc__', '__eq__',
		   '__format__', '__ge__', '__getattribute__',
		   '__getitem__', '__getnewargs__', '__gt__',
		   '__hash__', '__init__', '__init_subclass__',
		   '__iter__', '__le__', '__len__', '__lt__',
		   '__mod__', '__mul__', '__ne__', '__new__',
		   '__reduce__', '__reduce_ex__', '__repr__',
		   '__rmod__', '__rmul__', '__setattr__',
		   '__sizeof__', '__str__', '__subclasshook__',
		   'capitalize', 'casefold', 'center', 'count',
		   'encode', 'endswith', 'expandtabs', 'find',
		   'format', 'format_map', 'index', 'isalnum',
		   'isalpha', 'isascii', 'isdecimal', 'isdigit',
		   'isidentifier', 'islower', 'isnumeric',
		   'isprintable', 'isspace', 'istitle', 'isupper',
		   'join', 'ljust', 'lower', 'lstrip', 'maketrans',
		   'partition', 'removeprefix', 'removesuffix',
		   'replace', 'rfind', 'rindex', 'rjust',
		   'rpartition', 'rsplit', 'rstrip', 'split',
		   'splitlines', 'startswith', 'strip',
		   'swapcase', 'title', 'translate', 'upper', 'zfill']
		  ```
	- 其中以双下划线开头结尾的属性和方法称为[[特殊属性]]和[[特殊方法]]。 #定义
-