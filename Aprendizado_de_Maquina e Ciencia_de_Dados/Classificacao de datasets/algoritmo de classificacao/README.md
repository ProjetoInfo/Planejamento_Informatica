O algoritmo foi desenvolvido para ordenar uma lista de clientes com base em seus nomes, utilizando a ordem alfabética. Essa abordagem é útil para organizar os dados de forma mais intuitiva, facilitando a consulta, o gerenciamento e a visualização.

---

##Funcionamento do Algoritmo##
Estrutura de Dados:
Os dados dos clientes são representados como uma lista de dicionários, onde cada dicionário contém informações como um identificador único (Clientes_ID), nome do cliente (Nome), número de telefone e email.

##Processo de Classificação##:
O algoritmo utiliza a função sorted() do Python, com um parâmetro de chave (key) que acessa o campo Nome em cada dicionário. Essa função ordena os clientes em ordem alfabética crescente (A-Z).

##Exemplo de Código##:

clientes_classificados = sorted(clientes, key=lambda cliente: cliente["Nome"])

##Saída##:
Após a classificação, os clientes são exibidos em sequência alfabética no terminal, apresentando suas informações detalhadas.

##Visualização dos Dados##

Um gráfico complementar foi gerado para visualizar o tempo de execução da classificação em função do número de registros. Este gráfico mostra como o tempo de processamento aumenta conforme o tamanho da lista de clientes cresce, demonstrando a eficiência do algoritmo.

##Benefícios##

- Organização: Facilita a localização de clientes por nome.
- Visualização Intuitiva: A apresentação alfabética é mais natural para humanos.
- Escalabilidade: O algoritmo é eficiente mesmo para listas maiores, como evidenciado pela análise gráfica.
Uso
Este script pode ser facilmente adaptado para outras formas de classificação (por exemplo, por ID ou número de telefone) com ajustes mínimos na chave de ordenação. Ele é especialmente útil em aplicações de CRM, sistemas de cadastro e relatórios automatizados.