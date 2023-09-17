# PolarDB-PG-Benchmark

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



