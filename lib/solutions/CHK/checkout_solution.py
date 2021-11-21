

# noinspection PyUnusedLocal
# skus = unicode string

prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
offer_prices{'A': 130, 'B': 45}

def valid_skus(skus):
    for sku in skus:
        if sku not in prices:
            return False
    return True


def checkout(skus):
    if not valid_skus(skus):
        return -1
    quantities = {sku: skus.count(sku) for sku in skus}
    total = sum(quantities.get(sku, 0) * prices.get(sku, 0) for sku in skus)
    return total
