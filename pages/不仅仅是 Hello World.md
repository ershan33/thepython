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
	- 第 1 行我们从 `rich` 中引入了 `print` 函数，在 Python 中一个函数可以被看作一个工具，能够执行特定的功能，例如 [[print]] 函数的作用就是打印给定的内容。
	- 第 3 行我们使用 `print` 打印了一个字符串，这个字符串里面使用了一个简单的标记语法`[red][/red]`给对应的单词添加颜色属性，然后运行程序的时候会显示对应的彩色输出。
- 不过我一直觉得上面的例子不太好，为了能够让你有更多的第一印象，我参照 `C 语言` 的形式改写了上面的例子：
	- ```python
	  # hello_world.py ①
	  from rich import print  # ②
	  
	  
	  def main():  # ③
	    hello_world = '[red]hello[/red] [blue]world[/blue]'  # ④
	    print(hello_world)  # ⑤
	    
	  
	  if __name__ == '__main__':  # ⑥
	    main()  # ⑦
	  ```
		- 还记得我们之前聊过的 [[什么是编程？]]吗，现在我们在一个文件 `hello_world.py` 中写了==一系列的描述特定步骤的语句==，是不是和之前的定义就匹配上啦。
		- ① 我们使用 `#` 开头，表示当前行是一个注释，[[Python 解释器]]这个翻译官会忽视它，这一行实际是写给我们这些开发者看的。
		- ② 还记得我们在 [[认识 pip]]的时候安装的那个第三方库吗，没错就是它，我们通过 Python 的 `import` 系统引入了安装在操作系统中的第三方库 `rich` 提供的 `print` 方法。==在 Python 的眼里每个名字都是唯一的==，因此原本的 `print` 函数会被这个新来的给**覆盖**掉。
		- ③
		-
	- 上述这些知识点对于第一次接触编程的你来说可能有一些多，但是没关系，现在只要混个眼熟就可以啦，后面我们还会反反复复的接触这些概念，慢慢你就能逐个掌握它们了。