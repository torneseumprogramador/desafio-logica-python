lista_aberta = []
lista_aberta.append("Danilo")
lista_aberta.append("Walter")
lista_aberta.append("Douglas")
print(type(lista_aberta))
print(lista_aberta)

print("----------------------------")

lista_fechada = ("Jo", "cassio", "Nathalia")
print(type(lista_fechada))
print(lista_fechada)

print("-----------[Cast de tuple para lista e vice versa]-----------------")
lista_fechada = list(lista_fechada)
print(type(lista_fechada))
lista_fechada.append("Monica")
print(lista_fechada)
print("----------------------------")
lista_fechada = tuple(lista_fechada)
print(type(lista_fechada))
print(lista_fechada)

