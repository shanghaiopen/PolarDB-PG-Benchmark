import datetime

from scripts.tools.odoo import Client
from scripts.odoo_app import create_partners, create_products, create_purchase, confirm_purchase, create_sale, confirm_sale, validate_pickings

url = 'http://odoopg.test.shanghaiopen.org.cn'
db = 'odoo'


if __name__ == "__main__":
    print('事务, 明细, 并发, 发送请求, 成功请求, 耗时, SPT, TPS, Note')
    concurrences = [(10, 30), (20, 15), (30, 10), (50, 6), (100, 3), (150, 2), (300, 1)]
    for concurrency, request_number in concurrences:
        clients = []
        users = [
            {'url': url, 'db': db, 'username': f'user_{i + 1:0>3d}', 'password': '1'}
            for i in range(0, concurrency)
        ]
        for user in users:
            clients.append(Client(url, db, user['username'], user['password']))

        # 创建 product.template
        create_products(clients, request_number, concurrency)

        # 创建 res.partner
        create_partners(clients, request_number, concurrency)

        # 创建采购订单
        create_purchase(clients, request_number, 10, concurrency)
        create_purchase(clients, request_number, 30, concurrency)
        create_purchase(clients, request_number, 50, concurrency)
        create_purchase(clients, request_number, 100, concurrency)

        # 确认采购订单
        confirm_purchase(clients, request_number, 10, concurrency)
        confirm_purchase(clients, request_number, 30, concurrency)
        confirm_purchase(clients, request_number, 50, concurrency)
        confirm_purchase(clients, request_number, 100, concurrency)

        # # 审核采购入库
        # validate_pickings(clients, request_number, 10, concurrency, 'incoming')
        # validate_pickings(clients, request_number, 30, concurrency, 'incoming')
        # validate_pickings(clients, request_number, 50, concurrency, 'incoming')
        # validate_pickings(clients, request_number, 100, concurrency, 'incoming')

        # 创建销售订单
        create_sale(clients, request_number, 10, concurrency)
        create_sale(clients, request_number, 30, concurrency)
        create_sale(clients, request_number, 50, concurrency)
        create_sale(clients, request_number, 100, concurrency)

        # 确认销售订单
        confirm_sale(clients, request_number, 10, concurrency)
        confirm_sale(clients, request_number, 30, concurrency)
        confirm_sale(clients, request_number, 50, concurrency)
        confirm_sale(clients, request_number, 100, concurrency)

        # # 审核销售出库
        # validate_pickings(clients, request_number, 10, concurrency, 'outcoming')
        # validate_pickings(clients, request_number, 30, concurrency, 'outcoming')
        # validate_pickings(clients, request_number, 50, concurrency, 'outcoming')
        # validate_pickings(clients, request_number, 100, concurrency, 'outcoming')



