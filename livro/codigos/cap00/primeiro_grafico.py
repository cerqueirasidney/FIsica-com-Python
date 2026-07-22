"""Primeiro gráfico: posição medida em diferentes instantes."""

from pathlib import Path

import matplotlib.pyplot as plt

tempo = [0, 1, 2, 3, 4]
posicao = [0, 2, 4, 6, 8]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(tempo, posicao, marker="o")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Posição (m)")
ax.set_title("Movimento uniforme")
fig.tight_layout()

pasta_figuras = Path("figuras") / "cap00"
pasta_figuras.mkdir(parents=True, exist_ok=True)
arquivo = pasta_figuras / "primeiro-grafico.pdf"
fig.savefig(arquivo, bbox_inches="tight")
plt.close(fig)

print("Gráfico salvo em figuras/cap00/primeiro-grafico.pdf")
