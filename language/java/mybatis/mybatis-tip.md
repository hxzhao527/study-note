1. like查询
使用 ```concat``` 拼接 concat('%',#{keyword},'%')

2. 查询结果返回一个map
假定数据结构为
scm_name:

| id(int) | name(varchar) |
|:-------:|:-------------:|
|    1    |      git      |
|    2    |     github    |
|    3    |     gitlab    |

try this code
```java
@Select("select id, name from scm_name")
Map<Integer, String> getScmNameMap();
```
then get
```
org.mybatis.spring.MyBatisSystemException: nested exception is org.apache.ibatis.exceptions.TooManyResultsException: Expected one result (or null) to be returned by selectOne(), but found: 4
```

！！其实是对mybatis返回结果处理方式的错误理解。

### 什么时候使用map可以？
查询单条记录， 但不关心该记录的字段名称时。
比如
```java
@Select("select * from scm_name where id = #{id}")
Map<String, Object> getOneScmById(@Param("id")Integer id);
```
这时原本对应一个具体Object(属性固定)的返回，变成一个松散的Map。

### 前面为什么会报 ```TooManyResultsException```
因为没有限定返回的条目数， 默认 使用的是selectOne，因此会报错。

### 返回多条目，但是还想用map怎么办？
首先必须有一个具体的Object 去承接 查询的返回，比如
```java
@Data
public class ScmName{
    private Integer id;
    private String name;
}
```
然后使用mapkey表明哪个属性作为key
```java
@Select("select id, name from scm_name")
@MapKey("id") // 这里是Obj的属性名称， 不是sql字段名。
Map<Integer, ScmName> getScmNameMap();
```
