import odooly
from scripts.odoo_ini import create_partners, create_users, create_locations, create_products

url = 'http://odoopg.test.shanghaiopen.org.cn'
user = 'admin'
password = 'admin'
db = 'odoo'
client = odooly.Client(server=url, db=db, user=user, password=password)


if __name__ == "__main__":
    create_users(client, 1000)
    create_partners(client, 1000)
    create_products(client, 1000)
    create_locations(client, 1000)
