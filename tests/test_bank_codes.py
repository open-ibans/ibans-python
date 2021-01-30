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

        assert iban.bank_name is None

    def test_bai_bank_name(self, ao_bai_iban):
        iban = ibans.parse(ao_bai_iban)

        assert 'Banco Angolano de Investimentos, S.A.' == iban.bank_name

    def test_atlantico_bank_name(self, ao_atlantico_iban):
        iban = ibans.parse(ao_atlantico_iban)

        assert 'Banco Privado Atlântico, S.A.' == iban.bank_name

    def test_french_sigla(self, french_iban):
        iban = ibans.parse(french_iban)

        assert iban.sigla is None

    def test_bai_sigla(self, ao_bai_iban):
        iban = ibans.parse(ao_bai_iban)

        assert 'BAI' == iban.sigla

    def test_atlantico_sigla(self, ao_atlantico_iban):
        iban = ibans.parse(ao_atlantico_iban)
        print('iban.country')
        print(iban.country)
        print('iban.country_code')
        print(iban.country_code)
        print('iban.check_digit')
        print(iban.check_digit)
        print('iban.basic_bank_account_number')
        print(iban.basic_bank_account_number)
        print('iban.bank_code')
        print(iban.bank_code)
        print('iban.account_number')
        print(iban.account_number)
        print('iban.bank_name')
        print(iban.bank_name)
        print('iban.sigla')
        print(iban.sigla)
        print('iban.swift_bic')
        print(iban.swift_bic)
        print('iban.branch_code')
        print(iban.branch_code)
        print('iban.account_type')
        print(iban.account_type)
        print('iban.account_holder')
        print(iban.account_holder)
        print('iban.balance_account_number')
        print(iban.balance_account_number)
        print('iban.currency_code')
        print(iban.currency_code)

        assert 'BPA' == iban.sigla
