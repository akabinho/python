import os 
os.system("cls || clear")

# Criando o vetor(chamado de lista).
lista_numeros = []

# Variáeis para armazenar os números.
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

# Exibindo resultados.
for i in range(5):
    print(f"Número: {lista_numeros[i]}")


# É chamado de ForEach:
'''
for numero in lista_numeros:
    print(f"Número: {numero}")
'''

'''
print(f"Soma: {sum(lista_numeros)}")
print(f"Maior número:{ max(lista_numeros)}")
'''