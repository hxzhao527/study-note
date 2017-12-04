# golang 之 range

golang 里循环只有for， 遍历出了直接索引(数字 or Key)，剩下的就只有 ```range``` 了。
然而这个表达式还很是坑，
``` golang
package main

import (
	"fmt"
)

func main() {
	data := []int{1, 2, 3, 4, 5, 6, 7}
	for i, e := range data {
		fmt.Printf("第%d个, %v, %T, %v\n", i+1, e, e, &e)
	}
	fmt.Printf("%v", &data[0])
}

```
运行后输出 
```
第1个, 1, int, 0xc0420381d0
第2个, 2, int, 0xc0420381d0
第3个, 3, int, 0xc0420381d0
第4个, 4, int, 0xc0420381d0
第5个, 5, int, 0xc0420381d0
第6个, 6, int, 0xc0420381d0
第7个, 7, int, 0xc0420381d0
0xc042040080
```
循环里的 e 的地址就没变过，也就是 ```range``` 其实是做了一个实际值的副本，每次将新值复制一哈给 ```e```，然后用副本去招摇撞骗。
同时由于 golang 里**闭包**的变量传递(官方叫法：变量逃逸)是 **地址传递** 。所以如果 ```range``` 和闭包一起用，就会导致，只能拿到循环最后一个值。

``` golang
package main

import (
	"fmt"
)

func main() {
	data := []int{1, 2, 3, 4, 5, 6, 7}
	for i, e := range data {
		defer func() { fmt.Printf("第%d个, %v, %T, %v\n", i+1, e, e, &e) }()
	}
	fmt.Printf("%v\n", &data[0])
}
```
输出为：
```
0xc042040080
第7个, 7, int, 0xc0420381d8
第7个, 7, int, 0xc0420381d8
第7个, 7, int, 0xc0420381d8
第7个, 7, int, 0xc0420381d8
第7个, 7, int, 0xc0420381d8
第7个, 7, int, 0xc0420381d8
第7个, 7, int, 0xc0420381d8
```
可以看到结果都是 ```7```，同样的，在 ```range``` 循环中是无法修改原先序列中的值的。
``` golang
package main

import (
	"fmt"
)

func main() {
	data := []int{1, 2, 3, 4, 5, 6, 7}
	fmt.Printf("%v\n", &data[0])
	for _, e := range data {
		//defer func() { fmt.Printf("第%d个, %v, %T, %v\n", i+1, e, e, &e) }()
		e += 100
	}
	fmt.Printf("%d, %v", data[0], &data[0])
}
```
输出结果：
```
0xc042040080
1, 0xc042040080
```
由于函数的调用是值传递(传的指针，也是指针的copy)， ```range``` 产出的虽说指针是一个，但是值是变的，所以可以当作 里层函数 的参数传进去，这样值传递就可以实现想要的效果。
``` golang
package main

import (
	"fmt"
)

func main() {
	data := []int{1, 2, 3, 4, 5, 6, 7}
	for i, e := range data {
		defer func(index int, element int) {
			fmt.Printf("第%d个, %v, %T, %v\n", index+1, element, element, &element)
		}(i, e)
	}
	fmt.Printf("%v\n", &data[0])
}
```
输出结果
```
0xc04200a280
第7个, 7, int, 0xc04200c240
第6个, 6, int, 0xc04200c260
第5个, 5, int, 0xc04200c280
第4个, 4, int, 0xc04200c2a0
第3个, 3, int, 0xc04200c2c0
第2个, 2, int, 0xc04200c2e0
第1个, 1, int, 0xc04200c300
```
虽说还不是原生的地址，但是这次值是对的。