import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

# Dados dos clientes (como lista de dicionários)
clientes = [
    {"Clientes_ID": 1, "Nome": "Abagael", "Numero": "9912467124", "Email": "abagael@gmail.com"},
    {"Clientes_ID": 2, "Nome": "Anneliese", "Numero": "9120230121", "Email": "anneliese@gmail.com"},
    {"Clientes_ID": 3, "Nome": "Faustine", "Numero": "9177664652", "Email": "faustine@gmail.com"},
    {"Clientes_ID": 4, "Nome": "Happy", "Numero": "9912668780", "Email": "happy@gmail.com"},
    {"Clientes_ID": 5, "Nome": "Josy", "Numero": "9120468700", "Email": "josy@gmail.com"},
]

# Extrair a primeira letra de cada nome para classificar
primeiras_letras = [cliente["Nome"][0].upper() for cliente in clientes]

# Contar a frequência de cada letra
contagem_letras = Counter(primeiras_letras)

# Criar o gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(contagem_letras.keys(), contagem_letras.values(), color="skyblue")
plt.title("Classificação de Clientes por Primeira Letra do Nome", fontsize=14)
plt.xlabel("Primeira Letra", fontsize=12)
plt.ylabel("Quantidade de Clientes", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Exibir o gráfico
plt.show()