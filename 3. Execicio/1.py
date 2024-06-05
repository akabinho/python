import os

os.system("cls || clear")


nome = (input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
primeiraNota = int(input("Digite sua primeira nota: "))
segundaNota = int(input("Digite sua segunda nota: "))

nota = primeiraNota + segundaNota

media = nota / 2

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"primeiraNota: {primeiraNota}")
print(f"segundaNota: {segundaNota}")
print(f"nota: {nota}")
print(f"media: {media}")