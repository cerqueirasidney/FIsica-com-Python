"""Derivada como inclinacao da reta tangente."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**2


x0 = 2.0
h = 1e-5
derivada_numerica = (f(x0 + h) - f(x0 - h)) / (2 * h)
derivada_analitica = 2 * x0

print(f"Derivada analitica em x = {x0:.1f}: {derivada_analitica:.6f}")
print(f"Derivada numerica em x = {x0:.1f}: {derivada_numerica:.6f}")

x = np.linspace(-0.5, 4.5, 400)
tangente = f(x0) + derivada_analitica * (x - x0)

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(x, f(x), color="tab:blue", linewidth=2, label=r"$f(x)=x^2$")
ax.plot(
    x,
    tangente,
    color="tab:orange",
    linestyle="--",
    label="reta tangente em x = 2",
)
ax.scatter([x0], [f(x0)], color="tab:red", zorder=3, label="ponto de tangencia")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$f(x)$")
ax.set_ylim(-2, 20)
ax.grid(alpha=0.3)
ax.legend()
fig.tight_layout()

destino = Path(__file__).resolve().parents[2] / "figuras" / "cap01"
destino.mkdir(parents=True, exist_ok=True)
fig.savefig(destino / "derivada-tangente.pdf", bbox_inches="tight")
plt.close(fig)

