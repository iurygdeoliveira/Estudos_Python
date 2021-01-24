#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Manipulação de Arquivos</font>

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# - Arquivos TXT
# - Arquivos CSV 
# - Arquivos JSON

# ## Manipulando Arquivos TXT

# In[2]:


texto = "Cientista de Dados é a profissão que mais tem crescido em todo mundo.\n"
texto = texto + "Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning.\n"
texto += "E claro, em Big Data."


# In[3]:


print(texto)


# In[4]:


# Importando o módulo os
import os


# In[5]:


# Criando um arquivo 
arquivo = open(os.path.join('arquivos/cientista.txt'),'w')


# In[6]:


# Gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra+' ')


# In[7]:


# Fechando o arquivo
arquivo.close()


# In[8]:


# Lendo o arquivo
arquivo = open('arquivos/cientista.txt','r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)


# ### Usando a expressão `with` 
# 
# O método close() é executado automaticamente

# In[9]:


with open('arquivos/cientista.txt','r') as arquivo:
    conteudo = arquivo.read()


# In[10]:


print(len(conteudo))


# In[11]:


print(conteudo)


# In[12]:


with open('arquivos/cientista.txt','w') as arquivo:
    arquivo.write(texto[:21])
    arquivo.write('\n')
    arquivo.write(texto[:33])


# In[13]:


# Lendo o arquivo
arquivo = open('arquivos/cientista.txt','r')
conteudo = arquivo.read()
arquivo.close()

print (conteudo)


# ### Manipulando Arquivos CSV (comma-separated values )

# In[14]:


# Importando o módulo csv
import csv


# In[15]:


with open('arquivos/numeros.csv','w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('primeira','segunda','terceira'))
    writer.writerow((55,93,76)) 
    writer.writerow((62,14,86))


# In[16]:


# Leitura de arquivos csv
with open('arquivos/numeros.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print ('Número de colunas:', len(x))
        print(x)


# In[17]:


# Código alternativo para eventuais problemas com linhas em branco no arquivo
with open('arquivos/numeros.csv','r', encoding='utf8', newline = '\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print ('Número de colunas:', len(x))
        print(x)


# In[18]:


# Gerando uma lista com dados do arquivo csv
with open('arquivos/numeros.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)
    
    
print (dados)


# In[19]:


# Impriminfo a partir da segunda linha
for linha in dados[1:]:
    print (linha)


# ### Manipulando Arquivos JSON (Java Script Object Notation )
# JSON (JavaScript Object Notation) é uma maneira de armazenar informações de forma organizada e de fácil acesso. Em poucas palavras, ele nos dá uma coleção legível de dados que podem ser acessados de forma muito lógica. Pode ser uma fonte de Big Data.

# In[20]:


# Criando um dicionário
dict = {'nome': 'Guido van Rossum',
        'linguagem': 'Python',
        'similar': ['c','Modula-3','lisp'],
        'users': 1000000}


# In[21]:


for k,v in dict.items():
    print (k,v)


# In[22]:


# Importando o módulo Json
import json


# In[23]:


# Convertendo o dicionário para um objeto json
json.dumps(dict)


# In[24]:


# Criando um arquivo Json
with open('arquivos/dados.json','w') as arquivo:
    arquivo.write(json.dumps(dict))


# In[25]:


# Leitura de arquivos Json
with open('arquivos/dados.json','r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)


# In[26]:


print (data)


# In[27]:


print (data['nome'])


# In[28]:


# Imprimindo um arquivo Json copiado da internet
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]


# In[29]:


print ('Título: ', data['title'])
print ('URL: ', data['url'])
print ('Duração: ', data['duration'])
print ('Número de Visualizações: ', data['stats_number_of_plays'])


# In[30]:


# Copiando o conteúdo de um arquivo para outro
import os

arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/json_data.txt'


# In[31]:


# Método 1
with open(arquivo_fonte,'r') as infile:
    text = infile.read()
    with open(arquivo_destino,'w') as outfile:
        outfile.write(text)  


# In[32]:


# Método 2
open(arquivo_destino,'w').write(open(arquivo_fonte,'r').read()) 


# In[33]:


# Leitura de arquivos Json
with open('arquivos/json_data.txt','r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)


# In[34]:


print(data)


# # FIM
