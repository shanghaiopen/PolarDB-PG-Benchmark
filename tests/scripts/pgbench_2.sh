# 写入测试场景：模拟并发写入（插入、更新、删除）操作的情况
# pgbench -c <number_of_clients> -j <number_of_threads> -T <duration> -N -U <username> -d <database_name>
# 其中，-N选项表示只执行INSERT、UPDATE和DELETE语句。

#THREADS="10"
#CLIENTS="10 30 50 100 300 500"
for c in $CLIENTS; do
  pgbench -h $HOST -p $PORT -U postgres -T 60 -c $c -j $THREADS -N -r odoo
done