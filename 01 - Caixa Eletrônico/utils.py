import os


def header():
    print("*****************************")
    print("****** CAIXA ELETRÔNICO *****")
    print("*****************************")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
