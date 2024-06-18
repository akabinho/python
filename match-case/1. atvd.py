import os 
os.system("cls || clear")

dia_semana = int(input("Digite o número do dia: "))

match(dia_semana):
    case 1: 
        print("Domingo")
        print("Final de semana")
    case 2:
        print("Segunda")
        print("Dia Útil")
    case 3: 
        print("Terça")
        print("Dia Útil")
    case 4: 
        print("Quarta")
        print("Dia Útil")
    case 5:
        print("Quinta")
        print("Dia Útil")
    case 6: 
        print("Sexta")
        print("Dia Útil")
    case 7: 
        print("Sábado")
        print("Final de semana")
    case _:
        print("Opção Inválida.")

print("==FIM==")

