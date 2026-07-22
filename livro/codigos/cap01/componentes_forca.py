"""Representação de uma força e de suas componentes cartesianas."""

from pathlib import Path
import math

import matplotlib.pyplot as plt

forca = 80.0  # newtons
angulo_graus = 30.0
angulo = math.radians(angulo_graus)

forca_x = forca * math.cos(angulo)
forca_y = forca * math.sin(angulo)

fig, eixos = plt.subplots(1, 2, figsize=(9, 4.2), sharex=True, sharey=True)

for ax in eixos:
    ax.axhline(0, color="0.25", linewidth=0.8)
    ax.axvline(0, color="0.25", linewidth=0.8)
    ax.set_xlim(-5, 85)
    ax.set_ylim(-5, 65)
    ax.set_xlabel(r"componente horizontal $F_x$ (N)")
    ax.set_ylabel(r"componente vertical $F_y$ (N)")
    ax.set_aspect("equal")
    ax.grid(alpha=0.25)

# Primeiro painel: somente a força e o ângulo.
eixos[0].quiver(
    0, 0, forca_x, forca_y,
    angles="xy", scale_units="xy", scale=1,
    color="tab:blue", width=0.012,
)
eixos[0].text(forca_x * 0.52, forca_y * 0.60, r"$\vec{F}$", fontsize=12)
arco_x = [12 * math.cos(math.radians(a)) for a in range(31)]
arco_y = [12 * math.sin(math.radians(a)) for a in range(31)]
eixos[0].plot(arco_x, arco_y, color="0.25")
eixos[0].text(13, 3.5, r"$30^\circ$")
eixos[0].set_title("1. Vetor força")

# Segundo painel: força e projeções nos eixos cartesianos.
eixos[1].quiver(
    0, 0, forca_x, forca_y,
    angles="xy", scale_units="xy", scale=1,
    color="tab:blue", width=0.010,
)
eixos[1].quiver(
    0, 0, forca_x, 0,
    angles="xy", scale_units="xy", scale=1,
    color="tab:orange", width=0.012,
)
eixos[1].quiver(
    0, 0, 0, forca_y,
    angles="xy", scale_units="xy", scale=1,
    color="tab:green", width=0.012,
)
eixos[1].plot([forca_x, forca_x], [0, forca_y], "--", color="0.4")
eixos[1].plot([0, forca_x], [forca_y, forca_y], "--", color="0.4")
eixos[1].text(forca_x * 0.45, -4, r"$F_x$", color="tab:orange")
eixos[1].text(-5, forca_y * 0.45, r"$F_y$", color="tab:green")
eixos[1].text(forca_x * 0.55, forca_y * 0.60, r"$\vec{F}$", fontsize=12)
eixos[1].set_title("2. Componentes cartesianas")

fig.tight_layout()

pasta_figuras = Path("figuras") / "cap01"
pasta_figuras.mkdir(parents=True, exist_ok=True)
arquivo = pasta_figuras / "componentes-forca.pdf"
fig.savefig(arquivo, bbox_inches="tight")
plt.close(fig)

print(f"Fx = {forca_x:.1f} N")
print(f"Fy = {forca_y:.1f} N")
print("Gráfico salvo em figuras/cap01/componentes-forca.pdf")
