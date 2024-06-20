import os
os.system("cls || clear")

def verificar_paridade(numero):
    if numero % 2 == 0:
        print("é um número par.")
    else:
        print("é um número ímpar.")

numero = int(input("Digite um número: "))
verificar_paridade(numero)