class BankAccount:
    def __init__(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid amount. Balance cannot be negative.")
            self.__balance = 0

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount. Balance cannot be negative.")
    