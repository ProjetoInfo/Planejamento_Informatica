import random
import string

# Função para gerar uma placa de carro fictícia
def gerar_placa():
    # Gerar 3 letras aleatórias (ABC)
    letras = ''.join(random.choices(string.ascii_uppercase, k=3))
    
    # Gerar 4 caracteres: 1 número, 1 letra e 2 números (1D23)
    numero1 = random.choice(string.digits)  # Primeiro número
    letra = random.choice(string.ascii_uppercase)  # Letra entre os números
    numero2 = random.choice(string.digits)  # Segundo número
    numero3 = random.choice(string.digits)  # Terceiro número

    # Formar a placa no formato ABC1D23 (7 caracteres no total)
    placa = f"{letras}{numero1}{letra}{numero2}{numero3}"
    
    return placa

# Função para gerar placas e salvar em um arquivo .txt
def gerar_placas_salvar(quantidade, arquivo):
    with open(arquivo, 'w') as file:
        for _ in range(quantidade):
            placa = gerar_placa()
            file.write(placa + '\n')  # Escreve cada placa em uma nova linha

# Exemplo de uso: Gerar 15 placas e salvar em um arquivo "placas.txt"
gerar_placas_salvar(42, "placas.txt")