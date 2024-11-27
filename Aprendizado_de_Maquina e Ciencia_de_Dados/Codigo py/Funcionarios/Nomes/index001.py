import pandas as pd
from tkinter import Tk, filedialog

# Abrir janela para selecionar o arquivo
Tk().withdraw()  # Ocultar a janela principal do Tkinter
arquivo = filedialog.askopenfilename(title="Selecione o arquivo .txt", filetypes=[("Arquivos de texto", "*.txt")])

# Ler o arquivo e exibir pré-visualização
if arquivo:
    df = pd.read_csv(arquivo, sep=",", header=0)
    print("Pré-visualização do arquivo:")
    print(df.head())

    # Selecionar a segunda coluna
    segunda_coluna = df.iloc[:, 1]  # Coluna 'Name'
    print("\nSegunda coluna:")
    print(segunda_coluna)

    # Salvar a segunda coluna em um arquivo .txt
    caminho_salvar = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivo de Texto", "*.txt")])
    if caminho_salvar:
        segunda_coluna.to_csv(caminho_salvar, index=False, header=False)
        print(f"Arquivo salvo com sucesso em: {caminho_salvar}")
else:
    print("Nenhum arquivo foi selecionado.")