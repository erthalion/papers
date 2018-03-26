SELECT jsonb_agg(query) FROM (
    SELECT id, data
    FROM jsonb_table
) query;
