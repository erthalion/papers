WITH items AS (
    SELECT |\colorbox{RedOrange}{jsonb\_array\_elements}|(data->'items')
    AS item FROM test
)
SELECT * FROM items
WHERE item->>'value' = 'aaa';
