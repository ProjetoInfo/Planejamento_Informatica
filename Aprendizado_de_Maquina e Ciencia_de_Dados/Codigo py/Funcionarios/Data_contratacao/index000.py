import pandas as pd
from tkinter import Tk, filedialog

# Ocultar a janela principal do Tkinter
Tk().withdraw()

# Selecionar o arquivo
arquivo = filedialog.askopenfilename(title="Selecione o arquivo", filetypes=[("Arquivos de texto", "*.txt *.csv")])

if arquivo:
    # Ler o arquivo como DataFrame
    df = pd.read_csv(arquivo, sep=",", header=0)  # Ajuste o separador se necessário
    print("Pré-visualização do arquivo original:")
    print(df.head())

    # Selecionar apenas a quarta coluna (índice 3)
    quarta_coluna = df.iloc[:, 3]  # Índice começa em 0, então a quarta coluna é índice 3
    df_limpo = pd.DataFrame(quarta_coluna)  # Criar novo DataFrame apenas com a quarta coluna

    # Exibir a nova tabela
    print("\nNovo DataFrame apenas com a quarta coluna:")
    print(df_limpo.head())

    # Selecionar local para salvar o arquivo atualizado
    caminho_salvar = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivo CSV", "*.csv")])
    if caminho_salvar:
        df_limpo.to_csv(caminho_salvar, index=False, header=False)  # Salvar como CSV sem índice e cabeçalho
        print(f"Arquivo salvo com sucesso em: {caminho_salvar}")
else:
    print("Nenhum arquivo foi selecionado.")0