# ## Strings

# ### Criando uma String
# Para criar uma string em Python você pode usar aspas simples ou duplas. Por exemplo:

# Uma única palavra
'Oi'


# Uma frase
'Criando uma string em Python'


# Podemos usar aspas duplas
"Podemos usar aspas duplas ou simples para strings em Python"


# Você pode combinar aspas duplas e simples
"Testando strings em 'Python'"


# ### Imprimindo uma String

print('Testando Strings em Python')


print('Testando \nStrings \nem \nPython')


print('\n')


# ### Indexando Strings

# Atribuindo uma string
s = 'Iury Gomes de Oliveira'


print(s)


# Primeiro elemento da string.
s[0]


s[1]


s[2]


# Podemos usar um : para executar um slicing que faz a leitura de tudo até um ponto designado. Por exemplo:


# Retorna todos os elementos da string, começando pela posição (lembre-se que Python começa a indexação pela posição 0),
# até o fim da string.
s[1:]


# A string original permanece inalterada
s


# Retorna tudo até a posição 3
s[:3]


s[:]


# Nós também podemos usar a indexação negativa e ler de trás para frente.
s[-1]


# Retornar tudo, exceto a última letra
s[:-1]


# Nós também podemos usar a notação de índice e fatiar a string em pedaços específicos (o padrão é 1). Por exemplo, podemos usar dois pontos duas vezes em uma linha e, em seguida, um número que especifica a frequência para retornar elementos. Por exemplo:


s[::1]


s[::2]


s[::-1]


# ### Propriedades de Strings


s


# Alterando um caracter
s[0] = 'x'


# Concatenando strings
s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'


s = s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'


print(s)


# Podemos usar o símbolo de multiplicação para criar repetição!
letra = 'w'


letra * 3


# ### Funções Built-in de Strings

s


# Upper Case
s.upper()


# Lower case
s.lower()


# Dividir uma string por espaços em branco (padrão)
s.split()


# Dividir uma string por um elemento específico
s.split('y')


# ### Funções String

s = 'seja bem vindo ao universo de python'


s.capitalize()


s.count('a')


s.find('p')


s.center(20, 'z')


s.isalnum()


s.isalpha()


s.islower()


s.isspace()


s.endswith('o')


s.partition('!')


# ### Comparando Strings

print("Python" == "R")


print("Python" == "Python")

# # Fim
