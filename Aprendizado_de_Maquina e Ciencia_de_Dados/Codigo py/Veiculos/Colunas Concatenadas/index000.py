import pandas as pd
import tkinter as tk
from tkinter import filedialog
import csv
import random  # Para gerar valores aleatórios

# Função para abrir a janela de seleção de arquivos
def selecionar_arquivo(tipo_arquivo="Todos os Arquivos", extensao="*.*"):
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal
    arquivo = filedialog.askopenfilename(filetypes=[(tipo_arquivo, extensao)])
    return arquivo

# Selecionar o arquivo com os dados (apenas um dataset)
print("Selecione o arquivo com os dados do veículo (dataset com os dados):")
arquivo = selecionar_arquivo(tipo_arquivo="Arquivos TXT", extensao="*.txt")

# Carregar o dataset
df = pd.read_csv(arquivo, header=None, delimiter=',', encoding='utf-8')  # Ajuste o delimitador conforme necessário

# Definir os status aleatoriamente
status_opcoes = ['Disponível', 'Reservado', 'Em Manutenção']
df['Status'] = [random.choice(status_opcoes) for _ in range(df.shape[0])]

# Salvar o resultado em um novo arquivo .txt, separando as colunas com vírgula, sem aspas
arquivo_saida = "dataset_com_status.txt"
df.to_csv(arquivo_saida, header=False, index=False, sep=',', quoting=csv.QUOTE_NONE)

print(f"Arquivo com status adicionado salvo como: {arquivo_saida}")