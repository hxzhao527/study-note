# golang 之 函数参数传递方式
``` golang
package main

import (
	"fmt"
)

func haha(a *int) {
	fmt.Printf("函数里：\n\t收到的参数：%v\n\t收到的参数的地址%v\n", a, &a)
}

func main() {
	a := 1
	p := &a
	fmt.Printf("调用前：\n\ta指针为%v\n\ta指针的地址为%v\n", p, &p)
	haha(p)
}
```
输出结果
```
调用前：
	a指针为0xc04200c220
	a指针的地址为0xc042004028
函数里：
	收到的参数：0xc04200c220
	收到的参数的地址0xc042004038
```