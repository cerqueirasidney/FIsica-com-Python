"""Operações vetoriais pequenas, escritas para fins didáticos."""

from math import acos, degrees, sqrt
from typing import Sequence


def modulo(vetor: Sequence[float]) -> float:
    """Retorna a norma euclidiana de um vetor."""
    return sqrt(sum(componente**2 for componente in vetor))


def produto_escalar(a: Sequence[float], b: Sequence[float]) -> float:
    """Calcula o produto escalar de vetores com a mesma dimensão."""
    if len(a) != len(b):
        raise ValueError("os vetores devem ter a mesma dimensão")
    return sum(x * y for x, y in zip(a, b))


def angulo_graus(a: Sequence[float], b: Sequence[float]) -> float:
    """Calcula o menor ângulo entre dois vetores, em graus."""
    norma_a, norma_b = modulo(a), modulo(b)
    if norma_a == 0 or norma_b == 0:
        raise ValueError("o ângulo com o vetor nulo é indefinido")
    cosseno = produto_escalar(a, b) / (norma_a * norma_b)
    cosseno_limitado = max(-1.0, min(1.0, cosseno))
    return degrees(acos(cosseno_limitado))

