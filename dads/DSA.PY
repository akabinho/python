import os 
os.system("cls || clear") 

lista_numeros = []
notas = 0

for i in range(4):
    nota = int(input(f"Digite o {i + 1}º nota: "))
    lista_numeros.append(nota)

for notas in lista_numeros:
    print(f"Notas: {notas}")

if nota >= 7:
    print("Aprovado!")
else: 
    print("Reprovado!")

media_geral = sum(lista_numeros) / len(lista_numeros)

print(f"Média: {media_geral}")

