"""Componentes gráficos usados repetidamente no livro.

As funções deixam explícitas escolhas importantes para figuras físicas, como
escala cartesiana, proporção entre eixos, rótulos e grade.
"""

from collections.abc import Sequence

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure


def preparar_plano_vetorial(
    limites_x: tuple[float, float],
    limites_y: tuple[float, float],
    rotulo_x: str = "componente x",
    rotulo_y: str = "componente y",
) -> tuple[Figure, Axes]:
    """Cria e configura um plano cartesiano sem distorção geométrica."""
    fig, ax = plt.subplots()
    ax.axhline(0, color="0.25", linewidth=0.7)
    ax.axvline(0, color="0.25", linewidth=0.7)
    ax.set_xlim(*limites_x)
    ax.set_ylim(*limites_y)
    ax.set_xlabel(rotulo_x)
    ax.set_ylabel(rotulo_y)
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)
    return fig, ax


def desenhar_vetor(
    ax: Axes,
    origem: Sequence[float],
    vetor: Sequence[float],
    rotulo: str,
    cor: str = "tab:blue",
) -> None:
    """Desenha um vetor 2D com escala fiel às unidades dos eixos."""
    if len(origem) != 2 or len(vetor) != 2:
        raise ValueError("origem e vetor devem ter exatamente duas componentes")

    ax.quiver(
        origem[0],
        origem[1],
        vetor[0],
        vetor[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color=cor,
        label=rotulo,
    )
