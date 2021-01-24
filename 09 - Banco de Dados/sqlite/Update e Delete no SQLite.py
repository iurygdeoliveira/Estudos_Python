import sqlite3
import random
import time
import datetime

# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())

# ### Update e Delete

# Criando uma conexão
conn = sqlite3.connect('dsa.db')

# Criando um cursor
c = conn.cursor()

# Função para criar uma tabela


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '              'prod_name TEXT, valor REAL)')

# Função para inserir uma linha


def data_insert():
    c.execute("INSERT INTO produtos VALUES(002, '02-05-2020', 'teclado', 130 )")
    conn.commit()
    c.close()
    conn.close()

# Usando variáveis para inserir dados


def data_insert_var():
    new_date = datetime.datetime.now()
    new_prod_name = 'monitor'
    new_valor = random.randrange(50, 100)
    c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?, ?)",
              (new_date, new_prod_name, new_valor))
    conn.commit()

# Leitura de dados


def leitura_todos_dados():
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha)

# Leitura de registros específicos


def leitura_registros():
    c.execute("SELECT * FROM PRODUTOS WHERE valor > 70.0")
    for linha in c.fetchall():
        print(linha)

# Leitura de colunas específicos


def leitura_colunas():
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha[3])

# Update


def atualiza_dados():
    c.execute("UPDATE produtos SET valor = 70.00 WHERE valor = 98.0")
    conn.commit()

# Delete


def remove_dados():
    c.execute("DELETE FROM produtos WHERE valor = 62.0")
    conn.commit()


atualiza_dados()

leitura_todos_dados()

remove_dados()

leitura_todos_dados()

# # Fim
