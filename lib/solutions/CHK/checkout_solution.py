

# noinspection PyUnusedLocal
# skus = unicode string

prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
offer_prices = {'A': 130, 'B': 45}
offer_multiples = {'A': 3, 'B': 2}


def valid_skus(skus):
    for sku in skus:
        if sku not in prices:
            return False
    return True


def checkout(skus):
    if not valid_skus(skus):
        return -1
    quantities = {sku: skus.count(sku) for sku in skus}
    normal_quantities = {sku: quantities.get(sku)}
    total = sum(quantities.get(sku, 0) * prices.get(sku, 0) for sku in skus)
    return total

