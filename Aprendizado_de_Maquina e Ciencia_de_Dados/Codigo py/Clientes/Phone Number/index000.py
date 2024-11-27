import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def selecionar_aleatorio(num_linhas=75, sep=','):
    """
    Lê um arquivo selecionado pelo usuário, seleciona aleatoriamente um número especificado de linhas e exibe o resultado.

    Parâmetros:
        num_linhas (int): Número de linhas a serem selecionadas.
        sep (str): Separador do arquivo de texto (padrão: ',').

    Retorna:
        DataFrame: DataFrame contendo as linhas selecionadas.
    """
    try:
        # Oculta a janela principal do Tkinter
        Tk().withdraw()

        # Abre a janela de seleção de arquivo
        arquivo = askopenfilename(title="Selecione o arquivo de texto ou CSV",
                                  filetypes=[("Arquivos de texto", "*.txt"), ("Arquivos CSV", "*.csv")])
        
        if not arquivo:
            print("Nenhum arquivo selecionado.")
            return None

        # Lê o arquivo no formato de DataFrame
        dados = pd.read_csv(arquivo, sep=sep)

        # Verifica se o arquivo tem menos linhas do que as solicitadas
        if len(dados) < num_linhas:
            print(f"Seu arquivo contém apenas {len(dados)} linhas. Selecionando todas.")
            amostra = dados
        else:
            # Seleciona aleatoriamente 'num_linhas' linhas
            amostra = dados.sample(n=num_linhas, random_state=42)

        # Exibe as primeiras linhas da amostra
        print(amostra.head())
        
        return amostra
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        return None

# Seleciona 150 valores do arquivo aleatoriamente
amostra_selecionada = selecionar_aleatorio(num_linhas=75)

# Salva a amostra em um novo arquivo (opcional)
if amostra_selecionada is not None:
    amostra_selecionada.to_csv('phone_number.csv', index=False)
    print("Amostra salva no arquivo 'phone_number.csv'.")