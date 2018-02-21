# 1. Introduction and context

Explain what it this about, context - there was a talk before with much more
performance testing, but I've got a feedback, that people would like to see
more clear "best practices".

# 2. Sections

For app developers
For dba
For extensions developers

# 3. For developers

## 3.1 When do you need jsonb?

* there is a distinct model in your system that naturally requires a lot of
  flexibility

* you need to work with some external model that provided in the document form

## 3.2 When you don't need jsonb?

We need to store this value, and probably we need to think about how to
represent it, create a separate table/column. But we're too lazy, so we're
going to store it in jsonb column.

## 3.3 jsonb <-> relation

It's perfectly valid situation (and probably even ideal) when you move part of
your data from jsonb to relation form. There are some sings that you actually
need to do so - e.g. if you relies too much on a document structure already.

## 3.4 Sign that you need to move to relation

SELECT
    t_id AS id, t_created AS created,
    (CASE WHEN :minimal THEN t_tour::jsonb - 'shipments' ELSE t_tour END) AS tour
FROM tour
WHERE
    (:id::UUID IS NULL OR (t_created, t_id) > ((SELECT t_created FROM tour WHERE t_id = :id), :id))
    AND (:state::TEXT IS NULL OR t_state = :state)
    AND (:provider::TEXT IS NULL OR t_tour->>'logistics_provider_name' = :provider)
    AND (:shipment_id::TEXT IS NULL OR t_tour @> ('{"shipments":[{"id":"' || :shipment_id || '"}]}')::JSONB)
    AND (:product_id::TEXT IS NULL OR t_tour @> ('{"shipments":[{"items":[{"product_id":"' || :product_id || '"}]}]}')::JSONB)
    AND (:order_number::TEXT IS NULL OR t_tour @> ('{"shipments":[{"items":[{"order_number":"' || :order_number || '"}]}]}')::JSONB)
    AND (:tracking_number::TEXT IS NULL OR t_tour @> ('{"shipments":[{"tracking_number":"' || :tracking_number || '"}]}')::JSONB)
    AND (:before::TIMESTAMP WITH TIME ZONE IS NULL OR t_created <= :before)
ORDER BY t_created ASC, t_id ASC
LIMIT :limit

## 3.5 jsonb -> relation gradations

You can introduce constraints over jsonb, check that some paths are exist or
have some particular type. If you have complicated queries maybe you can use
jsquery (while SQL/JSONB is in progress).

You can check your documents agains schema:
https://github.com/gavinwahl/postgres-json-schema

## 3.6 jsonb <- relation

Don't forget that you can also transform data from relation form to json, which
can be convenient sometimes.

`jsonb_agg`

## 3.7 Id inside a document or as a separate column

Almost no functional difference, but id as a separate column is sometimes safer
in terms of performance (index rebuild, also fetch without index is a binary
search, it's easy to forget that).

## 3.8 Multiple jsonb columns inside a table

Tuple deformation? Varlena or nullable fields should be at the end of a table?

## 3.9 Where to unwrap a document

Let's imagine that you have a document. In the application you need to extract
only part of it, i.e. few fields. Where it's better to do so, right in a query,
or later in the application?

You can reduce amount of data passing through by extracting it directly in
query, but at the same time there maybe a performance penalties (like multiple
detoasting) if you want to extract too many fields.

In our app we decided that documents are not that big, and so far we unwrap
then in the application.

## 3.10 How to index documents

If your documents are not that big, as a start point you can easily index them
with GIN using jsonb_ops/jsonb_path_ops. After that you can create a function
index over particular paths as an optimization.

## 3.11 Useful extensions

jsquery
zson
is_jsonb_valid
postgres-json-schema
jsonb_explorer?

## 3.12 Jsonb array vs array

From functionality point of view there is only one difference, in jsonb array
you can put elements of different type. But it contradicts with the idea that
your document should represents a single model.

Performance difference?

## 3.13 Types

Highly opinionated - map jsonb document to something typed and well defined in
your system, otherwise you'll not not what'are you working with.

# 4. DBA

## 4.1 Update PG versions

Show an example with jsonb_populare_records

## 4.2 Performance of indexes

When id in document, GIN jsonb_ops vs GIN jsonb_path_ops vs jsquery vs BTree

## 4.3 Statistics

Investigage if there are any details about how postgres collects statistics for
jsonb

## 4.4 Jsonb array vs array

## 4.5 Multiple detoasting

## 4.6 Write jsonb diffs to wal

## 4.7 Huge documents

## 4.8 Alignment within a document

+- bits of alignment and total document size

# 5. Extensions developers

## 5.1 JsonbValue vs raw container

Iterate when update, find in a raw continer when search one key

## 5.2 Reuse existing infrastructure

Iterators, skip, find a single element etc.

## 5.3 Some random tips

* Clone iterator

* strings are not null terminated, don't forget about length

## 5.4 Reasons to write an extension?

It's possible to get something from working with jsonb on a low level. E.g. you
somehow forced that all your documents have first key `_id`, and you don't want
to create an index over it for some reason. If you'll create a function
jsonb_get_id, that would return directly a value of the first key, then you may
speed up e.g. seq scans, because for every key fetch you don't need to perform
search within a document.
