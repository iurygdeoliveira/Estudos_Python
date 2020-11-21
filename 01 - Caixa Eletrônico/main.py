# IMPORT
import getpass
import os

account_list = {
    '0001-01': {
        'password': '123456',
        'name': 'Fulano da Silva',
        'value': 150,
        'admin': False
    },
    '0002-01': {
        'password': '123456',
        'name': 'Sicrano da Silva',
        'value': 250,
        'admin': False
    },
    '1111-11': {
        'password': '123456',
        'name': 'Admin da Silva',
        'value': 11100,
        'admin': True
    },

}

money_slips = {
    '20': 5,
    '50': 5,
    '100': 5,
}

while True:
    print("*****************************")
    print("****** CAIXA ELETRÔNICO *****")
    print("*****************************")

    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    # print(account_typed)
    # print(type(account_typed))
    # print(password_typed)
    # print(type(password_typed))

    if account_typed in account_list and password_typed == account_list[account_typed]['password']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("*****************************")
        print("****** CAIXA ELETRÔNICO *****")
        print("*****************************")
        print("1 - saldo")
        print("2 - saque")
        if account_list[account_typed]['admin']:
            print("10 - incluir cedulas")
        option_typed = input("Escolha uma das opções acima: ")
        if option_typed == '1':
            print("Seu saldo é: %s" % account_list[account_typed]['value'])
        elif option_typed == '10' and account_list[account_typed]['admin']:
            amount_typed = input("Digite a quantidade de cédulas: ")
            money_bill_typed = input("Digite a cédula a ser inserida: ")
            money_slips[money_bill_typed] += int(amount_typed)
            print(money_slips)
        elif option_typed == '2':
            value_typed = input('Digite o valor a ser sacado: ')
            value_int = int(value_typed)

            money_slips_user = {}

            if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
                money_slips_user['100'] = value_int // 100
                value_int = value_int - value_int // 100 * 100

            if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
                money_slips_user['50'] = value_int // 50
                value_int = value_int - value_int // 50 * 50

            if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
                money_slips_user['20'] = value_int // 20
                value_int = value_int - value_int // 20 * 20

            if value_int != 0:
                print("O caixa não tem cédulas disponíveis pra este valor")
            else:
                for money_bill in money_slips_user:
                    money_slips_user[money_bill] -= money_slips_user[money_bill]
                print('Pegue as notas: ')
                print(money_slips_user)

    else:
        print("Conta Inválida")

    input('Pressione <ENTER> para continuar ...')
    os.system('cls' if os.name == 'nt' else 'clear')
