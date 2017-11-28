=# insert into test1 values('{"a": "aa", "b": 1}');
=# select pg_column_size(data) from test1;

 pg_column_size
----------------
             33
(1 row)


=# insert into test2 values('{"a": 1, "b": "aa"}');
=# select pg_column_size(data) from test2;
 pg_column_size
----------------
             35
(1 row)
