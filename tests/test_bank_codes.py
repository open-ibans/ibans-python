import ibans
import pytest


class TestBankCodes:

    @pytest.fixture
    def ao_atlantico_iban(self) -> str:
        return "AO06005500009209313310152"

    @pytest.fixture
    def ao_bai_iban(self) -> str:
        return "AO06004000008043114110135"

    @pytest.fixture
    def french_iban(self) -> str:
        return "FR7630006000011234567890189"

    def test_french_bank_name(self, french_iban):
        iban = ibans.parse(french_iban)

        assert iban.bank.name is None

    def test_bai_bank_name(self, ao_bai_iban):
        iban = ibans.parse(ao_bai_iban)

        assert 'Banco Angolano de Investimentos, S.A.' == iban.bank.name

    def test_atlantico_bank_name(self, ao_atlantico_iban):
        iban = ibans.parse(ao_atlantico_iban)

        assert 'Banco Privado Atlântico, S.A.' == iban.bank.name

    def test_french_sigla(self, french_iban):
        iban = ibans.parse(french_iban)

        assert iban.bank.short_name is None

    def test_bai_sigla(self, ao_bai_iban):
        iban = ibans.parse(ao_bai_iban)

        assert 'BAI' == iban.bank.short_name

    def test_atlantico_sigla(self, ao_atlantico_iban):
        iban = ibans.parse(ao_atlantico_iban)
        print('iban.country')
        print(iban.country)
        print('iban.country_code')
        print(iban.country.code)
        print('iban.check_digit')
        print(iban.check_digit)
        print('iban.basic_bank_account_number')
        print(iban.basic_bank_account_number)
        print('iban.bank_code')
        print(iban.bank.code)
        print('iban.account_number')
        print(iban.account.number)
        print('iban.bank_name')
        print(iban.bank.name)
        print('iban.sigla')
        print(iban.bank.short_name)
        print('iban.swift_bic')
        print(iban.bank.swift)
        print('iban.branch_code')
        print(iban.bank.branch)
        print('iban.account_type')
        print(iban.account.account_type)
        print('iban.account_holder')
        print(iban.account.holder)
        print('iban.balance_account_number')
        print(iban.account.balance_account)
        print('iban.currency_code')
        print(iban.account.currency_code)

        assert 'BPA' == iban.bank.short_name
