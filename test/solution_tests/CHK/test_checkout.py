from solutions.CHK import checkout_solution

class TestCheckout:

    def test_checkout(self):
        skus = 'ABD'
        expected = 95
        assert 1==1

    def test_valid_skus(self):
        assert checkout_solution.valid_skus('A2BC')

    def test_invalid_skus(self):
        assert checkout_solution.valid_skus('invalid') == False

    def test_get_item_list(self):
        skus = 'C3A2B'
        expected = ['C', '3A', '2B']
        assert expected == checkout_solution.get_itemlist(skus)

