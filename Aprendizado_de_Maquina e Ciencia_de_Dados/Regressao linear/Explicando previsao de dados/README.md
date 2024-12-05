Como Funciona o Processo de Previsão:

1. Divisão dos Dados: O conjunto de dados foi dividido em duas partes:

  - Conjunto de Treinamento: Usado para treinar o modelo. O modelo aprende a relação entre os dados (variáveis independentes) e os valores que estamos tentando prever (variável dependente).
  - Conjunto de Teste: Usado para testar a precisão do modelo, ou seja, como ele se comporta em novos dados que ele nunca viu antes.

---

2. Treinamento do Modelo: O modelo de regressão linear foi treinado com os dados de treinamento. Isso significa que o modelo ajustou uma "linha reta" (ou um conjunto de linhas, se houver mais de uma variável independente) para encontrar a melhor relação entre as variáveis e fazer previsões precisas.

---

3. Fazendo Previsões: Após ser treinado, o modelo foi usado para prever os valores da variável dependente com base nos dados do conjunto de teste. Ou seja, o modelo tentou "adivinhar" os valores reais, usando o que aprendeu.

---

4. Comparando Previsões com Valores Reais: Após as previsões, comparamos os valores previstos pelo modelo com os valores reais do conjunto de teste. Esse passo nos ajuda a entender o desempenho do modelo.

---

##Métricas de Avaliação##:
Para avaliar o desempenho do modelo, usamos duas métricas principais:

1. Erro Quadrático Médio (MSE): O MSE calcula o erro médio das previsões do modelo. Quanto menor o MSE, melhor o modelo, pois significa que as previsões estão mais próximas dos valores reais.

Fórmula:
MSE = (1/n) Σ (y_real - y_previsto)²

Onde:

n: número total de amostras.
yr eal: valores reais observados.
yp revisto: valores previstos pelo modelo.

---

2. Coeficiente de Determinação (R²): O R² indica quanto da variação nos dados foi explicada pelo modelo. Ele varia de 0 a 1:

R² = 1: O modelo explicou toda a variação nos dados, ou seja, as previsões foram perfeitas.
R² = 0: O modelo não conseguiu explicar nada da variação nos dados. Isso significa que o modelo não é útil.
Em geral, você deseja um R² o mais próximo possível de 1, pois isso indica que o modelo está fazendo boas previsões.

---

Exemplo de Interpretação:
Suponha que, após treinar o modelo, os resultados sejam:

MSE: 0.2 (isso significa que, em média, as previsões erraram por 0.2 unidades).
R²: 0.95 (isso significa que o modelo explicou 95% da variação nos dados, o que é excelente!).