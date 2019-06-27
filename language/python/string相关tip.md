# string

1. ```"\\x1f\\x8b"``` 怎么转换成 ```b'\x1f\x8b'```?
有时存进文本的是hex字符串， 然后再读取发现被转义了。。。变成了"\\x1f\\x8b"， 这不是搞事? 
为了以hex或字节形式读进来，做一下操作。
[python2参考文档](https://docs.python.org/2/library/codecs.html), 
[python3参考文档](https://docs.python.org/3/library/codecs.html)
```python
import codecs
codecs.escape_decode("\\x1f\\x8b") #(b'\x1f\x8b', 8)
```