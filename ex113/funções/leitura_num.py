# Função que lê um tipo inteiro de entrada
def Leiaint():
    while True: # Coloca-se em um loop infinito
        try:
            n = int(input('Numero inteiro > '))
        # Excessão para caso a entrada for um valor diferente do tipo imposto a ele, entra no except
        except ValueError: # Só é necessario verificar se o tipo da entrada for um erro de tipos, caso fosse de valores, este iria entrar nesse except toda vez, com letras e numeros mesclados tambem
            print('ERRO! NUMERO NAO INTEIRO')
        # Excessão para caso o usuario encerre o programa
        except KeyboardInterrupt: 
            print('\nO usuario preferiu nao digitar o valor')
            return 0
        # Caso a entrada seja valida como o tipo imposto no pedido do numero inteiro, entra nesse else
        else: 
            return n # Retorna o inteiro fornecido

# Função que lê um tipo float de entrada
def LeiaFloat():
    while True:
        try:
            n = float(input('Número flutuante: '))
        except ValueError:
            print('ERRO! NUMERO NÃO FLOAT!')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar o valor')
            return 0.0
        else:
            return n