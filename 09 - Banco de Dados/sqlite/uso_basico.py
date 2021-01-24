# Versão da Linguagem Python
import sqlite3
import os

from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())

# Documentação SQLite: http://www.sqlite.org/docs.html

# ### Acessando Banco de Dados com Python

# Reemove o arquivo com o banco de dados SQLite (caso exista)
os.remove("escola.db") if os.path.exists("escola.db") else None

# Cria uma conexão com o banco de dados.
# Se o banco de dados não existir, ele é criado neste momento.
con = sqlite3.connect('escola.db')

type(con)

# Criando um cursor
# (Um cursor permite percorrer todos os registros em um conjunto de dados)
cur = con.cursor()

type(cur)

# Cria uma instrução sql
sql_create = 'create table cursos ''(id integer primary key, ''titulo varchar(100), ''categoria varchar(140))'

# Executando a instrução sql no cursor
cur.execute(sql_create)

# Criando outra sentença SQL para inserir registros
sql_insert = 'insert into cursos values (?, ?, ?)'

# Dados
recset = [(1000, 'Ciência de Dados', 'Data Science'),
          (1001, 'Big Data Fundamentos', 'Big Data'),
          (1002, 'Python Fundamentos', 'Análise de Dados')]

# Inserindo os registros
for rec in recset:
    cur.execute(sql_insert, rec)

# Grava a transação
con.commit()

# Criando outra sentença SQL para selecionar registros
sql_select = 'select * from cursos'

# Seleciona todos os registros e recupera os registros
cur.execute(sql_select)
dados = cur.fetchall()

# Mostra
for linha in dados:
    print('Curso Id: %d, Título: %s, Categoria: %s \n' % linha)

# Gerando outros registros
recset = [(1003, 'Gestão de Dados com MongoDB', 'Big Data'),
          (1004, 'R Fundamentos', 'Análise de Dados')]

# Inserindo os registros
for rec in recset:
    cur.execute(sql_insert, rec)

# Gravando a transação
con.commit()

# Seleciona todos os registros
cur.execute('select * from cursos')

# Recupera os resultados
recset = cur.fetchall()

# Mostra
for rec in recset:
    print('Curso Id: %d, Título: %s, Categoria: %s \n' % rec)

# Fecha a conexão
con.close()

# # Fim
