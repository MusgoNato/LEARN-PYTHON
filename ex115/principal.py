# Importação das bibliotecas
from funcões import func_dados
from os import system

# Programa principal
# O programa não utiliza arquivo como pedido, os nomes sao dados e depois nao salvos
# Lista que vai ser usada para o cadastro das pessoas
lista_cadastros = []
arquivo = 'cadastros.txt'
# Tentativa para abri o arquivo, caso nao abra é necessario criar um
if not func_dados.Verifica_Arquivo(arquivo):
    func_dados.Cria_Arquivo(arquivo)

while True:
    # Chamada da função
    func_dados.menu()
    try:
        op = int(input('Insira uma opção : '))
    except (ValueError, TypeError, KeyboardInterrupt):
        system('cls')
        print('Opção inválida!')
    else:
        if op < 1 or op > 3:
            system('cls')
            print('Opção inválida!')
        # Listagem
        if op == 1:
            # Chama a função para ler um arquivo
            func_dados.Lê_Arquivo(arquivo)
            # Chama a função para listagem dos cadastros
            func_dados.listagem(lista_cadastros)
        # Cadastro
        if op == 2:
            # Chama a função para cadastrar uma pessoa no arquivo
            func_dados.Cadastra_Arquivo(arquivo)
            # Chama a função para cadastrar uma pessoas
            func_dados.cadastro(lista_cadastros)
        # Saida
        if op == 3:
            exit(0)

# desafio 115º (usando modularização, cadastrar pessoas pelo seu nome e idade em arquivo de 
# texto simples, tendo 2 opções, cadastrar uma nova pessoa e listar todas as pessoas cadastradas e sair do sistema)
