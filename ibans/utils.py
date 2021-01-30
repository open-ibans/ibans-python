import re
import pkg_resources


letter_to_replace = {
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


def get_iban_validation_str(country_code: str) -> list:
    """
    get_iban_validation_str retrieves a string from ibans.txt

    The string containing the IBAN definition for the selected country

    :param country_code: The country alpha-2 code that comes as
        the first 2 letters of an IBAN
    :type country_code: str
    :return: a list containing the IBAN validation data
    :rtype: list
    """
    try:
        stream = pkg_resources.resource_stream(__name__, 'data/ibans.txt')
    except FileNotFoundError:
        return []
    for line in stream:
        line = line.decode('utf-8')
        if country_code == line[0:2]:
            return line.strip().split("|")
    return []


def bank_validation_str(iban: str, bank_code: str) -> list:
    """
    Retrieves a string with the bank information

    :param iban: An iban string
    :type iban: str
    :param bank_code: the bank code
    :type bank_code: str
    :return: A list with the bank information
    :rtype: str
    """
    filename = f'{iban[:6]}.txt'
    location = f'data/banks/{filename}'
    try:
        stream = pkg_resources.resource_stream(__name__, location)
    except FileNotFoundError:
        return []
    for line in stream:
        line = line.decode('utf-8')
        if line.startswith(bank_code + '|'):
            return line.strip().split("|")
    return []


def bban_to_regex(bban_format: str) -> str:
    """
    converts the bban description into a regex

    :param bban_format: the bban format
    :type bban_format: str
    :return: a string representing a regex
    :rtype: str
    """
    bban_formats_list = bban_format.split(",")
    regex_list = []
    for x in bban_formats_list:
        type = x[-1]
        size = x[:-1]
        if type == 'a':
            regex_list.append(f"[A-Z]{{{size}}}")
        elif type == 'c':
            regex_list.append(f"[A-Za-z0-9]{{{size}}}")
        elif type == 'n':
            regex_list.append(f"[0-9]{{{size}}}")
    bban_regex = ''.join(regex_list)
    return bban_regex


def validate_mod_97(iban: str) -> int:
    """
    Validats an IBAN using MOD 97 operation

    :param iban: The iban to be validated
    :type iban: str
    :return: The remainder of the mod operation
    :rtype: int
    """
    iban = iban[4:] + iban[:4]
    iban = iban.upper()
    for letter, number in letter_to_replace.items():
        iban = iban.replace(letter, number)
    remainder = int(iban) % 97
    return remainder


def select_from_format(regex, iban_format: str, iban: str) -> str:
    """
    Selects part of an IBAN string using regex

    Use to extract info from IBAN such as country code, bank code and others

    :param regex: the regex
    :type regex: str/r
    :param iban_format: the iban format string used to locate the info position
    :type iban_format: str
    :param iban: The iban
    :type iban: str
    :return: a string representing the part of the iban
    :rtype: str
    """
    match = re.search(regex, iban_format)
    if match:
        start = match.start()
        end = match.end()
        return iban[start:end]
    else:
        return ""
