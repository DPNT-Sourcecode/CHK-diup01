# noinspection PyUnusedLocal
# skus = unicode string

prices = {'A': [(5, 40), (3, 130 / 3), (1, 50)], 'B': [(2, 45), (1, 30)],
          'C': [(1, 20)], 'D': [(1, 15)], 'E': [(1, 40)]}
freebies = {'E': 'B'}
freebie_multiples = {'E': 2}


def valid_skus(skus):
    for sku in skus:
        if sku not in prices:
            return False
    return True


def remove_freebies(quantities):
    free_skus = {freebies[sku]: quantities.get(sku, 0) // freebie_multiples[
        sku] for sku in freebies}
    result = {sku: quantities[sku] - free_skus.get(sku, 0) for sku in
              quantities}
    return result


def calc_price(sku: str, quantity: int) -> float:
    

def checkout(skus):
    if not valid_skus(skus):
        return -1
    quantities = {sku: skus.count(sku) for sku in skus}
    quantities = remove_freebies(quantities)
    total = sum(calc_price(sku, quantity) for sku, quantity in quantities.items())
    return sum

