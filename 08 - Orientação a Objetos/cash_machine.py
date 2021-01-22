class BankAccount:
    def __init__(self, account_number, name, password, value, admin):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.value = value
        self.admin = admin


accounts_list = [
    BankAccount('0001-02', 'Fulano da Silva', '123456', 100, False),
    BankAccount('0002-02', 'Fulano da Silva', '123456', 50, False),
    BankAccount('1111-11', 'Admin da Silva', '123456', 1000, True),
]
