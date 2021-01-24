import mysql.connector as mysql

user = 'root'
passwd = 'root'
base = 'PYTHON'
host = '127.0.0.1'
port = '3306'

db = mysql.connect(
    user=user,
    passwd=passwd,
    db=base,
    host=host,
    port=port)

print("Conexão feita com sucesso")

# db.close()
# db.commit()

cursor = db.cursor()

# INTERAGINDO COM CURSORES
#########################
# row_affected = cursor.execute('SELECT * FROM bank_accounts')
# print(row_affected)
#
# #print(list(cursor))
#
# rows = cursor.fetchall()
# print(rows)
# for row in rows:
#     print(row)
#
# for row in cursor:
#     print(row)
