import os
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)

# Escrevendo no arquivo
# recria o conteúdo do arquivo
# file = open(BASE_PATH + '/__file__test.dat', 'w')
# file.write('Iury Gomes de Oliveira')
# file.write('\n')
# file.write('Livia Barbosa Gomes de Oliveira')
# file.writelines(('sssss', 'aaaaa', 'bbbbb'))
# file.writelines(('sssss', '\n', 'aaaaa', '\n', 'bbbbb'))
# file.close()  # Fechando o arquivo

# Lendo o arquivo
file = open(BASE_PATH + '/__file__test.dat', 'r')
# print(file.read())  # Lendo o arquivo completo
# print(file.read(10))  # Lendo uma quantidade especifica de caracteres
# print(file.readline())  # Lendo uma linha inteira no arquivo
print(file.readlines())  # Lendo uma linha inteira no arquivo
file.close
