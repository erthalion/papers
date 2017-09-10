# NoSQL Best Practices for PostgreSQL

Everyone already knows the Jsonb data type: one of PostgreSQL's most attractive
features that allows efficient work with semi-structured data without
sacrificing strong consistency and ability to use all the power of proven
relational technology. But what exactly is inside Jsonb? Are there any caveats,
and how can you accidentally bring down performance?

We will discuss all these questions together with advantages and disadvantages
of using Jsonb in different situations in comparison with other solutions and
existing standards. I'll show some important best practices about how to write
compact queries to work with Jsonb, and avoid common mistakes/performance
problems.
