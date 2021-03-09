import ibans
import pkg_resources
import pytest


class TestIbanParser:

    @pytest.fixture
    def sample_ibans(self):
        stream = pkg_resources.resource_stream(
            __name__, "data/iban_test_sample.txt")
        return [line.decode('utf-8') for line in stream]

    def test_iban_parser(self, sample_ibans):
        for line in sample_ibans:
            country_code, check_digit, bban, iban_str = line.split("|")
            if len(country_code) > 2:
                continue
            iban_str = iban_str.rstrip()
            iban = ibans.parse(iban_str)
            assert iban.country.code == country_code
            assert iban.check_digit == check_digit
            assert iban.basic_bank_account_number == bban
