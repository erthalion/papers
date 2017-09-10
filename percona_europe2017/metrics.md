# PG

* built-in

pg_stat_bgwriter
pg_stat_database
pg_stat_user_tables
pg_stat_user_indexes
pg_statio_user_tables
pg_statio_user_indexes

* extensions

pg_stat_statements

shared_preload_libraries = 'pg_stat_statements'
pg_stat_statements.track = all

# MongoDB

mongostat
serverStatus

# MySQL

performance_schema?
sys?
