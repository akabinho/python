import os
os.system("cls || clear")

print("--------------------------------------------------")
print("                     MENU DE OPÇÕES               ")
print("--------------------------------------------------")

print("CÓDIGO               PRATOS                  PREÇO")
print(" 1                   PICANHA                  R$25")
print(" 2                   LASANHA                  R$20")
print(" 3                  STROGONOFF                R$18")
print(" 4                 BIFE ACEBOLADO             R$15")
print(" 5                  PÃO COM OVO               R$5 ")

número_prato = int(input("Dgite o número do prato desejado: "))


match(número_prato):
    case 1: 
        print("PICANHA")
        print("R$25")
    case 2: 
        print("LASANHA")
        print("R$20")
    case 3: 
        print("STROGONOFF")
        print("R$18")
    case 4: 
        print("BIFE ACEBOLADO")
        print("R$15")
    case 5: 
        print("PÃO COM OVO")
        print("R$5")
    case _:
        print("Opção Inválida.")

print("==FIM==")