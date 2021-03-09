
class TestCalculateMod97:

    def test_calculate_mod97(self):
        valid_iban: str = "GE60NB0000000123456789"
        mod97 = __calculate_mod97(valid_iban)

        assert mod97 == 1, "Should be 1"
