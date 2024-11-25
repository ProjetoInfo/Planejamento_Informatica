import pandas as pd
import tkinter as tk
from tkinter import filedialog


def processar_arquivo():
    
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    arquivo = filedialog.askopenfilename(title="Selecione o arquivo CSV", filetypes=[("CSV files", "*.csv")])

    if arquivo:
        # Ler o arquivo CSV
        df = pd.read_csv(arquivo)

        
        df.insert(0, 'clientes_ID', range(1, len(df) + 1))

        
        caminho_saida = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        
        if caminho_saida:
            df.to_csv(caminho_saida, sep=',', index=False, header=True)
            print(f"Arquivo salvo em: {caminho_saida}")
        else:
            print("Nenhum arquivo de saída foi selecionado.")
    else:
        print("Nenhum arquivo foi selecionado.")


processar_arquivo()