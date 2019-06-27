# 添加依赖(1)

使用`cmake`处理`c/c++`依赖, 其实是建立在原本*头文件-源代码-静态库*的模式基础上的.

## 依赖分类
1. 作为当前项目的子模块
2. 外部项目, 且使用了`cmake`
3. 外部项目, 且没有使用`cmake`

这里先看子模块这种依赖形式.

## 子模块
从文件的角度看, 其实就是项目文件组织形式, 有一些源代码或者头文件在当前项目的某个子目录下.
也是属于这个项目的代码, 出于某种原因, 独立为一个模块. 最后再通过链接生成最终的执行文件.

比如此示例里, 定义了一个`laugh`子模块, 放在`lib/laugh`中. 为了能让`cmake`找到这个模块, 我们在顶级的`CMakeLists.txt`中使用了`add_subdirectory ("${PROJECT_SOURCE_DIR}/lib/laugh")`, 但只是找到并不解决问题, `cmake`并不知道这个目录该怎么组织怎么构建, 因此这个目录下还需要一个`CMakeLists.txt`文件.

子模块的`CMakeLists.txt`文件里只有一行
```
add_library(Laugh laugh.cc)
```
与前面提过的`add_executable`类似, 那个是构建可执行文件, 这里是构建一个库, 默认是相对目录下的静态库, 至于是`libLaugh.a`还是`Laugh.lib`, 根据构建系统而定. 注意这里给库命名为`Laugh`, 后面引用是也需要是这个, 还有就是不要命名冲突.

构建完, 还要链接才能得到最后的执行程序, 所以在顶级的`CMakeLists.txt`中在添加子目录后, 有了这三行:
```
set (EXTRA_LIBS ${EXTRA_LIBS} Laugh)
add_executable (main main.cc)
target_link_libraries (main ${EXTRA_LIBS})
```
为了便于管理链接目标, 使用变量`${EXTRA_LIBS}`存了下来, 在`set`命令后面, 有一个`Laugh`, 这就是前面定义的子模块.
再通过`target_link_libraries`指明构建目标`main`的链接参数.