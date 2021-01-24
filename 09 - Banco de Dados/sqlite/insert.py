# Versão da Linguagem Python
from platform import python_version
import os
import sqlite3

print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())

# ### Criando o Banco de Dados e Inserindo Dados
# Reemove o arquivo com o banco de dados SQLite (caso exista)
os.remove("dsa.db") if os.path.exists("dsa.db") else None

# Criando uma conexão
conn = sqlite3.connect('dsa.db')

# Criando um cursor
c = conn.cursor()

# Função para criar uma tabela


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '              'prod_name TEXT, valor REAL)')

# Função para inserir uma linha


def data_insert():
    c.execute(
        "INSERT INTO produtos VALUES(10, '2020-05-02 14:32:11', 'Teclado', 90 )")
    conn.commit()
    c.close()
    conn.close()


# Criar tabela
create_table()

# Inserir dados
data_insert()

# # Fim
