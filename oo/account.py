class Account:

    def __init__(self, number, holder, balance, limit):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def statement(self):
        print(f"Balance: {self.__balance}\n Holder: {self.__holder}")

    def deposit(self, value):
        self.__balance += value

    def __can_withdraw(self, value_to_withdraw):
        available_value_to_withdraw = self.__balance + self.__limit
        return value_to_withdraw <= available_value_to_withdraw

    def withdraw(self, value):
        if self.__can_withdraw(value):
            self.__balance -= value
        else:
            print("Insufficient funds!")

    def transfer(self, value, account):
        self.withdraw(value)
        account.deposit(value)

    @property
    def balance(self):
        return self.__balance

    @property
    def holder(self):
        return self.__holder

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def codigo_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
