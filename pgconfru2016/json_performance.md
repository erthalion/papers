# General info

* Platform: Gentoo 64-bit
* GGG: 4.8.3
* MySql 5.7.8-rc, default configuration
* PostgreSQL 9.5alpha2, default configuration

# Test update value

#### PostgreSQL

```sql
CREATE OR REPLACE FUNCTION test_jsonb_set()
RETURNS void
AS $$
DECLARE
  test_json_data JSONB;
  result JSONB;
BEGIN
  test_json_data = '{"key1": "value", "key2": "value", "key3": "value", "key_nested": {"key": "value"}}'::jsonb;
  FOR Loopid  IN 0..100000 LOOP
     SELECT jsonb_set(test_json_data, '{key_nested, key}', '"new_value"') into result;
  END LOOP;
RETURN;
END;
$$ LANGUAGE plpgsql;
```

```sql
=# select test_jsonb_set();
 test_jsonb_set 
----------------
 
(1 row)

Time: 371.726 ms
```

#### MySql

```sql
DELIMITER // 
DROP PROCEDURE IF EXISTS test_set;
CREATE procedure test_set() 
BEGIN   
    declare x INT;   
    declare test_json_data JSON;
    SET x = 0;    
    SET test_json_data = '{"key1": "valve", "key2": "valve", "key3": "valve", "key_nested": {"key": "value"}}';
    WHILE x <= 100000 DO
        SET x = x + 1;       
        select json_set(test_json_data, '$.key_nested.key', 'new_value') into @result;
    END WHILE; 
END // 
DELIMITER ;
```

```sql
> call test_set();
Query OK, 1 row affected (1.29 sec)
```

#### Results

* PostgreSQL  ~ 0.37 sec
* MySql       ~ 1.29 sec

# Test insert key/value

#### PostgreSQL

```sql
CREATE OR REPLACE FUNCTION test_jsonb_insert()
RETURNS void
AS $$
DECLARE
  test_json_data JSONB;
  result JSONB;
BEGIN
  test_json_data = '{"key1": "value", "key2": "value", "key3": "value", "key_nested": {"key_nested2": {"key": "value"}}}'::jsonb;
  FOR Loopid  IN 0..100000 LOOP
     SELECT jsonb_set(test_json_data, '{key_nested, key_nested2, key}', '"new_value"') into result;
  END LOOP;
RETURN;
END;
$$ LANGUAGE plpgsql;
```

```sql
=# select test_jsonb_insert();
 test_jsonb_insert 
-------------------
 
(1 row)

Time: 409.381 ms
```

#### MySql

```sql
DELIMITER // 
DROP PROCEDURE IF EXISTS test_insert;
CREATE procedure test_insert() 
BEGIN   
    declare x INT;   
    declare test_json_data JSON;
    SET x = 0;    
    SET test_json_data = '{"key1": "valve", "key2": "valve", "key3": "valve", "key_nested": {"key_nested2": {"key": "value"}}}';
    WHILE x <= 100000 DO
        SET x = x + 1;       
        select json_insert(test_json_data, '$.key_nested.key_nested2.new_key', 'new_value') into @result;
    END WHILE; 
    select @result;
END // 
DELIMITER ;
```

```sql
> call test_insert();
Query OK, 1 row affected (1.54 sec)
```

## Results

* PostgreSQL  ~ 0.4 sec
* MySql       ~ 1.54 sec

# Test remove key

#### PostgreSQL

```sql
CREATE OR REPLACE FUNCTION test_jsonb_remove()
RETURNS void
AS $$
DECLARE
  test_json_data JSONB;
  result JSONB;
BEGIN
  test_json_data = '{"key1": "value", "key2": "value", "key3": "value", "key_nested": {"key": "value"}}'::jsonb;
  FOR Loopid  IN 0..100000 LOOP
     SELECT test_json_data #- '{key_nested, key}' into result;
  END LOOP;
RETURN;
END;
$$ LANGUAGE plpgsql;
```

```sql
=# select test_jsonb_remove();                                                                                                                
 test_jsonb_remove 
-------------------
 
(1 row)

Time: 379.772 ms
```

#### MySql

```sql
DELIMITER // 
DROP PROCEDURE IF EXISTS test_remove;
CREATE procedure test_remove() 
BEGIN   
    declare x INT;   
    declare test_json_data JSON;
    SET x = 0;    
    SET test_json_data = '{"key1": "valve", "key2": "valve", "key3": "valve", "key_nested": {"key": "value"}}';
    WHILE x <= 100000 DO
        SET x = x + 1;       
        select json_remove(test_json_data, '$.key_nested.key') into @result;
    END WHILE; 
END // 
DELIMITER ;
```

```sql
> call test_remove();
Query OK, 1 row affected (1.21 sec)
```

#### Results

* PostgreSQL  ~ 0.38 sec
* MySql       ~ 1.21 sec

# Test merge data

#### PostgreSQL

```sql
CREATE OR REPLACE FUNCTION test_jsonb_merge()
RETURNS void
AS $$
DECLARE
  test_json_data1 JSONB;
  test_json_data2 JSONB;
  result JSONB;
BEGIN
  test_json_data1 = '{"key1": "value", "key2": "value", "key3": "value", "key_nested": {"key": "value"}}'::jsonb;
  test_json_data2 = '{"key4": "value", "key5": "value", "key6": "value", "key_nested2": {"key": "value"}}'::jsonb;
  FOR Loopid  IN 0..100000 LOOP
     SELECT test_json_data1 || test_json_data2 into result;
  END LOOP;
RETURN;
END;
$$ LANGUAGE plpgsql;
```

```sql
=# select test_jsonb_merge();
 test_jsonb_merge 
------------------
 
(1 row)

Time: 483.261 ms
```

#### MySql

```sql
DELIMITER // 
DROP PROCEDURE IF EXISTS test_merge;
CREATE procedure test_merge() 
BEGIN   
    declare x INT;   
    declare test_json_data1 JSON;
    declare test_json_data2 JSON;
    SET x = 0;    
    SET test_json_data1 = '{"key1": "valve", "key2": "valve", "key3": "valve", "key_nested": {"key": "value"}}';
    SET test_json_data2 = '{"key4": "valve", "key5": "valve", "key6": "valve", "key_nested2": {"key": "value"}}';
    WHILE x <= 100000 DO
        SET x = x + 1;       
        select json_merge(test_json_data1, test_json_data2) into @result;
    END WHILE; 
END // 
DELIMITER ;
```

```sql
> call test_merge();
Query OK, 1 row affected (1.52 sec)
```

#### Results

* PostgreSQL  ~ 0.48 sec
* MySql       ~ 1.52 sec

# Total

| Test        |  PostgreSQL  |  MySql   |
|-------------|-------------:|---------:|
| test_set    | 0.37 sec     | 1.29 sec |
| test_insert | 0.4  sec     | 1.54 sec |
| test_remove | 0.38 sec     | 1.21 sec |
| test_merge  | 0.48 sec     | 1.52 sec |
