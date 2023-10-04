import xmlrpc.client


class Client(object):
    """
    odoo 客户端基于 xmlrpc 封装...
    """

    def __init__(self, url, db, username, password):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
        self.uid = self._login()

    def _login(self):
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        uid = common.authenticate(self.db, self.username, self.password, {})
        return uid

    def execute(self, *args, **kwargs):
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
        res = models.execute_kw(self.db, self.uid, self.password, *args, **kwargs)
        return res


if __name__ == "__main__":
    url = 'http://odoopg.test.shanghaiopen.org.cn'
    username = 'admin'
    password = 'admin'
    db = 'odoo'
    client = Client(url=url, db=db, username=username, password=password)
    res = client.execute('sale.order', 'create', [{'partner_id': 2660, 'note': 10, 'order_line': [(0, 0, {'name': 'product_100', 'product_id': 100, 'product_uom_qty': 1, 'price_unit': 1}), (0, 0, {'name': 'product_101', 'product_id': 101, 'product_uom_qty': 1, 'price_unit': 1}), (0, 0, {'name': 'product_102', 'product_id': 102, 'product_uom_qty': 1, 'price_unit': 1}), (0, 0, {'name': 'product_103', 'product_id': 103, 'product_uom_qty': 1, 'price_unit': 1}), (0, 0, {'name': 'product_104', 'product_id': 104, 'product_uom_qty': 1, 'price_unit': 1}), (0, 0, {'name': 'product_105', 'product_id': 105, 'product_uom_qty': 1, 'price_unit': 1}), (0, 0, {'name': 'product_106', 'product_id': 106, 'product_uom_qty': 1, 'price_unit': 1}), (0, 0, {'name': 'product_107', 'product_id': 107, 'product_uom_qty': 1, 'price_unit': 1}), (0, 0, {'name': 'product_108', 'product_id': 108, 'product_uom_qty': 1, 'price_unit': 1}), (0, 0, {'name': 'product_109', 'product_id': 109, 'product_uom_qty': 1, 'price_unit': 1})]}
])
    print(res)




