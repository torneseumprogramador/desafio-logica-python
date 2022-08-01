# aluno = {
#     "nome": "Daniel",
#     "notas": [5,8,9],
#     "media": 7.33,
#     "situacao": "Recuperação"
# }

aluno = {}
aluno["nome"] = "Daniel"
aluno["notas"] = [5,8,9]
aluno["media"] = 7.33
aluno["situacao"] = "Recuperação"

print(f"Tipo da variável aluno {type(aluno)}")

print("-----------------------")
print(f"Nome: {aluno['nome']}")
print(f"Notas: {aluno['notas']}")
print(f"Média: {aluno['media']}")
print(f"Situação: {aluno['situacao']}")