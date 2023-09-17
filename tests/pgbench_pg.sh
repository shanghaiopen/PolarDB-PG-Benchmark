export HOST='47.103.109.192'
export PORT='5434'
export THREADS="10"
export CLIENTS="10 30 50 100 300 500"

./scripts/pgbench_0.sh
./scripts/pgbench_1.sh > ./data/pgbench_pg_1.txt
./scripts/pgbench_2.sh > ./data/pgbench_pg_2.txt
./scripts/pgbench_3.sh > ./data/pgbench_pg_3.txt
./scripts/pgbench_4.sh > ./data/pgbench_pg_4.txt
./scripts/pgbench_5.sh > ./data/pgbench_pg_5.txt
./scripts/pgbench_6.sh > ./data/pgbench_pg_6.txt