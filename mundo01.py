
#O desafio é imprimir na tela as boas vindas ao usuario de acordo com o valor digitado
#Todos os arquivos nessa pasta sao referenetes ao 1° modulo do python no curso em video
#Esse é o primeiro video, primeiro desafio (Boas vindas ao usuário)
'''nome = input('Qual o seu nome ')
print('Boas vindas', nome , 'prazer em conhecê-lo')'''

#Segundo desafio (Pedido de nascimento do usuario)
'''dia = input('Dia: ')
mes = input('Mes: ')
ano = input('Ano: ')
print('Voce nasceu em', dia, 'de', mes, 'do ano de' , ano)# O + vai concatenar as stirngs, o virgula é um tipo de separador, independente de qual tipo for a variavel
#Um outro jeito de imprimir na tela a mesma coisa porem utilizando '{}' e '.format()', segue abaixo
print('Voce nasceu em {} de {} do ano de {}' .format(dia, mes, ano)) #O format vai seguir a ordem das chaves para impressão, o chaves é chamado de mascara'''

#Terceiro desafio (Soma de 2 dois numeros)
#aqui ele fala sobre os tipos primitivos, antes de pedir o numero ao usuario ele formata a string para um tipo int, para que depois seja somado e nao concatenado
'''num1 = int(input('Insira um numero: '))
num2 = int(input('Insira um numero: '))
soma = num1 + num2
print('A soma entre {} e {} vale {}'.format(num1, num2, soma))'''

#No caso do valor booleano, ele so retorna verdadeiro se tem algo dentro da variavel, caso nao tenha retorna False (Exemplo de false é apertando 'enter')
'''n1 = bool(input('Insira algo: '))
print(n1)'''

#Existe um modulo que é o 'is'algumacoisa(), ele vai dizer se é possivel converter o valor da variavel em um numero retornando True ou False, o mesmo vale para os outros tipos depois do 'is'
#Quarto desafio (Todas as informações de uma variável)
'''variavel = input('Insira algo: ')
print(variavel.isalnum()) #Me diz se a variavel é numero
print(variavel.isalpha()) #Se é do alfabeto
print(variavel.isascii()) # Se é da tabela ascii
print(variavel.isdecimal()) #Se é decimal
print(variavel.isdigit()) #Se é um digito
print(variavel.isidentifier()) #Ele é um idenificador, varre a string verificando se ela se adequa a referencia da documentação do python pra esse metodo
print(variavel.islower()) #Verifica se a string ta toda com os caraceteres minusculos
print(variavel.isnumeric()) #Verifica se a variavel é numerica
print(variavel.isprintable()) #Verifica se a string passada, os caracteres sao visiveis quando manda imprimir na tela
print(variavel.isspace()) #Verifica se é um espaço
print(variavel.istitle()) #Verifica se a string a primeira palavra dela for maiuscula, assim retorna True, caso contrario retorna False, numeros sao tratados como string entao na contam
print(variavel.isupper()) #Verifica se a string esta com os caracteres todos maisuculos'''

#Referente a aula 7
#Ordem de precedência esta em numero
#1° '()', 2° '**', 3° '*' '/' '//' '%', 4° '+' '-' 
'''Operadores aitmeticos '+' -> Soma   '*' -> Multiplicação '/' -> Divisão '-' -> Subtração '**' -> Potência '//' -> Divisão inteira '%' -> Resto da divisão '''
#Qualquer numero elevado a (1/2) vai dar sua raiz

#Quinto desafio (Sucessor e antecessor de um numero)
'''num = int(input('Digite um numero: '))
print('O antecessor de {} é {} e o sucessor é {}' .format(num, num - 1, num + 1)) #O format aceita fazer aritmetica simples pra imprimir depois, isso ajuda a economizar memoria pois nao crio variaveis aux'''

#Sexto desafio (Dobro, triplo e raiz quadrada de um numero)
'''num = int(input('Insira um numero: '))
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}' .format(num, num * 2, num * 3, num ** (1/2))) #O ':.2f' dentro do {}, é pra deixar com dois numeros apos o ponto flutuante'''

#Mesmo dasafio porem adicionei uma funcao que calcula a raiz quadrada pra mim
'''import math #Adicinei essa biblioteca de matematica que me traz o módulo sqrt pra calcular a raiz quadrada
#from math import sqrt #Caso eu queira usar só a raiz quadrada, usa esse código, para rapidez do proprio programa ja que se importar a biblioteca inteira ela pesa demais o programa pois traz todos os modulos dela
num = int(input('Insira um numero: '))
print('O dobro de {} é {}, triplo {} e raiz quadrada {}'.format(num, num * 2, num * 3, math.sqrt(num)))'''

#Setimo desafio (Media de duas notas de um aluno)
'''nome = str(input('Qual o nome do aluno: '))
nota1 = int(input('Insira a nota 1: '))
nota2 = int(input('Insira a nota 2: '))
media = (nota1 + nota2) / 2
print('Media do aluno {} é {:.2f}' .format(nome, float(media)))'''

#Oitavo desafio (Conversão de metros para centimetros e milimetros)
'''metros = float(input('Insira a medida em metros: '))
print('A medida de {} m em centimetros é {:.0f} cm, em milimetros é {:.0f} mm'.format(metros, metros * 100, metros * 1000)) #{:.0f} -> Não me exibe na tela os numeros apos o ponto flutuante'''

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
'''num = int((input('Insira um numero: ')))
print('\nTABUADA\n')
for i in range(1, num + 1, 1): # Aqui o for funciona criando uma variavel a qual é o 'i', e vai ate o range('inicio, parada, incremento')
    print('{} X {} = {}' .format(num, i, num * i)) #Aqui pensei em simplificar, multipliquei as variaveis ao inves de criar uma variavel pra armazenar a multiplicação do 'i' e o 'num'
print('\n')'''

#10° desafio (Quanto tem de dinheiro na carteira do usuario e quantos dolares ele consegue comprar com o dinheiro dele)
'''num = float(input('Quanto dinheiro há na sua carteira? '))
print('Quantidade na carteira {:.2f}, dolares que podem ser comprados {:.2f}' .format(num, num / 4,93)) #Cotação 'atual' do dolar'''

#11° desafio (Ler largura e altura de uma parede em metros e calcular a area , cada litro de tinta é 2m² por area, quantos preciso pra pintar a parede toda?)
'''largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area = largura * altura
print('Voce precisa de {:.2f} litros para pintar sua parede de area {}!'.format(area/2, area))'''

#12° desafio (Ler um preco de um produto, devolve-lo com 5% de desconto)
'''produto = float(input('Qual o valor do produto? '))
desconto = float(input('Qual o valor de desconto? ')) # O pedido de desconto nao precisava, mas quis testar pra ver se conseguia com o usuario pedindo
produto = produto - (produto * (desconto/100))
print('Valor final com 5% de desconto é {}!' .format(produto))'''

#13° desafio (Ler um salario de um funcionário e devolve com 15% de aumento)
'''nome = str(input('Qual o nome do funcionário? '))
aumento = int(input('Quantos de aumento {} receberá? '.format(nome)))
salario = float(input('Qual o sálario do {}? '. format(nome))) #Da pra aplicar o format direto no input
aumento = salario + (salario * (aumento/100)) #burrooooo, era aumento/100, quase 30m tentando resolver e era só inverter a ordem
print('O sálario do funcionário {} é {:.2f}, com aumento fica {:.2f}!' .format(nome, salario, aumento))'''

#14° desafio (Transformar celsius em Farenheith)
'''c = float(input('Insira a temperatura em Celsius: '))
f = (c * 9/5) + 32 
print('Graus {}°C para Farenheith é {}°F'.format(c, f))'''

#15° desafio (Calcular aluguel de um carro, quantos dias foi alugado, quantos km rodou, querendo saber o preço que custou, sabendo que é R$60 por dia e R$0.15 por km rodado)
'''dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
custo = (dias * 60) + (km * 0.15)
print('O custo total foi de R${}!'.format(custo)) '''

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
'''from math import floor
n = float(input('Insira um numero: '))
print(floor(n))'''

#Outro jeito que seria o do vídeo
'''from math import trunc
n = float(input('Insira um numero: '))
print(trunc(n))'''

#Mais um jeito
'''n = float(input('Insira um numero: '))
print(type(n))
print('{} valor inteiro é : {}'.format(n, int(n))) #Mostra o valor inteiro, para a variavel n ter o valor inteiro em si, teria que haver uma atribuicao, por isso ela continua com o tipo float apos esse código'''

#17° desafio (Ler cateto oposto e adjacente, devolver a hipotenusa)
'''from math import hypot
oposto = float(input('Insira o cateto oposto: '))
adjacente = float(input('Insira o cateto adjacente: '))
hip = hypot(oposto, adjacente) #Estou começando a usar variaveis auxiliares pq depois vou precisar usar variaveis auxiliares em programas mais complexos, entao na pratica ao inves de fazer direto os resultados vou armazenando em variaveis aux, por mais que utilize mais memoria
print('Hipotenusa: {:.2f}'.format(hip))'''

#18° desafio (Seno, cosseno e tangente de um numero)
#Esse exerciico eu tinha feito errado, precisava converter o angulo para radiano, meu programa nao fazia entao o resultado estava errado, adicionando a conversao por meio do radians consegui chegar no resultado correto
'''from math import sin, cos, tan, radians
n = float(input('Insira um numero: '))
sen = sin(radians(n))
coss = cos(radians(n))
tang = tan(radians(n))
print('O seno do numero {} é {:.2f}, cosseno é {:.2f} e tangente é {:.2f}'.format(n, sen, coss, tang))'''

#19° desafio (Sorteio de 4 alunos, escreva o nome do escolhido sorteando-o)
'''from random import choice #esse módulo ele escolhe aleatoriamente algo dentro de uma lista
nomes = ['Hugo', 'João', 'Maria', 'Lucas'] #Aqui supus que era desse jeito e deu certo
print('O nome do escolhido é : {}!'.format(choice(nomes))) '''

#Mesmo exercicio melhorado, utilizando estrutura de repetição (O usuario pode colocar os nomes, eles nao vem pre-definidos como o código anterior)
'''nomes = [] #Inicializa uma variavel como lista vazia
for i in range(1, 6, 1): #Aqui coloco o parametro de inicio e parada
    nomes.append(str(input('Insira o nome: '))) #Aqui a função append vai colocar no final da lista o que o usuário digitar
print('O nome escolhido foi {}'.format(choice(nomes))) #Aqui eu faço o sorteio ja com a lista cheia'''

#20° desafio (Escolha aleatoriamente alunos e sua ordem de apresentação de cada um)
'''from random import shuffle
n1 = str(input('Insira um nome : '))
n2 = str(input('Insira um nome : '))
n3 = str(input('Insira um nome : '))
lista = [n1, n2, n3]
shuffle(lista)
print('A ordem de apresentação sera ')
print(lista)'''

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
