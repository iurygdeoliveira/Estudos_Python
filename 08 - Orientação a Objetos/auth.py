from cash_machine import accounts_list


class AuthBankAccount:

    @staticmethod
    def authenticate(account_number, password):
        for bank_account in accounts_list:
            if bank_account.account_number == account_number and bank_account.password == password:
                print('Estamos autenticados')
