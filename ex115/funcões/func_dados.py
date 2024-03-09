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

# Verifica se existe algum arquivo
def Verifica_Arquivo(arq):
    try:
        arquivo = open(arq, 'rt') # 'rt' para ler um arquivo txt
        arquivo.close()
    except FileNotFoundError: 
        return False
    else:
        return True
    
# Cria o arquivo caso nao exista
def Cria_Arquivo(arq):
    try:
        arquivo = open(arq, 'wt+') # wt+ para escrita em txt e cria um arquivo caso nao exista
        arquivo.close() 
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print('O arquivo foi criado com sucesso!')

# Aqui vai ler o arquivo existente ou que foi criado
def Lê_Arquivo(arq):
    try:
        arquivo = open(arq, '+rt')
    except:
        print('Houve um problema')
    else:
        print(arquivo.read())
        arquivo.close()
        sleep(1)

# Cadastra uma pessoa no arquivo
def Cadastra_Arquivo(arq, nome='desconhecido', idade=0):
    try:
        arquivo = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            arquivo.write('\n')
            arquivo.write(f'{nome};{idade}')
        except:
            print('Houve um erro da digitação do arquivo!')
        else:
            print('Nome adicionado com sucesso!')
            arquivo.close()

