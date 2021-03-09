import re
from re import Pattern
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from specs_pb2 import IbanFormatSpec
    from ibans import Bank, Account, Country
from .iban_format import IbanFormat


class Iban:
    """
    This class represents a parsed IBAN
    """
    def __init__(
            self, check_digit: str, basic_bank_account_number: str,
            formats: 'IbanFormatSpec',
            bank: 'Bank', account: 'Account', country: 'Country'):
        """
        __init__ Constructs an IBAN

        Constructs an IBAN providing its format and rest of data

        :param check_digit:The country two number check code
        :type check_digit: str
        :param basic_bank_account_number: The BBAN (Basic Bank Account Number) the number that uniquely
                identifies an account in the country
        :type basic_bank_account_number: str
        :param formats: Iban Formats
        :type formats: IbanFormatSpec
        :param bank: Bank data
        :type bank: Bank
        :param account: Account information
        :type account: Account
        :param country: Country data
        :type country: Country
        """

        self.__check_digit: str = check_digit
        self.__basic_bank_account_number: str = basic_bank_account_number
        self.__formats: 'IbanFormatSpec' = formats
        self.__bank: 'Bank' = bank
        self.__account: 'Account' = account
        self.__country: 'Country' = country

    @property
    def check_digit(self):
        return self.__check_digit

    @property
    def basic_bank_account_number(self):
        return self.__basic_bank_account_number

    @property
    def formats(self):
        return self.__formats

    @property
    def bank(self):
        return self.__bank

    @property
    def account(self):
        return self.__account

    @property
    def country(self):
        return self.__country

    def __str__(self) -> str:
        """
        __str__ Returns a string representing the iban

        :return: The IBAN as a string
        :rtype: str
        """

        return self.country.code + self.check_digit + self.basic_bank_account_number

    def format(self, iban_format: 'IbanFormat') -> str:
        """
        format Format Formats an IBAN

        Formats IBAN as specified per country

        :params iban_format: Iban format
        :type iban_format: str
        :return: Format iban string
        :rtype: str
        """

        iban = self.__iban_formatter(iban_format=iban_format)
        return iban

    def __iban_formatter(self, iban_format: 'IbanFormat') -> str:
        """
        __iban_formatter formats the iban by putting spaces inside the string

        :param iban_format: the format type
        :type iban_format: IbanFormat
        :return: The IBAN as a formatted string
        :rtype: str
        """
        is_hidden: bool = iban_format == IbanFormat.PRINT_HIDDEN or iban_format == IbanFormat.ELECTRONIC_HIDDEN
        is_print: bool = iban_format == IbanFormat.PRINT or iban_format == IbanFormat.PRINT_HIDDEN
        basic_bank_account_number = self.basic_bank_account_number

        if is_hidden:
            bban_length = len(basic_bank_account_number) - 4
            bban = "*******************************"
            basic_bank_account_number = bban[:bban_length] + basic_bank_account_number[-4:]

        iban = f"{self.country.code}{self.check_digit}{basic_bank_account_number}"
        if is_print:
            pattern: Pattern = re.compile(self.formats.print.pattern)
            iban = pattern.sub(self.formats.print.replacement.replace("$", "\\"), iban)

        return iban
