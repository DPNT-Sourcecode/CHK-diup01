from solutions.CHK import checkout_solution


class TestCheckout:

    def test_checkout_no_offer(self):
        skus = 'ABBDA'
        expected = 175
        assert expected == checkout_solution.checkout(skus)

    def test_checkout_with_offer(self):
        skus = 'DADAABB'
        expected = 130 + 45 + 30
        assert expected == checkout_solution.checkout(skus)

    def test_valid_skus(self):
        assert checkout_solution.valid_skus('ABCBBD')

    def test_invalid_skus(self):
        assert checkout_solution.valid_skus('invalid') == False





