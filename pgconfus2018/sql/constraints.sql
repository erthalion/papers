CREATE TABLE test (
    data jsonb,
    CHECK (jsonb_typeof(data->'key') = 'array')
);
CREATE TABLE test (
    data jsonb,
    CHECK (data @@ 'key IS ARRAY OR key IS OBJECT')
);
CREATE TABLE test (
    data jsonb,
    CHECK (validate_json_schema('{"key": "array"}', data))
);
