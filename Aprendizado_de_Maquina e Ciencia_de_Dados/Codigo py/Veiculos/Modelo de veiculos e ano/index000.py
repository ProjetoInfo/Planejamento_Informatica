import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Criar uma janela oculta do Tkinter
Tk().withdraw()

# Abrir a janela para selecionar o arquivo de entrada
file_path = askopenfilename(
    title="Selecione o arquivo TXT ou CSV", 
    filetypes=[("Arquivos de texto", "*.txt"), ("Arquivos CSV", "*.csv")]
)

# Verificar se um arquivo foi selecionado
if file_path:
    try:
        # Carregar o dataset com um delimitador adequado
        dataset = pd.read_csv(file_path, delimiter=",", header=None)  # Ajuste o delimitador, se necessário
        
        # Selecionar a primeira coluna e obter valores únicos
        primeira_coluna = dataset[0]
        valores_unicos = primeira_coluna.unique()
        
        # Abrir uma janela para salvar o arquivo de saída
        save_path = asksaveasfilename(
            title="Salvar como arquivo de texto",
            defaultextension=".txt",
            filetypes=[("Arquivo de texto", "*.txt")]
        )
        
        if save_path:
            # Salvar os valores únicos em um arquivo de texto
            with open(save_path, "w") as f:
                for valor in valores_unicos:
                    f.write(f"{valor}\n")
            
            print(f"Valores únicos salvos em: {save_path}")
        else:
            print("Nenhum local de salvamento foi selecionado.")
    
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
else:
    print("Nenhum arquivo foi selecionado.")