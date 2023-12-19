
#O desafio é imprimir na tela as boas vindas ao usuario de acordo com o valor digitado
#Todos os arquivos nessa pasta sao referenetes ao 1° modulo do python no curso em video
#Esse é o primeiro video, primeiro desafio (Boas vindas ao usuário)
#CTRL + K + C #Comenta em jogo da velha
'''nome = input('Qual o seu nome ')
cores = {'verde': '\033[0;32m', 'azul': '\033[0;31m', 'limpa' : '\033[m'}
print('Boas vindas {}{}{} prazer em conhecê-lo'.format(cores['verde'], nome, cores['limpa']))'''

#Segundo desafio (Pedido de nascimento do usuario)
'''dia = input('Dia: ')
mes = input('Mes: ')
ano = input('Ano: ')
cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m'}
print('Voce nasceu em', dia, 'de', mes, 'do ano de' , ano)# O + vai concatenar as stirngs, o virgula é um tipo de separador, independente de qual tipo for a variavel
#Um outro jeito de imprimir na tela a mesma coisa porem utilizando '{}' e '.format()', segue abaixo
print('Voce nasceu em {}{}\033[m de {}{}\033[m do ano de {}{}\033[m' .format(cores['azul'], dia, cores['verde'], mes, cores['red'], ano)) #O format vai seguir a ordem das chaves para impressão, o chaves é chamado de mascara'''

#Terceiro desafio (Soma de 2 dois numeros)
#aqui ele fala sobre os tipos primitivos, antes de pedir o numero ao usuario ele formata a string para um tipo int, para que depois seja somado e nao concatenado
'''num1 = int(input('Insira um numero: '))
num2 = int(input('Insira um numero: '))
cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m'}
soma = num1 + num2
print('A soma entre {}{}\033[m e {}{}\033[m vale {}{}\033[m'.format(cores['verde'], num1, cores['red'], num2, cores['azul'], soma))'''

#No caso do valor booleano, ele so retorna verdadeiro se tem algo dentro da variavel, caso nao tenha retorna False (Exemplo de false é apertando 'enter')
'''n1 = bool(input('Insira algo: '))
print(n1)'''

#Existe um modulo que é o 'is'algumacoisa(), ele vai dizer se é possivel converter o valor da variavel em um numero retornando True ou False, o mesmo vale para os outros tipos depois do 'is'
#Quarto desafio (Todas as informações de uma variável)
'''variavel = input('Insira algo: ')
cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
print('{}{}\033[m'.format(cores['yellow'], variavel.isalnum())) #Me diz se a variavel é numero
print('{}{}\033[m'.format(cores['red'], variavel.isalpha())) #Se é do alfabeto
print('{}{}\033[m'.format(cores['azul'], variavel.isascii())) # Se é da tabela ascii
print('{}{}\033[m'.format(cores['verde'], variavel.isdecimal())) #Se é decimal
print('{}{}\033[m'.format(cores['ciano'], variavel.isdigit())) #Se é um digito
print('{}{}\033[m'.format(cores['roxo'], variavel.isidentifier())) #Ele é um idenificador, varre a string verificando se ela se adequa a referencia da documentação do python pra esse metodo
print('{}{}\033[m'.format(cores['sla'], variavel.islower())) #Verifica se a string ta toda com os caraceteres minusculos
print('{}{}\033[m'.format(cores['sla'], variavel.isnumeric())) #Verifica se a variavel é numerica
print('{}{}\033[m'.format(cores['sla2'], variavel.isprintable())) #Verifica se a string passada, os caracteres sao visiveis quando manda imprimir na tela
print('{}{}\033[m'.format(cores['azul'], variavel.isspace())) #Verifica se é um espaço
print('{}{}\033[m'.format(cores['roxo'], variavel.istitle())) #Verifica se a string a primeira palavra dela for maiuscula, assim retorna True, caso contrario retorna False, numeros sao tratados como string entao na contam
print('{}{}\033[m'.format(cores['verde'], variavel.isupper())) #Verifica se a string esta com os caracteres todos maisuculos'''

#Referente a aula 7
#Ordem de precedência esta em numero
#1° '()', 2° '**', 3° '*' '/' '//' '%', 4° '+' '-' 
'''Operadores aitmeticos '+' -> Soma   '*' -> Multiplicação '/' -> Divisão '-' -> Subtração '**' -> Potência '//' -> Divisão inteira '%' -> Resto da divisão '''
#Qualquer numero elevado a (1/2) vai dar sua raiz

#Quinto desafio (Sucessor e antecessor de um numero)
'''cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
num = int(input('Digite um numero: '))
print('O antecessor de {}{}\033[m é {}{}\033[m e o sucessor é {}{}\033[m' .format(cores['azul'], num, cores['red'], num - 1, cores['sla'], num + 1)) #O format aceita fazer aritmetica simples pra imprimir depois, isso ajuda a economizar memoria pois nao crio variaveis aux'''

#Sexto desafio (Dobro, triplo e raiz quadrada de um numero)
'''num = int(input('Insira um numero: '))
cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;42m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
print('O dobro de {}{}\033[m é {}{}\033[m, o triplo é {}{}\033[m e a raiz quadrada é {}{:.2f}\033[m' .format(cores['red'], num, cores['roxo'], num * 2, cores['verde'], num * 3, cores['ciano'], num ** (1/2))) #O ':.2f' dentro do {}, é pra deixar com dois numeros apos o ponto flutuante'''

#Mesmo dasafio porem adicionei uma funcao que calcula a raiz quadrada pra mim
'''import math #Adicinei essa biblioteca de matematica que me traz o módulo sqrt pra calcular a raiz quadrada
#from math import sqrt #Caso eu queira usar só a raiz quadrada, usa esse código, para rapidez do proprio programa ja que se importar a biblioteca inteira ela pesa demais o programa pois traz todos os modulos dela
num = int(input('Insira um numero: '))
print('O dobro de {} é {}, triplo {} e raiz quadrada {}'.format(num, num * 2, num * 3, math.sqrt(num)))'''

#Setimo desafio (Media de duas notas de um aluno)
'''cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
nome = str(input('Qual o nome do aluno: '))
nota1 = int(input('Insira a nota 1: '))
nota2 = int(input('Insira a nota 2: '))
media = (nota1 + nota2) / 2
print('Media do aluno {}{}\033[m é {}{:.2f}\033[m' .format(cores['yellow'], nome, cores['roxo'], float(media)))'''

#Oitavo desafio (Conversão de metros para centimetros e milimetros)
'''cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
metros = float(input('Insira a medida em metros: '))
print('A medida de {}{}\033[m m em centimetros é {}{:.0f}\033[m cm, em milimetros é {}{:.0f}\033[m mm'.format(cores['roxo'], metros, cores['red'], metros * 100, cores['sla2'], metros * 1000)) #{:.0f} -> Não me exibe na tela os numeros apos o ponto flutuante'''

#Nono desafio (Tabuada de um numero qualquer)
#Versao podre
'''num = int(input('Insira um numero: '))
print('\nTABUADA\n')
print('1 X {} = {}' .format(num, num * 1))
print('2 X {} = {}' .format(num, num * 2))
print('3 X {} = {}' .format(num, num * 3))
print('4 X {} = {}' .format(num, num * 4))
print('5 X {} = {}' .format(num, num * 5))
print('6 X {} = {}' .format(num, num * 6))
print('7 X {} = {}' .format(num, num * 7))
print('8 X {} = {}' .format(num, num * 8))
print('9 X {} = {}' .format(num, num * 9))
print('10 X {} = {}\n' .format(num, num * 10))'''

#Versao melhorada do mesmo desafio
'''cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
num = int((input('Insira um numero: ')))
print('\nTABUADA\n')
for i in range(1, num + 1, 1): # Aqui o for funciona criando uma variavel a qual é o 'i', e vai ate o range('inicio, parada, incremento')
    print('{}{}\033[m X {}{}\033[m = {}{}\033[m' .format(cores['sla2'], num, cores['azul'], i, cores['roxo'], num * i)) #Aqui pensei em simplificar, multipliquei as variaveis ao inves de criar uma variavel pra armazenar a multiplicação do 'i' e o 'num'
print('\n')'''

#10° desafio (Quanto tem de dinheiro na carteira do usuario e quantos dolares ele consegue comprar com o dinheiro dele)
'''cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
num = float(input('Quanto dinheiro há na sua carteira? '))
print('Quantidade na carteira {}{:.2f}\033[m, dolares que podem ser comprados {}{:.2f}\033[m' .format(cores['ciano'], num, cores['sla2'], num / 4,93)) #Cotação 'atual' do dolar'''

#11° desafio (Ler largura e altura de uma parede em metros e calcular a area , cada litro de tinta é 2m² por area, quantos preciso pra pintar a parede toda?)
'''cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area = largura * altura
print('Voce precisa de {}{:.2f}\033[m litros para pintar sua parede de area {}{}\033[m'.format(cores['azul'], area/2, cores['red'], area))'''

#12° desafio (Ler um preco de um produto, devolve-lo com 5% de desconto)
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# produto = float(input('Qual o valor do produto? '))
# desconto = float(input('Qual o valor de desconto? ')) # O pedido de desconto nao precisava, mas quis testar pra ver se conseguia com o usuario pedindo
# produto = produto - (produto * (desconto/100))
# print('Valor final com 5% de desconto é {}{}\033[m!' .format(cores['sla'], produto))

#13° desafio (Ler um salario de um funcionário e devolve com 15% de aumento)
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# nome = str(input('Qual o nome do funcionário? '))
# aumento = int(input('Quantos de aumento {}{}\033[m receberá? '.format(cores['ciano'], nome)))
# salario = float(input('Qual o sálario do {}{}\033[m? '. format(cores['red'], nome))) #Da pra aplicar o format direto no input
# aumento = salario + (salario * (aumento/100)) #burrooooo, era aumento/100, quase 30m tentando resolver e era só inverter a ordem
# print('O sálario do funcionári o {}{}\033[m é {}{:.2f}\033[m, com aumento fica {}{:.2f}\033[m' .format(cores['azul'], nome, cores['roxo'], salario, cores['yellow'], aumento))

#14° desafio (Transformar celsius em Farenheith)]
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# c = float(input('Insira a temperatura em Celsius: '))
# f = (c * 9/5) + 32 
# print('Graus {}{}\033[m°C para Farenheith é {}{}\033[m°F'.format(cores['red'], c, cores['verde'], f))

#15° desafio (Calcular aluguel de um carro, quantos dias foi alugado, quantos km rodou, querendo saber o preço que custou, sabendo que é R$60 por dia e R$0.15 por km rodado)
# dias = int(input('Quantos dias o carro foi alugado? '))
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# km = float(input('Quantos km rodados? '))
# custo = (dias * 60) + (km * 0.15)
# print('O custo total foi de R${}{}\033[m'.format(cores['azul'], custo))

#Abaixo é referente a aula 08
'''import math
n = float(input('Insira um numero: '))
print('{}'.format(math.sqrt(n)))'''

'''import random
n = random.random() #O random gera um numero de 0 ate 1
m = random.randint(1, 10) #Randomiza um numero inteiro, colocando o intervalo dentro dele
print(m) #recebe o intervalo de 1 ate 10
print(n) #n recebendo numero aleatório, abaixo chamando a função diretamente
print('numero aleatorio {}'.format(random.random())) #Lembrando que o random devolve um valor aleatorio para uma variavel ou simplesmente escrevendo na tela'''
'''import emoji #Lembrando que o pip foi instalado no diretorio 'Scripts', nao no PATH, teria que instalar ele, nao sei que problema isso vai gerar mas ate agora ta de boa
print(emoji.emojize('Python is fun :thumbsup:', language='alias'))'''

#16° desafio (Mostrar a porção inteira de um valor real)
# from math import floor
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# n = float(input('Insira um numero: '))
# print('{}{}\033[m'.format(cores['sla2'], floor(n)))

#Outro jeito que seria o do vídeo
'''from math import trunc
n = float(input('Insira um numero: '))
print(trunc(n))'''

#Mais um jeito
'''n = float(input('Insira um numero: '))
print(type(n))
print('{} valor inteiro é : {}'.format(n, int(n))) #Mostra o valor inteiro, para a variavel n ter o valor inteiro em si, teria que haver uma atribuicao, por isso ela continua com o tipo float apos esse código'''

#17° desafio (Ler cateto oposto e adjacente, devolver a hipotenusa)
# from math import hypot
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# oposto = float(input('Insira o cateto oposto: '))
# adjacente = float(input('Insira o cateto adjacente: '))
# hip = hypot(oposto, adjacente) #Estou começando a usar variaveis auxiliares pq depois vou precisar usar variaveis auxiliares em programas mais complexos, entao na pratica ao inves de fazer direto os resultados vou armazenando em variaveis aux, por mais que utilize mais memoria
# print('Hipotenusa: {}{:.2f}\033[m'.format(cores['red'], hip))

#18° desafio (Seno, cosseno e tangente de um numero)
#Esse exerciico eu tinha feito errado, precisava converter o angulo para radiano, meu programa nao fazia entao o resultado estava errado, adicionando a conversao por meio do radians consegui chegar no resultado correto
# from math import sin, cos, tan, radians
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# n = float(input('Insira um numero: '))
# sen = sin(radians(n))
# coss = cos(radians(n))
# tang = tan(radians(n))
# print('O seno do numero {}{}\033[m é {}{:.2f}\033[m, cosseno é {}{:.2f}\033[m e tangente é {}{:.2f}\033[m'.format(cores['red'], n, cores['roxo'], sen, cores['verde'], coss, cores['sla'], tang))

#19° desafio (Sorteio de 4 alunos, escreva o nome do escolhido sorteando-o)
# from random import choice #esse módulo ele escolhe aleatoriamente algo dentro de uma lista
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# nomes = ['Hugo', 'João', 'Maria', 'Lucas'] #Aqui supus que era desse jeito e deu certo
# print('O nome do escolhido é : {}{}\033[m!'.format(cores['verde'], choice(nomes)))

#Mesmo exercicio melhorado, utilizando estrutura de repetição (O usuario pode colocar os nomes, eles nao vem pre-definidos como o código anterior)
# from random import choice
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# nomes = [] #Inicializa uma variavel como lista vazia
# for i in range(1, 6, 1): #Aqui coloco o parametro de inicio e parada
#     nomes.append(str(input('Insira o nome: '))) #Aqui a função append vai colocar no final da lista o que o usuário digitar
# print('O nome escolhido foi {}{}\033[m'.format(cores['ciano'], choice(nomes))) #Aqui eu faço o sorteio ja com a lista cheia

#20° desafio (Escolha aleatoriamente alunos e sua ordem de apresentação de cada um)
# from random import shuffle
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# n1 = str(input('Insira um nome : '))
# n2 = str(input('Insira um nome : '))
# n3 = str(input('Insira um nome : '))
# lista = [n1, n2, n3]
# shuffle(lista)
# print('A ordem de apresentação sera ')
# print('{}{}\033[m'.format(cores['azul'], lista))

#Outro jeito de fazer com estrutura de repeticao
'''from random import shuffle
nomes = []
for i in range(1, 4, 1):
    nome = str(input('Insira um nome: '))
    nomes.append(nome) #Aqui ele já faz uma atribuicao a lista nome, apos essa linha nomes contem todos os nomes que foram dados de stdin
shuffle(nomes) #Embaralha a lista
print('A apresentação sera nesta ordem : {}'.format(nomes)) #Imprime a lista completa, pois já foi embaralhada'''

#21° desafio (Tocar uma música)
'''from pygame import mixer
mixer.init() #Inicia a biblioteca do pygame
mixer.music.load("D:\HUGO\musica.mp3") #Carrega a musica no diretorio de origem dela
mixer.music.set_volume(0.7) #Aqui regula o volume
mixer.music.play() #Coloca na lista de espera de um certo modo de dizer, ja que o comando abaixo em si toca a musica
input("  ")  #Por algum motivo o input seria um tipo de play na musica pra comecar a tocar, tipo um pressionamento'''

#Abaixo é referente a aula 9
#Fatiamento de strings -> frase[9:13] -> Caso eu mande imprimir na tela, ele vai pegar a posicao 9 da string e vai ate a posicao 13-1, pois a ultima posição ele nunca pega, é sempre uma antes
#frase[9:21:2] -> Os dois primieiros parametros fazem o mesmo que o exemplo anterior, o '2' vai pular duas casas e ai mostrar na tela
#frase[:5] -> Mesma coisa que frase[0:5]
#frase[15:] -> Comeca no caractere 15, nao sabendo o final ele vai ate o fim da string
#frase[9::3] -> Comeca no 9 e vai ate o final da string pulando de 3 em 3 caracteres
#len(frase) -> Me mostra o comprimento da frase
#frase.count('o') ->O count ele conta quantas vezes a letra 'o' minuscula
#frase.count('o', 0, 13) ->Vai do 0 ate o 12, ja conta sendo fatiada a string
#frase.find('deo') -> Ele mostra em que momento começou essa frase, mostra a posição (caso o valor retornado seja -1, significa que a sstring passada nao foi encontrada)
#Operador 'in' -> 'Curso' in frase -> O operador in retorna True se existe dentro da string a palavra Curso, caso nao esteja é False
#frase.replace('Python, 'Android') -> Substitui o primeiro parametro pelo segundo
#frase.upper() -> Vai colocar a string toda em maiusculo, se ja estiver ele deixa
#frase.lower() -> Contrario do upper
#frase.capitalize() -> O capitalize trasforma todos os caracteres em minusculo, só a primeira letra ele coloca em maisuculo
#frase.title() -> Ele analisa toda a string, onde tem espaço ele quebra e coloca em cada palavra quebrada, a primeira letra ele coloca em maisucula
#frase.strip() -> remove todos os espaços inuteis no inicio e no fim da string
#frase.rstrip() -> Remove somente os ultimos espaços direita
#frase.lstrip() -> Remove somente os primeiros espaços da esquerda
#frase.split() -> ocorre uma divisao dentro da string considerando os espaços, ele divide a string inteira em outras strings, a partir dos espaços
#'-'.join(frase) -> Junção de strings usando um separador '-'

'''frase = 'hugo josué'
print(frase[0]) 
print(frase[14:2])
print('hugo' in frase)
print(frase.upper().find('HUGO')) #Aqui ele joga todas as letras em maisuculo primeiro e depois faz a  busca na string ja modificada, por isso o valor retornado vai ser verdade, pois encontrou
print(frase.count('o'))
print(frase.replace('Hugo', 'Joãozinho'))
print(frase.capitalize())
print(len(frase))
print("""AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
      AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
      AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ZE DA MANGA!!!!!""")
print(frase.split())
frase = frase.split() 
print(' '.join(frase)) #Aqui ele junta a lista contendo varias strings que foram dividias pelo split anteriormente, mas só mostrara na tela, apos esse trecho o que esta na string continua sendo o mesmo de antes ou seja, é uma lista de strings'''

#22° desafio (Ler uma string e mostrar ela toda maiuscula, minuscula, quantas letras sem considerar espaços e quantas letras tem o primeiro nome)
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# nome = str(input('Insira seu nome : ').strip()) #O strip elimina os espaços da string
# print('Seu nome completo em maiuscula: {}{}\033[m'.format(cores['roxo'], nome.upper())) #Transforma a string em maisucula
# print('Seu nome completo em minuscula: {}{}\033[m'.format(cores['azul'], nome.lower())) #Transforma a string em minuscula
# nome = nome.split() #Separa a string em substring onde houver espaços
# print('Quantidade de letras do primeiro nome: {}{}\033[m'.format(cores['yellow'], len(nome[0]))) #Da o tamanho da primeira substring
# nome = ' '.join(nome) #Junta tudo de novo colocando espaço, assim como a string original
# nome = nome.replace(' ', '') #troca os espaços por espaço vazio
# print('Quantidade de caracteres do nome : {}{}\033[m'.format(cores['red'], len(nome))) #Tudo junto me retorna o tamanho da string

#23° desafio (Ler uma string como numero e separar a unidade, dezena, centena e milhar) #Aqui como é string nao tem uma verificacao para o intervalo, caso coloque algum numero dentro do intervalo porem sem 4 digitos, ele vai dar erro
# num = str(input('Insira um numero : '))
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# print('Unidade : {}{}\033[m\nDezena : {}{}\033[m\nCentena : {}{}\033[m\nMilhar : {}{}\033[m'.format(cores['azul'], len(num), cores['ciano'], num[2], cores['red'], num[1], cores['roxo'], num[0]))

#Outro jeito de fazer tratando a string como um numero
'''from math import trunc
num = int(input('Insira um numero: '))
if num >= 0 and num <= 9999: #Coloquei uma condição pra saber o intervalo do numero, se o usuario digitou errado ou não

    unidade = num % 10 #Calculo para saber a unidade
    print('Unidade : {}'.format(unidade))
    dezena = (num // 10) % 10 #calculo para saber a dezena
    print('Dezena : {}'.format(dezena))
    centena = (num // 100) % 10 #Calculo para saber a centena
    print('Centena : {}'.format(centena))
    milhar = (num // 1000) % 10 #Calculo para milhar
    print('Milhar : {}'.format(milhar))
else:
    print('Numero fora do intervalo!')'''

#24° desafio (Ler uma cidade e saber se ela começa com 'Santo' ou nao)
'''city = str(input('Insira o nome da cidade : ')).strip() #Elimina os espaços da esquerda e direita
city = city.split() #Divide em substring a strinng inteira, criando uma lista
print(city[0].upper() == 'SANTO') #Forma simples de fazer, a outra que tinha tenatado era mais complicada'''

#25° desafio (Le um nome e ver se ele tem 'Silva' no nome)
# nome = str(input('Insira seu nome: ')).upper()
# encontrou = nome.find('SILVA') #Aqui criei uma variavel booleana pra saber se falhou ou nao a procura, caso falhe entao nao tem silva o nome, caso de certo o nome Silva foi encontrado
# if encontrou == -1: #find acima retorna -1 caso nao ache
#     print('\033[4;31;46mNão há Silva no nome!\033[m')
# else:
#     print('\033[1;30;43mHá Silva no nome!\033[m')

#Outro jeito de fazer o mesmo desafio
'''nome = str(input('Insira seu nome: '))
print('SILVA' in nome.upper()) #Transforma a string dada em maiuscula, assim usando o operador in é facil de compreender''' 

#26 desafio (Quantas vezes aparece a letra 'A', em que posição ela aparece a primeira vez, em que posição ela aparece a ultima vez)
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# string = str(input('Insira uma palavra : ')).upper().strip() #Isso tem que ser memorizado, o usuario pode digitar qualquer coisa na hora, nao significa que estara errado (Ele coloca tudo em maisuculo e depois remove os espaços da esquerda e direita)
# print('Aparece {}{}\033[m vezes!'.format(cores['azul'], string.count('A')))
# print('Primeira {}{}\033[m que aparece!'.format(cores['sla2'], string.find('A')))
# print('Ultima {}{}\033[m que aparece'.format(cores['ciano'], string.rfind('A'))) #Começa a procura a partir da direita

#27 desafio (Ler nome completo de uma pessoa, mostrar o primeiro e ultimo nome separadamente)
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# nome = str(input('Insira seu nome: ')).strip()
# nome = nome.split()
# print('Primeiro nome : {}{}\033[m'.format(cores['yellow'], nome[0])) #aqui o primeiro elemento e a posicao 0 mesmo
# print('Último nome : {}{}\033[m'.format(cores['red'], nome[-1])) #A string pode ser acessada de tras pra frente, por isso o -1
# #print('Último nome : {}'.format(nome[len(nome) - 1])) #Outro jeito de pegar o ultimo nome

#Referente a aula 10
#Para situações mais simplificadas pode-se usar: print('Carro Novo' if tempo <= 3 else 'Carro Velho')
'''nome = str(input('Insira seu nome: ')).strip()
if nome == 'Hugo':
    print('Ahhhh ze da manga!!')
else:
    print('Manoel gomes galera uuuu!!!')'''

#Desafio atras melhorado com uso de condição composta
'''nota1 = float(input('Insira a nota 1: '))
nota2 = float(input('Insira a nota 2: '))
media = (nota1 + nota2) / 2
#print('Sua média é {}, Tu passou meu patrão'.format(media) if media >= 6 else 'Sua média é {}, se ferrou aaaa!!!!'.format(media)) #Jeito simplificado de fazer o mesmo if abaixo
if media >= 6:
    print('Sua média é {}, Tu passou meu patrão!'.format(media))
else:
    print('Sua média é {}, se ferrou aaaaa!!!!'.format(media))'''

#28° desafio (Fazer o computador pensar em um numero de 0 a 5, mandar o usuario tentar acertar o numero)
# from random import randint
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# from time import sleep #Importei a biblioteca time pra dar um ar de que o pc ta pensando no numero
# num = randint(0, 5)
# user = int(input('Em que numero estou pensando? '))
# print('PENSANDO...')
# sleep(1)
# if user >= 0 and user <= 5:
#     if user == num:
#         print('\033[1;34;44mParabéns voce acertou!\033[m')
#     else:
#         print('\033[4;33;47mInfelizmente voce errou!\033[m')
# else:
#     print('\033[7;29;33mNumero passou do intervalo de adivinhação!\033[m')

#29° desafio (Escreva na tela se um carro ultrapassar 80km/h, dizendo que ele foi multado sabendo que cada km equivale a 7)
# from colorama import Fore, init #Importei a biblioteca que troca de cor os textos do print
# init(autoreset=True) #Reseta automaticamente a cor pra original do console após o print ser executado
# km = int(input('Insira a velocidade do carro: '))
# multa = (km - 80) * 7
# if km > 80:
#     print(Fore.RED + 'Voce foi multado, valor da multa é igual a : {}'.format(multa)) #O fore muda a cor do print
# else:
#     print(Fore.GREEN + 'Ta de boa pébo')

#30° desafio (Mostrar se numero é par ou impar)
# num = int(input('Insira um numero: '))
# if num % 2 == 0:
#     print('\033[1;35;45mNumero par!\033[m')
# else:
#     print('\033[4;31;44mNumero ímpar!\033[m')

#31° desafio (Pergunte a distancia  de uma viagem, calcule o preço da passagem, cobrando 0,50 por km em ate 200km/h, para viagens mais longas 0,45)
# distancia = int(input('Insira a distancia percorrida: '))
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# #print('Preco a pagar : {:.2f}'.format(float(distancia * 0.50)) if distancia <= 200 else 'Preço a pagar : {:.2f}'.format(float(distancia * 0.45))) #If simplificado
# if distancia <= 200:
#     preco = distancia * 0.50
#     print('Preço a pagar : {}{:.2f}\033[m'.format(cores['red'], float(preco)))
# else:
#     preco = distancia * 0.45
#     print('Preço a pagar : {}{:.2f}\033[m'.format(cores['roxo'], float(preco)))

#32° desafio (Ano qualquer e mostrar se ele é bissexto)
# from datetime import date #Importando a data atual em ano
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# ano = int(input('Insira um ano : '))
# if ano == 0:
#     ano = date.today().year #Me retorna em que ano estamos
#     print('{}{}\033[m'.format(cores['sla2'], ano))
# if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
#     print('\033[1;34;40mAno bissexto\033[m')
# else:
#     print('\033[7;30;40mAno nao bissexto\033[m')

#33° desafio (Encontrar o maior e menor de 3 numeros)
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# numeros = []
# for i in range(1, 4, 1):
#     num = int(input('Insira um numero : '))
#     numeros.append(num)
# menor_valor = min(numeros)
# maior_valor = max(numeros)
# print('Menor valor é : {}{}\033[m'.format(cores['azul'], menor_valor))
# print('Maior valor é : {}{}\033[m'.format(cores['red'], maior_valor))

#34° desafio (Calcular o valor do aumento de um funcionário, superior a 1250 é aumento de 10%, para inferior ou igual é 15%)
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# nome = str(input('Insira o nome do funcionário: ')).strip()
# salario = float(input('Insira o salário de {}{} : \033[m'.format(cores['verde'], nome)))
# if salario > 1250:
#     novo_salario = salario + (salario * (10/100))
#     print('Novo salário ficou em : {}{}\033[m'.format(cores['red'], novo_salario))
# else:
#     novo_salario = salario + (salario * (15/100))
#     print('Novo salário ficou em : {}{}\033[m'.format(cores['sla'], novo_salario))

#35° desafio (Ler tres retas e dizer se pode ou nao formar um triangulo)
# reta1 = int(input('Insira o valor : '))
# reta2 = int(input('Insira o valor : '))
# reta3 = int(input('Insira o valor : '))
# if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
#     print('\033[1;34;46mDá pra formar um triângulo\033[m')
# else:
#     print('\033[7;36;47mNão dá pra formar um triângulo\033[m')

#Referente a aula 11
#\033[m -> Padrao do terminal
#\033[style;text;backgroundm ->Codigo de cor no python
#Códigos de estilo que funcionam melhor para o python do padrão ANSI(0 -> sem estilo; 1 -> Negrito; 4 -> Sublinhado; 7 -> Negativo (Inverte as cores))
#códigos de texto que funcionam melhor para o pyhton do padrão ANSI(30 ate 37)
#códigos de background que funcionam melhor para o pyhton do padrão ANSi (40 a 47) -> mesmas cores que o do texto
#Pra letra preta utiliza-se o código 7, pois ele inverte a cor
'''a = 3
b = 5
print('Os valores sao \033[33m{} e {}\033[32m'.format(a, b))
nome = 'Hugo'
print('Muito prazer em te conhecer {}{}{}'.format('\033[4;34m',nome,'\033[m'))'''
'''nome = 'Hugo'
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m','pretoebranco':'\033[7;30m'} #Isso é um dicionario, pra ficar mais facil de entender é uma estrutura, onde eu defino o nome do código que ira fazer algo pra mim, nesse caso sao as cores
print('Olá muito prazer em te conhecer {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa'])) #Aqui entre colchetes é chamado o nome que eu dei pra cor que eu desejo usar do dicionario'''
