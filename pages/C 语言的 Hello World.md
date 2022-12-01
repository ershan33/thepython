- ```c
  // hello_world.c
  #include <stdio.h>
  
  int main() {
      const char* hello_world = "hello world";
      printf("%s\n", hello_world);
      return 0;
  }
  ```
- 使用 [[gcc]] 编译运行：
	- ```sh
	  > gcc hello_world.c -o hello_world
	  > ls -lh hello_world
	  -rwxr-xr-x 1 ershan ershan 17K Dec  1 20:41 hello_world
	  > ./hello_world
	  hello world
	  ```
-