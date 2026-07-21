"""Ferramentas elementares de incerteza para os capítulos iniciais."""

from math import hypot


def divisao_com_incerteza(
    numerador: float,
    sigma_numerador: float,
    denominador: float,
    sigma_denominador: float,
) -> tuple[float, float]:
    """Propaga incertezas independentes para y = numerador / denominador."""
    if denominador == 0:
        raise ValueError("o denominador não pode ser zero")
    if sigma_numerador < 0 or sigma_denominador < 0:
        raise ValueError("incertezas devem ser não negativas")

    valor = numerador / denominador
    termo_n = sigma_numerador / numerador if numerador != 0 else 0.0
    termo_d = sigma_denominador / denominador
    sigma = abs(valor) * hypot(termo_n, termo_d)
    return valor, sigma

