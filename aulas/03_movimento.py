"""Aula 03 — comparar posição e velocidade em dois gráficos."""

import matplotlib.pyplot as plt
import numpy as np

tempo = np.linspace(0.0, 8.0, 161)
posicao_inicial = 0.0
velocidade_inicial = 12.0
aceleracao = -2.0

# FÍSICA: equações para aceleração constante.
posicao = posicao_inicial + velocidade_inicial * tempo + 0.5 * aceleracao * tempo**2
velocidade = velocidade_inicial + aceleracao * tempo

# PYTHON: dois eixos compartilham o mesmo eixo horizontal de tempo.
figura, (eixo_x, eixo_v) = plt.subplots(2, 1, sharex=True)

eixo_x.plot(tempo, posicao, label="posição", color="tab:blue")
eixo_x.set_ylabel("posição, x (m)")
eixo_x.grid(alpha=0.3)
eixo_x.legend()

eixo_v.plot(tempo, velocidade, label="velocidade", color="tab:orange")
eixo_v.axhline(0, color="0.25", linewidth=0.8)
eixo_v.set_xlabel("tempo, t (s)")
eixo_v.set_ylabel("velocidade, v (m/s)")
eixo_v.grid(alpha=0.3)
eixo_v.legend()

figura.suptitle("Movimento com aceleração constante")
figura.tight_layout()
plt.show()

# EXPERIMENTE:
# 1. Em que instante a velocidade se anula?
# 2. Onde esse instante aparece no gráfico da posição?
# 3. Troque a aceleração por um valor positivo.

