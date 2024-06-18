import os
os.system("cls || clear")

# Função com retorno.
def calcular_media(lista_notas):
    soma = sum(lista_notas)
    quantidade_notas = len(lista_notas)
    resultado = soma / quantidade_notas
    return resultado

lista_notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1}º nota: "))
    lista_notas.append(nota)

# Chamando a função com retorno.
media = calcular_media(lista_notas)

print(f"Média: {media}")