"""
Crie uma aplicação com python e django seguindo o tutorial abaixo
https://docs.djangoproject.com/en/4.1/intro/tutorial01/

Guia:
# doc
- https://docs.djangoproject.com/en/4.0/topics/install/

```shell
pipenv install Django
# pipenv shell # opcional caso vc não queira digitar "pipenv run"
pipenv run python -m django --version
pipenv run django-admin startproject desafio21diaspython
cd desafio21diaspython
pipenv install
pipenv install Django
pipenv install mysqlclient
pipenv run python manage.py runserver
mysql -uroot -p'root'
mysql> create database desafio21dias_python_django;
mysql> exit
pipenv run python manage.py migrate
pipenv run python manage.py createsuperuser
pipenv run python manage.py runserver
pipenv run python manage.py startapp web
```
"""
