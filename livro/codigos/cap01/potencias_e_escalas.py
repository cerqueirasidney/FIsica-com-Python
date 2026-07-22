"""Potencias, raizes e uma verificacao de lei de escala."""

quadrado = 5**2
cubo = 3**3
potencia_negativa = 10**-3
raiz_quadrada = 25**0.5
raiz_cubica = 64 ** (1 / 3)

print(f"5 ao quadrado = {quadrado}")
print(f"3 ao cubo = {cubo}")
print(f"10 elevado a -3 = {potencia_negativa}")
print(f"Raiz quadrada de 25 = {raiz_quadrada}")
print(f"Raiz cubica de 64 = {raiz_cubica}")
print(f"Raiz cubica de 64, formatada = {raiz_cubica:.2f}")

massa = 2.0  # kg
velocidade_1 = 3.0  # m/s
velocidade_2 = 3 * velocidade_1

energia_1 = 0.5 * massa * velocidade_1**2
energia_2 = 0.5 * massa * velocidade_2**2

fator_velocidade = velocidade_2 / velocidade_1
fator_energia = energia_2 / energia_1

print(f"Energia cinetica inicial = {energia_1:.2f} J")
print(f"Energia cinetica final = {energia_2:.2f} J")
print(f"Fator da velocidade = {fator_velocidade:.0f}")
print(f"Fator da energia = {fator_energia:.0f}")

