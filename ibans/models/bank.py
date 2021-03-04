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