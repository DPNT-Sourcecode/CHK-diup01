# noinspection PyUnusedLocal
# skus = unicode string

prices = {'A': [(5, 40), (3, 130 / 3), (1, 50)], 'B': [(2, 45/2), (1, 30)],
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
    price = 0
    remainder = quantity
    for index, tuple in enumerate(prices[sku]):
        multiple = tuple[0]
        unit_price = tuple[1]
        if unit_price == 1:
            price += remainder * unit_price
        else:
            price += (remainder // multiple) * multiple * unit_price
            remainder = remainder % multiple
    return price


def checkout(skus):
    if not valid_skus(skus):
        return -1
    quantities = {sku: skus.count(sku) for sku in skus}
    quantities = remove_freebies(quantities)
    total = sum(calc_price(sku, quantity) for sku, quantity in quantities.items())
    return total

