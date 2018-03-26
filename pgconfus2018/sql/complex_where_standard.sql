SELECT id, created FROM some_table
WHERE

    data @~ '$.items[*] ? (@id = '||:a||')'
    AND data @~ '$.items[*].elems[*] ? (@name = '||:b||')'
    AND data @~ '$.items[*].elems[*] ? (@id = '||:c||')'
    AND data @~ '$.items[*](@name = '||:d||')'

ORDER BY created ASC, id ASC;
