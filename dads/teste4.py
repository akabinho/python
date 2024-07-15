from typing import List

TAM = 3

def calcular_media(notas: List[float]) -> float:
    """
    Calcula a média das notas fornecidas.

    Args:
        notas (List[float]): Lista de notas.

    Returns:
        float: Média das notas.
    """
    soma: float = sum(notas)
    return soma / TAM

def verificar_situacao(media: float) -> str:
    """
    Verifica a situação do aluno com base na média.

    Args:
        media (float): Média das notas.

    Returns:
        str: Situação do aluno ("Aprovado!" ou "Reprovado!").
    """
    return "Aprovado!" if media >= 7 else "Reprovado!"

def mostrar_resultado(notas: List[float]) -> None:
    """
    Mostra a média e a situação do aluno.

    Args:
        notas (List[float]): Lista de notas.
    """
    media: float = calcular_media(notas)
    situacao: str = verificar_situacao(media)
    print(f"\nMédia: {media:.1f}")
    print(f"Resultado: {situacao}")

def main() -> None:
    """
    Função principal que executa o programa.
    """
    notas: List[float] = []

    for i in range(TAM):
        nota: float = float(input(f"Digite a {i + 1}ª nota: "))
        notas.append(nota)
    
    mostrar_resultado(notas)

if __name__ == "__main__":
    main()
