# 延迟测试场景：测试数据库在高延迟网络环境
# pgbench -c <number_of_clients> -j <number_of_threads> -T <duration> -l -U <username> -d <database_name>
# 其中，-l选项表示启用休眠以模拟延迟。

#THREADS="10"
#CLIENTS="10 30 50 100 300 500"
for c in $CLIENTS; do
  pgbench -h $HOST -p $PORT -U postgres -T 60 -C -c $c -j $THREADS -L 100 odoo
done