import os 
from dataclasses import dataclass

os.system("cls || clear")

QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno:
    nome: str
    idade: int
    altura: float
    peso: float
    CPF: float
    email: str

alunos = []

print("Solicitando dados.")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite sua altura: ")),
        CPF = float(input("Digite seu CPF: ")),
        email = str(input("Digite seu email: "))
    )
    alunos.append(aluno)
    print()

# Nome do arquivo.
nome_do_arquivo = 'ficha_alunos.txt'

# Grava os dados no arquivo
with open(nome_do_arquivo, 'w') as arquivo:
    for aluno in alunos:
        arquivo.write(f"{aluno.nome}, {aluno.idade}, {aluno.peso}, {aluno.altura}, {aluno.CPF}, {aluno.email}\n")

print(f"Dados gravados em {arquivo}")

# Lista para armazenar os alunos lidos
listaAlunos = []

# Lê os dados do arquivo
with open(nome_do_arquivo, 'r') as arquivo:
    for linha in arquivo:
        nome, idade, peso, altura, CPF, email = linha.strip().split(',')
        listaAlunos.append(Aluno(nome=nome, idade=int(idade), peso=peso, altura=altura,CPF=CPF, email=email))

# Exibe os dados lidos
print("\nExibindo dados.")
for i in listaAlunos:
    print(f"Nome: {i.nome}")
    print(f"idade: {i.idade}")
    print(f"peso: {i.peso}")
    print(f"Altura: {i.altura}")
    print(f"CPF: {i.CPF}")
    print(f"Email: {i.email}")