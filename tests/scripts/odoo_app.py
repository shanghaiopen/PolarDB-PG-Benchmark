import datetime
import random
import time

from .tools.tools import future_multi_process


def create_partners(clients, number, pool_size):
    time.sleep(5)
    counts1 = clients[0].execute('res.partner', 'search_count', [[]])
    vals = [{'ref': f'{i + 1:0>3d}', 'name': f'Partner_{i + 1:0>4d}'} for i in range(0, number)]
    states = []
    for val in vals:
        for client in clients:
            state = (client, 'execute', ['res.partner', 'create', [val]])
            states.append(state)

    time_begin = datetime.datetime.now()
    future_multi_process(pool_size, states)
    time_end = datetime.datetime.now()
    time_spend = (time_end - time_begin).seconds
    counts2 = clients[0].execute('res.partner', 'search_count', [[]])

    msg = (
        f"创建res.partner, 无, {pool_size}, {number * pool_size}, {counts2 - counts1}, {time_spend}, "
        f"{time_spend / (number * pool_size)}, {(number * pool_size) / time_spend}, 无")
    print(msg)
    time.sleep(5)


def create_products(clients, number, pool_size):
    time.sleep(5)
    counts1 = clients[0].execute('product.template', 'search_count', [[]])
    vals = [{'default_code': f'{i + 1:0>4d}', 'name': f'Product_{i + 1:0>4d}', 'detailed_type': 'product'} for i in range(0, number)]
    states = []
    for val in vals:
        for client in clients:
            state = (client, 'execute', ['product.template', 'create', [val]])
            states.append(state)

    time_begin = datetime.datetime.now()
    future_multi_process(pool_size, states)
    time_end = datetime.datetime.now()
    time_spend = (time_end - time_begin).seconds
    counts2 = clients[0].execute('product.template', 'search_count', [[]])

    msg = (
        f"创建product.template, 无, {pool_size}, {number * pool_size}, {counts2 - counts1}, {time_spend}, "
        f"{time_spend / (number * pool_size)}, {(number * pool_size) / time_spend}, 无")
    print(msg)
    time.sleep(5)


def create_purchase(clients, number, line, pool_size):
    time.sleep(5)
    counts1 = clients[0].execute('purchase.order', 'search_count', [[]])
    vals = [{'partner_id': random.randint(10, 1000), 'notes': line} for i in range(0, number)]
    states = []
    for val in vals:
        lines = [(0, 0, {'name': f'product_{i}', 'product_id': i, 'product_qty': 1, 'price_unit': 1}) for i in range(100, line+100)]
        val['order_line'] = lines
        for client in clients:
            state = (client, 'execute', ['purchase.order', 'create', [val]])
            states.append(state)

    time_begin = datetime.datetime.now()
    future_multi_process(pool_size, states)
    time_end = datetime.datetime.now()
    time_spend = (time_end - time_begin).seconds
    counts2 = clients[0].execute('purchase.order', 'search_count', [[]])

    msg = (
        f"创建purchase.order, {line}, {pool_size}, {number * pool_size}, {counts2 - counts1}, {time_spend}, "
        f"{time_spend / (number * pool_size)}, {(number * pool_size) / time_spend}, 无")
    print(msg)
    time.sleep(5)


def confirm_purchase(clients, number, line, pool_size):
    time.sleep(5)
    purchase_ids = clients[0].execute('purchase.order', 'search', [[['state', '=', 'draft']]], {'order': 'id asc'})
    counts1 = len(purchase_ids)
    states = []
    i = 0
    for purchase_id in purchase_ids:
        counts = clients[0].execute('purchase.order.line', 'search_count', [[['order_id', '=', purchase_id]]])
        if counts == line:
            i += 1
            state = (random.choice(clients), 'execute', ['purchase.order', 'button_confirm', [[purchase_id]]])
            states.append(state)
            if i >= number*pool_size:
                break

    time_begin = datetime.datetime.now()
    future_multi_process(pool_size, states)
    time_end = datetime.datetime.now()
    time_spend = (time_end - time_begin).seconds
    purchase_ids = clients[0].execute('purchase.order', 'search', [[['state', '=', 'draft']]])
    counts2 = len(purchase_ids)

    msg = (
        f"确认purchase.order, {line}, {pool_size}, {number * pool_size}, {counts1 - counts2}, {time_spend}, "
        f"{time_spend / (number * pool_size)}, {(number * pool_size) / time_spend}, 无")
    print(msg)
    time.sleep(5)


def validate_pickings(clients, number, line, pool_size, bound):
    time.sleep(5)
    picking_ids = clients[0].execute('stock.picking', 'search', [[['state', '=', 'assigned'], ['picking_type_id.code', '=', bound]]], {'order': 'id asc'})
    counts1 = len(picking_ids)
    states1 = []
    states2 = []
    i = 0
    for picking_id in picking_ids:
        counts = clients[0].execute('stock.move', 'search_count', [[['picking_id', '=', picking_id]]])
        if counts == line:
            i += 1
            state = (random.choice(clients), 'execute', ['stock.picking', 'action_set_quantities_to_reservation', [[picking_id]]])
            states1.append(state)
            if i >= number*pool_size:
                break
    for picking_id in picking_ids:
        counts = clients[0].execute('stock.move', 'search_count', [[['picking_id', '=', picking_id]]])
        if counts == line:
            i += 1
            state = (random.choice(clients), 'execute', ['stock.picking', 'button_validate', [[picking_id]]])
            states2.append(state)
            if i >= number*pool_size:
                break

    time_begin = datetime.datetime.now()
    future_multi_process(pool_size, states1)
    future_multi_process(pool_size, states2)
    time_end = datetime.datetime.now()
    time_spend = (time_end - time_begin).seconds
    picking_ids = clients[0].execute('stock.picking', 'search', [[['state', '=', 'assigned'], ['picking_type_id.code', '=', bound]]])
    counts2 = len(picking_ids)

    msg = (
        f"审核stock.picking-{bound}, {line}, {pool_size}, {number * pool_size}, {counts1 - counts2}, {time_spend}, "
        f"{time_spend / (number * pool_size)}, {(number * pool_size) / time_spend}, 无")
    print(msg)
    time.sleep(5)


def create_sale(clients, number, line, pool_size):
    time.sleep(5)
    counts1 = clients[0].execute('sale.order', 'search_count', [[]])
    vals = [{'partner_id': random.randint(1000, 4000), 'note': line} for i in range(0, number)]
    states = []
    for val in vals:
        lines = [(0, 0, {'name': f'product_{i}', 'product_id': i, 'product_uom_qty': 1, 'price_unit': 1}) for i in range(100, line+100)]
        val['order_line'] = lines
        for client in clients:
            state = (client, 'execute', ['sale.order', 'create', [val]])
            states.append(state)

    time_begin = datetime.datetime.now()
    future_multi_process(pool_size, states)
    time_end = datetime.datetime.now()
    time_spend = (time_end - time_begin).seconds
    counts2 = clients[0].execute('sale.order', 'search_count', [[]])

    msg = (
        f"创建sale.order, {line}, {pool_size}, {number * pool_size}, {counts2 - counts1}, {time_spend}, "
        f"{time_spend / (number * pool_size)}, {(number * pool_size) / time_spend}, 无")
    print(msg)
    time.sleep(5)


def confirm_sale(clients, number, line, pool_size):
    time.sleep(5)
    sale_ids = clients[0].execute('sale.order', 'search', [[['state', '=', 'draft']]], {'order': 'id asc'})
    counts1 = len(sale_ids)
    states = []
    i = 0
    for sale_id in sale_ids:
        counts = clients[0].execute('sale.order.line', 'search_count', [[['order_id', '=', sale_id]]])
        if counts == line:
            i += 1
            state = (random.choice(clients), 'execute', ['sale.order', 'action_confirm', [[sale_id]]])
            states.append(state)
            if i >= number*pool_size:
                break

    time_begin = datetime.datetime.now()
    future_multi_process(pool_size, states)
    time_end = datetime.datetime.now()
    time_spend = (time_end - time_begin).seconds
    purchase_ids = clients[0].execute('sale.order', 'search', [[['state', '=', 'draft']]])
    counts2 = len(purchase_ids)

    msg = (
        f"确认sale.order, {line}, {pool_size}, {number * pool_size}, {counts1 - counts2}, {time_spend}, "
        f"{time_spend / (number * pool_size)}, {(number * pool_size) / time_spend}, 无")
    print(msg)
    time.sleep(5)
