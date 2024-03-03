# Importação das bibliotecas
from funcões import func_dados
from os import system

# Programa principal
# O programa não utiliza arquivo como pedido, os nomes sao dados e depois nao salvos
# Lista que vai ser usada para o cadastro das pessoas
lista_cadastros = []
# with open('cadastros.txt', 'r') as arquivo:
#     texto = arquivo.read()
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
            func_dados.listagem(lista_cadastros)
        # Cadastro
        if op == 2:
            func_dados.cadastro(lista_cadastros)
        # Saida
        if op == 3:
            exit(0)

# desafio 115º (usando modularização, cadastrar pessoas pelo seu nome e idade em arquivo de 
# texto simples, tendo 2 opções, cadastrar uma nova pessoa e listar todas as pessoas cadastradas e sair do sistema)
