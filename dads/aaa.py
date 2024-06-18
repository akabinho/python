"""
Descrição das variáveis:
  - quantidade_pares: Quantidade de números pares.
  - quantidade_impares: Quantidade de números ímpares.
  - quantidade_positivos: Quantidade de números positivos.
  - quantidade_negativos: Quantidade de números negativos.
  - maior_numero: O maior número.
  - menor_numero: O menor número.
  - media_pares: Média dos números pares.
  - media_impares: Média dos números ímpares.
  - media_geral: Média de todos os números.
  - numeros_invertidos: Os números na ordem inversa.
"""

import os 
os.system("cls || clear")

# Variáveis para armazenar os números
lista_numeros = []
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista_numeros.append(numero)

if numero % 2 == 0:
    pares += 1
else:
    impares += 1

if numero > 0:
    positivos += 1
elif numero < 0:
    negativos += 1 
    

# Calculando as médias
media_pares = pares / pares if pares > 0 else 0
media_impares = impares / impares if impares > 0 else 0 
media_geral = sum(lista_numeros) 

# Invertendo a ordem dos números 
numeros_inverso = lista_numeros[::-1]

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print(f"Quantidade de positivos: {positivos}")
print(f"Quantidade de negativos: {negativos}")
print(f"Soma: {sum(lista_numeros)}")
print(f"Maior número: {max(lista_numeros)}")
print(f"Menor número: {min(lista_numeros)}")
print(f"Media dos numero pares: {media_pares}")
print(f"Media dos numero impares: {media_impares}")
print(f"Media de números inseridos: {media_geral}")
print(f"Numero na ordem inversa: {numeros_inverso}")
