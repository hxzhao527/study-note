# 添加依赖(2)

除了子模块这种依赖外, 很多情况下, 项目还要依赖一些第三方的库, 比如`Boost`, 比如`Zlib`等. 
对于这种类型的依赖, `cmake`里怎么处理呢?

### 什么是`package`?
在`cmake`中总共两种类型的`package`,
* 外部项目, 且使用了`cmake`, 基于`config`的`package`
* 外部项目, 且没有使用`cmake`, 基于`module`的`package`

#### 基于`module`的`package`
在这种模式下, 执行`find_package(<PackageName>)`命令时, `cmake`会先从`CMAKE_MODULE_PATH`中搜索`Find<PackageName>.cmake`文件, 找不到时再搜索`cmake`内置的module.

这个文件主要是为了检测并设置`<PackageName>_FOUND`变量来表示对应的`package`是否存在. 
同时还会设置一下使用这个`package`的一些需要的变量, 这里简单列几个(假设文件名为`FindXxx.cmake`), 其他的可以在这找[Standard Variable Names](https://cmake.org/cmake/help/latest/manual/cmake-developer.7.html#standard-variable-names):
* `Xxx_INCLUDE_DIRS`: 头文件目录, 编译时用
* `Xxx_LIBRARIES`: 静态库, 链接时用, 需要是全路径
* `Xxx_VERSION`, `Xxx_VERSION_MAJOR`, `Xxx_VERSION_MINOR`, `Xxx_VERSION_PATCH`: 表明版本的, 在`find_package`时可以用来筛选
* `Xxx_LIBRARY_RELEASE`, `Xxx_LIBRARY_DEBUG`: 有的分调试和发行

至于`cmake`内置的`module`, 可以在[cmake-modules](https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html)查询.

### 自定义`module`
以`FFmpeg`为目标, 参看官方的`FindZLIB.cmake`, 照虎画猫.