"""
create database desafio_21_dias_python;

use desafio_21_dias_python;

CREATE TABLE usuarios (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    email VARCHAR(100) NOT NULL,
    endereco VARCHAR(255),
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

show tables;

select * from usuarios;

insert into usuarios(nome, email, endereco)
values('Danilo', 'danilo@torneseumprogramador.com.br', 'Rua teste');

select * from usuarios;

update usuarios set nome = 'Danilo', email = 'danilo@torneseumprogramador.com.br', endereco = 'Rua teste 123'
where id = 1;

select * from usuarios;

delete from usuarios where id=2;

select * from usuarios;

# instalando driver mysql pip
- https://pynative.com/python-mysql-database-connection/

# Pipenv - gerenciador de pacotes python
- https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv


# usando pip env
sudo apt install pipenv # linux
brew install pipenv # macos
pipenv install

pipenv install mysql-connector-python
pipenv run python mysql.py 

pipenv shell # caso queira rodar sem "pipenv run"
python mysql.py 
"""

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='desafio_21_dias_python',
                                         user='root',
                                         password='root')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
