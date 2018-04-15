SELECT array[0] FROM some_table;
SELECT jsonb->0 FROM some_table;
-- WIP
SELECT jsonb[0] FROM some_table;

UPDATE some_table SET array[0] = 'new_value';
UPDATE some_table
SET jsonb = jsonb_set(jsonb, '{0}', 'new_value');
-- WIP
UPDATE some_table SET jsonb[0] = 'new_value';
