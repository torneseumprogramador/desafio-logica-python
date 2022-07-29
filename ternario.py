numero = int(input("Digite o tipo:\n1 - Numero\n2- String\n"))
# resultado = (numero == 1 ? "Número" : "String") # outras linguagens
resultado = 'Número' if numero == 1 else 'String'
print(f"O tipo digitado foi {resultado}")
