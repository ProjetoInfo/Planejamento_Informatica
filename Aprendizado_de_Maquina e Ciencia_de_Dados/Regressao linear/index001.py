import pandas as pd
import os
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Caminho para a pasta de datasets
pasta_datasets = Path("../Planejamento_Informatica/Aprendizado_de_Maquina e Ciencia_de_Dados/Datasets")

# Carregar o dataset de clientes
caminho_clientes = os.path.join(pasta_datasets, 'Clientes.csv')
dados_clientes = pd.read_csv(caminho_clientes)

# Renomear colunas para remover espaços extras
dados_clientes.rename(columns=lambda x: x.strip(), inplace=True)

# Definir as variáveis independentes (X) e dependente (y)
# No seu código, X e y estão como 'Cliente_id', mas vou ajustar para algo mais interessante
X = dados_clientes[['Cliente_id']]  # Variáveis independentes
y = dados_clientes['Cliente_id']    # Variável dependente

# Divisão do conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Fazer previsões
y_pred = modelo.predict(X_test)

# Gerar gráfico de dispersão
plt.figure(figsize=(10,6))

# Plotar os pontos reais (valores de teste)
plt.scatter(X_test, y_test, color='blue', label='Valores reais')

# Plotar a linha de regressão (previsões)
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Linha de regressão')

# Adicionar título e rótulos aos eixos
plt.title('Regressão Linear - Cliente_id vs Cliente_id')
plt.xlabel('Cliente_id (Variável Independente)')
plt.ylabel('Cliente_id (Variável Dependente)')

# Exibir a legenda
plt.legend()

# Exibir o gráfico
plt.show()