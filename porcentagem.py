
total = float(input("Digite o valor total\n"))
retirada = float(input("Digite o valor de retirada\n"))
ficou = total - retirada

porcentagem = ficou / total * 100

print("Estamos operando com {:0.2f}% da capacidade".format(porcentagem))