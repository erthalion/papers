-- PG since 9.4
select jsonb_agg(query) from (
    select id, data
    from jsonb_table
) query;
-- MySQL since 8
select json_objectagg(`key`, val)
as `key_val` from t1;
