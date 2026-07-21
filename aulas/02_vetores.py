"""Aula 02 — componentes, módulo, soma e desenho de vetores."""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# PYTHON: informa onde está a pasta principal do projeto. Assim, esta aula pode
# importar as funções reutilizáveis que ficam na pasta codigo.
PASTA_DO_PROJETO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PASTA_DO_PROJETO))

from codigo.visualizacao import desenhar_vetor, preparar_plano_vetorial

# PYTHON: um array armazena as componentes x e y.
a = np.array([3.0, 4.0])
b = np.array([-1.0, 2.0])
resultante = a + b

# FÍSICA: o módulo é o comprimento geométrico do vetor.
modulo_a = np.linalg.norm(a)

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {resultante}")
print(f"módulo de a = {modulo_a:.2f}")

# A origem de b é deslocada até a extremidade de a.
figura, eixo = preparar_plano_vetorial(
    limites_x=(-1.0, 5.0),
    limites_y=(-1.0, 7.0),
    rotulo_x="componente x",
    rotulo_y="componente y",
)

desenhar_vetor(eixo, (0, 0), a, "vetor a", "tab:blue")
desenhar_vetor(eixo, a, b, "vetor b", "tab:orange")
desenhar_vetor(eixo, (0, 0), resultante, "resultante", "tab:green")
eixo.legend()
eixo.set_title("Soma vetorial pela regra do triângulo")
plt.show()

# EXPERIMENTE:
# 1. Altere as componentes de a e b.
# 2. Desenhe os dois vetores a partir da origem.
# 3. Crie dois vetores perpendiculares e calcule seu produto escalar.
