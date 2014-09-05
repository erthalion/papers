select pg_relation_filepath(oid),
relpages from pg_class
where relname = 'table_name';

 pg_relation_filepath | relpages 
----------------------+----------
 base/40960/325477    |        0
(1 row)
