import os 
os.system ("cls || clear")

def solicitar_dados():
    # Solicita a matrícula, senha e salário base do funcionário.
    matricula = input("Digite a matrícula do funcionário: ")
    senha = input("Digite a senha do funcionário: ")
    salario_base = float(input("Digite o salário base do funcionário (R$): "))
    return matricula, senha, salario_base

def calcular_inss(salario_base):
    # Calcula o desconto do INSS com base no salário base do funcionário.
    if salario_base <= 1100.00:
        return salario_base * 0.075
    elif salario_base <= 2203.48:
        return salario_base * 0.09
    elif salario_base <= 3305.22:
        return salario_base * 0.12
    elif salario_base <= 6433.57:
        return salario_base * 0.14
    else:
        return 854.36

def calcular_irrf(salario_base, dependentes):
    # Calcula o desconto do IRRF com base no salário base do funcionário e número de dependentes.
    deducao_dependente = 189.59
    base_calculo = salario_base - (deducao_dependente * dependentes)
    
    if base_calculo <= 1903.98:
        return 0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225
    else:
        return base_calculo * 0.275

def calcular_vale_transporte(salario_base, utiliza_vale):
    # Calcula o desconto do vale transporte, se aplicável.
    return salario_base * 0.06 if utiliza_vale else 0

def calcular_vale_refeicao(valor):
    # Calcula o desconto do vale refeição.
    return valor * 0.20

def calcular_plano_saude():
    # Calcula o desconto do plano de saúde.
    return 150.00

def calcular_salario_liquido(salario_base, inss, irrf, vale_transporte, vale_refeicao, plano_saude):
    # Calcula o salário líquido após aplicar os descontos.
    total_descontos = inss + irrf + vale_transporte + vale_refeicao + plano_saude
    return salario_base - total_descontos

def main():
    # Função principal que coordena a entrada de dados e cálculo do salário líquido.
    matricula, senha, salario_base = solicitar_dados()
    dependentes = 1  # Considerando que o funcionário possui apenas um dependente
    
    utiliza_vale = input("Deseja receber vale transporte? (s/n): ").lower() == 's'
    valor_vale_refeicao = float(input("Digite o valor do vale refeição fornecido pela empresa (R$): "))
    
    inss = calcular_inss(salario_base)
    irrf = calcular_irrf(salario_base, dependentes)
    vale_transporte = calcular_vale_transporte(salario_base, utiliza_vale)
    vale_refeicao = calcular_vale_refeicao(valor_vale_refeicao)
    plano_saude = calcular_plano_saude()
    
    salario_liquido = calcular_salario_liquido(salario_base, inss, irrf, vale_transporte, vale_refeicao, plano_saude)
    
    print("\nDetalhamento dos descontos:")
    print(f"INSS: R$ {inss:.2f}")
    print(f"IRRF: R$ {irrf:.2f}")
    print(f"Vale Transporte: R$ {vale_transporte:.2f}")
    print(f"Vale Refeição: R$ {vale_refeicao:.2f}")
    print(f"Plano de Saúde: R$ {plano_saude:.2f}")
    
    print(f"\nSalário líquido: R$ {salario_liquido:.2f}")

# Garantir que a função main seja executada apenas quando o script é executado diretamente.
if __name__ == "__main__":
    main()
