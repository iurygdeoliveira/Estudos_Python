
# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())

# Condicional If
if 5 > 2:
    print("Python funciona!")

# Statement If...Else
if 5 < 2:
    print("Python funciona!")
else:
    print("Algo está errado!")

if 5 == 5:
    print("Testando Python!")

if True:
    print('Parece que Python funciona!')


# Atenção com a sintaxe
if 4 > 3
print("Tudo funciona!")

# Atenção com a sintaxe
if 4 > 3:
print("Tudo funciona!")


# ### Condicionais Aninhados
idade = 18
if idade > 17:
    print("Você pode dirigir!")

Nome = "Bob"
if idade > 13:
    if Nome == "Bob":
        print("Ok Bob, você está autorizado a entrar!")
    else:
        print("Desculpe, mas você não pode entrar!")

idade = 13
Nome = "Bob"
if idade >= 13 and Nome == "Bob":
    print("Ok Bob, você está autorizado a entrar!")

idade = 12
Nome = "Bob"
if (idade >= 13) or (Nome == "Bob"):
    print("Ok Bob, você está autorizado a entrar!")


dia = "Terça"
if dia == "Segunda":
    print("Hoje fará sol!")
else:
    print("Hoje vai chover!")

if dia == "Segunda":
    print("Hoje fará sol!")
elif dia == "Terça":
    print("Hoje vai chover!")
else:
    print("Sem previsão do tempo para o dia selecionado")


# ### Operadores Lógicos

idade = 18
nome = "Bob"
if idade > 17:
    print("Você pode dirigir!")

idade = 18
if idade > 17 and nome == "Bob":
    print("Autorizado!")

# Usando mais de uma condição na cláusula if

disciplina = input('Digite o nome da disciplina: ')
nota_final = input('Digite a nota final (entre 0 e 100): ')

if disciplina == 'Geografia' and nota_final >= '70':
    print('Você foi aprovado!')
else:
    print('Lamento, acho que você precisa estudar mais!')

# Usando mais de uma condição na cláusula if e introduzindo Placeholders

disciplina = input('Digite o nome da disciplina: ')
nota_final = input('Digite a nota final (entre 0 e 100): ')
semestre = input('Digite o semestre (1 a 4): ')

if disciplina == 'Geografia' and nota_final >= '50' and int(semestre) != 1:
    print('Você foi aprovado em %s com média final %r!' %
          (disciplina, nota_final))
else:
    print('Lamento, acho que você precisa estudar mais!')

# # Fim
