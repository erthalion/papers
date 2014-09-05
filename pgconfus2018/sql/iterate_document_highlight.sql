WITH items AS (
    SELECT |\colorbox{RedOrange}{jsonb\_each}|(data->'items')
    AS item FROM test
)
SELECT (item).key FROM items
WHERE (item).value->>'status' = 'true';
