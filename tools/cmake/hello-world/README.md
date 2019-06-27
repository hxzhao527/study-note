# 万物开始之 `Hello World`

相信最简单的不过用`cmake`构建一个最简单的程序.

## 构建 && 运行

项目准备好以后, `Ctrl + Shift + P`, 选择 `CMake: Configure` 进行配置, 然后`Build`. 然后`Shift + F5` 运行.

## cmake
`cmake`处理的项目, 要求顶级目录含有一个`CMakeLists.txt`文件, 就和用`.cpp`或`.cc`表示是`c++`的源代码一样表明身份. 同时文件中指明构建的配置和方式. 

这里很简单, 只是构建一个`Hello World`, 所以`CMakeLists.txt`也很简单, 仅三行.

```cmake
cmake_minimum_required(VERSION 2.6)
project(hello-world)
add_executable(main hello.cc)
```

* 用`cmake_minimum_required`表明对`cmake`版本的要求, 有些特性或功能, 低版本的`cmake`可能没有, 同时还有一些默认的策略也可能发生变化, 具体见[cmake_minimum_required](https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html)
* 用`project`表明项目名称, 当然使用`project`配置项目使用的语言(c, c++, asm), 项目的描述信息等, 具体可见[project](https://cmake.org/cmake/help/latest/command/project.html)
* 用`add_executable`配置构建结果, 表明构建的是可执行文件. 第一个参数指明产物的文件名, 后面指明源文件, 当然要求存在`main`函数, 否则会构建失败.