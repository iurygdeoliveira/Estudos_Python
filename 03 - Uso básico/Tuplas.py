# ## Tuplas

# Criando uma tupla
tupla1 = ("Geografia", 23, "Elefantes")


# Imprimindo a tupla
tupla1


# Tuplas não suportam append()
tupla1.append("Chocolate")


# Tuplas não suportam delete de um item específico
del tupla1["Gatos"]


# Tuplas podem ter um único item
tupla1 = ("Chocolate")


tupla1


tupla1 = ("Geografia", 23, "Elefantes")


tupla1[0]


# Verificando o comprimento da tupla
len(tupla1)


# Slicing, da mesma forma que se faz com listas
tupla1[1:]


tupla1.index('Elefantes')


# Tuplas não suportam atribuição de item
tupla1[1] = 21


# Deletando a tupla
del tupla1

# Criando uma tupla
t2 = ('A', 'B', 'C')


# Tuplas não suportam atribuição de item
t2[0] = 'D'


# Usando a função list() para converter uma tupla para lista
lista_t2 = list(t2)


lista_t2.append('D')


# Usando a função tuple() para converter uma lista para tupla
t2 = tuple(lista_t2)

# # Fim
