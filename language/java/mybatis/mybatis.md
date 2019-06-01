# mybatis
###1. xml中出现```>=```或者```<=```怎么处理.
方式1: 使用escape字符, 
|  &lt;  | < | 小于号 |
|:------:|:-:|:------:|
|  &gt;  | > | 大于号 |
|  &amp; | & |   和   |
| &apos; | ’ | 单引号 |
| &quot; | " | 双引号 |
方式2, 使用```<![CDATA[ ]]>```
示例:
```xml
<if test="beginTime!=null and beginTime!=''">
    <![CDATA[   and DATE_FORMAT(tr.add_time, '%Y-%m-%d')>=  DATE_FORMAT(#{beginTime}, '%Y-%m-%d')   ]]>
</if>
<if test="endTime!=null and endTime!=''">
    <![CDATA[  and DATE_FORMAT(tr.add_time, '%Y-%m-%d') <= DATE_FORMAT(#{endTime}, '%Y-%m-%d')    ]]>
</if>
```