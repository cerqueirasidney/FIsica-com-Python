"""Valores trigonometricos e grafico de seno e cosseno."""

from pathlib import Path
import math

import matplotlib.pyplot as plt
import numpy as np

for angulo_graus in (0, 30, 45, 60, 90):
    angulo_rad = math.radians(angulo_graus)
    seno = math.sin(angulo_rad)
    cosseno = math.cos(angulo_rad)
    print(
        f"{angulo_graus:>2} graus: "
        f"sen = {seno:.4f}, cos = {cosseno:.4f}"
    )

theta = np.linspace(0, 2 * np.pi, 500)
angulo_desenho = math.radians(40)

fig, ax = plt.subplots(figsize=(5, 5))
ax.add_patch(plt.Circle((0, 0), 1, fill=False, color="0.25", linewidth=1.5))
x_ponto = math.cos(angulo_desenho)
y_ponto = math.sin(angulo_desenho)
ax.quiver(
    0,
    0,
    x_ponto,
    y_ponto,
    angles="xy",
    scale_units="xy",
    scale=1,
    color="tab:blue",
    label=r"raio unitario",
)
ax.plot([x_ponto, x_ponto], [0, y_ponto], "--", color="tab:orange")
ax.plot([0, x_ponto], [y_ponto, y_ponto], "--", color="tab:green")
ax.text(x_ponto / 2, -0.10, r"$\cos(\theta)$", ha="center")
ax.text(x_ponto + 0.08, y_ponto / 2, r"$\sin(\theta)$", va="center")
arco = np.linspace(0, angulo_desenho, 80)
ax.plot(0.22 * np.cos(arco), 0.22 * np.sin(arco), color="tab:red")
ax.text(0.27, 0.08, r"$\theta$")
ax.axhline(0, color="0.25", linewidth=0.8)
ax.axvline(0, color="0.25", linewidth=0.8)
ax.set_xlabel(r"eixo $x$")
ax.set_ylabel(r"eixo $y$")
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect("equal")
ax.grid(alpha=0.25)
fig.tight_layout()

destino = Path(__file__).resolve().parents[2] / "figuras" / "cap01"
destino.mkdir(parents=True, exist_ok=True)
fig.savefig(destino / "circulo-trigonometrico.pdf", bbox_inches="tight")
plt.close(fig)

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(theta, np.sin(theta), color="tab:blue", label=r"$\sin(\theta)$")
ax.plot(
    theta,
    np.cos(theta),
    color="tab:orange",
    linestyle="--",
    label=r"$\cos(\theta)$",
)
ax.axhline(0, color="0.25", linewidth=0.8)
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.15, 1.15)
ax.set_xticks(
    [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
    [r"$0$", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"],
)
ax.set_xlabel(r"angulo $\theta$ (rad)")
ax.set_ylabel("valor da funcao")
ax.grid(alpha=0.3)
ax.legend()
fig.tight_layout()

fig.savefig(destino / "seno-cosseno.pdf", bbox_inches="tight")
plt.close(fig)
