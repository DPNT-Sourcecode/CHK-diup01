

# noinspection PyUnusedLocal
# skus = unicode string

prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

def checkout(skus):
    total = sum(sku * price for sku, price in prices.items())
    return total
