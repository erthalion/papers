WITH items AS (
    SELECT jsonb_array_elements(data->'items')
    AS item FROM test
)
SELECT * FROM items
WHERE item->>'value' = 'aaa';
