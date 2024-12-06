import pandas as pd
import os
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# 1. Importação dos Datasets
# --- Define a pasta onde os datasets estão armazenados ---
pasta_datasets = Path("../Planejamento_Informatica/Aprendizado_de_Maquina e Ciencia_de_Dados/Datasets")

# Carregar o dataset de clientes
caminho_clientes = os.path.join(pasta_datasets, 'Clientes.csv')
dados_clientes = pd.read_csv(caminho_clientes)

# Renomear colunas para remover espaços extras
dados_clientes.rename(columns=lambda x: x.strip(), inplace=True)

# Verificar as colunas disponíveis no dataset
print("Colunas no dataset 'Clientes':", dados_clientes.columns)

# Definir as variáveis independentes (X) e dependente (y)
# Substitua pelas colunas que façam sentido no seu caso
# Exemplo fictício:
X = dados_clientes[['Cliente_id']]  # Ajustar para variáveis preditoras
y = dados_clientes['Cliente_id']    # Ajustar para variável alvo

# Divisão do conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Fazer previsões
y_pred = modelo.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Erro Quadrático Médio (MSE): {mse}")
print(f"Coeficiente de Determinação (R²): {r2}")