# Criando uma lista
seq = ['a', 'b', 'c']

enumerate(seq)

list(enumerate(seq))

# Imprimindo os valores de uma lista com a função enumerate() e seus respectivos índices
for indice, valor in enumerate(seq):
    print(indice, valor)


for indice, valor in enumerate(seq):
    if indice >= 2:
        break
    else:
        print(valor)


lista = ['Marketing', 'Tecnologia', 'Business']

for i, item in enumerate(lista):
    print(i, item)

for i, item in enumerate('Isso é uma string'):
    print(i, item)

for i, item in enumerate(range(10)):
    print(i, item)

# # FIM
