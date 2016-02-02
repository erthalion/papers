This document is intended to compare the json support in different relational databases: MySql, Oracle, DB2, MsSql.
Besides that it shows a comparison between MySql and PostgreSQL, with the aim of displaying what is missing in PostgreSQL
(but not vice verse).

#MySql
Json support since **mysql 5.7.7**.

###Data selection
####MySql
```sql
1. select json_extract(data, '$.key') from test_json_table;
2. select data->"$.array[1]" from test_json_table;
```
####PostgreSQL
```sql
1. select data -> 'key' from test_json_table;
2. select data #> '{array, 1}' from test_json_table;
```

###Data modification
####MySql
```sql
1. update test_json_table set field = json_set(field, '$.key', cast(value as json));
2. update test_json_table set field = json_insert(field, '$.key', cast(value as json));
3. update test_json_table set field = json_replace(field, '$.key', cast(value as json));
4. update test_json_table set field = json_array_append(array_field, '$', 'value');
5. update test_json_table set field = json_array_insert(array_field, '$[2]', 'value');
6. update test_json_table set field = json_remove(field, '$.key');
7. update test_json_table set field = json_merge(field, '{"key": "value"}')
```

*NOTE*:
```sql
update test_json_table set field = json_merge('{"a": 1, "b": 2}', '{"a": 3, "c": 4}');
```
will result
```sql
{"a": [1, 3], "b": 2, "c": 3}
```

####PostgreSQL
```sql
1. update test_json_table set field = jsonb_set(field, '{key}', '"value"');
2. update test_json_table set field = jsonb_set(field, '{key}', '"value"');
3. update test_json_table set field = jsonb_set(field, '{key}', '"value"', false);
-- it's slightly dirty, because required to make big enough index
4. update test_json_table set field = jsonb_set(array_field, '{key, 10000}', '"value"');
5. n/a
6. update test_json_table set field = field #- '{key}';
7. update test_json_table set field = field || '{"key": "value"}';
```

###Examine data
####MySql
```sql
1. select json_contains(field, "value", '$.key') from test_json_table;
2. select json_contains_path(field, 'one' '$.key') from test_json_table;
3. select json_contains_path(field, 'all' '$.key') from test_json_table;
4. select json_deep(field) from test_json_table;
5. select json_length(array_field) from test_json_table;
6. select json_length(object_field) from test_json_table;
7. select json_keys(object_field) from test_json_table;
8. select json_search(field, 'one', 'pattern') from test_json_table;
9. select json_type(field) from test_json_table;
```

####PostgreSQL
```sql
1. select field @> '{"key": "value"}' from test_json_table;
2. select field ?| 'key' from test_json_table;
3. select field ?& 'key' from test_json_table;
4. n/a
5. select jsonb_array_length(array_field) from test_json_table;
6. n/a
7. select jsonb_object_keys(object_field) from test_json_table;
8. n/a
9. select jsonb_typeof(field) from test_json_table;
```
###Documentation
[JSON Function Reference](https://dev.mysql.com/doc/refman/5.7/en/json-function-reference.html)

#Oracle

Json support since **12.1.0.2** version.
As far as I see, `JSON` type isn't binary, it looks like is close to `json` type in PostgreSQL,
which can be stored in `VARCHAR2`, `CLOB`, `BLOB`.
It requires the use of `is json` check constraint to ensure that value is valid JSON.
By default, `JSON` field can contains duplicated keys, unless `WITH UNIQUE KEYS` was used in `is json` constraint.
It allows using the `strict` and `lax` json syntax.

```sql
CREATE TABLE json_data
   (id          RAW (16) NOT NULL,
    document CLOB
    CONSTRAINT ensure_json CHECK (document IS JSON));
```

###Data selection

Using dotted notation:
```sql
INSERT INTO json_data
  VALUES (SYS_GUID(),
          '{"Number"        : 42,
            "String"        : "Text value",
            "Boolean"       : true,
            "Null"          : null,
            "Nested" : {...},
            "Array"         : [...]}');

SELECT json.document.Number FROM json_data json;
SELECT json.document.Nested.key FROM json_data json;
```

Using `JSON Path Expressions`:
```sql
SELECT json_query(document, '$.Nested.Array[*].type' WITH WRAPPER) FROM json_document;
SELECT json_value(document, '$.Number' RETURNING NUMBER) FROM json_document;
```

Full-Text search:
```sql
CREATE INDEX json_search_idx ON json_data (document)
  INDEXTYPE IS CTXSYS.CONTEXT
  PARAMETERS ('section group CTXSYS.JSON_SECTION_GROUP SYNC (ON COMMIT)');

SELECT document FROM json_data WHERE json_textcontains(document, '$.Array.Description', 'Some description');
```

###Data existence
```sql
SELECT * FROM json_data WHERE json_exists(document, '$.String' error_handler ON ERROR);
```

###Format transformations
Convert to the relational format.
```sql
SELECT * FROM json_data json,
    json_table
    ( json.document, '$'
      columns
        json_number     NUMBER      path '$.Number'
    );
```
###Documentation
[Documentation](http://docs.oracle.com/database/121/ADXDB/json.htm#ADXDB6246)

#db2

The JSON data is stored in a binary-encoded format BSON, and to interact with that data we can use MongoDB query language.
As far as I see it's exactly a NoSql solution with restricted possibility to interact with data using the sql interface 
(only in DB2 11 for z/OS with functions like `SYSTOOLS.JSON2BSON`, `JSON_VAL`, etc., see this [paper](http://www.ibm.com/developerworks/data/library/techarticle/dm-1501sql-json-db2/index.html)).

#MsSql

Support is expected in the MS SQL server 2016, [see](http://blogs.msdn.com/b/jocapc/archive/2015/05/16/json-support-in-sql-server-2016.aspx)
