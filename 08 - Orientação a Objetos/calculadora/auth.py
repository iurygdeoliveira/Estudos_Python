from cash_machine import accounts_list


class AuthBankAccount:
    bank_account_authenticated = None

    @staticmethod
    def authenticate(account_number, password):
        for bank_account in accounts_list:
            if AuthBankAccount.__has_bank_account_valid(bank_account, account_number, password):
                AuthBankAccount.bank_account_authenticated = bank_account
                return bank_account
        return False

    # Tornando o método privado
    @staticmethod
    def __has_bank_account_valid(bank_account, account_number, password):
        return bank_account.check_account_number(account_number) and bank_account.check_password(password)
