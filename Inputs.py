import csv
from fuzzywuzzy import fuzz
from datetime import date

def encontrar_texto_aproximado(caminho_arquivo, indice_coluna, valor_busca):
    maior_similaridade = 0
    valor_encontrado = None

    with open(caminho_arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            if len(linha) > indice_coluna:
                similaridade = fuzz.ratio(valor_busca, linha[indice_coluna])
                if similaridade > maior_similaridade:
                    maior_similaridade = similaridade
                    valor_encontrado = linha[2]  # Índice 2 corresponde à coluna 3

    return valor_encontrado

def escrever_dados():
    # Obter os dados
    dados = obter_dados()

    # Adicionar a data atual aos dados
    data_atual = date.today().strftime("%d/%m/%Y")
    dados.append(data_atual)

    # Caminho do arquivo CSV
    caminho_arquivo = r'C:\Users\rafad\Desktop\estoque\estoque.csv'

    # Escrever os dados no arquivo CSV
    with open(caminho_arquivo, 'a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv, delimiter=',')
        escritor_csv.writerow(dados)
        print(dados)

def obter_dados():
    bd = []
    bd.append(input("Peça: "))
    bd.append(input("Quantidade: "))
    bd.append(input("Local: "))
    bd.append(input("Cliente: "))
    bd.append(input("OS: "))
    return bd

def main():
    opcao = input("Digite 1 para cadastrar ou 2 para procurar: ")

    if opcao == "1":
        escrever_dados()
    elif opcao == "2":
        caminho_arquivo = r'C:\Users\rafad\Desktop\estoque\estoque.csv'
        indice_coluna = 0  # Índice da coluna onde o texto deve ser procurado
        valor_busca = input("Que item você está procurando? ")

        resultado = encontrar_texto_aproximado(caminho_arquivo, indice_coluna, valor_busca)
        if resultado:
            print(f"Local: {resultado}")
        else:
            print("Valor não encontrado.")
    else:
        print("Opção inválida.")

