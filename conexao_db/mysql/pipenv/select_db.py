###### Não deixe o nome deste arquivo como init.py dá incompatibilidade ##########

"""
# para o S.O.
sudo apt update
sudo apt install mysql-server

sudo mysql

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root'; flush privileges;

mysql -uroot -p'root'

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


insert into usuarios(nome, email, endereco)
values('Clayton', 'clyton@torneseumprogramador.com.br', 'Rua graziana 12');


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

# para o S.O.
sudo apt update
sudo apt-get install libmysqlclient-dev
sudo apt-get install libssl-dev
sudo apt-get install -y python3-mysqldb
sudo apt install python3-pip

git clone https://github.com/torneseumprogramador/desafio-logica-python

#### usando pip
pip install mysql-connector-python
python3 init.py 


#### usando pip env
sudo apt install pipenv # linux
brew install pipenv # macos
pipenv install

pipenv install mysql-connector-python
pipenv run python init.py 

pipenv shell # caso queira rodar sem "pipenv run"
python3 init.py 


"""

import os
import time

import mysql.connector
from mysql.connector import Error

try:
    os.system('clear')
    connection = mysql.connector.connect(host=os.getenv("HOST"),
                                         database=os.getenv("DATABASE"),
                                         user=os.getenv("USER"),
                                         password=os.getenv("PASS"))
    if connection.is_connected():
        cursor = connection.cursor()

        inserir = int(input("Deseja cadastrar um usuario?\n1 - para sim\n0 - para não\n"))
        if inserir == 1:
            usuario = {}
            usuario["nome"] = input("Digite o nome\n")
            usuario["email"] = input("Digite o email\n")
            usuario["endereco"] = input("Digite o endereco\n")
            
            cursor.execute(
                f"insert into usuarios(nome, email, endereco) values('{usuario['nome']}', '{usuario['email']}', '{usuario['endereco']}');"
            )

            os.system('clear')
            print("Usuário inserido com sucesso")
            time.sleep(2)



        cursor.execute("select * from usuarios")
        records = cursor.fetchall()

        os.system("clear")

        for record in records:
            print("================================")
            print(f"Id: {record[0]}")
            print(f"Nome: {record[1]}")
            print(f"Email: {record[2]}")
            print(f"Endereco: {record[3]}")
            print(f"Data: {record[4]}")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
