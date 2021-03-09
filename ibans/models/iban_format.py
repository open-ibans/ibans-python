from enum import Enum


class IbanFormat(Enum):
    PRINT = 0
    ELECTRONIC = 1
    PRINT_HIDDEN = 3
    ELECTRONIC_HIDDEN = 4
