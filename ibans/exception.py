class ParseException(Exception):
    """This class represents an exception thrown parsing an IBAN
    """
    def __init__(self, message: str):
        self.__message: str = message
        super().__init__(message)

    @property
    def message(self):
        return self.__message


class ValueException(ParseException):
    """Represents an invalid value exception
    """
    def __init__(self, message: str):
        super().__init__(message)


class InvalidBBANException(ParseException):
    """
    Represents a Basic Bank Account Number validation exception
    """
    def __init__(self, message: str):
        super().__init__(message)


class InvalidCheckDigitException(ParseException):
    """
    Invalid Check digit
    """
    def __init__(self, message: str):
        super().__init__(message)


class InvalidMod97Exception(ParseException):
    """
    Invalid Mod 97 operation result
    """
    def __init__(self, message: str):
        super(message)


class InvalidReservedValues(ParseException):
    """
    Represents an invalid reserved value
    """
    def __init__(self, message: str):
        super().__init__(message)


class ResourceNotFound(Exception):
    """
    ResourceNotFound Represents an file not found exception

    """
    def __init__(self, message: str):
        super().__init__(message)
