# Edge cases for jsonb performance

* array operations:

    - read from small array

    - read from big array

    - update small array

    - update big array

* gin index

    - JGIN_MAXLENGTH - if text representation is more than this constant,
      hashing will be applied.

* on-disk representation

    - JB_OFFSET_STRIDE

    - key are more compact in memory, effective cache?

* TOAST'ing

The TOAST management code is triggered only
when a row value to be stored in a table is wider than
TOAST_TUPLE_THRESHOLD bytes (normally 2 kB).


* memory consumption

    - how about operate with low amount of available memory?

* type convertion

    - to jsonb

    - from jsonb

* json vs jsonb

* how is index rebuild for jsonb? (functional, see mailing list)

* get stacktrace for each type of workload (for one row or for some set of
  requests) and work it through in the matter of performance


* question - why jsonb doesn't use "expanded object" as arrays?

* empty null trick for jsonb to save a little bit of space?

* 4 bits alignment and storage tricks (numeric vs string)?

* maximum document depth - mongodb 100, mysql 100, pg - no
