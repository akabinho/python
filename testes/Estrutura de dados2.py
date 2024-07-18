import os 
from dataclasses import dataclass

os.system("cls || clear")

QUANTIDADE_ALUNOS = 2

class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    aluno = Aluno(nome = nome, idade = idade)
    alunos.append(aluno)

for i in alunos:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")