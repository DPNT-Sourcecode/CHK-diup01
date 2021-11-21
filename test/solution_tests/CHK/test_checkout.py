from solutions.CHK import checkout_solution


class TestCheckout:

    def test_checkout(self):
        skus = 'A2BD'
        expected = 110
        assert expected == checkout_solution.checkout(skus)

    def test_valid_skus(self):
        assert checkout_solution.valid_skus('A2BC')

    def test_invalid_skus(self):
        assert checkout_solution.valid_skus('invalid') == False




