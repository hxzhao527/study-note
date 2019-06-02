# 对项目进行配置

使用`configure_file`和`set`命令达到项目配置的目的, 当然是通过生成文件当方式传递变量.


## cmake

1. 使用`configure_file`命令渲染底板文件, 生成头文件或其他项目源代码使用的文件, 以达到传递配置信息的目的.具体详解见[configure_file](https://cmake.org/cmake/help/latest/command/configure_file.html), 这里只简略一提
* `<input>` 中的 `@VAR@` 或 `${VAR}` 会被`set`命令设置的变量渲染替换. 如果没有定义就是空字符串.
* `#cmakedefine VAR ...` 会被 翻译成`#define VAR ...`
* 通过参数`@ONLY`可以限定只渲染替换`@VAR@`, 保留`${VAR}`

2. 通过`set`命令设置变量属性, 从而传递配置项. 当然除了能设置变量外, 还能设置属性的作用域, 以及(临时的)环境变量. 详解见[set](https://cmake.org/cmake/help/latest/command/set.html)

3. `include_directories`指明`include`目录.

4. 通过`cmake_host_system_information`或许一些构建机器的系统信息.

### 补充
1. 这里`project`命令与前面不同, 同时对`cmake`版本的要求也发生了改变. 这是因为通过`project`命令配置项目版本的功能, 是新版本的`cmake`才有的.
2. `${PROJECT_SOURCE_DIR}` 和 `${PROJECT_BINARY_DIR}`都是调用`project`命令后才被自动定义的变量, 分别用来表明项目的顶级目录和项目的构建(生成的build文件夹)目录.