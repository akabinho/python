import os 
os.system("cls || clear")

numero_turma = int(input("Digite o número da turma: "))

#Equivale ao Switch-case em C.
match(numero_turma):
    case 111:
        print("Desenvolvimento de sistemas")
    case 222:
        print("Logística")
    case 333: 
        print("Alimentos")
    case _:
        print("Opção Inválida.")

print("==FIM==")
