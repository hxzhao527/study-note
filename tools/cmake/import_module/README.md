# 添加依赖(1)

有时为了项目管理, 将一个项目分成若干子项目, 用父子目录的方式管理. 各自独立构建测试, 完事儿了链接生成最终执行文件.
**这里的依赖是项目自身分割, 与对外部库的依赖不是一个.**

## cmake
1. 子目录必须有`CMakeLists.txt`文件, 并通过`add_library`命令指明库(子项目, 子文件夹)生成的方式, 包括库名, 生成类型, 源代码等. 具体查看[add_library](https://cmake.org/cmake/help/latest/command/add_library.html)
2. 顶级项目为使用子项目, 需要调用`add_subdirectory`命令, 让子目录也会被构建, 只有构建了才能变成库, 才能引用.
3. 第2步生成了库文件, 自然链接时就要用上, 因此通过`target_link_libraries`命令添加链接库, 这里使用的名称和在第一步中定义的库名保持一致. 不过`target_link_libraries`命令很复杂, 具体见官方文档好了.[跳转](https://cmake.org/cmake/help/latest/command/target_link_libraries.html)
4. 但有时构建项目并不想使用子项目的实现, 或者有若干实现需要根据具体场景决定使用哪一个, 因此引用`option`命令, 作为配置选项起一个开关作用. 并用`if`语句做判断. 具体`option`功效可参考文档[option](https://cmake.org/cmake/help/latest/command/option.html)

## 构建 && 运行
这里是记录使用`vscode`的方式.

找到`settings.json`文件, 如果想使用子目录实现, 就添加`"cmake.configureSettings":{"USE_MYMATH": "ON"}`,
如果不想使用, 就添加`"cmake.configureSettings":{"USE_MYMATH": "OFF"}`.

这里只是简单的一个选项的配置, 关于复杂的选项配置, 可参看插件的文档[conf-cmake-configuresettings](https://vector-of-bool.github.io/docs/vscode-cmake-tools/settings.html#conf-cmake-configuresettings) 和 [CMake Variants](https://vector-of-bool.github.io/docs/vscode-cmake-tools/variants.html#variants)


