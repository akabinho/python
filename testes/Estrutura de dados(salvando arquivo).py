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

print(f"Dados gravados com sucesso.")


# 'w' = write | 'r' = read | 'as' = apelido