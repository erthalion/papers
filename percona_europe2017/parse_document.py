import psycopg2
import json


condition_parse = json.dumps({"YCSB_KEY": "user8401433899964320217"})
condition_no_parse = "jsonb_build_object('YCSB_KEY', 'user8401433899964320217')"

conn = psycopg2.connect("dbname=ycsb user=erthalion")
conn.autocommit = True
cur = conn.cursor()
for i in range(100000):
    # cur.execute("select * from usertable where data @> '{}'::jsonb".format(condition_parse))
    cur.execute("select * from usertable where data @> {}".format(condition_no_parse))

cur.close()
