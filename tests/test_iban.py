import ibans
import pytest


class TestIban:

    @pytest.fixture
    def ao_atlantico_iban(self) -> str:
        return "AO06005500009209313310152"

    @pytest.fixture
    def ao_bai_iban(self) -> str:
        return "AO06004000008043114110135"

    def test_iban_country_code(self, ao_bai_iban):
        iban = ibans.parse(ao_bai_iban)

        assert iban.country.code == "AO"

    def test_iban_basic_bank_account_number(self, ao_bai_iban):
        iban = ibans.parse(ao_bai_iban)

        assert iban.basic_bank_account_number == "004000008043114110135"

    def test_iban_bank_code(self, ao_atlantico_iban):
        iban = ibans.parse(ao_atlantico_iban)

        assert iban.bank.code == "055"

    def test_iban_account_number(self, ao_bai_iban):
        iban = ibans.parse(ao_bai_iban)

        assert iban.account.number == "80431141"

    def test_iban_country(self, ao_bai_iban):
        iban = ibans.parse(ao_bai_iban)

        assert iban.country.name == "Angola"

    def test_iban_check_digit(self, ao_bai_iban):
        iban = ibans.parse(ao_bai_iban)

        assert iban.check_digit == "06"
