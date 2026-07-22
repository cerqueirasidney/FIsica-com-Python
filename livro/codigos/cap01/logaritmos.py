"""Logaritmos, decaimento exponencial e escalas logaritmicas."""

from pathlib import Path
import math

import matplotlib.pyplot as plt
import numpy as np

print(f"log10(1000) = {math.log10(1000):.1f}")
print(f"ln(4) = {math.log(4):.6f}")

tau = 2.0  # s
tempo_quarto = tau * math.log(4)
print(f"Tempo para N0/4: {tempo_quarto:.3f} s")

x = np.logspace(0, 2, 200)
y = 3 * x**2

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.loglog(x, y, color="tab:blue", linewidth=2, label=r"$y=3x^2$")
ax.set_xlabel(r"$x$ (escala logaritmica)")
ax.set_ylabel(r"$y$ (escala logaritmica)")
ax.grid(True, which="both", alpha=0.3)
ax.legend()
fig.tight_layout()

pasta_figuras = Path("figuras") / "cap01"
pasta_figuras.mkdir(parents=True, exist_ok=True)
arquivo = pasta_figuras / "lei-potencia-loglog.pdf"
fig.savefig(arquivo, bbox_inches="tight")
plt.close(fig)

print("Gráfico salvo em figuras/cap01/lei-potencia-loglog.pdf")
