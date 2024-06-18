import os
os.system("cls || clear")

def calcular_soma(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def calcular_subtracao(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero

def calcular_divisao(primeiro_numero, segundo_numero):
    return primeiro_numero / segundo_numero

def calcular_multiplicacao(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero

primeiro_numero = int(input(f"Digite o primeiro número: "))
segundo_numero = int(input(f"Digite o segundo número: "))

soma = calcular_soma(primeiro_numero, segundo_numero)
subtracao = calcular_subtracao(primeiro_numero, segundo_numero)
divisao = calcular_divisao(primeiro_numero, segundo_numero)
multiplicacao = calcular_multiplicacao(primeiro_numero, segundo_numero)

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Divisão: {divisao}")
print(f"Multiplicação: {multiplicacao}")


