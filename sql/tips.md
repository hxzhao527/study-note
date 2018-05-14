1. 删除库中所有外键:
```sql
SELECT concat('alter table ',table_schema,'.',table_name,' DROP FOREIGN KEY ',constraint_name,';')
FROM information_schema.table_constraints
WHERE constraint_type='FOREIGN KEY'
AND table_schema='数据库名';
```
2. 检查库中表的索引
```sql
SELECT TABLE_NAME, ENGINE FROM information_schema.TABLES WHERE TABLE_SCHEMA = '数据库名';
```