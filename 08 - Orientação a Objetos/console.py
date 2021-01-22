from auth import AuthBankAccount
import getpass


class AuthBankAccountConsole:

    @staticmethod
    def is_auth():
        account_number_typed = input('Digite sua conta: ')
        password_typed = getpass.getpass('Digite sua senha: ')

        return AuthBankAccount.authenticate(account_number_typed, password_typed)


class CashMachineConsole:

    # Obtendo escolha do usuário
    @staticmethod
    def call_operation():
        option_typed = CashMachineConsole.__get_menu_options_typed()
        CashMachineOperation.do_operation(option_typed)

    # Disponibilizando opções de escolha ao usuário
    @staticmethod
    def __get_menu_options_typed():
        print("%s - Saldo" % CashMachineOperation.OPERATION_SHOW_BALANCE)
        print("%s - Saque" % CashMachineOperation.OPERATION_WITHDRAW)
        return input('Escolha uma das opções acima: ')


class CashMachineOperation:
    OPERATION_SHOW_BALANCE = '1'
    OPERATION_WITHDRAW = '2'

    @staticmethod
    def do_operation(option):
        if option == CashMachineOperation.OPERATION_SHOW_BALANCE:
            ShowBalanceOperation.do_operation()
        elif option == CashMachineOperation.OPERATION_WITHDRAW:
            WithDrawOperation.do_operation()


class ShowBalanceOperation:

    @staticmethod
    def do_operation():
        print('Mostrar saldo')


class WithDrawOperation:

    @staticmethod
    def do_operation():
        print('Sacar Dinheiro')
