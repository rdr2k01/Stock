import csv
from tkinter import Tk, Label, Button, Entry, messagebox

def cadastrar():
    # Obter os dados do formulário
    peca = entry_peca.get()
    quantidade = entry_quantidade.get()
    local = entry_local.get()
    cliente = entry_cliente.get()
    os = entry_os.get()

    # Caminho do arquivo CSV
    caminho_arquivo = 'estoque.csv'

    # Escrever os dados no arquivo CSV
    with open(caminho_arquivo, 'a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow([peca, quantidade, local, cliente, os])
    
    # Limpar os campos do formulário
    entry_peca.delete(0, 'end')
    entry_quantidade.delete(0, 'end')
    entry_local.delete(0, 'end')
    entry_cliente.delete(0, 'end')
    entry_os.delete(0, 'end')

    messagebox.showinfo('Cadastro', 'Dados cadastrados com sucesso!')

def procurar():
    # Obter o item a ser pesquisado
    item = entry_item.get()

    # Caminho do arquivo CSV
    caminho_arquivo = 'estoque.csv'

    # Procurar o item no arquivo CSV
    encontrado = False
    with open(caminho_arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            if item in linha:
                messagebox.showinfo('Resultado', f'Item encontrado!\nLocal: {linha[2]}')
                encontrado = True
                break

    if not encontrado:
        messagebox.showinfo('Resultado', 'Item não encontrado.')

# Criar a janela principal
janela = Tk()
janela.title('Aplicativo de Estoque')

# Criar os rótulos e campos de entrada
label_peca = Label(janela, text='Peça:')
entry_peca = Entry(janela)
label_peca.grid(row=0, column=0, padx=10, pady=5)
entry_peca.grid(row=0, column=1, padx=10, pady=5)

# Repita os mesmos passos para os outros campos

# Criar os botões
botao_cadastrar = Button(janela, text='Cadastrar', command=cadastrar)
botao_cadastrar.grid(row=6, column=0, padx=10, pady=5)

botao_procurar = Button(janela, text='Procurar', command=procurar)
botao_procurar.grid(row=6, column=1, padx=10, pady=5)

# Iniciar a execução do aplicativo
janela.mainloop()

