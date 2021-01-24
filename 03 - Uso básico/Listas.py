# ## Listas
# Criando uma lista
listadomercado = ["ovos, farinha, leite, maças"]

# Imprimindo a lista
print(listadomercado)

# Criando outra lista
listadomercado2 = ["ovos", "farinha", "leite", "maças"]

# Imprimindo a lista
print(listadomercado2)

# Criando lista
lista3 = [12, 100, "Universidade"]

# Imprimindo
print(lista3)

lista3 = [12, 100, "Universidade"]

# Atribuindo cada valor da lista a uma variável.
item1 = lista3[0]
item2 = lista3[1]
item3 = lista3[2]

# Imprimindo as variáveis
print(item1, item2, item3)

# ### Atualizando um item da lista

# Imprimindo um item da lista
print(listadomercado2[2])

# Atualizando um item da lista
listadomercado2[2] = "chocolate"

# Imprimindo lista alterada
print(listadomercado2)

# Out of index. Não é possível deletar um item que não existe na lista
del listadomercado2[4]

# Deletando um item específico da lista
del listadomercado2[3]

# Imprimindo o item com a lista alterada
print(listadomercado2)

# Criando uma lista de listas
listas = [[1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]]

# Imprimindo a lista
print(listas)

# Atribuindo um item da lista a uma variável
a = listas[0]

print(a)

b = a[0]

print(b)

list1 = listas[1]

print(list1)

valor_1_0 = list1[0]

print(valor_1_0)

valor_1_2 = list1[2]

print(valor_1_2)


# ### Operações com listas
# Criando uma lista aninhada (lista de listas)
listas = [[1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]]

# Atribuindo à variável a, o primeiro valor da primeira lista
a = listas[0][0]

b = listas[1][2]

c = listas[0][2] + 10

d = 10

e = d * listas[2][0]

# ### Concatenando listas
lista_s1 = [34, 32, 56]

lista_s2 = [21, 90, 51]

lista_s2

# Concatenando listas
lista_total = lista_s1 + lista_s2

lista_total


# ## Operador in
# Criando uma lista
lista_teste_op = [100, 2, -5, 3.4]

# Verificando se o valor 10 pertence a lista
print(10 in lista_teste_op)

# Verificando se o valor 100 pertence a lista
print(100 in lista_teste_op)


# ## Funções Built-in
# Função len() retorna o comprimento da lista
len(lista_teste_op)

# Função max() retorna o valor máximo da lista
max(lista_teste_op)

# Função min() retorna o valor mínimo da lista
min(lista_teste_op)

# Criando uma lista
listadomercado2 = ["ovos", "farinha", "leite", "maças"]

# Adicionando um item à lista
listadomercado2.append("carne")

listadomercado2

listadomercado2.append("carne")

listadomercado2

listadomercado2.count("carne")

# Criando uma lista vazia
a = []

print(a)

type(a)

a.append(10)

a

a.append(50)

a

old_list = [1, 2, 5, 10]

new_list = []

# Copiando os itens de uma lista para outra
for item in old_list:
    new_list.append(item)

new_list

c = [20, 30]

c.append(60)

c.append(70)

c

c.count(20)

cidades = ['Recife', 'Manaus', 'Salvador']
cidades.extend(['Fortaleza', 'Palmas'])
print(cidades)

cidades.index('Salvador')


# Lembre-se: em Python o índice começa por 0!
cidades.index('Rio de Janeiro')

cidades

cidades.insert(2, 110)

cidades

# Remove um item da lista
cidades.remove(110)

cidades

# Reverte a lista
cidades.reverse()

# Imprime a lista
cidades

x = [3, 4, 2, 1]

x

# Ordena a lista
x.sort()

x


# # Fim
