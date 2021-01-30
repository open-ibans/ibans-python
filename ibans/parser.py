"""


[extended_summary]

:raises Exception: [description]
:raises IbanParseException: [description]
:raises IbanParseException: [description]
:raises IbanParseException: [description]
:raises IbanParseException: [description]
:raises IbanParseException: [description]
:return: [description]
:rtype: [type]
"""
from ibans.exception import ExceptionType, IbanParseException
from .utils import bban_to_regex, get_iban_validation_str, \
    select_from_format, validate_mod_97, bank_validation_str
from .iban import Iban
import re


def parse(iban: str) -> Iban:
    """
    Parses a string to an iban object

    :param iban: The IBAN
    :type iban: str
    :raises IbanParseException: Exception thrown if the iban parsing failed
    :return: An Iban object
    :rtype: Iban
    """
    if iban is None or iban == '':
        raise Exception('iban can not be empty')

    iban: str = iban.replace(' ', '')
    country_code: str = iban[:2].upper()
    check_digit: str = iban[2:4]
    bban: str = iban[4:]
    bank_code: str = None
    account_number: str = None
    bank_name = None
    sigla = None
    swift_bic = None
    branch_code = None
    account_type = None
    account_holder = None
    balance_account_number = None
    currency_code = None
    iban_format: list = []
    iban_length: str = len(iban)

    line = get_iban_validation_str(country_code)
    if not line:
        raise IbanParseException(ExceptionType.INVALID_COUNTRY_CODE)

    _, country, length, bban_format, fields = line
    bban_regex = bban_to_regex(bban_format)
    check_code_regex = fields[2:4].replace('k', '[0-9]')

    if iban_length != int(length):
        raise IbanParseException(ExceptionType.INVALID_LENGTH)

    if not re.match(check_code_regex, check_digit):
        raise IbanParseException(ExceptionType.INVALID_CHECK_CODE)

    if not re.match(bban_regex, bban):
        raise IbanParseException(
            ExceptionType.INVALID_BASIC_BANK_ACCOUNT_NUMBER)

    if validate_mod_97(iban) != 1:
        raise IbanParseException(ExceptionType.FAILED_MOD97_VALIDATION)

    for match in re.finditer(" ", fields):
        iban_format.append(match.start())

    fields_no_spaces = fields.replace(" ", "").replace("c", "n")

    bank_code = select_from_format(r"b.*b", fields_no_spaces, iban)
    account_number = select_from_format(r"n.*n", fields_no_spaces, iban)
    branch_code = select_from_format(r"s.*s", fields_no_spaces, iban)
    account_type = select_from_format(r"t.*t", fields_no_spaces, iban)
    account_holder = select_from_format(r"i.*i", fields_no_spaces, iban)
    balance_account_number = select_from_format(
        r"a.*a", fields_no_spaces, iban)
    currency_code = select_from_format(r"m.*m", fields_no_spaces, iban)

    account_number_match = re.search(r"n.*n", fields_no_spaces)
    if account_number_match:
        start = account_number_match.start()
        end = account_number_match.end()
        account_number = iban[start:end]

    branch_code_match = re.search(r"s.*s", fields_no_spaces)
    if branch_code_match:
        start = branch_code_match.start()
        end = branch_code_match.end()
        branch_code = iban[start:end]

    if bank_code:
        bank = bank_validation_str(iban, bank_code)
        if bank:
            bank_name = bank[1] if bank[1] else None
            sigla = bank[2] if bank[2] else None
            swift_bic = bank[3] if bank[3] else None

    return Iban(
        iban_format,
        country_code,
        check_digit,
        bban,
        country,
        bank_code=bank_code,
        account_number=account_number,
        bank_name=bank_name,
        sigla=sigla,
        swift_bic=swift_bic,
        branch_code=branch_code,
        account_type=account_type,
        account_holder=account_holder,
        balance_account_number=balance_account_number,
        currency_code=currency_code)
