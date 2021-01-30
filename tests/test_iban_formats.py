from ibans import Iban, IbanFormat
import ibans
import pytest


class TestIbanFormats:

    @pytest.fixture
    def ao_bai_iban(self) -> Iban:
        return ibans.parse("AO06004000008043114110135")

    @pytest.fixture
    def ee_iban(self) -> Iban:
        return ibans.parse("EE382200221020145685")

    def test_angola_iban_electronic_format(self, ao_bai_iban):
        print = ao_bai_iban.format(IbanFormat.ELECTRONIC)

        assert "AO06004000008043114110135" == print

    def test_angola_iban_print_format(self, ao_bai_iban):
        print = ao_bai_iban.format(IbanFormat.PRINT)

        assert "AO06 0040 0000 8043 1141 1013 5" == print

    def test_angola_iban_print_hidden_format(self, ao_bai_iban):
        print = ao_bai_iban.format(IbanFormat.PRINT_HIDDEN)

        assert "AO06 **** **** **** **** *013 5" == print

    def test_angola_iban_electronic_hidden_format(self, ao_bai_iban):
        print = ao_bai_iban.format(IbanFormat.ELECTRONIC_HIDDEN)

        assert "AO06*****************0135" == print

    def test_estonia_iban_print_format(self, ee_iban):
        print = ee_iban.format(IbanFormat.PRINT)

        assert "EE38 22 00 2210 2014 568 5" == print

    def test_estonia_print_hidden_format(self, ee_iban):
        print = ee_iban.format(IbanFormat.PRINT_HIDDEN)

        assert "EE38 ** ** **** **** 568 5" == print
