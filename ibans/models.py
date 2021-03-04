from enum import Enum


class IbanFormat(Enum):
    PRINT = 0
    ELECTRONIC = 1
    PRINT_HIDDEN = 3
    ELECTRONIC_HIDDEN = 4


class Country:
    def __init__(self, code: str, name: str) -> None:
        self.__code = code
        self.__name = name
        """
        __init__ Constructs a country object

        :param code: Country alpha 2 code
        :type code: str
        :param name: Country Name
        :type name: str
        """

    @property
    def code(self) -> str:
        return self.__code

    @property
    def name(self) -> str:
        return self.__name


class Account:
    def __init__(self, number: str, account_type: str = None,
                 holder: str = None, currency_code: str = None,
                 balance_account: str = None,
                 owner_account_number: str = None) -> None:
        self.__number = number
        self.__account_type = account_type
        self.__holder = holder
        self.__currency_code = currency_code
        self.__balance_account = balance_account
        self.__owner_account_number = owner_account_number
        """
        __init__ Constructs a bank account

        Provided the Account number and other data
        :param number: The account number
        :type number: str
        :param account_type: The account type
        :type account_type: str
        :param holder: Account holder
        :type holder: str
        :param currency_code: currency code
        :type currency_code: str
        :param balance_account: balance account number
        :type balance_account: str
        :param owner_account_number: owner account number
        :type owner_account_number: str
        """

    @property
    def number(self):
        return self.number

    @property
    def account_type(self):
        return self.account_type

    @property
    def holder(self):
        return self.holder

    @property
    def currency_code(self):
        return self.currency_code

    @property
    def balance_account(self):
        return self.balance_account

    @property
    def owner_account_number(self):
        return self.owner_account_number


class Bank:
    """
    Represents a bank in a country
    """
    def __init__(self, code: str, name: str, branch: str = None, short_name: str = None, swift: str = None):
        self.__name = name
        self.__code = code
        self.__branch = branch
        self.__short_name = short_name
        self.__swift = swift
        """Constructs a bank object
        
        Provided the bank national code and rest of information
        :param code: Bank national code
        :type code: str
        :param name: bank name
        :type code: str
        :param branch: Bank branch
        :type branch: str
        :param short_name: Bank initials or short name
        :type short_name: str
        :param swift: Bank SWIFT/BIC code
        type swift: str
        """

    @property
    def name(self):
        return self.__name

    @property
    def code(self):
        return self.__code

    @property
    def branch(self):
        return self.__branch

    @property
    def short_name(self):
        return self.__short_name

    @property
    def swift(self):
        return self.__swift


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
