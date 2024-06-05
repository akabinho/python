import os

os.system("cls || clear")


nome = (input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
primeiraNota = int(input("Digite sua primeira nota: "))
segundaNota = int(input("Digite sua segunda nota: "))
terceiraNota = int(input("Digite sua terceira nota: "))

nota = primeiraNota + segundaNota + terceiraNota

media = nota / 3

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"notas inseridas: {primeiraNota}, {segundaNota}, {terceiraNota}")
print(f"nota: {nota}")
print(f"media: {media}")

if media < 7:
    print("Reprovado!")
else:
    print("Aprovado!")