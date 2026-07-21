"""Aula 00 — números, variáveis, unidades e funções."""

# PYTHON: print mostra uma informação na tela.
print("Olá! Este é o primeiro programa do livro Física com Python.")

# PYTHON: uma variável associa um nome a um valor.
# FÍSICA: registramos as unidades nos comentários e nos nomes impressos.
distancia = 120.0  # metros
tempo = 10.0  # segundos

# PYTHON: / realiza uma divisão.
# FÍSICA: velocidade média = deslocamento / intervalo de tempo.
velocidade_media = distancia / tempo

print(f"Distância: {distancia:.1f} m")
print(f"Tempo: {tempo:.1f} s")
print(f"Velocidade média: {velocidade_media:.1f} m/s")


# PYTHON: uma função reúne instruções que podem ser reutilizadas.
def converter_m_s_para_km_h(velocidade_m_s: float) -> float:
    """Converte uma velocidade de m/s para km/h."""
    return velocidade_m_s * 3.6


velocidade_km_h = converter_m_s_para_km_h(velocidade_media)
print(f"Velocidade média: {velocidade_km_h:.1f} km/h")

# EXPERIMENTE:
# 1. Troque distancia por 250 e tempo por 20.
# 2. O que acontece se tempo for igual a zero?
# 3. Crie uma variável chamada massa, medida em quilogramas.

