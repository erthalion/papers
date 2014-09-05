UPDATE test
SET data = jsonb_set(data, '{items}',
(SELECT
    jsonb_agg(
        CASE WHEN item->>'value' = 'aaa'
        THEN jsonb_set(item, '{value}', '"NEW"')
        ELSE item END
    )
    FROM (SELECT
        jsonb_array_elements(data->'items')
        AS item) q));
