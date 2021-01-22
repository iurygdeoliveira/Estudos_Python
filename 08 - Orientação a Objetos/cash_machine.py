class BankAccount:
    def __init__(self, account_number, name, password, value, admin):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.value = value
        self.admin = admin

    def check_account_number(self, account_number):
        return account_number == self.account_number

    def check_password(self, password):
        return password == self.password


class CashMachine:
    def __init__(self, money_slips):
        self.money_slips = money_slips
        self.money_slips_user = {}
        self.value_remaining = 0


def WithDraw(self, value):
    self.value_remaining = value

    self.__calculate_money_slips_user('100')
    self.__calculate_money_slips_user('50')
    self.__calculate_money_slips_user('20')

    if self.value_remaining == 0:
        self.__decrease_money_slips()

    return False if self.value_remaining != 0 else self.money_slips

    def __calculate_money_slips_user(self, money_bill):
        money_bill_int = int(money_bill)
        if 0 < self.value_remaining // money_bill_int <= self.money_slips[money_bill]:
            self.money_slips_user[money_bill] = self.value_remaining // money_bill_int
        self.value_remaining = self.value_remaining - \
            self.value_remaining // money_bill_int * money_bill_int

    def __decrease_money_slips(self):
        for money_bill in self.money_slips_user:
            self.money_slips[money_bill] -= self.money_slips_user[money_bill]


accounts_list = [
    BankAccount('0001-02', 'Fulano da Silva', '123456', 100, False),
    BankAccount('0002-02', 'Fulano da Silva', '123456', 50, False),
    BankAccount('1111-11', 'Admin da Silva', '123456', 1000, True),
]
