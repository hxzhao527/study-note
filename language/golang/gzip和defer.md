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
	defer w.Close() //有问题
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
`gzip.NewWriter`的`Close`还会写入数据, 用`defer`有问题
