import os

os.system("cls || clear")

login = input("Digite o login: ")
senha = input("Digite a senha: ")

if login == "admin" and senha == "1234":
    print("Bem-vindo!")
else:
    print("Acesso Negado!")