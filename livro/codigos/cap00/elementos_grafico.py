"""Elementos de um gráfico científico com duas séries de dados."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

tempo = np.linspace(0, 5, 101)
posicao_a = 2.0 * tempo
posicao_b = 1.0 + 1.2 * tempo

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(tempo, posicao_a, color="tab:blue", label="Objeto A")
ax.plot(
    tempo,
    posicao_b,
    color="tab:orange",
    linestyle="--",
    label="Objeto B",
)
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Posição (m)")
ax.set_title("Comparação entre dois movimentos")
ax.set_xlim(0, 5)
ax.set_ylim(0, 11)
ax.grid(alpha=0.3)
ax.legend()
ax.annotate(
    "mesma posição",
    xy=(1.25, 2.5),
    xytext=(2.0, 1.2),
    arrowprops={"arrowstyle": "->"},
)
fig.tight_layout()

pasta_figuras = Path("figuras") / "cap00"
pasta_figuras.mkdir(parents=True, exist_ok=True)
arquivo = pasta_figuras / "elementos-grafico.pdf"
fig.savefig(arquivo, bbox_inches="tight")
plt.close(fig)

print(f"Foram calculados {tempo.size} pontos por curva.")
print("Gráfico salvo em figuras/cap00/elementos-grafico.pdf")
