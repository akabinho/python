import os
os.system("cls || clear")

def metro_centimetro(metro):
    centimetro = metro * 100
    return centimetro

metro = float(input("Digite a quantidade de metro: "))
centimetro = metro_centimetro(metro)

print(f"Valor em metro: {metro}")
print(f"Valor em centimetro: {centimetro}")