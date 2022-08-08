# ========= Instalar o componente pyodbc =========
# python -m pip install pyodbc
# pip install pyodbc
# ========= Instalar o componente pyodbc =========
# para testar
# python3
# import pyodbc
# pyodbc.drivers()
# ========= Criar um banco de dados no sql server com o nome migracao e uma tabela com o nome importacao(id int, texto varchar(1000)) =========

"""
create database migracao;

CREATE TABLE importacao (
    id int IDENTITY(1,1) PRIMARY KEY,
    texto varchar(255) NOT NULL
);


"""

import pyodbc

server="localhost"
db="migracao"
user="sa"
pwd="!1#2a3d4c5g6v"

connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=' + server + ';'
                            'Database=' + db + ';'
                            'UID=' + user + ';'
                            'PWD=' + pwd)

# # windows
# connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
#                               'SERVER=' + server + ';'
#                               'DATABASE=' + db + ';'
#                               'UID=' + user + ';'
#                               'PWD=' + pwd)

cursor=connection.cursor()

# insiro dados no banco
cursor.execute("insert into importacao(texto)values('Um deste inserido pelo python')")
connection.commit()

# busco dados dados no banco
dados = cursor.execute("SELECT * from importacao")
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print("---------------")
    print(f"texto: {row.texto}")

cursor.close()
connection.close()
