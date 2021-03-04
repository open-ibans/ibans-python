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