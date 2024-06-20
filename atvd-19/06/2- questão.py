import os
os.system("cls || clear")

def tabuada(numero):
    for i in range(10):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)

numero = int(input("Digite um número para ver a tabuada: "))

tabuada(numero)