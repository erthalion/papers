Best practices and anti-patterns for

* application developers

* dba

* extensions developers


When jsonb is needed?

* there is a distinct model in your system that naturally requires a lot of
  flexibility

* you need to work with some external model that provided in the document form

Transform data between jsonb and relational format.

When it makes sense to transform jsonb document to the relational form?

There are some signs of it - mostly if you relies too much on a document
structure already.

But it's not just jsonb -> relational, there are some intermediate stages, when
you can introduce some constraints on jsonb structure, check schema for some
parts of it, check type of a particular item and so on.

Also sometimes it's relational -> jsonb

ID inside a document or as a separate column?

Multiple jsonb documents on a table?

Unwrap a document on the database level or on the client?

How to index? A relatively small document - best start with GIN
jsonb_ops/jsonb_path_ops, then Btree as an optimization

Useful extensions?

Huge documents (up to 1GB) from performance/usability perspective

Use jsonb array instead of regular array?

Opinionated - map a document from a database to something typed and
well-defined in application

Update PG versions - as an example, but in jsonb_populare_record and null
handling

Best practices for extensions developers:

* when to iterate a JsonbValue and when to find inside a raw container?

* reuse existing infrastructure (iterators, access to a single element with
  find)

* values are not null terminated, so don't forget about lenght

* clone iterator to look forward and keep current position

Good or not to encode some information into a document key name? It can be
useful sometimes, but it makes it more complicated to fetch this data without
iterating (it basically makes a document structure more obscure, and you need
to put some information about it into a query).
