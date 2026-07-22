"""Integral como area algebrica sob um grafico."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

tempo = np.linspace(0, 4, 401)  # s
velocidade = 2 * tempo  # m/s

deslocamento_numerico = np.trapezoid(velocidade, tempo)
deslocamento_exato = 4**2

print(f"Deslocamento exato: {deslocamento_exato:.2f} m")
print(f"Deslocamento numerico: {deslocamento_numerico:.2f} m")

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(tempo, velocidade, color="tab:blue", linewidth=2, label=r"$v(t)=2t$")
ax.fill_between(
    tempo,
    velocidade,
    color="tab:blue",
    alpha=0.2,
    label=r"$\Delta x=\int_0^4 v(t)\,dt$",
)
ax.set_xlabel("tempo, t (s)")
ax.set_ylabel("velocidade, v (m/s)")
ax.set_xlim(0, 4)
ax.set_ylim(0, 8.5)
ax.grid(alpha=0.3)
ax.legend()
fig.tight_layout()

pasta_figuras = Path("figuras") / "cap01"
pasta_figuras.mkdir(parents=True, exist_ok=True)
arquivo = pasta_figuras / "integral-area.pdf"
fig.savefig(arquivo, bbox_inches="tight")
plt.close(fig)

print("Gráfico salvo em figuras/cap01/integral-area.pdf")
