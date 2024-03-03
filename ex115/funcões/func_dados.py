from os import system
from time import sleep
# Função para menu do sitema
def menu(str='MENU PRINCIPAL'):
    print(20*'-=')
    print(f'{str.center(40)}')
    print(20*'-=')
    print('\033[33m1\033[m - \033[0;34mListar pessoas cadastradas\033[m')
    print('\033[33m2\033[m - \033[0;34mCadastrar uma nova pessoa\033[m')
    print('\033[33m3\033[m - \033[0;34mSair do programa\033[m')
    print(20*'-=')

# Função para cadastrar pessoas
def cadastro(lista_cadastros):
    system('cls')
    msg = 'NOVO CADASTRO'
    print(20*'-=')
    print(f'{msg.center(40)}')
    print(20*'-=')
    
    pessoas = dict()
    # Cadastro da pessoa nova
    while True:
        try:
            pessoas['Nome'] = str(input('Insira seu nome : ')).strip()
            pessoas['Idade'] = int(input('Insira sua idade : '))
            # Apos as entradas serem compativeis é adicionado ao final da lista o cadastro da pessoa
            lista_cadastros.append(pessoas)
        except (ValueError, TypeError):
            print(f'Valor incompatível!')
            pessoas.clear()
        # Após dar certo os tipos de nome e idade da pessoa, nao e necessario continuar dentro do loop, o break do else esta para interromper o laço
        else:
            # with open('cadastros.txt', 'a') as arquivo:
            #     for i in range(len(lista_cadastros)):
            #         texto = arquivo.writelines(lista_cadastros[i]['Nome'])
            #         texto = arquivo.writelines(str(lista_cadastros[i]['Idade']))
            # print(texto)
            # sleep(2)
            break;
    system('cls')

# Lista as pessoas cadastradas
def listagem(lista_cadastro):
    system('cls')
    msg = 'PESSOAS CADASTRADAS'
    msg1 = 'Nome'
    msg2 = 'Idade'
    print(20*'-=')
    print(f'{msg.center(40)}')
    print(20*'-=')
    print(f'{msg1:<40}{msg2}')
    for i in range(len(lista_cadastro)):
        print(f'{lista_cadastro[i]["Nome"]:<40} {lista_cadastro[i]["Idade"]}')