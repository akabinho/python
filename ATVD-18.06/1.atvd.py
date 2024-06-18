import os

def logo_senai():
    os.system("cls || clear")
    print("== SENAI | FIEB ==") 

def calcular_notas(lista_notas):
    soma = sum(lista_notas)
    quantidade_notas = len(lista_notas)
    resultado = soma / quantidade_notas
    return resultado

lista_notas = []

for i in range(4):
    logo_senai()
    nota = float(input(f"Digite a {i+1}º nota: "))
    lista_notas.append(nota)

media = calcular_notas(lista_notas)

logo_senai()
print(f"Média: {media}")
