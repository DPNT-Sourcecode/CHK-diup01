# noinspection PyUnusedLocal
# skus = unicode string

prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
offer_prices = {'A': 130, 'B': 45}
offer_multiples = {'A': 3, 'B': 2}
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


def checkout(skus):
    if not valid_skus(skus):
        return -1
    quantities = {sku: skus.count(sku) for sku in skus}
    quantities = remove_freebies(quantities)
    normal_quantities = {sku: (quantities[sku] % offer_multiples[
        sku]) if sku in offer_multiples else quantities[sku] for sku in skus}
    non_offer_total = sum(
        normal_quantities.get(sku, 0) * prices.get(sku, 0) for sku
        in normal_quantities)
    offer_quantities = {sku: quantities.get(sku, 0) // offer_multiples.get(
        sku) for sku in offer_multiples}
    offer_total = sum(offer_quantities.get(sku, 0) * offer_prices.get(sku,
                                                                      0) for
                      sku in offer_multiples)
    return non_offer_total + offer_total
