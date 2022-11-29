note-type:: 基础笔记

- Python 解释器的作用就是把我们用人类可以理解的程序语句转换成机器能够理解的 0 和 1 序列。
  id:: 638615ce-bf68-4ccc-a1c9-dd7bafa2d6f1
- 所以==Python 解释器有点儿像个翻译官==。翻译官可以一句一句翻译（交互式）也可以读取整个文件后一次性翻译（非交互式）。
- 我们使用 [[文本编辑工具]] 编写程序语句，Python 解释器把我们写好的程序解释成计算机能够执行的二进制形式。
- 常用的 Python 解释器有：
	- **CPython：**最广泛使用的 Python 解释器，使用 C 语言实现的 Python 解释器，通常说的 Python 默认就是指 CPython，我们将要安装和学习的也是 CPython。
	- **PyPy：**PyPy 是一种 Python 编程语言的实现，可用于替代 CPython。PyPy 通常运行得比 CPython 更快，大多数情况下与 CPython 兼容性良好。
	- **Jython：**使用 Java 实现的 Python 解释器，直接把 Python 代码编译成 Java 字节码执行。
	- **IronPython：**IronPython 是 Python 解释器的开源实现，运行在微软 .net 平台上，可以直接把 Python 代码编译成 .net 的字节码。
-