import os 
from dataclasses import dataclass

os.system("cls || clear")

QUANTIDADE_LIVRO = 2

@dataclass
class Livro:
    titulo: str
    autor: str 
    numero_paginas: int
    preco: float 

livros = []

print("Solicitando dados.")
for i in range(QUANTIDADE_LIVRO):
    livro = Livro(
        titulo = input("Digite o título do livro: "),
        autor = (input("Informe o nome do autor: ")),
        numero_paginas = int(input("Digite o número de páginas: ")),
        preco = float(input("Digite o preço do livro: "))
    )
    livros.append(livro)
    print()

# Nome do arquivo.
nome_do_arquivo = 'ficha_livros.txt'

# Grava os dados no arquivo
with open(nome_do_arquivo, 'w') as arquivo:
    for livro in livros:
        arquivo.write(f"{livro.titulo}, {livro.autor}, {livro.numero_paginas}, {livro.preco}\n")

print(f"Dados gravados em {arquivo}")

# Lista para armazenar os alunos lidos
listaLivros = []

# Lê os dados do arquivo
with open(nome_do_arquivo, 'r') as arquivo:
    for linha in arquivo:
        titulo, autor, numero_paginas, preco = linha.strip().split(',')
        listaLivros.append(Livro(titulo=titulo, autor=autor, numero_paginas=int(numero_paginas), preco=preco))

# Exibe os dados lidos
print("\nExibindo dados.")
for i in listaLivros:
    print(f"Título: {i.titulo}")
    print(f"Autor: {i.autor}")
    print(f"Número de Páginas: {i.numero_paginas}")
    print(f"Preço: {i.preco}")