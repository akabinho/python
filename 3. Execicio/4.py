import os

os.system("cls || clear")

loginSalvo = "admin"
senhaSalva = "1234"

login = str(input("Digite seu login: "))

os.system("cls || clear")

senha = str(input("Digite sua senha: "))

os.system("cls || clear")

if login == loginSalvo and senha == senhaSalva:
    print("Sucesso: Bem-vindo!")
else:
    print("Login Invalido!")

print(f"Login: {loginSalvo}")
print(f"Senha: {senhaSalva}")    

# && = and
# || = or