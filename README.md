# PolarDB-PG-Benchmark

## 测试报告

### 基准测试

使用pgbench，6个场景不同并发，PolarDB-PG和Postgres的性能表现情况。测试脚本和数据：[tests](tests)

1. 读取测试场景：模拟并发读取操作的情况

| 数据库/并发数/TPS | clients: 10<br />threads: 10 | clients: 30<br />threads: 10 | clients: 50<br />threads: 10 | clients: 100<br />threads: 10 | clients: 300<br />threads: 10 | clients: 500<br />threads: 10 |
| ----------------- | ---------------------------- | ---------------------------- | ---------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| PolarDB-PG        | 856                          | 2714                         | 4216                         | 8652                          | 21925                         | 21429                         |
| Postgres          | 897                          | 2814                         | 4572                         | 9281                          | 22011                         | 21456                         |




2. 写入测试场景：模拟并发写入（插入、更新、删除）操作的情况

| 数据库/并发数/TPS | clients: 10 <br/>threads: 10 | clients: 30 <br/>threads: 10 | clients: 50 <br/>threads: 10 | clients: 100 <br/>threads: 10 | clients: 300 <br/>threads: 10 | clients: 500 <br/>threads: 10 |
| ----------------- | ----------------------- | ----------------------- | ----------------------- | ------------------------ | ------------------------ | ------------------------ |
| PolarDB-PG        | 183                     | 489                     | 791                     | 1765                     | 5211                     | 6003                     |
| Postgres          | 176                     | 556                     | 918                     | 1715                     | 5097                     | 6042                     |



3. 混合读写测试场景：模拟并发的读取和写入操作的情况

| 数据库/并发数/TPS | clients: 10 <br/>threads: 10 | clients: 30 <br/>threads: 10 | clients: 50 <br/>threads: 10 | clients: 100 <br/>threads: 10 | clients: 300 <br/>threads: 10 | clients: 500 <br/>threads: 10 |
| ----------------- | ----------------------- | ----------------------- | ----------------------- | ------------------------ | ------------------------ | ------------------------ |
| PolarDB-PG        | 44                      | 46                      | 46                      | 46                       | 43                       | 45                       |
| Postgres          | 44                      | 45                      | 45                      | 46                       | 42                       | 43                       |



4. 并发连接测试场景：测试数据库在高并发连接情况

| 数据库/并发数/TPS | clients: 10 <br/>threads: 10 | clients: 30 <br/>threads: 10 | clients: 50 <br/>threads: 10 | clients: 100 <br/>threads: 10 | clients: 300 <br/>threads: 10 | clients: 500 <br/>threads: 10 |
| ----------------- | ----------------------- | ----------------------- | ----------------------- | ------------------------ | ------------------------ | ------------------------ |
| PolarDB-PG        | 45                      | 34                      | 37                      | 36                       | 36                       | 35                       |
| Postgres          | 40                      | 33                      | 32                      | 32                       | 31                       | 35                       |



5. 大事务测试场景：测试数据库在大型事务处理情况

| 数据库/并发数/TPS | clients: 10 <br/>threads: 10 | clients: 30 <br/>threads: 10 | clients: 50 <br/>threads: 10 | clients: 100 <br/>threads: 10 | clients: 300 <br/>threads: 10 | clients: 500 <br/>threads: 10 |
| ----------------- | ----------------------- | ----------------------- | ----------------------- | ------------------------ | ------------------------ | ------------------------ |
| PolarDB-PG        | 46                      | 38                      | 37                      | 37                       | 36                       | 36                       |
| Postgres          | 44                      | 38                      | 33                      | 33                       | 29                       | 32                       |



6. 延迟测试场景：测试数据库在高延迟网络环境(100ms延时)

| 数据库/并发数/TPS | clients: 10 <br/>threads: 10 | clients: 30 <br/>threads: 10 | clients: 50 <br/>threads: 10 | clients: 100 <br/>threads: 10 | clients: 300 <br/>threads: 10 | clients: 500 <br/>threads: 10 |
| ----------------- | ----------------------- | ----------------------- | ----------------------- | ------------------------ | ------------------------ | ------------------------ |
| PolarDB-PG        | 45                      | 37                      | 32                      | 30                       | 34                       | 32                       |
| Postgres          | 45                      | 38                      | 36                      | 36                       | 35                       | 35                       |


### 应用测试
| Clients: 10 | create product.template | create res.partner | create puchase.order | confirm purchase.order | create sale.order | confirm sale.order |
| ----------- | ----------------------- | ------------------ | -------------------- | ---------------------- | ----------------- | ------------------ |
| PolarDB-PG  | 4.33                    | 7.68               | 4.93                 | 3.99                   | 12.67             | 9.61               |
| Postgres    | 4.50                    | 11.60              | 4.85                 | 4.11                   | 6.71              | 4.57               |



| Clients: 20 | create product.template | create res.partner | create puchase.order | confirm purchase.order | create sale.order | confirm sale.order |
| ----------- | ----------------------- | ------------------ | -------------------- | ---------------------- | ----------------- | ------------------ |
| PolarDB-PG  | 4.19                    | 5.57               | 4.64                 | 4.25                   | 9.38              | 6.66               |
| Postgres    | 4.81                    | 5.83               | 6.18                 | 4.44                   | 12.28             | 5.28               |



| Clients: 30 | create product.template | create res.partner | create puchase.order | confirm purchase.order | create sale.order | confirm sale.order |
| ----------- | ----------------------- | ------------------ | -------------------- | ---------------------- | ----------------- | ------------------ |
| PolarDB-PG  | 6.02                    | 6.69               | 4.71                 | 4.54                   | 12.72             | 5.77               |
| Postgres    | 5.56                    | 9.71               | 4.54                 | 4.41                   | 11.24             | 5.57               |



| Clients: 50 | create product.template | create res.partner | create puchase.order | confirm purchase.order | create sale.order | confirm sale.order |
| ----------- | ----------------------- | ------------------ | -------------------- | ---------------------- | ----------------- | ------------------ |
| PolarDB-PG  | 6.18                    | 6.16               | 4.77                 | 4.93                   | 12.54             | 6.68               |
| Postgres    | 5.77                    | 6.88               | 5.04                 | 5.93                   | 10.50             | 8.64               |



| Clients: 100 | create product.template | create res.partner | create puchase.order | confirm purchase.order | create sale.order | confirm sale.order |
| ------------ | ----------------------- | ------------------ | -------------------- | ---------------------- | ----------------- | ------------------ |
| PolarDB-PG   | 6.35                    | 6.76               | 5.39                 | 5.25                   | 6.92              | 5.53               |
| Postgres     | 6.75                    | 7.32               | 5.58                 | 4.94                   | 8.75              | 5.85               |


## 测试步骤
### 基准测试
1. 进入[tests](tests)目录，分别执行 [pgbench_pd.sh](tests%2Fpgbench_pd.sh) 和 [pgbench_pg.sh](tests%2Fpgbench_pg.sh) 
2. 进入[data](tests%2Fdata) 查看测试结果

### 应用测试
1. 数据初始：分别执行 [odoo_init_pd.py](tests%2Fodoo_init_pd.py) 和 [odoo_init_pg.py](tests%2Fodoo_init_pg.py) 
2. 应用测试：分别执行 [odoo_pd.sh](tests%2Fodoo_pd.sh) 和 [odoo_pg.sh](tests%2Fodoo_pg.sh)
3. 进入[data](tests%2Fdata) 查看测试结果

## 测试环境

| 实例    | 配置                                                        | 备注                                                                           | 链接                                                                                                                               |
|-------|-----------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 数据服务器 | 阿里云 4 vCPU 16 GiB （I/O优化）<br/>ecs.g7.xlarge   20Mbps （峰值） | CentOS 7.0；PolarDB-PG(11.9)和Postgres(11.21)都直接部署在这个服务器                       | PolarDB-PG参数：[postgresql-pd.conf](odoopd%2Fpostgresql-pd.conf)<br/> Postgres参数：[postgresql-pg.conf](odoopg%2Fpostgresql-pg.conf) |
| 应用服务器 | 阿里云 4 vCPU 16 GiB （I/O优化）<br/>ecs.g7.xlarge   20Mbps （峰值） | Ubuntu 22.04；通过docker部署，两个ODOO(16社区版)环境，后端分别为PolarDB-PG和Postgres，前端通过NGINX代理 | NGINX参数：[nginx.conf.example](nginx%2Fnginx.conf.example)<br/> ODOO-PG参数：[odoo.conf.example](odoopg%2Fconfig%2Fodoo.conf.example)<br/> ODOO-PD参数：[odoo.conf.example](odoopd%2Fconfig%2Fodoo.conf.example) |




## 环境部署
### 准备工作
1. 安装docker、docker compose: https://docs.docker.com/engine/install/

### PolarDB-PG和Postgres数据库服务器部署
部署文档：https://github.com/digoal/blog/blob/master/202310/20231011_01.md#%E5%AE%9E%E7%8E%B0%E5%92%8C%E5%AF%B9%E7%85%A7
备注: 版本11的PolarDB-PG需要 `drop extension pg_trgm CASCADE;` 

### ODOO服务器部署
两个ODOO(16社区版)环境，后端数据库分别为PolarDB-PG和Postgres。部署步骤如下：
1. `git clone https://github.com/shanghaiopen/PolarDB-PG-Benchmark.git`
2. `cd PolarDB-PG-Benchmark`
3. `cp .env.example .env`, 更新 `.env` 变量
4. `cp nginx/nginx.conf.example nginx/nginx.conf`
5. `cp odoopd/config/odoo.conf.example odoopd/config/odoo.conf`
6. `cp odoopg/config/odoo.conf.example odoopg/config/odoo.conf`
7. `chmod -R 777 odoop*`
8. `docker compose up -d`
9. DNS解析设置：通过域名DSN服务器或者通过修改应用客户端hosts, 分别设置odoopd和odoopg两个服务的域名解析，域名同 .env内的`PG_ODOO_HOST`和`PD_ODOO_HOST`环境变量
10. 实例起来之后，通过浏览器访问odoo，在URL输入`http://` `.env`配置的`PG_ODOO_HOST`或`PD_ODOO_HOST`,然后分别对pg和PolarDB数据库后端进行配置：创建数据库, 安装销售、采购、库存等应用模块

更详细的部署可参考: https://github.com/digoal/blog/blob/master/202310/20231011_01.md


