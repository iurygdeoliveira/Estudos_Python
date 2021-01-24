# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())

# Criando uma tupla e imprimindo cada um dos valores
tp = (2, 3, 4)
for i in tp:
    print(i)

# Criando uma lista e imprimindo cada um dos valores
ListaDoMercado = ["Leite", "Frutas", "Carne"]
for i in ListaDoMercado:
    print(i)

# Imprimindo os valores no intervalo entre 0 e 5 (exclusive)
for contador in range(0, 5):
    print(contador)

# Imprimindo na tela os números pares da lista de números
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in lista:
    if num % 2 == 0:
        print(num)

# Listando os números no intervalo entre 0 e 101, com incremento em 2
for i in range(0, 101, 2):
    print(i)

# Strings também são sequências
for caracter in 'Python é uma linguagem de programação divertida!':
    print(caracter)

# ### Loops Aninhados

# Loops aninhados
for i in range(0, 5):
    for a in range(0, 5):
        print(a)

# Operando os valores de uma lista com loop for
listaB = [32, 53, 85, 10, 15, 17, 19]
soma = 0
for i in listaB:
    double_i = i * 2
    soma += double_i

print(soma)

# Loops em lista de listas
listas = [[1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]]
for valor in listas:
    print(valor)

# Contando os itens de uma lista
lista = [5, 6, 10, 13, 17]
count = 0
for item in lista:
    count += 1

print(count)

# Contando o número de colunas
lst = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
primeira_linha = lst[0]
count = 0
for column in primeira_linha:
    count = count + 1

print(count)

# Pesquisando em listas
listaC = [5, 6, 7, 10, 50]

# Loop através da lista
for item in listaC:
    if item == 5:
        print("Número encontrado na lista!")

# Listando as chaves de um dicionário
dict = {'k1': 'Python', 'k2': 'R', 'k3': 'Scala'}
for item in dict:
    print(item)

# Imprimindo chave e valor do dicionário. Usando o método items() para retornar os itens de um dicionário
for k, v in dict.items():
    print(k, v)

# # Fim
