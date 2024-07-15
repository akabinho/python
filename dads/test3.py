import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("== SENAI ==")

# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para interpretar o IMC
def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau 1"
    elif 35 <= imc < 40:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3 (mórbida)"

# Definindo listas vazias para armazenar os dados do usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")

    # Verificar se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("Digite o sobrenome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))

    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    nome_completo = f"{nomes[i]} {sobrenomes[i]}"
    imc = calcular_imc(pesos[i], alturas[i])
    situacao_imc = interpretar_imc(imc)
    
    print(f"Usuário {i + 1}:")
    print("Nome completo:", nome_completo)
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"IMC: {imc:.2f}")
    print("Situação:", situacao_imc)
    print()
