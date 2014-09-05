-- PG
copy table_name(jsonb_column_name)
from 'data.json';
-- MySQL
load data infile 'data.json'
into table table_name (json_column_name);
