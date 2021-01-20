# IMPORT
import utils
import operations
from bank_account_variables import money_slips
from file import load_bank_data


def main():
    load_bank_data()
    utils.header()  # Imprimindo o header do programa
    account_auth = operations.auth_account()  # Autenticando no caixa eletrônico

    if account_auth:
        utils.clear()  # Limpando a tela
        utils.header()  # Imprimindo o header do programa

        option_typed = operations.get_option(account_auth)
        operations.do_operation(option_typed, account_auth)

    else:
        print("Conta Inválida")


def pause():
    input('Pressione <ENTER> para continuar ...')  # Pause do programa


while True:
    main()
    pause()
    utils.clear()  # Limpar a tela
