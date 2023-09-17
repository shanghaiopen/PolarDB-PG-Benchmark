# 大事务测试场景：测试数据库在大型事务处理情况
# pgbench -c <number_of_clients> -j <number_of_threads> -T <duration> -N -M extended -U <username> -d <database_name>
# 其中，-M extended 选项表示使用扩展模式执行事务。

#THREADS="10"
#CLIENTS="10 30 50 100 300 500"
for c in $CLIENTS; do
  pgbench -h $HOST -p $PORT -U postgres -T 60 -C -c $c -j $THREADS -M extended -r odoo
done