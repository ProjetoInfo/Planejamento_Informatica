import tkinter as tk
from tkinter import filedialog
import os

def gerar_emails():
    # Abre uma janela para selecionar o arquivo
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt")])

    if not arquivo:
        print("Nenhum arquivo selecionado.")
        return

    # Lê o arquivo e cria emails
    with open(arquivo, "r", encoding="utf-8") as file:
        nomes = file.readlines()

    emails = []
    for nome in nomes:
        nome = nome.strip()
        if nome:  # Verifica se o nome não está vazio
            email = f"{nome.lower().replace(' ', '')}@easyroad.com.br"
            emails.append(f"{nome}, {email}")

    # Salva os emails em um novo arquivo
    diretorio = os.path.dirname(arquivo)
    arquivo_saida = os.path.join(diretorio, "emails_gerados.txt")
    with open(arquivo_saida, "w", encoding="utf-8") as file:
        file.write("\n".join(emails))

    print(f"Emails gerados com sucesso! Salvo em: {arquivo_saida}")

# Executa a função
if __name__ == "__main__":
    gerar_emails()