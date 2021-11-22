from solutions.CHK import checkout_solution


class TestCheckout:

    def test_checkout_no_offer(self):
        skus = 'ABDA'
        expected = 145
        assert expected == checkout_solution.checkout(skus)

    def test_checkout_with_offer(self):
        skus = 'DADAABB'
        expected = 130 + 45 + 30
        assert expected == checkout_solution.checkout(skus)

    def test_checkout_aaa(self):
        skus = 'AAA'
        expected = 130
        assert expected == checkout_solution.checkout(skus)

    def test_valid_skus(self):
        assert checkout_solution.valid_skus('ABCBBD')

    def test_invalid_skus(self):
        assert checkout_solution.valid_skus('invalid') == False

    def test_freebie_offer_all_free(self):
        skus = 'DEEEB'
        expected = 15 + 3 * 40
        assert expected == checkout_solution.checkout(skus)

    def test_freebie_offer_not_all_free(self):
        skus = 'DEEEBB'
        expected = 15 + 3 * 40 + 30
        assert expected == checkout_solution.checkout(skus)

    def test_3_for_2_exact(self):
        skus = 'FFFFFFD'
        expected = 55
        assert expected == checkout_solution.checkout(skus)

    def test_3_for_2_remainder_2(self):
        skus = 'FFFFFD'
        expected = 55
        assert expected == checkout_solution.checkout(skus)

    def test_3_for_2_remainder_1(self):
        skus = 'FFFFD'
        expected = 45
        assert expected == checkout_solution.checkout(skus)

