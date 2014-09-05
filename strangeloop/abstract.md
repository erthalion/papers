# Efficient seamless integration of NoSQL inside PostgreSQL: tips and tricks

If you're trying to build a data instensive application, the last thing you
want is to be limited in what you can do with the data. But that's what
actually happens when you're using one database. E.g. in the dimension of
"normalization - denormalization" any document oriented database limits you in
terms of reports and data joins, and any relational database limits you in
terms of schema flexibility. And exactly because of that there is a clear trend
among different databases to support data in different formats.

Everyone already knows that PostgreSQL provides `jsonb` data type as a nice
solution for the problem described above. It gives you flexibility of using
schema-less documents and seamless integration with all the standard sql
features. But what is inside of `jsonb`, how it implemented, are there any
caveats and what do you need to use it efficiently?

We will discuss all that questions altogether with advantages and disadvantages
of using jsonb in different situations in comparison with other solutions and
existing standards. The goal of this talk is to provide:

* a guidance of how to start efficiently using jsonb and don't get lost

* an overview of performance and important corner cases
