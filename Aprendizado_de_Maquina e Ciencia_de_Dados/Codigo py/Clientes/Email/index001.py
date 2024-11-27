import tkinter as tk
from tkinter import filedialog
import os

def remover_primeira_coluna():
    # Abre uma janela para selecionar o arquivo
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt")])

    if not arquivo:
        print("Nenhum arquivo selecionado.")
        return

    # Lê o arquivo e processa as linhas para remover a primeira coluna
    with open(arquivo, "r", encoding="utf-8") as file:
        linhas = file.readlines()

    emails = []
    for linha in linhas:
        linha = linha.strip()
        if "," in linha:  # Verifica se há separação por vírgula
            _, email = linha.split(",", 1)  # Divide em duas partes, ignorando o nome
            emails.append(email.strip())

    # Salva os emails em um novo arquivo
    diretorio = os.path.dirname(arquivo)
    arquivo_saida = os.path.join(diretorio, "emails_somente.txt")
    with open(arquivo_saida, "w", encoding="utf-8") as file:
        file.write("\n".join(emails))

    print(f"Emails extraídos com sucesso! Salvo em: {arquivo_saida}")

# Executa a função
if __name__ == "__main__":
    remover_primeira_coluna()