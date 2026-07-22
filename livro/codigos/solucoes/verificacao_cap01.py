"""Verificação numérica de exercícios selecionados do Capítulo 1."""

import math

# Exercício 1
diametro_m = 0.00000032
diametro_nm = diametro_m / 1e-9

# Exercício 4
forca = 120.0
angulo = math.radians(40.0)
forca_x = forca * math.cos(angulo)
forca_y = forca * math.sin(angulo)

# Exercício 5
angulo_rad = math.radians(150.0)
angulo_graus = math.degrees(5 * math.pi / 6)

# Exercício 7
deslocamento = (5 * 4 - 4**2) - (5 * 0 - 0**2)

# Exercício 8
def f(x):
    return x**3 - 6 * x**2 + 9 * x + 2

# Exercício 10
velocidade = (25 - 7) / (8 - 2)
posicao_inicial = 7 - velocidade * 2

print(f"Ex. 1: {diametro_m:.1e} m = {diametro_nm:.0f} nm")
print(f"Ex. 4: Fx = {forca_x:.1f} N; Fy = {forca_y:.1f} N")
print(f"Ex. 5: 150 graus = {angulo_rad / math.pi:.3f} pi rad")
print(f"Ex. 5: 5pi/6 rad = {angulo_graus:.0f} graus")
print(f"Ex. 7: deslocamento = {deslocamento:.1f} m")
print(f"Ex. 8: f(1) = {f(1):.1f}; f(3) = {f(3):.1f}")
print(f"Ex. 10: v = {velocidade:.1f} m/s; x0 = {posicao_inicial:.1f} m")
