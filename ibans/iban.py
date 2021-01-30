from enum import Enum


class IbanFormat(Enum):
    PRINT = 0
    ELECTRONIC = 1
    PRINT_HIDDEN = 3
    ELECTRONIC_HIDDEN = 4


class Iban:
    """
    This class represents a parsed IBAN
    """
    def __init__(
            self, iban_format: list,
            country_code: str, check_digit: str,
            bban: str, country: str,
            **kwargs):
        """
        Constructs an IBAN

        Constructs an IBAN providing its format and rest of data

        :param iban_format: A list of ints with the positions of the spaces
        :type iban_format: list
        :param country_code: A two letter country code
        :type country_code: str
        :param check_digit: The country two number check code
        :type check_digit: str
        :param bban: The BBAN (Basic Bank Account Number) the number that uniquely
                identifies an account in the country
        :type bban: str
        :param country: Name of the country
        :type country: str
        """

        self.__iban_format: list = iban_format
        self.country: str = country
        self.country_code: str = country_code
        self.check_digit: str = check_digit
        self.basic_bank_account_number: str = bban

        self.bank_code: str = kwargs.get('bank_code', None)
        self.account_number: str = kwargs.get('account_number', None)
        self.bank_name: str = kwargs.get('bank_name', None)
        self.sigla: str = kwargs.get('sigla', None)
        self.swift_bic: str = kwargs.get('swift_bic', None)
        self.branch_code: str = kwargs.get('branch_code', None)
        self.account_type: str = kwargs.get('account_type', None)
        self.account_holder: str = kwargs.get('account_holder', None)
        self.balance_account_number: str =\
            kwargs.get('balance_account_number', None)
        self.currency_code: str = kwargs.get('currency_code', None)

    def __str__(self) -> str:
        """
        Returns a string representing the iban

        :return: The IBAN as a string
        :rtype: str
        """

        return self.country_code + self.check_digit\
            + self.basic_bank_account_number

    def format(
            self, format: IbanFormat) -> str:
        """
        Formats an IBAN

        Formats IBAN as specified per country

        Parameters:
            format (IbanFormat): The printing format

        Returns:
            str: Formated string
        """

        formated_iban = self.__iban_formatter(format=format)
        return formated_iban

    def __iban_formatter(
            self, format: IbanFormat) -> str:
        """
        formats the iban by putting spaces inside the string

        :param format: the format type
        :type format: IbanFormat
        :return: The IBAN as a formatted string
        :rtype: str
        """            
        is_print_hidden = format == IbanFormat.PRINT_HIDDEN
        is_electronic_hidden = format == IbanFormat.ELECTRONIC_HIDDEN
        is_print = format == IbanFormat.PRINT

        if is_print_hidden or is_electronic_hidden:
            bban_length = len(self.basic_bank_account_number) - 4
            bban = "*******************************"
            bban = bban[:bban_length] + self.basic_bank_account_number[-4:]
        else:
            bban = self.basic_bank_account_number

        new_iban = f"{self.country_code}{self.check_digit}{bban}"

        if is_print or is_print_hidden:
            for pos in self.__iban_format:
                new_iban = new_iban[:pos] + ' ' + new_iban[pos:]

        return new_iban
