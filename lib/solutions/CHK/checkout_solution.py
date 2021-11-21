

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
    item_list = get_item_list(skus)
    total = sum(prices.get(item, 0) for item in item_list)
    return total


def get_item_list(skus):
    items = ''
    for sku in skus:
        if sku.isnumeric():
            items += sku
        else:
            items += f'{sku}|'
    items = items[0:-1]
    item_list = items.split('|')
    return item_list





