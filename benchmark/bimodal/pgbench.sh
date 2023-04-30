bin/pgbench -i -s 400
bin/pgbench -T 120 -M prepared -S -c 4 -j 2 -P 10 -l


cd /sys/fs/cgroup/memory/

mkdir postgres
cd postgres

# 32 mb
echo 33554432 > memory.limit_in_bytes
echo 33554432 > memory.kmem.limit_in_bytes

for p in $(pgrep postgres); do echo $p > tasks; done

# perf record --call-graph=dwarf -g -p $(pgrep postgres | tr '\n' ',')
