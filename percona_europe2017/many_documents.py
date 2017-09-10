import psycopg2
import json


document1 = {"a": "a", "b": 1}
document2 = {"a": 1, "b": "a"}

conn = psycopg2.connect("dbname=erthalion user=erthalion")
conn.autocommit = True
cur = conn.cursor()
for i in range(10000):
    cur.execute("insert into test2 values('{}');".format(json.dumps(document2)))

cur.close()
