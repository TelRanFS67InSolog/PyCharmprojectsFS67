class BAccount:

    def __init__(self, name: str, id: int, account_balance: float):
        self.__name = name
        self.__id = id
        self.__account_balance = account_balance

    def __repr__(self):
        return (f"Client of bank: {self.__name}\t"
                f"account's number: {self.__id}\t"
                f"balance: {self.__account_balance}\n")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is not None:
            self.__name = name
        print("Name cannot be None!")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if id is not None:
            self.__id = id
        print("id cannot be None")

    @property
    def account_balance(self):
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, account_balance):
        if account_balance is not None and account_balance>=0:
            self.__account_balance = account_balance
        raise ValueError("Operation of changing balance failed!")


