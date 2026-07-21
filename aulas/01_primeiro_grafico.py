"""Aula 01 — arrays NumPy e o primeiro gráfico científico."""

import matplotlib.pyplot as plt
import numpy as np

# PYTHON: linspace cria 101 valores igualmente espaçados entre 0 e 10.
tempo = np.linspace(0.0, 10.0, 101)  # segundos

# FÍSICA: modelo de movimento uniforme x(t) = x0 + v*t.
posicao_inicial = 2.0  # metros
velocidade = 3.0  # metros por segundo
posicao = posicao_inicial + velocidade * tempo

# PYTHON: subplots cria uma figura e um sistema de eixos.
figura, eixo = plt.subplots()
eixo.plot(tempo, posicao, label="móvel A", color="tab:blue")

# Um gráfico científico informa grandezas e unidades.
eixo.set_xlabel("tempo, t (s)")
eixo.set_ylabel("posição, x (m)")
eixo.set_title("Movimento com velocidade constante")
eixo.grid(alpha=0.3)
eixo.legend()

plt.show()

# EXPERIMENTE:
# 1. Use velocidade = -3. O que muda no gráfico?
# 2. Use posicao_inicial = 10.
# 3. Acrescente uma segunda curva com outra velocidade.

