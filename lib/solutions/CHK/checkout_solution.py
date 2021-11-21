

# noinspection PyUnusedLocal
# skus = unicode string

prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, '3A': 130, '2B': 45}


def valid_skus(skus):
    for sku in skus:
        if (sku not in prices) and (sku not in ['2', '3']):
            return False
    return True


def checkout(skus):
    if not valid_skus(skus):
        return -1
    item_list = get_itemlist(skus)
    total = sum(item * prices.get(item, 0) for item in item_list)
    return total


def get_itemlist(skus):
    items = None
    for sku in skus:
        if not items:
            items = sku
        elif sku.isnumeric():
            items = items.join(['', sku])
        else:
            items = items.join(['|', sku])

    itemlist = items.split('|')
    return itemlist


