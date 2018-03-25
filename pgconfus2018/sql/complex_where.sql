SELECT id AS id, created AS created
FROM some_table
WHERE

(data->>'name' = :a
AND (data @> ('{"items":[{"id":"'||:b||'"}]}'))
AND (data @> ('{"items":[{"elems":[{"name":"'||:c||'"}]}]}'))
AND (data @> ('{"items":[{"elems":[{"id":"'||:d||'"}]}]}'))
AND (data @> ('{"items":[{"name":"'||:e||'"}]}'))

ORDER BY created ASC, id ASC;
