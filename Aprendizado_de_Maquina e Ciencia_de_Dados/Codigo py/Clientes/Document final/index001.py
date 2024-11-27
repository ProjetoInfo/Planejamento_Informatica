import tkinter as tk
from tkinter import filedialog
import os

def juntar_dados_cliente():
    # Seleciona os arquivos
    print("Selecione o arquivo de nomes.")
    arquivo_nomes = carregar_arquivo("Selecione o arquivo de nomes")

    print("Selecione o arquivo de emails.")
    arquivo_emails = carregar_arquivo("Selecione o arquivo de emails")

    print("Selecione o arquivo de números de telefone.")
    arquivo_telefones = carregar_arquivo("Selecione o arquivo de números de telefone")

    if not arquivo_nomes or not arquivo_emails or not arquivo_telefones:
        print("Algum arquivo não foi selecionado. Tente novamente.")
        return

    # Lê os arquivos
    with open(arquivo_nomes, "r", encoding="utf-8") as f:
        nomes = [linha.strip() for linha in f.readlines()]
    
    with open(arquivo_emails, "r", encoding="utf-8") as f:
        emails = [linha.strip() for linha in f.readlines()]
    
    with open(arquivo_telefones, "r", encoding="utf-8") as f:
        telefones = [linha.strip() for linha in f.readlines()]
    
    # Verifica consistência
    if len(nomes) != len(emails) or len(nomes) != len(telefones):
        print("Os arquivos não têm a mesma quantidade de linhas. Verifique os datasets.")
        return

    # Junta os dados no formato desejado
    clientes = []
    for i in range(len(nomes)):
        clientes.append(f'("{nomes[i]}", "{telefones[i]}", "{emails[i]}")')

    # Salva o arquivo combinado
    diretorio = os.path.dirname(arquivo_nomes)
    arquivo_saida = os.path.join(diretorio, "clientes_combinados_para_bd.txt")
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(",\n".join(clientes))

    print(f"Arquivo combinado gerado: {arquivo_saida}")

def carregar_arquivo(titulo):
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(title=titulo, filetypes=[("Arquivos de texto", "*.txt")])

if __name__ == "__main__":
    juntar_dados_cliente()