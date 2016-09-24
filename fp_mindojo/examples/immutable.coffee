
record = {"id": 1, "name": "first record"}
record.id = 2   # ok

Object.freeze record
record.id = 3   # nothing was changed
