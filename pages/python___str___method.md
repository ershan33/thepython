- 在[[Python]]中针对每一种类型特定的操作称为**方法**。举个例子来说，有一个[[字符串]]`'hello world'`，**把这个[[字符串]]里所有的小写字母替换成大写**`'HELLO WORLD'`的形式，这个过程就是一个**操作**。 #python/method
- [[Python]]中的[[字符串]]有许多的方法，完成上述操作的方法就是 `upper` 方法。
- ## 消除
  
  ```python
  # 移除两端空格
  <str> = <str>.strip()
  # 移除两端出现的 <chars>
  <str> = <str>.strip('<chars>')
  ```
  
  还有 `lstrip()`, `rstrip()`。
- ## 切分与拼接
  
  ```python
  # 基于空格把字符串分成不同的部分
  <list> = <str>.split()
  
  # 基于给定的 sep 字符把字符串分成不同部分
  # maxsplit 指定最多切分几次
  <list> = <str>.split(sep=None, maxsplit=-1)
  
  # 把字符串按行切分
  # keepends 是否保留换行符
  # [\n\r\f\v\x1c-\x1e\x85\u2028\u2029] and \r\n.
  <list> = <str>.splitlines(keepends=False)
  
  # 用给定的字符串作为分隔符拼接任意长度的字符串
  <str> = <str>.join(<coll_of_strings>)
  ```
  
  还有 `rsplit()`。
- ## 替换
  
  ```python
  # 用 new 替换 old，最多 count 次
  <str>  = <str>.replace(old, new [, count])
  # 字符串映射，映射表可以用 str.maketrans(<dict>) 生成
  <str>  = <str>.translate(<table>)
  ```
- ## 转换
  id:: 636f3a23-a072-4a64-b6dd-7b42cd86e07f
  
  ```python
  # 把整数转换成字符
  <str> = chr(<int>)
  
  # 把字符转换成整数
  <int> = ord(<str>)
  
  # 把字符串转成数字
  <int> = int(<str>)
  <float> = float(<str>)
  
  # 把数字转换成字符串
  <str> = str(<int>)
  <str> = str(<float>)
  
  # 转换成全大写
  <str> = <str>.upper()
  
  # 转换成全小写
  <str> = <str>.lower()
  
  # 转换成首字母大写
  <str> = <str>.capitalize()
  
  # 转换成（英语）标题
  <str> = <str>.title()
  ```
- ## 查找与索引
  
  ```python
  # 返回第一个匹配位置的起始索引或 -1（没找到）
  <int> = <str>.find(<sub_str>)
  # 和上面类似，只不过找不到抛出 ValueError 的异常
  <int> = <str>.index(<sub_str>)
  ```
  
  还有 `rindex()`, `rfind`。
- ## 格式化
  
  ```python
  # 把字符串在给定长度内居中显示
  # 用 fillchar 填充两端
  str.center(<width>, <fillchar>)
  str.ljust(<width>, <fillchar>)  # 左对齐
  str.rjust(<width>, <fillchar>)  # 右对齐
  
  # 在字符串左边补零，直到字符串达到指定长度
  str.zfill(<width>)
  
  # 格式化
  "{} xxx {}".format(<el1>, <el2>)
  
  # f-string
  f"{el1} xxx {el1}"
  ```
- ## 检查与判断
  
  ```python
  # 检查字符串是否包含子串
  <bool> = <sub_str> in <str>
  
  # 检查字符串是否以给定的一个或一组字符串为开头或结尾
  # 用字符串元组传入一组字符串
  <bool> = <str>.startswith(<sub_str>)
  <bool> = <str>.endswith(<sub_str>)
  <bool> = <str>.isalph() # 检查字符串是否为字母
  <bool> = <str>.isdigit() # 检查字符串是否为数字
  <bool> = <str>.isalnum() # 检查字符串是否为数字和字母
  <bool> = <str>.islower() # 检查字符串是否为小写字母
  <bool> = <str>.isidentifier() # 检查字符串是否为标识符
  <bool> = <str>.isascii() # 检查字符串是否为 ASCII
  <bool> = <str>.isspace() # 检查字符串是否为空格[ \t\n]
  ```
  `isspace()` 检查 `[ \t\n\r\f\v\x1c-\x1f\x85\u2000…]`
  |               | !\#$%… | a-zA-Z | ¼½¾ | ²³¹ | 0-9 |
  | ------------- | ----- | ------ | --- | --- | --- |
  | isprintable() | yes   | yes    | yes | yes | yes |
  | isalnum()     |       | yes    | yes | yes | yes |
  | isnumeric()   |       |        | yes | yes | yes |
  | isdigit()     |       |        |     | yes | yes |
  | isdecimal()   |       |        |     |     | yes |
-