## 1. win10 下， 提示 gopath entry is relative
环境变量中的gopath结尾有一个分号导致，选择编辑文本，去掉结尾的分号即可。

## 2. GOPATH 设置。
情景：每新创建一个项目就要改环境变量的GOPATH，很是不方便。经查，可以这样做。
VSCode 的设置中有
```json
{
  "go.inferGopath": true,
  //"go.toolsGopath": "D:\\Go\\gopath", // 实际的位置
}  
```
其中 ```go.inferGopath``` 可以让 VSCode 实现一下操作：
> * 检查 *打开的当前目录*的目录名
> * 如果 **当前文件夹**名是**src**，就将 *父文件夹* 加入到GOPATH 中，这样，VSCode 里 GOPATH 就自动变化了。


注： 这种骚操作，对vscode里的terminal都不好使，还是需要自己定义一遍。