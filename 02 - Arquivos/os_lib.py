import os

print(os.path.abspath('.'))  # Caminho até chegar no arquivo atual

path_test_file = os.path.abspath('.')

print(os.path.dirname(path_test_file))  # Diretorio base do arquivo atual
print(os.path.exists(path_test_file))  # Verificando existencia de caminho
print(os.path.isfile(path_test_file))  # Verificando se um caminho é um arquivo
# Verificando se um caminho é um diretorio
print(os.path.isdir(path_test_file))

print(__file__)  # Obtendo nome do arquivo
print(os.path.abspath(__file__))  # Obtendo caminho absoluto do arquivo
