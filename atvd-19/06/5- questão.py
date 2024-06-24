import os
os.system("cls || clear")

def calcular_nascimento(nascimento):
    ano_atual = 2024
    idade = ano_atual - nascimento
    return idade

nascimento = int(input("Digite o ano que foi nascido: "))
idade = calcular_nascimento(nascimento)

print(f"A idade informada é {idade} anos.")