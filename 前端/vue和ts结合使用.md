# 怎么初始化工程

1. 使用vue-template
这个最方便, 使用官方的```CLI```工具[Vue CLI](https://github.com/vuejs/vue-cli),结合[vue-webpack-typescript](https://github.com/ducksoupdev/vue-webpack-typescript), 缺点就是这里面东西也太多了点~~

2. 手动档
参考巨硬提供的[TypeScript-Vue-Starter](https://github.com/Microsoft/TypeScript-Vue-Starter), 这里不赘余.
其中, 添加```tsconfig.json```一段, 可以使用```tsc```的```init```功能, 
```shell
tsc --init -m es2015 --strict --outDir ./build  --sourceMap --noImplicitReturns -t es5
```
会生成一个完美的(有注释说明的)```tsconfig.json```, 根据自己需要再改改就好了.
*注:对typescript版本有要求, 1.6及以后*
还有就是巨硬提供的这个, 版本太老, 可以参看自己fork之后更新的内容[HeartUnchange/TypeScript-Vue-Starter](https://github.com/HeartUnchange/TypeScript-Vue-Starter)