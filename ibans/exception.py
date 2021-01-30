

from enum import Enum


class ExceptionType(Enum):
    """
    ExceptionType an enum representing the types of exceptions thrown
    """
    EMPTY_IBAN = 0
    INVALID_COUNTRY_CODE = 1
    INVALID_LENGTH = 2
    INVALID_CHECK_CODE = 3
    INVALID_BASIC_BANK_ACCOUNT_NUMBER = 4
    FAILED_MOD97_VALIDATION = 5


class IbanParseException(Exception):
    """
    This class represents an exception thrown parsing an IBAN
    """

    def __init__(self, kind: ExceptionType):
        """
        Constructs an IBAN parsing exception

        :param kind: The type of exception
        :type kind: ExceptionType
        """
        
        self.kind: ExceptionType = kind
        if self.kind == ExceptionType.EMPTY_IBAN:
            self.description = 'IBAN can not be empty'
        elif self.kind == ExceptionType.INVALID_COUNTRY_CODE:
            self.description = 'Invalid country code'
        elif self.kind == ExceptionType.INVALID_LENGTH:
            self.description = 'Invalid length for IBAN'
        elif self.kind == ExceptionType.INVALID_CHECK_CODE:
            self.description = 'The check code is invalid'
        elif self.kind == ExceptionType.INVALID_BASIC_BANK_ACCOUNT_NUMBER:
            self.description = 'Invalid basic bank account number'
        elif self.kind == ExceptionType.FAILED_MOD97_VALIDATION:
            self.description = 'failed basic mod-97 operation'\
                            '(as described in ISO'\
                            ' 7064)'
