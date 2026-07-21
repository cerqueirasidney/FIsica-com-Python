"""Funções básicas para estudar movimento uniforme."""


def posicao(t: float, x0: float = 0.0, v: float = 1.0) -> float:
    """Calcula x(t) = x0 + v*t usando unidades consistentes."""
    return x0 + v * t


if __name__ == "__main__":
    print(f"x(5 s) = {posicao(5, x0=2, v=3):.1f} m")

