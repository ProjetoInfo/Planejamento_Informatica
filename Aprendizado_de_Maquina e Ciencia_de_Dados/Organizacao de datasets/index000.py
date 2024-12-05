import pandas as pd
import os

# 1. Importação dos Datasets
# --- Define a pasta onde os datasets estão armazenados ---
pasta_datasets = r'Planejamento_Informatica\Aprendizado_de_Maquina e Ciencia_de_Dados\Datasets'

# --- Define a pasta onde os datasets serão salvos ---
salvar_datasets = r'Planejamento_Informatica\Aprendizado_de_Maquina e Ciencia_de_Dados\Organizacao de datasets\Datasets_limpos'

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


# 2. Padronização dos Dados
print("\n--- Padronização dos Dados ---")
for nome, df in datasets.items():
    # --- Renomear as colunas para snake_case ---
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    # --- Padronizar formatos ---
    if "email" in df.columns:
        df["email"] = df["email"].str.lower()
    if "data" in df.columns:  # --- Padroniza colunas que indicam datas ---
        df["data"] = pd.to_datetime(df["data"], errors='coerce')
    
    # --- Atualiza no dicionário ---
    datasets[nome] = df
    print(f"Colunas padronizadas no dataset {nome}: {df.columns.tolist()}")


# 3. Tratamento de Dados
for nome, df in datasets.items():
    print(f"\nTratando dados do dataset: {nome}")
    antes = len(df)
    
    # Define colunas relevantes para remover duplicatas
    if nome == 'clientes' and 'cliente_id' in df.columns:
        df = df.drop_duplicates(subset=['cliente_id'])  # Exemplo: 'cliente_id' como chave
    elif nome == 'funcionarios' and 'funcionario_id' in df.columns:
        df = df.drop_duplicates(subset=['funcionario_id'])  # Exemplo: 'funcionario_id' como chave
    else:
        df = df.drop_duplicates()  # Remoção padrão para outros datasets

    depois = len(df)
    print(f"Duplicatas removidas em {nome}: {antes - depois} linhas.")

    # Tratamento de valores nulos (opcional: preencher ou remover)
    if df.isnull().values.any():
        print(f"Valores nulos encontrados em {nome}.")
        print(df.isnull().sum())  # Exibe a quantidade de valores nulos por coluna
    
    # Atualiza o dataset no dicionário
    datasets[nome] = df


# 4. Relacionamento entre Datasets
print("\n--- Relacionamento entre Datasets ---")
# --- Exemplo de relacionamento (você pode expandir com joins se necessário) ---
if 'funcionarios' in datasets and 'cargos' in datasets:
    funcionarios = datasets['funcionarios']
    cargos = datasets['cargos']
    merged_df = pd.merge(funcionarios, cargos, on='cargo_id', how='left')
    print(f"Funcionários com Cargos relacionados:\n{merged_df.head()}")


# 5. Organização Hierárquica
print("\n--- Organização Hierárquica ---")
for nome, df in datasets.items():
    if "id" in df.columns:
        df.sort_values(by="id", inplace=True)
        print(f"{nome} organizado por ID.")
    elif "nome" in df.columns:
        df.sort_values(by="nome", inplace=True)
        print(f"{nome} organizado por Nome.")


# 6. Agregação de Dados
print("\n--- Agregação de Dados ---")
if 'salarios' in datasets:
    salarios = datasets['salarios']
    if 'departamento_id' in salarios.columns:
        sal_por_departamento = salarios.groupby('departamento_id')['salario'].sum()
        print("Salários totais por departamento:")
        print(sal_por_departamento)

if 'funcionarios' in datasets:
    funcionarios = datasets['funcionarios']
    if 'departamento_id' in funcionarios.columns:
        func_por_departamento = funcionarios['departamento_id'].value_counts()
        print("Número de funcionários por departamento:")
        print(func_por_departamento)


# 7. Exportação de Dados
print("\n--- Exportação de Dados ---")
for nome, df in datasets.items():
    caminho_exportacao = os.path.join(salvar_datasets, f"{nome}_limpo.csv")
    df.to_csv(caminho_exportacao, index=False)
    print(f"{nome} exportado para {caminho_exportacao}")