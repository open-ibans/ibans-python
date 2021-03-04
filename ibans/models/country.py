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