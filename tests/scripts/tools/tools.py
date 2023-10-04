from concurrent.futures import as_completed, Future, ProcessPoolExecutor, ThreadPoolExecutor
import multiprocessing


def future_multi_process(pool_size=None, states=tuple(tuple())):
    pool_size = pool_size
    results = []
    turns = len(states) // pool_size
    for i in range(0, turns+1):
        futures = []
        with ProcessPoolExecutor(max_workers=pool_size, mp_context=multiprocessing.get_context('spawn')) as executor:
            for obj, func, args in states[i*pool_size:(i+1)*pool_size]:
                f = executor.submit(future_multi_worker, obj, func, args)
                futures.append(f)
        as_completed(futures, timeout=10)
        results.extend(futures)
        executor.shutdown()
    return results


def future_multi_worker(obj, func, args):
    func = getattr(obj, func)
    action = func(*args)
    return action


if __name__ == "__main__":
    states = [
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
        ('res.partner', 'create', {'ref': '001', 'name': 'Partner_0001'}),
    ]

    future_multi_process(16, states)
