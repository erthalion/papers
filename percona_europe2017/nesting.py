from string import ascii_lowercase
from itertools import cycle


key_sequence = cycle(ascii_lowercase)
document = {}
subdoc = document

for i in range(0, 200):
    key = next(key_sequence)
    if i < 199:
        subdoc[key] = {}
        subdoc = subdoc[key]
    else:
        subdoc[key] = {"value": "test"}


conn = psycopg2.connect("dbname=erthalion user=erthalion")
cur = conn.cursor()
cur.execute("insert into test_depth values('{}');".format(json.dumps(document)))
