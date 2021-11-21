

# noinspection PyUnusedLocal
# skus = unicode string

prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}


def valid_skus(skus):
    for sku in skus:
        if (sku not in prices) and (sku not in ['2', '3']):
            return False
    return True


def checkout(skus):
    if not valid_skus(skus):
        return -1

    itemlist = ''
    for sku in skus:
        if sku.isnumeric():
            


    total = sum(sku * price for sku, price in prices.items())
    return total




