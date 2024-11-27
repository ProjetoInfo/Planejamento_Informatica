import pandas as pd
import tkinter as tk
from tkinter import filedialog
import csv  # Para manipulação das aspas

# Função para abrir a janela de seleção de arquivos
def selecionar_arquivo(tipo_arquivo="Todos os Arquivos", extensao="*.*"):
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal
    arquivo = filedialog.askopenfilename(filetypes=[(tipo_arquivo, extensao)])
    return arquivo

# Selecionar os dois arquivos
print("Selecione o primeiro arquivo (dataset com 1 coluna):")
arquivo1 = selecionar_arquivo(tipo_arquivo="Arquivos TXT", extensao="*.txt")

print("Selecione o segundo arquivo (dataset com 3 colunas):")
arquivo2 = selecionar_arquivo(tipo_arquivo="Arquivos TXT", extensao="*.txt")

# Carregar os datasets
df1 = pd.read_csv(arquivo1, header=None, delimiter=',', encoding='utf-8')  # Ajuste o delimitador conforme necessário
df2 = pd.read_csv(arquivo2, delimiter=',', header=None, encoding='utf-8')  # Ajuste o delimitador conforme necessário

# Verificar se o df1 tem apenas uma coluna
if df1.shape[1] != 1:
    print("O primeiro dataset não tem uma coluna única.")
else:
    # Concatenar df1 (com 1 coluna) como a última coluna de df2 (com 3 colunas)
    df_combined = pd.concat([df2, df1], axis=1)

    # Salvar o resultado em um novo arquivo .txt, separando as colunas com vírgula, sem aspas
    arquivo_saida = "dataset_combinado.txt"
    df_combined.to_csv(arquivo_saida, header=False, index=False, sep=',', quoting=csv.QUOTE_NONE)

    print(f"Arquivo combinado salvo como: {arquivo_saida}")