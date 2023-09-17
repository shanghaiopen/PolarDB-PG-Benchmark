# PolarDB-PG-Benchmark



## 环境部署
### 准备工作
1. 安装docker、docker compose: https://docs.docker.com/engine/install/

### PolarDB-PG和Postgres数据库服务器部署
略

### ODOO服务器部署
两个ODOO环境，后端数据库分别为PolarDB-PG和Postgres。部署步骤如下：
1. `git clone https://github.com/shanghaiopen/PolarDB-PG-Benchmark.git`
2. `cd PolarDB-PG-Benchmark`
3. `cp .env.example .env`, 更新 `.env` 变量
4. `cp nginx/nginx.conf.example nginx/nginx.conf`
5. `cp odoopd/config/odoo.conf.example odoopd/config/odoo.conf`
6. `cp odoopg/config/odoo.conf.example odoopg/config/odoo.conf`
7. `docker compose up -d`



