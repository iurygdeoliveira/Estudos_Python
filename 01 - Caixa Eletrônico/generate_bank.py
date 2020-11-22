from file import open_file_bank, write_money_slips, write_bank_accounts
from utils import header


def main():
    header()
    make_money_slips("w")
    file = open_file_bank('a')
    file.write('\n')
    file.close()
    make_bank_accounts("a")


def make_money_slips(mode):
    file = open_file_bank(mode)
    write_money_slips(file)
    file.close()
    print('Cédulas Gravadas com sucesso')


def make_bank_accounts(mode):
    file = open_file_bank(mode)
    write_bank_accounts(file)
    file.close()
    print('Contas Bancarias Gravadas com sucesso')


main()
