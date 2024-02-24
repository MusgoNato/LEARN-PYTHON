# def Leia_Dinheiro(aux): # Desta forma consigo uma abodagem mais direta na leitura do numero, na entrada principal somente é necessario colocar a string de pergunta ao usuario
    # num = str(input(aux))
def Leia_Dinheiro():
    num = input('Insira um valor : ').strip()
    # num = input('Insira um valor : ').strip().replace(',', '.') # Consigo fazer uma abordagem mais direta, vai ocorrer a separação de espaços começo e fim da string e todos as virgulas sao trocadas por pontos
    while num == '' or num.isalpha(): # Verificação de erro caso o usuario insira um espaço vazio de inicio
        print('ERRO! NUMERO NÃO INTEIRO')
        num = input('Insira um numero : ').strip()
    if ',' in num: # Caso contenha na entrada uma virgula, esta é substituida por . flutuante, porem continua sendo uma string
        num = num.replace(',','.', 1)
    while True: # Enquanto a string passada nao for um numero valido, nao saira do loop continuo
        if num.isdigit() and num.isalpha():
            print('ERRO! NUMERO NÃO INTEIRO')
            num = input('Insira um numero : ').strip()
        else:
            break;
    num = float(num) # Faz a conversao de string para float
    return num # Retorna um float ao final de todo o processo

# Fiz algumas correções, em entradas como 'asd', onde somente tinham caracteres meu programa não funcionava
# consegui chegar na solução, porem em entradas como ' 2 2 ', este código nao funciona
# para solucionar é necessario separar os espaços do meio da string, isso pode ser feito dividindo ela e
# depois juntando com o join