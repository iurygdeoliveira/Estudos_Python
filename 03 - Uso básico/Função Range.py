
# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())

# ### Range
# Imprimindo números pares entre 50 e 101
for i in range(50, 101, 2):
    print(i)

for i in range(3, 6):
    print(i)

for i in range(0, -20, -2):
    print(i)

lista = ['Morango', 'Banana', 'Abacaxi', 'Uva']
lista_tamanho = len(lista)
for i in range(0, lista_tamanho):
    print(lista[i])

# Tudo em Python é um objeto
type(range(0, 3))
# # Fim
