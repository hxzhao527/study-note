# varchar "慷慨"

我们已经知道```varchar```相对于```char```的优势, 就是指定的长度是最大长度而不是固定长度, 即```varchar```储存时占据的空间是根据内容长度的, 不像```char```是写死的.

那```varchar(20)```和```varchar(255)```有什么区别? 写成 **255**, 既能满足长度, 储存空间又不会多. 区别在哪呢?

在储存空间上, 是没有差异的, 但是在内存的使用方面是存在区别的. 因为在内存中, MySQL会做对齐, ```varchar(255)```占据空间```255```, ```varchar(20)```占据空间```20```, 也就是吃的内存不同. 所以这个最大长度并不是越大越好, 实用最好.


参考:

* [internal-temporary-tables](https://dev.mysql.com/doc/refman/5.5/en/internal-temporary-tables.html)
* [are-there-disadvantages-to-using-a-generic-varchar255-for-all-text-based-field](https://stackoverflow.com/questions/262238/are-there-disadvantages-to-using-a-generic-varchar255-for-all-text-based-field)