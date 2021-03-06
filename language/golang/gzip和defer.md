## Golang里的gizp

原本以为和`py`的`zlib`一样简单, 没想到, 还有**坑**.

在网上随便一搜, 都有如下一段代码:
```golang
//gZipEncode
//
// use gzip to compress data
//
// @return []byte result data
//
// @return error error occur during compress
//
func gZipEncode(in []byte) ([]byte, error) {
	var b bytes.Buffer
	w := gzip.NewWriter(&b)
	w.Write(in)
	w.Flush()
	defer w.Close()
	return b.Bytes(), nil
}

// gZipDecode
//
// use gzip to decompress data
//
// @return []byte result data
//
// @return error error occur during decompress
//
func gZipDecode(in []byte) ([]byte, error) {
	r, err := gzip.NewReader(bytes.NewReader(in))
	defer r.Close()
	if err != nil {
		return nil, err
	}
	return ioutil.ReadAll(r)
}
```

`gzip`压缩时没毛病, 但是"解压"时就抛了`error`, 一行行的debug发现, 并不是算法或者数据有问题, 而是`ioutil.ReadAll`在读取解压后的数据时抛了`io.EOF`, 为什么会抛这个`error`?
难道是`gzip.Reader`出了问题? 于是试了下`bufio.Reader`, 没发现啥毛病.
最终找到了大佬的一番说辞: [compress/gzip: Reader returns EOF even if requested read successfully completed](https://github.com/golang/go/issues/24713), [compress/zlib: reading data with known length](https://github.com/golang/go/issues/14867)

意思就是: 不知道该读取多长, 索性读到一个`io.EOF`就返回, 并顺便抛一个`error`.
其实也在情理之中, `gzip`的byte没有标注压缩信息, 并判断不了解压后应该是多长.

再细看一下`io.Reader`的注释:
>When Read encounters an error or end-of-file condition after
successfully reading n > 0 bytes, it returns the number of
bytes read. It may return the (non-nil) error from the same call
or return the error (and n == 0) from a subsequent call.
An instance of this general case is that a Reader returning
a non-zero number of bytes at the end of the input stream may
return either err == EOF or err == nil. The next Read should
return 0, EOF.

意思是`Read`方法在读取到数据时还是可能返回`io.EOF`的, 然后再调用`Read`时, 会返回`0, EOF`. 看上去也没啥毛病.


________________________________

## 检验输入

发现用`gZipEncode`压缩得到的byte和别的语言的不一样, 这时为啥?
难道是压缩环节出了问题?

## 瞅瞅源码

发现如果`w.Close()`不用`defer`修饰, 结果就是对的, 难道`close`执行有问题?
查了一下源码和文档, `close`负责写入gzip的footer, 那就是`defer`导致footer没写入.

## defer到底做了啥
[defer](https://golang.org/ref/spec#Defer_statements)

**函数返回的过程是这样的：先给返回值赋值，然后调用defer表达式，最后才是返回到调用函数中。**

因此, `b.Bytes()`在前, `w.Close()`在后, 导致拿到的压缩数据有问题.
