from solutions.CHK.checkout_solution import checkout, valid_skus


class TestCheckout:

    def test_checkout_no_offer(self):
        skus = 'ABDA'
        expected = 145
        assert expected == checkout(skus)

    def test_checkout_with_offer(self):
        skus = 'DADAABB'
        expected = 130 + 45 + 30
        assert expected == checkout(skus)

    def test_checkout_aaa(self):
        skus = 'AAA'
        expected = 130
        assert expected == checkout(skus)

    def test_valid_skus(self):
        assert valid_skus('ABCBBD')

    def test_invalid_skus(self):
        assert valid_skus('invalid') == False

    def test_freebie_offer_all_free(self):
        skus = 'DEEEB'
        expected = 15 + 3 * 40
        assert expected == checkout(skus)

    def test_freebie_offer_not_all_free(self):
        skus = 'DEEEBB'
        expected = 15 + 3 * 40 + 30
        assert expected == checkout(skus)

    def test_3_for_2_exact(self):
        skus = 'FFFFFFD'
        expected = 55
        assert expected == checkout(skus)

    def test_3_for_2_remainder_2(self):
        skus = 'FFFFFD'
        expected = 55
        assert expected == checkout(skus)

    def test_3_for_2_remainder_1(self):
        skus = 'FFFFD'
        expected = 45
        assert expected == checkout(skus)

    def test_h_10(self):
        skus = 10 * 'H'
        assert 80 == checkout(skus)

    def test_h_5(self):
        skus = 5 * 'H'
        assert 45 == checkout(skus)

    def test_h_17(self):
        skus = 17 * 'H'
        expected = 80 + 45 + 20
        assert expected == checkout(skus)

    def test_k_3(self):
        skus = 3 * 'K'
        expected = 150 + 80
        assert expected == checkout(skus)

    def test_n(self):
        skus = 'NNNNMM'
        expected = 4 * 40 + 15
        assert expected == checkout(skus)

    def test_p(self):
        skus = 7 * 'P'
        expected = 200 + 100
        assert expected == checkout(skus)

    def test_q(self):
        skus = 4 * 'Q'
        expected = 80 + 30
        assert expected == checkout(skus)

    def test_r(self):
        skus = 7 * 'R' + 12 * 'Q'
        expected = 7 * 50 + 3 * 80 + 30
        assert expected == checkout(skus)

    def test_u_7(self):
        skus = 7 * 'U'
        expected = 6 * 40
        assert expected == checkout(skus)

    def test_u_9(self):
        skus = 9 * 'U'
        expected = 7 * 40
        assert expected == checkout(skus)

    def test_v_10(self):
        skus = 10 * 'V'
        expected = 3 * 130 + 50
        assert expected == checkout(skus)

    def test_v_17(self):
        skus = 17 * 'V'
        expected = 5 * 130 + 90
        assert expected == checkout(skus)


