import os

os.system("cls || clear")

primeiroNumero = int(input("Digite o primeiro numero: "))
segundoNumero = int(input("Digite o segundo numero: "))

soma = primeiroNumero + segundoNumero
produto = primeiroNumero * segundoNumero

if primeiroNumero > segundoNumero:
    print("É Maior!")
else:
    print("É Menor!")

if primeiroNumero == segundoNumero:
    print("Primeiro numero é igual ao Segundo Numero!")
else:
    print("Primeiro numero não é igual ao segundo numero")

media = soma / 2

print(f"Numeros inseridas: {primeiroNumero}, {segundoNumero}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Media: {media}")


# Alternativa para maior e menor:
#maior = max(primeiroNumero, segundoNumero)
#menor = min(primeiroNumero, segundoNumero)

# Maior e menor se n forem iguais:
#if primeiroNumero == segundoNumero:
#   print("Os números são iguais.")
#else:
#   print(f"Maior Número: {maior}")
#   print(f"Menor Número: {menor}")