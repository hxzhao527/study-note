# 添加依赖(3)

前面使用内置的module时, 粗略的提了一下`module`和`package`, 实际的`package`还是可以再细分的.

## cmake
```
find_package(Foo [major[.minor[.patch[.tweak]]]]
             [EXACT] [QUIET] [REQUIRED]
             [[COMPONENTS] [components...]]
             [OPTIONAL_COMPONENTS components...]
             [NO_POLICY_SCOPE])
```
`find_package`到底是怎么找到构建的依赖的?package是啥?
### `package`到底是啥?
其实细分的话, 有两种. 可以很容易的想象, 并不是所有的项目都用`cmake`处理构建的. 使用`cmake`处理构建的, 称之为基于配置文件的`package`; 不使用`cmake`处理构建的, 或者是通过提供给用户的就是头文件和静态库这种形式的库, 称之为基于`module`的`package`.




