# 初始化测试环境
#pgbench -h 47.103.109.192 -p 5433 -U postgres -i -d odoo
pgbench -h $HOST -p $PORT -U postgres -i -d odoo