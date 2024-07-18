import os 
from dataclasses import dataclass

os.system("cls || clear")

QUANTIDADE_PET = 2

@dataclass
class Pet:
    nome: str
    idade: str 
    raca: str
    porte: str
    alimentacao: str

pets = []

print("Solicitando dados.")
for i in range(QUANTIDADE_PET):
    pets = Pet(
        nome = input("Digite o nome do pet: "),
        idade = (input("Informe a idade do pet: ")),
        raca = (input("Digite a raça do pet: ")),
        porte = (input("Digite o porte do pet: ")),
        alimentacao = (input("Digite o tipo de alimentação do pet: "))
    )
    pets.append(Pet)
    print()

# Nome do arquivo.
nome_do_arquivo = 'ficha_pets.txt'

# Grava os dados no arquivo
with open(nome_do_arquivo, 'w') as arquivo:
    for pets in Pet:
        arquivo.write(f"{pets.nome}, {pets.idade}, {pets.raca}, {pets.porte}, {pets.alimentacao}\n")

print(f"Dados gravados em {arquivo}")

# Lista para armazenar os alunos lidos
listaPets = []

# Lê os dados do arquivo
with open(nome_do_arquivo, 'r') as arquivo:
    for linha in arquivo:
        nome, idade, raca, porte, alimentacao = linha.strip().split(',')
        listaPets.append(Pet(nome=nome, idade=idade, raca=raca, porte=porte, alimentacao=alimentacao))

# Exibe os dados lidos
print("\nExibindo dados.")
for i in listaPets:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Raça: {i.raca}")
    print(f"Porte: {i.porte}")
    print(f"Alimentação: {i.alimentacao}")