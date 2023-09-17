# PolarDB-PG-Benchmark

## 测试报告

### 基准测试

使用pgbench，6个场景下，PolarDB-PG和Postgres的性能表现情况。测试脚本和数据：[tests](tests)

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



## 测试环境

| 实例    | 配置                                                        | 备注                                                                           | 链接                                                                                                                               |
|-------|-----------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 数据服务器 | 阿里云 4 vCPU 16 GiB （I/O优化）<br/>ecs.g7.xlarge   20Mbps （峰值） | CentOS 7.0；PolarDB-PG(11.9)和Postgres(11.21)都直接部署在这个服务器                       | PolarDB-PG参数：[postgresql-pd.conf](odoopd%2Fpostgresql-pd.conf)<br/> Postgres参数：[postgresql-pg.conf](odoopg%2Fpostgresql-pg.conf) |
| 应用服务器 | 阿里云 4 vCPU 16 GiB （I/O优化）<br/>ecs.g7.xlarge   20Mbps （峰值） | Ubuntu 22.04；通过docker部署，两个ODOO(16社区版)环境，后端分别为PolarDB-PG和Postgres，前端通过NGINX代理 | NGINX参数：[nginx.conf.example](nginx%2Fnginx.conf.example)<br/> ODOO-PG参数：[odoo.conf.example](odoopg%2Fconfig%2Fodoo.conf.example)<br/> ODOO-PD参数：[odoo.conf.example](odoopd%2Fconfig%2Fodoo.conf.example) |




## 环境部署
### 准备工作
1. 安装docker、docker compose: https://docs.docker.com/engine/install/

### PolarDB-PG和Postgres数据库服务器部署
部署过程有待补充。备注: 版本11的PolarDB-PG需要 `drop extension pg_trgm CASCADE;` 

### ODOO服务器部署
两个ODOO(16社区版)环境，后端数据库分别为PolarDB-PG和Postgres。部署步骤如下：
1. `git clone https://github.com/shanghaiopen/PolarDB-PG-Benchmark.git`
2. `cd PolarDB-PG-Benchmark`
3. `cp .env.example .env`, 更新 `.env` 变量
4. `cp nginx/nginx.conf.example nginx/nginx.conf`
5. `cp odoopd/config/odoo.conf.example odoopd/config/odoo.conf`
6. `cp odoopg/config/odoo.conf.example odoopg/config/odoo.conf`
7. `docker compose up -d`
8. 实例起来之后，通过数据库管理页面，创建数据库 `odoo`, 安装销售、采购、库存等应用模块



