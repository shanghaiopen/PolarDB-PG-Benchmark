# 混合读写测试场景：模拟并发的读取和写入操作的情况
# pgbench -c <number_of_clients> -j <number_of_threads> -T <duration> -M simple -U <username> -d <database_name>
# 其中，-M mixed选项表示同时执行读取和写入操作。

#THREADS="10"
#CLIENTS="10 30 50 100 300 500"
for c in $CLIENTS; do
  pgbench -h $HOST -p $PORT -U postgres -T 60 -c $c -j $THREADS -M simple -r odoo
done