Estrutura da organização dos datasets

---

1. Importação dos Datasets
Primeiramente, os dados seriam carregados para DataFrames do Pandas.    
---

2. Padronização dos Dados
Os datasets seriam verificados para garantir consistência e uniformidade:

Nomes das Colunas: Renomear as colunas para seguir um padrão (exemplo: usar snake_case como clientes_id, numero_telefone, etc.).
Tipos de Dados: Certificar-se de que cada coluna tenha o tipo correto (por exemplo, IDs e telefones como strings, datas no formato datetime, etc.).
Formatos de Dados: Padronizar formatos, como e-mails sempre em minúsculas.

---

3. Tratamento de Dados
Essa etapa envolve corrigir e preparar os dados para uso:

Valores Nulos: Identificar e tratar valores ausentes, preenchendo com valores padrão ou removendo registros incompletos.
Duplicatas: Remover linhas duplicadas, se necessário.
Validação: Verificar se os dados seguem as regras esperadas (ex.: IDs únicos, emails válidos).

---

4. Relacionamento entre Datasets
Os datasets relacionados seriam organizados para permitir fusões (joins) futuras, como:

Relacionar Funcionários com Cargos pelo cargo_id.
Relacionar Cargos com Departamentos pelo departamento_id.
Criar um esquema claro de relações primária-estrangeira para consultas e manipulações.

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