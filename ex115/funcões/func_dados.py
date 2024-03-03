from time import sleep
from os import system

# Função para menu do sitema
def menu(str='MENU PRINCIPAL'):
    print(20*'-=')
    print(f'{str.center(40)}')
    print(20*'-=')
    print('\033[33m1\033[m - \033[0;34mListar pessoas cadastradas\033[m')
    print('\033[33m2\033[m - \033[0;34mCadastrar uma nova pessoa\033[m')
    print('\033[33m3\033[m - \033[0;34mSair do programa\033[m')
    print(20*'-=')
    # Tem que fazer o loop infinito caso de errado nas entradas das opções, fazer sem o try e cadastrar a pessoa nova no arquivo, isso eu faço com o try, 
    # Continuar aqui
# Função para cadastrar pessoas
def cadastro():
    system('cls')
    msg = 'NOVO CADASTRO'
    print(20*'-=')
    print(f'{msg.center(40)}')
    print(20*'-=')
    sleep(1)
    # Cadastro da pessoa nova