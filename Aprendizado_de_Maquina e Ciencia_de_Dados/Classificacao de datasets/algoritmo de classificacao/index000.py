import pandas as pd
from pathlib import Path
import os

# 1. Importação dos Datasets
# --- Define a pasta onde os datasets estão armazenados ---
pasta_datasets = Path("../Planejamento_Informatica/Aprendizado_de_Maquina e Ciencia_de_Dados/Datasets")

# --- Dicionário com os nomes dos arquivos ---
arquivos = {
    'clientes': 'Clientes.csv',
    'funcionarios': 'Funcionarios.csv',
    'departamentos': 'Departamentos.csv',
    'cargos': 'Cargos.csv',
    'salarios': 'Salarios.csv',
    'veiculos': 'Veiculos.csv',
    'aluguel': 'Aluguel.csv'
}

datasets = {}  # --- Dicionário para armazenar os DataFrames ---
for nome, arquivo in arquivos.items():
    caminho_arquivo = os.path.join(pasta_datasets, arquivo)
    print(f"Tentando carregar o arquivo: {caminho_arquivo}")
    datasets[nome] = pd.read_csv(caminho_arquivo)

# --- Exibe o conteúdo completo de cada dataset no terminal ---
for nome, df in datasets.items():
    print(f"\nConteúdo do dataset: {nome}")
    print(df.to_string())  # --- Exibe todas as linhas e colunas do dataset ---

    # Dataset de clientes como lista de dicionários
clientes = [
    {"Clientes_ID": 1, "Nome": "Abagael", "Numero": "9912467124", "Email": "abagael@gmail.com"},
    {"Clientes_ID": 2, "Nome": "Anneliese", "Numero": "9120230121", "Email": "anneliese@gmail.com"},
    {"Clientes_ID": 3, "Nome": "Faustine", "Numero": "9177664652", "Email": "faustine@gmail.com"},
    {"Clientes_ID": 4, "Nome": "Happy", "Numero": "9912668780", "Email": "happy@gmail.com"},
    {"Clientes_ID": 5, "Nome": "Josy", "Numero": "9120468700", "Email": "josy@gmail.com"},
    # Adicione outros clientes conforme necessário
]

# Função para classificar clientes por nome
def classificar_clientes_por_nome(clientes):
    return sorted(clientes, key=lambda cliente: cliente["Nome"])

# Classificar os clientes
clientes_classificados = classificar_clientes_por_nome(clientes)

# Exibir os clientes classificados
print("Clientes classificados por nome:")
for cliente in clientes_classificados:
    print(f"ID: {cliente['Clientes_ID']}, Nome: {cliente['Nome']}, Número: {cliente['Numero']}, Email: {cliente['Email']}")