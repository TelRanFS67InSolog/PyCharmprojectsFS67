class Account:
    def __init__(self, owner: str, balance: float | int, acc_type: str):
        self.owner = owner   #public
        self.__balance = balance    #privat
        self._acc_type = acc_type   #protected - mark not to change

    def __str__(self) -> str:
        return (f"Account: owner {self.owner}\n"
                f"balance: {self.__balance}\n"
                f"acc_type: {self._acc_type}")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance: float | int):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Operation failed!!!")
