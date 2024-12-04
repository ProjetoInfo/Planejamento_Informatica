Estrutura da organização dos datasets

---

1. Importação dos Datasets
Carregar todos os dados em DataFrames do pandas.

---

2. Padronização dos Dados
Certificar-se de que os datasets seguem um padrão, incluindo renomeação de colunas, padronização de formatos e ajuste de tipos de dados.

---

3. Tratamento de Dados
Essa etapa envolve identificar e corrigir inconsistências:
- Valores Nulos: Preenchimento ou remoção de registros com valores ausentes.
- Remoção de Duplicatas: Identificar e excluir linhas duplicadas para evitar redundância.

---

4. Relacionamento entre Datasets
Estabelecer relações entre os datasets com base em chaves primárias e estrangeiras.

---

5. Organização Hierárquica
Organizar os dados em um fluxo que reflita a estrutura da empresa:

Clientes: Listagem de clientes ordenada por clientes_id ou nome.
Departamentos: Mostrando a estrutura da empresa.
Cargos: Associando os cargos aos departamentos correspondentes.
Funcionários: Relacionando cada funcionário ao cargo e departamento.

---

6. Agregação de Dados
Realizar cálculos ou sumarizações úteis:

Salários por departamento.
Número de funcionários em cada departamento.
Contagem de clientes ativos.

---

7. Exportação de Dados
Depois da organização, os datasets poderiam ser exportados para novos arquivos organizados (ex.: clientes_limpos.csv, funcionarios_organizados.csv).