# Versão da Linguagem Python
import pandas as pd
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ### Lendo Arquivos

# Abrindo o arquivo para leitura
arq1 = open("arquivos/arquivo1.txt", "r")

# Lendo o arquivo
print(arq1.read())

# Contar o número de caracteres
print(arq1.tell())

# Retornar para o iníco do arquivo
print(arq1.seek(0, 0))

# Ler os primeiros 10 caracteres
print(arq1.read(10))

# ### Gravando Arquivos


# Abrindo arquivo para gravação
arq2 = open("arquivos/arquivo1.txt", "w")


# Como abrimos o arquivo apenas para gravação, não podemos usar comandos de leitura.
print(arq2.read())


# Gravando arquivo
arq2.write("Testando gravação de arquivos em Python ")


arq2.close()


# Lendo arquivo gravado
arq2 = open("arquivos/arquivo1.txt", "r")


print(arq2.read())


# Acrescentando conteúdo
arq2 = open("arquivos/arquivo1.txt", "a")


arq2.write(" Acrescentando conteúdo")


arq2.close()


arq2 = open("arquivos/arquivo1.txt", "r")


print(arq2.read())


# Retornando ao início do arquivo para leitura
arq2.seek(0, 0)


print(arq2.read())


# ### Automatizando o processo de gravação


fileName = input("Digite o nome do arquivo: ")


fileName = fileName + ".txt"


arq3 = open(fileName, "w")


arq3.write("Incluindo texto no arquivo criado")


arq3.close()


arq3 = open(fileName, "r")


print(arq3.read())


arq3.close()


# ### Abrindo um dataset em uma única linha


f = open('arquivos/salarios.csv', 'r')


data = f.read()


rows = data.split('\n')


print(rows)


# ### Dividindo um dataset em colunas


f = open('arquivos/salarios.csv', 'r')


data = f.read()


rows = data.split('\n')


full_data = []


for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)


print(full_data)


# ### Contando as linhas de um arquivo


f = open('arquivos/salarios.csv', 'r')


data = f.read()


rows = data.split('\n')


full_data = []


for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)


count = 0
for row in full_data:
    count += 1   # Equivalente a: count = count + 1


print(count)


# ### Contando o número de colunas de um arquivo


f = open('arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []


for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    first_row = full_data[0]
count = 0


for column in first_row:
    count = count + 1

# Outra solução possível
# for column in full_data[0]:
#     count = count + 1


print(count)


# ### Gravando arquivo pelo Jupyter Notebook


get_ipython().run_cell_magic('writefile', 'arquivos/teste.txt   ',
                             'Olá este arquivo foi gerado pelo próprio Jupyter Notebook.\nPodemos gerar quantas linhas quisermos e o Jupyter gera o arquivo final.')


arq4 = open("arquivos/teste.txt", 'r')


arq4.read()


# Estamos no final do arquivo e não há mais nada para ler
arq4.read()


# Retornando ao início do arquivo
arq4.seek(0)


arq4.seek(0)
arq4.readlines()


# Podemos usar um loop for para ler o arquivo
for line in open('arquivos/teste.txt'):
    print(line)


# ## Importando um dataset com Pandas


pd.__version__

file_name = "arquivos/binary.csv"

df = pd.read_csv(file_name)

df.head()

file2 = "arquivos/salarios.csv"

df2 = pd.read_csv(file2)

df2.head()
