-- PG since 9.4
select jsonb_build_object(
    'id', 1,
    'data', 'aaa'
);
-- MySQL since 5.7
select json_object(
    'id', 1,
    'data', 'aaa'
);
