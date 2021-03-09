from typing import Optional
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from specs_pb2 import IbanSpec, BankData
    from . import Iban, Account, Country, Bank
    from re import Pattern, Match

from specs_pb2 import BanksData, IbansSpecs
from . import Iban, Account, Country, Bank
import pkg_resources
from .exception import ValueException, ParseException, InvalidBBANException,\
    InvalidCheckDigitException, InvalidMod97Exception, InvalidReservedValues
import re

LETTERS = {
    "A": "10",
    "B": "11",
    "C": "12",
    "D": "13",
    "E": "14",
    "F": "15",
    "G": "16",
    "H": "17",
    "I": "18",
    "J": "19",
    "K": "20",
    "L": "21",
    "M": "22",
    "N": "23",
    "O": "24",
    "P": "25",
    "Q": "26",
    "R": "27",
    "S": "28",
    "T": "29",
    "U": "30",
    "V": "31",
    "W": "32",
    "X": "33",
    "Y": "34",
    "Z": "35",
}


def parse(iban_string: str) -> 'Iban':
    assert iban_string is not None, "Must not be empty"
    iban_string = iban_string.replace(" ", "")
    country_code = iban_string[:2]
    spec: 'IbanSpec' = __get_iban_spec(country_code)

    if spec is None:
        raise ValueException("This country doesn't support iban")

    validate(iban_string, spec)

    iban_regex: 'Pattern' = re.compile(spec.iban_pattern)
    match: 'Match' = iban_regex.match(iban_string)
    bank_code: str = match.group(spec.bank_code)
    check_digit: str = match.group(spec.check_digit)
    account_number: str = match.group(spec.account_number)
    branch_code: str = __get_match_group(match, spec.branch_code)
    account_type: str = __get_match_group(match, spec.branch_code)
    account_holder_number: str = __get_match_group(match, spec.branch_code)
    balance_account_number: str = __get_match_group(match, spec.branch_code)
    currency_code: str = __get_match_group(match, spec.branch_code)
    owner_account_number: str = __get_match_group(match, spec.branch_code)
    account: 'Account' = Account(account_number, account_type=account_type,
                                 holder=account_holder_number, currency_code=currency_code,
                                 balance_account=balance_account_number,
                                 owner_account_number=owner_account_number)
    country: 'Country' = Country(country_code, spec.country_name)
    bank: 'Bank' = __get_bank(country_code, bank_code, branch_code)
    basic_bank_account_number: str = iban_string[4:]
    iban: 'Iban' = Iban(check_digit, basic_bank_account_number, spec.formats, bank,
                        account, country)
    return iban


def is_valid(iban_string: str, spec: 'IbanSpec') -> bool:
    try:
        validate(iban_string, spec)
    except ParseException:
        return False
    return True


def validate(iban_string: str, spec: 'IbanSpec'):
    bban: str = iban_string[4:]
    iban_match: 'Match' = re.compile(spec.iban_pattern).match(iban_string)
    bban_match: 'Match' = re.compile(spec.bban_pattern).match(bban)

    if spec.length != len(iban_string):
        raise ValueException('Invalid Iban length')

    if bban_match is None:
        raise InvalidBBANException('Invalid Basic Bank Account Number')

    if iban_match[spec.check_digit] is None:
        raise InvalidCheckDigitException('Invalid Check Digit')

    if spec.reserved_fields is not None:
        reserved_fields_match: 'Match' = re.compile(spec.reserved_fields.pattern).match(iban_string)
        if reserved_fields_match is None:
            raise InvalidReservedValues("Expected reserved values where not found")

    if __calculate_mod97(iban_string) != 1:
        raise InvalidMod97Exception('Invalid MOD 97 Operation Result')


def __calculate_mod97(iban: str) -> int:
    iban = iban[4:] + iban[:4]
    assert iban.isupper(), f"{iban} must be upper case"
    for letter, number in LETTERS.items():
        iban = iban.replace(letter, number)
    remainder = int(iban) % 97
    return remainder


def __get_match_group(match: 'Match', code) -> Optional[str]:
    if code == 0:
        return None
    return match[code]


def __get_iban_spec(country_code: str) -> Optional['IbanSpec']:
    """
    Retrieves Banks data from resources

    Providing the country code

    :param country_code: The iban country code
    :type country_code: str
    :return: Specification for IBAN from the country or none if not found
    :rtype: list
    """
    specs: 'IbansSpecs' = IbansSpecs()
    iban_spec: 'IbanSpec'
    try:
        stream = pkg_resources.resource_string(__name__, f'data/ibans/{country_code[0]}.dat')
        specs.ParseFromString(stream)
    except FileNotFoundError:
        specs = None

    if specs and country_code in specs.specs:
        iban_spec = specs.specs[country_code]
    else:
        iban_spec = None

    return iban_spec


def __get_bank(country_code: str, bank_code: str, branch: str) -> Optional['Bank']:
    """
    get_iban_validation_str retrieves a string from ibans.txt

    The string containing the IBAN definition for the selected country

    :param country_code: The resource folder
    :type country_code: str
    :param bank_code: The resource file
    :type bank_code: str
    :return: a list containing the IBAN validation data
    :rtype: list
    """
    banks: 'BanksData' = BanksData()
    bank: 'Bank'
    data: 'BankData'
    bank_key: str = country_code + bank_code
    try:
        stream = pkg_resources.resource_string(__name__, f'data/banks/{country_code}.dat')
        banks.ParseFromString(stream)
    except FileNotFoundError:
        banks = None

    if banks and bank_key in banks.banks:
        data = banks.banks[bank_key]
        bank = Bank(data.code, name=data.name, short_name=data.short_name, branch=branch, swift=data.swift)
    else:
        bank = Bank(bank_code, branch=branch)
    return bank
