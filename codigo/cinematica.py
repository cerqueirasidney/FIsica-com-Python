"""Modelos analíticos básicos de cinemática unidimensional."""


def posicao_mru(t: float, x0: float = 0.0, v: float = 1.0) -> float:
    """Calcula a posição no movimento com velocidade constante."""
    return x0 + v * t


def estado_mruv(
    t: float, x0: float = 0.0, v0: float = 0.0, a: float = 0.0
) -> tuple[float, float]:
    """Retorna posição e velocidade para aceleração constante."""
    posicao = x0 + v0 * t + 0.5 * a * t**2
    velocidade = v0 + a * t
    return posicao, velocidade

