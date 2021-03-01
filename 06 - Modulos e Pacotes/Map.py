
# Criando duas funções

# Função 1 - Recebe uma temperatura como parâmetro e retorna a temperatura em Fahrenheit
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

# Função 2 - Recebe uma temperatura como parâmetro e retorna a temperatura em Celsius


def celsius(T):
    return (float(5)/9)*(T-32)


# Criando uma lista
temperaturas = [0, 22.5, 40, 100]

# Aplicando a função a cada elemento da lista de temperaturas.
# Em Python 3, a funçãp map() retornar um iterator
map(fahrenheit, temperaturas)

# Função map() reotrnando a lista de temperaturas convertidas em Fahrenheit
list(map(fahrenheit, temperaturas))

# Usando um loop for para imprimir o resultado da função map()
for temp in map(fahrenheit, temperaturas):
    print(temp)

# Convertendo para Celsius
map(celsius, temperaturas)

list(map(celsius, temperaturas))

# Usando lambda
map(lambda x: (5.0/9)*(x - 32), temperaturas)

list(map(lambda x: (5.0/9)*(x - 32), temperaturas))

# Somando os elementos de 2 listas
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

list(map(lambda x, y: x+y, a, b))

# Somando os elementos de 3 listas
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]

list(map(lambda x, y, z: x+y+z, a, b, c))
