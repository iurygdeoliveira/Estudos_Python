import os
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)
# recria o conteúdo do arquivo
file = open(BASE_PATH + '/__file__test.dat', 'w')
file.write('Iury Gomes de Oliveira')
file.write('\n')
file.write('Livia Barbosa Gomes de Oliveira')
file.close()  # Fechando o arquivo
