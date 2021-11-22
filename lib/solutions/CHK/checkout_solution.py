# noinspection PyUnusedLocal
# skus = unicode string

prices = {'A': [(5, 40), (3, 130 / 3), (1, 50)],
          'B': [(2, 45 / 2), (1, 30)],
          'C': [(1, 20)],
          'D': [(1, 15)],
          'E': [(1, 40)],
          'F': [(3, 20 / 3), (1, 10)],
          'G': [(1, 20)],
          'H': [(10, 8), (5, 9), (1, 10)],
          'I': [(1, 35)],
          'J': [(1, 60)],
          'K': [(2, 75), (1, 80)],
          'L': [(1, 90)],
          'M': [(1, 15)],
          'N': [(1, 40)],
          'O': [(1, 10)],
          'P': [(5, 40), (1, 50)],
          'Q': [(3, 80 / 3), (1, 30)],
          'R': [(1, 50)],
          'U': [(4, 120 / 4), (1, 40)],
          'V': [(3, 130 / 3), (2, 45), (1, 50)],
          'W': [(1, 20)]
          }
group = ['S', 'T', 'X', 'Y', 'Z']
group_unit_prices = [('X', 17), ('S', 20), ('T', 20), ('Y', 20), ('Z', 21)]
group_multiple = 3
group_price = 45
freebies = {'E': 'B', 'N': 'M', 'R': 'Q'}
freebie_multiples = {'E': 2, 'N': 3, 'R': 3}


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


def extract_groups(skus):
    grouped = [sku for sku in skus if sku in group]
    non_grouped = [sku for sku in skus if sku not in group]
    return non_grouped, grouped


def calc_group_price(group_skus):
    sort_order = ''.join(x[0] for _, x in enumerate(group_unit_prices))
    sorted_group_skus = 
    quantities = {sku: group_skus.count(sku) for sku in group_skus}

    sorted_group_skus = dict(sorted(quantities.items(), key=lambda item:
                             item[1]))



def checkout(skus):
    if not valid_skus(skus):
        return -1
    skus, group_skus = extract_groups(skus)
    quantities = {sku: skus.count(sku) for sku in skus}
    quantities = remove_freebies(quantities)
    non_group_total = sum(
        calc_price(sku, quantity) for sku, quantity in quantities.items())
    group_total = calc_group_price(group_skus)
    return non_group_total + group_total


