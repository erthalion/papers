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

* type convertion

    - to jsonb

    - from jsonb

* memory consumption

    - how about operate with low amount of available memory?
