# golang 之 函数参数传递方式
``` golang
package main

import (
	"fmt"
)

func testPoint(a *int) {
	fmt.Printf("testPoint 函数里：\n\t收到的参数：%v\n\t收到的参数的地址%p\n", a, &a)
}
func testSlice(slice []int) {
	fmt.Printf("testSlice 函数里：\n\t收到的参数：%v\n\t收到的参数的地址%p\n", slice, &slice)
}

func main() {
	a := 1
	p := &a
	b := []int{1, 2, 3, 4, 5}
	fmt.Printf("testPoint 调用前：\n\ta指针为%v\n\ta指针的地址为%p\n", p, &p)
	testPoint(p)
	fmt.Printf("testSlice 调用前：\n\ta指针为%v\n\ta指针的地址为%p\n", b, &b)
	testSlice(b)
}
```
输出结果
```
testPoint 调用前：
	a指针为0xc0420381d0
	a指针的地址为0xc042050018
testPoint 函数里：
	收到的参数：0xc0420381d0
	收到的参数的地址0xc042050028
testSlice 调用前：
	a指针为[1 2 3 4 5]
	a指针的地址为0xc04203e400
testSlice 函数里：
	收到的参数：[1 2 3 4 5]
	收到的参数的地址0xc04203e460
```