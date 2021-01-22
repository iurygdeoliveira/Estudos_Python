from console import CashMachineConsole, AuthBankAccountConsole
from utils import clear, header


def main():
    clear()  # Limpando a tela
    header()  # Imprimindo cabeçalho
    AuthBankAccountConsole.is_auth()
    # CashMachineConsole.call_operation()


# Verificando se o nome do arquivo é igual a main
if __name__ == '__main__':
    while True:
        main()
        input('Presssione <ENTER> para continuar ...')
