def main():
    menu = {
        1: ('Bacalhau à Brás', 12.50),
        2: ('Francesinha', 15.00),
        3: ('Arroz de Pato', 10.00),
        4: ('Cozido à Portuguesa', 14.00),
        5: ('Caldo Verde', 7.00),
        6: ('Açorda de Marisco', 16.50),
        7: ('Polvo à Lagareiro', 18.00)
    }
    
    pedidos = []
    total = 0.0
    
    while True:
        print("\nMenu:")
        for codigo, (nome, preco) in menu.items():
            print(f"{codigo} - {nome} - €{preco:.2f}")
        
        codigo = int(input("\nInsira o código do prato desejado (0 para finalizar): "))
        
        if codigo == 0:
            break
        elif codigo in menu:
            pedidos.append((codigo, menu[codigo][0], menu[codigo][1]))
            total += menu[codigo][1]
        else:
            print("Código inválido. Tente novamente.")
        
        continuar = input("Deseja fazer mais um pedido? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    if not pedidos:
        print("Nenhum pedido realizado.")
        return
    
    print("\nFormas de pagamento:")
    print("1 - À vista (10% de desconto)")
    print("2 - Cartão de crédito (10% de acréscimo)")
    
    forma_pagamento = int(input("Escolha a forma de pagamento: "))
    
    if forma_pagamento == 1:
        desconto = total * 0.10
        total_final = total - desconto
        descricao_pagamento = "À vista"
    elif forma_pagamento == 2:
        acrescimo = total * 0.10
        total_final = total + acrescimo
        descricao_pagamento = "Cartão de crédito"
    else:
        print("Forma de pagamento inválida.")
        return
    
    print("\nResumo do pedido:")
    for codigo, nome, preco in pedidos:
        print(f"Código: {codigo} - {nome} - €{preco:.2f}")
    
    if forma_pagamento == 1:
        print(f"Forma de pagamento: {descricao_pagamento}")
        print(f"Desconto: -€{desconto:.2f}")
    elif forma_pagamento == 2:
        print(f"Forma de pagamento: {descricao_pagamento}")
        print(f"Acréscimo: +€{acrescimo:.2f}")
    
    print(f"Subtotal: €{total:.2f}")
    print(f"Total a pagar: €{total_final:.2f}")

if __name__ == "__main__":
    main()
    