"""Representação de funções matemáticas em domínios escolhidos."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.2, 4.0, 300)

def funcao_linear(valor):
    return 2.0 * valor + 1.0

def funcao_quadratica(valor):
    return valor**2

def funcao_inversa(valor):
    return 1.0 / valor

fig, eixos = plt.subplots(1, 3, figsize=(10, 3.4))

funcoes = [funcao_linear, funcao_quadratica, funcao_inversa]
rotulos = [r"$f(x)=2x+1$", r"$g(x)=x^2$", r"$h(x)=1/x$"]

for ax, funcao, rotulo in zip(eixos, funcoes, rotulos):
    ax.plot(x, funcao(x), label=rotulo)
    ax.set_xlabel("x")
    ax.set_ylabel("valor da função")
    ax.grid(alpha=0.3)
    ax.legend()

fig.tight_layout()

pasta_figuras = Path("figuras") / "cap01"
pasta_figuras.mkdir(parents=True, exist_ok=True)
arquivo = pasta_figuras / "funcoes-basicas.pdf"
fig.savefig(arquivo, bbox_inches="tight")
plt.close(fig)

print(f"Domínio: {x[0]:.1f} <= x <= {x[-1]:.1f}")
print(f"Quantidade de pontos: {x.size}")
print("Gráfico salvo em figuras/cap01/funcoes-basicas.pdf")
