# 读取测试场景：模拟并发读取操作的情况
# pgbench -c <number_of_clients> -j <number_of_threads> -T <duration> -S -U <username> -d <database_name>
# 其中，-S选项表示只执行SELECT语句。

#THREADS="10"
#CLIENTS="10 30 50 100 300 500"
for c in $CLIENTS; do
  pgbench -h $HOST -p $PORT -U postgres -T 60 -c $c -j $THREADS -S -r odoo
done