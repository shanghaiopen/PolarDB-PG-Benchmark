from .tools.tools import future_multi_process


def create_users(client, number):
    vals = [{'login': f'user_{i + 1:0>3d}', 'name': f'User_{i + 1:0>3d}', 'password': '1'} for i in range(0, number)]
    for val in vals:
        user_id = client.env['res.users'].create(val)
        print(user_id)


def create_partners(client, number):
    vals = [{'ref': f'{i + 1:0>3d}', 'name': f'Partner_{i + 1:0>4d}'} for i in range(0, number)]
    for val in vals:
        partner_id = client.env['res.partner'].create(val)
        print(partner_id)


def create_products(client, number):
    vals = [{'default_code': f'{i + 1:0>4d}', 'name': f'Product_{i + 1:0>4d}', 'detailed_type': 'product'} for i in range(0, number)]
    for val in vals:
        product_id = client.env['product.template'].create(val)
        print(product_id)


def create_locations(client, number):
    vals = [{'name': f'{i + 1:0>4d}', 'location_id': '8'} for i in range(0, number)]
    for val in vals:
        location_id = client.env['stock.location'].create(val)
        print(location_id)



