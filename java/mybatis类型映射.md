参考: http://www.mybatis.org/mybatis-3/zh/configuration.html#typeHandlers
https://docs.oracle.com/javase/9/docs/api/java/sql/JDBCType.html
|           Java 类型           |                             JDBC 类型                             |
|:-----------------------------:|:-----------------------------------------------------------------:|
|   java.lang.Boolean, boolean  |                        数据库兼容的 BOOLEAN                       |
|      java.lang.Byte, byte     |                    数据库兼容的 NUMERIC 或 BYTE                   |
|     java.lang.Short, short    |               数据库兼容的 NUMERIC 或 SHORT INTEGER               |
|     java.lang.Integer, int    |                  数据库兼容的 NUMERIC 或 INTEGER                  |
|      java.lang.Long, long     |                数据库兼容的 NUMERIC 或 LONG INTEGER               |
|     java.lang.Float, float    |                   数据库兼容的 NUMERIC 或 FLOAT                   |
|    java.lang.Double, double   |                   数据库兼容的 NUMERIC 或 DOUBLE                  |
|      java.math.BigDecimal     |                  数据库兼容的 NUMERIC 或 DECIMAL                  |
|        java.lang.String       |                           CHAR, VARCHAR                           |
|         java.io.Reader        |                                 -                                 |
|        java.lang.String       |                         CLOB, LONGVARCHAR                         |
|        java.lang.String       |                          NVARCHAR, NCHAR                          |
|        java.lang.String       |                               NCLOB                               |
|      java.io.InputStream      |                                 -                                 |
|             byte[]            |                       数据库兼容的字节流类型                      |
|             byte[]            |                        BLOB, LONGVARBINARY                        |
|         java.util.Date        |                             TIMESTAMP                             |
|         java.util.Date        |                                DATE                               |
|         java.util.Date        |                                TIME                               |
|       java.sql.Timestamp      |                             TIMESTAMP                             |
|         java.sql.Date         |                                DATE                               |
|         java.sql.Time         |                                TIME                               |
|              Any              |                         OTHER 或未指定类型                        |
|        Enumeration Type       |     VARCHAR-任何兼容的字符串类型，存储枚举的名称（而不是索引）    |
|        Enumeration Type       | 任何兼容的 NUMERIC 或 DOUBLE 类型，存储枚举的索引（而不是名称）。 |
|       java.time.Instant       |                             TIMESTAMP                             |
|    java.time.LocalDateTime    |                             TIMESTAMP                             |
|      java.time.LocalDate      |                                DATE                               |
|      java.time.LocalTime      |                                TIME                               |
|    java.time.OffsetDateTime   |                             TIMESTAMP                             |
|      java.time.OffsetTime     |                                TIME                               |
|    java.time.ZonedDateTime    |                             TIMESTAMP                             |
|         java.time.Year        |                              INTEGER                              |
|        java.time.Month        |                              INTEGER                              |
|      java.time.YearMonth      |                       VARCHAR or LONGVARCHAR                      |
| java.time.chrono.JapaneseDate |                                DATE                               |