# 并发连接测试场景：测试数据库在高并发连接情况
# pgbench -C -j <number_of_threads> -T <duration> -U <username> -d <database_name>
# 其中，-C选项表示每个线程都使用独立的数据库连接。

#THREADS="10"
#CLIENTS="10 30 50 100 300 500"
for c in $CLIENTS; do
  pgbench -h $HOST -p $PORT -U postgres -T 60 -C -c $c -j $THREADS -r odoo
done