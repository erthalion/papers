import psycopg2
import json
from random import choice
from string import ascii_lowercase
from itertools import cycle


key_sequence = cycle(ascii_lowercase)
document = {"{}{}".format(next(key_sequence), i): "".join([choice(ascii_lowercase) for _ in range(1000)]) for i in range(0, 1000)}

conn = psycopg2.connect("dbname=erthalion user=erthalion")
conn.autocommit = True
cur = conn.cursor()
cur.execute("insert into test values('{}');".format(json.dumps(document)))
cur.close()
