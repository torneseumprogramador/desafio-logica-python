# https://www.w3schools.com/python/python_arrays.asp

a = [1,2,4,5,7,8,9]
print("Criando array")

cars = ["Ford", "Volvo", "BMW"]

# cars[2] = "Mercedes"
# cars[3] = "Mercedes" # não deixa pois não existe este indice
# cars[1] = 2.3

cars.append("Mercedes") # acrescenta um item dentro da lista
cars.append("Cherry")
cars.append("Kia")
cars.append("Kia")

# car1 = cars.pop() # tira o ultimo item da lista
# car2 = cars.pop(1) # tira um item da lista baseado em seu indice
cars.remove("Cherry") # tira um item da lista baseado em seu indice

# cars.clear() # limpa todos os dados da lista

copy_of_cars = cars

qtd = copy_of_cars.count("Kia") # conta a quantidade baseado no valor passado
qtd = len(copy_of_cars) # conta a quantidade no total

new_cars = ["Honda", "Fiat"]
copy_of_cars.extend(new_cars) # faz um merge de lista

copy_of_cars.insert(1, "Yahha") # insere um item pelo indice da lista

copy_of_cars.sort() # ordena as informações da lista
copy_of_cars.reverse() # inverte as informações da lista


for x in cars:
  print(f"O valor do array no seu indice é {x}")


matriz = [[3,4,7], [6,8,9]]
retorna_o_8 = matriz[1][1]

# lista itens da matriz

for itens in matriz:
  print("=======[Matriz]======")
  for item in itens:
    print(f"Item: {item}")




# tamanho máximo, depende da quantidade de memória que tem em um computador 
import six
print(f"O tamanho máximo de itens na lista deste computador {six.MAXSIZE}")
