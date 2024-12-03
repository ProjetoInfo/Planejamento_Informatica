import pandas as pd
import os

# Define a pasta onde os datasets estão armazenados
pasta_datasets = r'C:\Users\ah097\OneDrive\Documentos\Workspace\Faculdade\2° Semestre\Atividades\Projeto em informatica\Arquivo_empresa\Planejamento_Informatica\Aprendizado_de_Maquina e Ciencia_de_Dados\Datasets'

# Dicionário com os nomes dos arquivos, incluindo o dataset de aluguel
arquivos = {
    'clientes': 'Clientes.csv',
    'funcionarios': 'Funcionarios.csv',
    'departamentos': 'Departamentos.csv',
    'cargos': 'Cargos.csv',
    'salarios': 'Salarios.csv',
    'veiculos': 'Veiculos.csv',
    'aluguel': 'Aluguel.csv'
}

datasets = {}  # Dicionário para armazenar os DataFrames

# Carrega os arquivos no dicionário de datasets
for nome, arquivo in arquivos.items():
    caminho_arquivo = os.path.join(pasta_datasets, arquivo)
    print(f"Tentando carregar o arquivo: {caminho_arquivo}")  # Log para depuração
    datasets[nome] = pd.read_csv(caminho_arquivo)

# Exibe o conteúdo completo de cada dataset no terminal
for nome, df in datasets.items():
    print(f"\nConteúdo do dataset: {nome}")
    print(df.to_string())  # Exibe todas as linhas e colunas do dataset