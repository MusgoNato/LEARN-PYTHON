#referente a aula 12
#Condiçoes aninhaddas sao agrupamentos de condicoes
#if, else, elif -> (É um senao se) dentro do if pode ter varios elif, agora nao da pra usar elif sem o if

# #36° desafio (Pergunta o valor da casa, salario do comprador e em quantos anos ela vai ser paga, calcular o valor da prestação mensal e nao pode exceder 30% do salario senao vai ser negado o empréstimo)
# valor_casa = float(input('Qual o valor da casa? '))
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# salario_comprador = float(input('Qual o salario do comprador? '))
# ano = int(input('Quantos anos a casa vai ser paga? '))
# prestacao_mensal = valor_casa / (ano * 12) #prestacao paga em meses
# posi_nega = salario_comprador * (30 / 100) #30% do salario do comprador
# if prestacao_mensal <= posi_nega:
#     print('{}Valor do empréstimo aprovado, você consegue pagar!\033[m'.format(cores['verde']))
#     print('Prestação mensal de : {}{:.2f}\033[m'.format(cores['verde'], posi_nega))
# else:
#     print('{}Empréstimo Negado, valor da prestação é {:.2f}!\033[m'.format(cores['red'], prestacao_mensal))

#37° desafio (O usuario escolhe se o numero dado vai ser transformado para binario, hexadecimal ou octal)
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# num = int(input('Insira um numero : '))
# print('0 - BINÁRIO\n1 - HEXADECIMAL\n2 - OCTAL')
# op = int(input('Insira uma opção: '))
# if op == 0:
#     print('Numero em binário : {}{}\033[m'.format(cores['verde'], bin(num)[2:])) #Aqui o [2:] vai fatiar a string, ele só ira imprimir na tela a partir da posição 2 da string ate o final
# elif op == 1:
#     print('Numero em Hexadecimal : {}{}\033[m'.format(cores['yellow'], hex(num)[2:]))
# elif op == 2:
#     print('Numero em octal : {}{}\033[m'.format(cores['roxo'], oct(num)[2:]))
# else:
#     print('{}Opção não disponível!\033[m'.format(cores['red']))

#38° desafio (Dois numeros, mostrar qual deles é maior e se sao iguais)
# num1 = int(input('Insira um numero: '))
# num2 = int(input('Insira outro numero: '))
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# if num1 < num2:
#     print('Maior {}{}\033[m'.format(cores['verde'], num2))
# elif num2 < num1:
#     print('Maior {}{}\033[m'.format(cores['azul'], num1))
# else:
#     print('{}Os valores sao iguais!\033[m'.format(cores['sla']))

#39° desafio (Ler ano de nascimento, informar se ele ainda vai se alistar no exercito, se é hora de se alistar, passou do tempo de se alistar, programa deve mostrar o tempo que falta ou que passou do prazo)
# from datetime import date
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# ano = int(input('Insira o ano do seu nascimento : '))
# idade = date.today().year - ano
# if idade < 18:
#     print('Você é menor de 18 anos, seu alistamento ocorre em {}{}\033[m'.format(cores['red'], ano + 18))
# elif idade == 18:
#     print('{}Você deve se alistar\033[m'.format(cores['verde']))
# elif idade > 18:
#     print('Passou do tempo de alistar-se, você tem {}{} e deveria ter se alistado no ano de {}\033[m'.format(cores['yellow'], idade, ano + 18))

#40° desafio (ler duas notas e calcular a media, reprovado < 5.0, recuperação entre 5.0 e 6.9, aprovado 7.0 ou superior)
# nota1 = float(input('Insira sua 1° nota : '))
# nota2 = float(input('Insira sua 2° nota : '))
# cores = {'verde': '\033[0;32m', 'azul': '\033[0;34m', 'red': '\033[1;31m', 'yellow' : '\033[1;30;43m', 'roxo' : '\033[35;47m', 'ciano' : '\033[36;47m', 'sla' : '\033[1;37;42m', 'sla2' : '\033[0;30;46m'}
# media = (nota1 + nota2)/2
# if media < 5.0:
#     print('Sua média foi {}{}\033[m, você esta reprovado!'.format(cores['red'], media))
# elif media >= 5.0 and media <= 6.9:
#     print('Sua média foi {}{}\033[m, você esta de recuperação!'.format(cores['yellow'], media))
# elif media > 7.0:
#     print('PARABÉNS, você foi aprovado, média {}{}\033[m'.format(cores['verde'], media))

#41° desafio (ler ano de nascimento do nadador e informar seu grau, ate 9 anos mirim, 14 infantil, 19 junior, 20 senior, acima master)
# from datetime import date
# ano = int(input('Insira seu ano de nascimento: '))
# idade = date.today().year - ano
# if idade <= 9:
#     print('mirim!')
# elif idade <= 14:
#     print('infantil!')
# elif idade <= 19:
#     print('Junior!')
# elif idade <= 20:
#     print('Sênior!')
# elif idade > 20:
#     print('MASTER!!!!')

#42° desafio (ver se existe a possibilidade de existencia de um triangulo, formar um triangulo isoceles, equilatero ou escaleno)
# reta1 = int(input('Insira o angulo A: '))
# reta2 = int(input('Insira o angulo B: '))
# reta3 = int(input('Insira o angulo C: '))

# if reta1 < reta2 + reta3 or reta2 < reta1 + reta3 or reta3 < reta1 + reta2:
#     print('Condição de existência satisfeita para criação do triângulo!')
#     if reta1 != reta2 and reta2 != reta3 and reta3 != reta1: #Outro jeito de fazer isso de forma simplificada (reta1 != reta2 != reta3 != reta1)
#         print('Triangulo escaleno!')
#     if reta1 == reta2 and reta2 == reta3: #Outro jeito de fazer isso de forma simplificada (reta1 == reta2 == reta3)
#         print('Triangulo equilatero!')
#     if (reta1 == reta2 and reta1 != reta3) or (reta2 == reta3 and reta2 != reta1) or (reta1 == reta3 and reta1 != reta2):
#         print('Trangulo isoceles!')
# else:
#     print('Condição de existencia do triângulo não satisfeita!')

#43° desafio (Ler peso e altura e mostrar seu imc, abaixo de 18.5 abaixo do peso, entre 19.5 e 25.0 peso ideal, 25 ate 30 sobrepeso, 30 ate 40 obesidadee e acima de 40 obesidade morbida)
# peso = float(input('Insira seu peso : '))
# altura = float(input('Insira sua altura: '))
# imc = peso / pow(altura,2)
# print('Seu IMC é {:.2f}'.format(imc))
# if imc < 18.5:
#     print('Abaixo do peso!')
# elif imc >= 19.5 and imc <= 25.0:
#     print('Peso ideal!')
# elif imc >= 25.0 and imc <= 30.0:
#     print('Sobrepeso!')
# elif imc >= 30.0 and imc <= 40:
#     print('Obesidade!')
# elif imc > 40:
#     print('Obesidade Móbida!')

#44° desafio (Valor a ser pago pelo produto, a vista ou cheque é 10% de desconto, no cartao a vista e 5% de desconto, 2x no cartao preco normal e 3x no cartao 20% de juros)
# print('{:=^40}'.format(' LOJA HUGO ')) #Centraliza a frase na hora de imprimi-la
# produto = float(input('Preço do produto: '))
# print('0 - DINHEIRO/CHEQUE\n1 - Á VISTA NO CARTÃO\n2 - 2X NO CARTÃO\n3 - 3x OU MAIS NO CARTÃO')
# op = int(input('Qual a forma de pagamento? '))
# if op == 0:
#     produto = produto - (produto * (10/100))
#     print('Valor final do produto {}'.format(produto))
# elif op == 1:
#     produto = produto - (produto * (5/100))
#     print('Valor dinal do produto a vista no cartão {}'.format(produto))
# elif op == 2:
#     print('2X parcelas de {}, preço padrão do produto sem alterações {}!'.format(produto/2, produto))
# elif op == 3:
#     parcela = int(input('Quantas parcelas? ')) #Como o ex pede mais de 3 parcelas, o usuario vai digitar elas e o programa ira dividir no que ele deseje
#     produto = produto + (produto * (20/100))
#     print('{}X parcelas de {:.2f}, preço final do produto : {}'.format(parcela, produto/parcela, produto))
# else:
#     print('Opção não cadastrada!')

#45° desafio (Jokenpo)
# from random import choice
# opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
# pc = choice(opcoes)
# user = str(input('Insira sua jogada: ')).strip().upper()
# if pc == user:
#     print('Empate!')
# elif pc == 'PEDRA' and user == 'PAPEL':
#     print('Voce venceu, pc jogou pedra!')
# elif pc == 'PAPEL' and user == 'TESOURA':
#     print('Voce venceu, pc jogou papel!')
# elif pc == 'TESOURA' and user == 'PEDRA':
#     print('Voce venceu, pc jogou tesoura!')
# elif user == 'PEDRA' and pc == 'PAPEL':
#     print('Voce perdeu, pc jogou papel!')
# elif user == 'PAPEL' and pc == 'TESOURA':
#     print('Voce perdeu, pc jogou tesoura!')
# elif user == 'TESOURA' and pc == 'PEDRA':
#     print('Voce perdeu, pc jogou pedra!')

#Referente a aula 13
# for c in range(0,6):
#     print('Oi')
# print('Fim')

# for c in range(1, 7):#O ultimo ele sempre ignora
#     print(c)
# print('Fim')

# for c in range(6, 0, -1): #Começa ao contrario
#     print(c)
# print('Fim')

# for c in range(0, 7, 2): #Pula de dois em dois, de tras para frente
#     print(c)
# print('Fim')

# n = int(input('Digite o Inicio: '))
# f = int(input('Digite o Fim: '))
# p = int(input('Digite o passo : '))
# for c in range(n, f, p): #Posso usar variaveis para determinar o inicio e fim do dor, tambem para dizer em quantos passos quero
#     print(c)
# print('FIM')

# s = 0
# for c in range(0, 3):
#     n = int(input('Insira um numero: '))
#     s += n
# print('Soma : {}'.format(s))

#46º desafio (Contagem regressiva de 10 ate 0, pausando 1 segundo)
# from time import sleep
# import emoji
# for i in range(10, 0 , -1):
#     print('Contagem regressiva : {}'.format(i))
#     sleep(1)
# print(emoji.emojize('FOGOS ESTOURADOS :thumbsup:', language='alias'))

#47º desafio (Criar um programa com todos os numeros pares, no intervalo de 1 ate 50)
# for i in range(1, 50 + 1):
#     if i % 2 == 0:
#         print('Par : {}'.format(i))
#     else:
#       print('Impar : {}'.format(i)) #Crie um else pra mostrar os impares, porem o desafio so pediu pares

#Outro jeito de fazer sem fazer duas iterações
# for i in range(1, 51, 2): #Aqui ele pula de dois em dois pois nao é necessario verificar os impares
#    if i % 2 == 0:
#       print('Par : {}'.format(i))

#48º desafio (Soma de impares multiplos de 3 no range 0 ate 50) #Faltou acumulador
# s = 0        
# cont = 0
# for i in range(1, 501):
#     if i % 2 == 1 and i % 3 == 0:
#         s += i
#         cont += 1
#         print('{}'.format(i))
# print('A soma dos {} valores são {}'.format(cont, s))

#Outro jeito de fazer
# for i in range(1, 501, 2):
#     if and i % 3 == 0:
#         s += i
#         print('{}'.format(i))
# print('A soma dos {} valores são {}'.format(cont, s))

#49º desafio (Tabuada usando for)
# n = int(input('Insira o numero da tabuada: '))
# mult = 1
# for i in range(1, 11):
#     print('{} X {} = {}'.format(n, i, mult * i))

#50º desafio (ler 6 numeros e se for par soma) #Faltou ler o numero
# s = 0
# for i in range(1, 5, 1): #Pula de um em um
#     valor = int(input('Insira o {} numero: ').format(i))
#     if valor % 2 == 0:
#         s += valor
# print('Soma : {}'.format(s))

#51º desafio (ler o primeiro termo e a razao de uma prorgressao artmetica) #Essa eu consegui fazer porem com numero magico, a formula ajudou a calcular com qualquero numero inicial
# p_termo = int(input('Insira o primeiro termo : '))
# r = int(input('Insira a razao : '))
# n_esimotermo = p_termo + (10 - 1) * r #Formula que calcula ate o decimo termo  
# for i in range(p_termo, n_esimotermo + r, r):
#     print('{}'.format(i))

#52º desafio (dizer se n é numero primo)
# n = int(input('Insira um numero : '))
# resultado = 0
# for i in range(1 , n + 1):
#     if n % i == 0: #Aqui estava errado, eu negava ser igual a 0 para ele somar no resultado, eu quase consegui o mesmo resultado porem tava fazendo ao contrario
#         resultado += 1

# #Como ele e divisivel por um e por ele msm, so e necessario saber quantas vezes foi divisivel o numero, acima de 2 nao e divisivel por causa da regra de um numero primo
# if resultado <= 2:
#     print('Primo: {}'.format(n))
# else:
#     print('Ñ primo : {}'.format(n))

#53º desafio (Verificar se uma string é palidromo descosiderando espaços)
# string = str(input('Digite a palavra: ')).strip().split()
# string  = ''.join(string).upper()
# retorno = 0
# tamanho = len(string)
# for i in range(0, tamanho): #Vai de 0 ate tamanho - 1, lembrando que o ultimo valo nao pega
#     if string[i] == string[tamanho - i - 1]: #Aqui ele começa com uma posicao a mais, por isso e necessario decremetar um de inicio na variavel tamanho
#         retorno += 1
#     else:
#         retorno = 0 #Caso ele encontre uma letra que nao seja igual entao nao precisa verificar mais e sai do loop
#         break;

# if retorno != 0: #Faz uma verificação pra informar se a palavra é palindromo
#     print('Palavra {} é palíndromo!'.format(string).lower())
# else:
#     print('Palavra não é palindromo!')

#54º desafio (Ler ano de nascimento de 7 pessoas e dizer se é maior que 21 anos de idade)
# import datetime
# resultado = datetime.datetime.today().year
# for i in range(0, 8):
#     nome = str(input('Insira seu nome: ')).strip()
#     ano = int(input('Qual seu ano de nascimento : '))
#     maior = resultado - ano
#     if maior >= 21:
#         print('Voce é maior de idade {}'.format(nome))
#     else:
#         print('Voce é de menor {}, falta {} anos pra ser de maior!'.format(nome, 21 - maior))

#55º desafio (Ler peso de 5 pessoas e determinar qual foi o maior e menor peso lido)
# nome = []
# peso = []
# cont = 0
# for i in range(0, 3): #Dentro desse loop ocorre a adicao no final da lista criada para nome e peso, para isso e necessario criar uma variavel pegar os elementos lidos e depois juntalos utilizando append e de começo colocando o nome da lista
#     pessoa = str(input('Insira seu nome : ')).strip()
#     valor = float(input('Insira seu peso: '))
#     nome.append(pessoa)
#     peso.append(valor)

# Aqui encontra o menor e maior valor da lista passada
# maior = max(peso) 
# menor = min(peso)
# print(maior)
# print(menor)

#56° desafio (ler nome, sexo e idade de 4 pessoas e depois retornar a media de idade do grupo, o nome do homem mais velho e quantas mulheres tem menos de 20 anos)
# nome = []
# idade = []
# sexo = []
# homens_velhos = []
# media = 0.0
# cont = 0
# maior = 0
# for i in range(4):
#     pessoa = str(input('Insira seu nome : ')).strip().upper()
#     anos = int(input('Insira sua idade : '))
#     genero = str(input('Insira seu sexo: ')).strip().upper()
#     nome.append(pessoa)
#     idade.append(anos)
#     sexo.append(genero)
#     if genero == 'F' or genero == 'FEMININO' and anos < 20: #Outro jeito é (if genero in 'Ff'), ele faz tipo um or dentro das aspas, se for um ou outro ele entra no if
#         cont += 1 #Conta as mulheres
#     if genero == 'M' or genero == 'MASCULINO':
#         homens_velhos.append(anos) #Aqui adiciono a idade em homens mais velhos para saber qual é
#         maior = max(homens_velhos) #Aqui guardo a idade mais alta conforme o loop vai rodando
#         homem_maisvei = idade.index(max(homens_velhos)) #Aqui atribui uma variavel para guardar o indice do numero maior da lista de homenns_velhos

# print('{} é o mais velho com {} anos!'.format(nome[homem_maisvei], maior)) #Aqui procuro na lista passando como indice a variavel homem_maisvei que criei dentro do loop e pega o indice do maior elemento dentro da lista
# print('Existem {} mulheres menores que 20 anos!'.format(cont))
# media = sum(idade)/len(idade) #O sum vai somar todos os elementos de uma lista e depois divido pela quantidade, onde o lem me retorna essa valor
# print('Media da idade do grupo : {} anos!'.format(media))

#Referente a aula 14
#O for é mais certo usar quando eu sei o limite
#Já o while e comum usar quando nao sei o limite

# for c in range(1, 10):
#     print(c)
# print('Fim')

#FLAG = ponto de parada
# c = 1
# while c <= 10:
#     print(c)
#     c += 1
# print('Fim')

#57° desafio (Fazer um programa que leia o sexo de uma pessoa, sendo m ou f, caso esteja errado pedir novamente ate ter o valor correto)
# sexo = ''

# #Modo de loop mais simplificado do que o tradicional
# #while sexo not in 'MmFf': #Aqui a traducao ficaria 'enquanto sexo nao é encontrado dentro de M ou m ou F ou f, dai ele continua rodando o código'

# while sexo != 'F' and sexo != 'M':

#     #Modo de leitura um pouco mais simples
#     #sexo = str(input('Informe seu sexo : [M/F]')).strip().upper()[0] #Esse [0] vai pegar somente a primeira letra da string
     
#     sexo = str(input('Insira seu gênero: ')).strip().upper()
#     if sexo == 'M':
#         print('Você é menino!')
#         break;
#     elif sexo == 'F':
#         print('Você é menina!')
#         break;

#58° desafio (adivinhar numero que o pc pensou de 0 a 10 e dizer quantos palpites foram necessarios)
# from random import randint
# pc = randint(0, 10)
# palpites = 0
# player = 0
# while pc != player:
#     player = int(input('Insira um numero: '))
#     palpites += 1
#     if pc == player:
#         print('Parabens voce acertou o numero, foram necessarios {} palpites'.format(palpites))
#         break;
#     if player < pc:
#         print('Mais, tente novamente | ', end=' ')
#     else:
#         print('Menos, tente novamente | ', end=' ')

#59° desafio (Criar programa que le 2 valores e ter um menu pra realizar a operacao solicitada, somar, maior, multiplicar, novos numeros, ou sair)
# import os
# from time import sleep
# op = True
# n1 = int(input('Insira o valor 1° : '))
# n2 = int(input('Insira o valor 2° : '))
# while op:
#     print('[1]SOMAR\n[2]MAIOR\n[3]MULTIPLICAR\n[4]NOVOS NUMEROS\n[5]SAIR\n')
#     op = int(input('Insira a opção : '))
#     os.system('cls')
#     if op == 1:
#         print('Soma : {}'.format(n1 + n2))
#         sleep(2)
#     elif op == 2:
#         print('Maior : {}'.format(max(n1, n2)))
#         sleep(2)
#     elif op == 3:
#         print('Multiplicação : {}'.format(n1 * n2))
#         sleep(2)
#     elif op == 4:
#         n1 = int(input('Insira o valor 1° : '))
#         n2 = int(input('Insira o valor 2° : '))
#     elif op == 5:
#         op = False
    
#60° desafio (Fatorial de um numero)
#Fatorial usando o for
# n = int(input('Insira um numero : '))
# fat = 1
# for c in range(1, n + 1):
#     fat = fat * c
# print('Fatorial de {} é {}'.format(n, fat))

#Fatorial usando o while
# n = int(input('Insira um numero : '))
# i = 1
# fat = 1
# while i != n + 1: #Tanto no 'for' quanto no 'while', essas estruturas excluem o ultimo valor do parametro de parada do loop, por isso é necessario adicionar +1 a variavel n nesse desafio
#     fat *= i
#     i += 1
# print('O fatorial do numero {} é {}'.format(n, fat))

#Um jeito diferente de fazer a condição
# print('{}'.format(i), end=' ')
# print(' X ' if i > 1 else ' = ', end=' ')


#Outro jeito de fazer
# from math import factorial
# n = int(input('Insira um numero : '))
# fact = factorial(n)
# print(n)

#61° desafio (Fazer uma pa)
# n = int(input('Insira o 1° termo : '))
# r = int(input('Insira a razao : '))
# i = 10
# j = 0
# while i >= j:
#     enesimo = n + (i * r)
#     print('{}'.format(enesimo), end= ' ')
#     i -= 1
        
#62° desafio (Fazer uma pa e o usuario pode pedir mais termos)
# n = int(input('Insira o 1° termo : '))
# r = int(input('Insira a razao : '))
# i = 10
# j = 0
# while i >= j:
#     enesimo = n + (i * r)
#     print('{}'.format(enesimo), end= ' ')
#     i -= 1
#     if i == j:
#         op = int(input('\nQuantos termos a mais voce vai querer? '))
#         if op == 0:
#             break;
#         else:
#             i += 10 + op

#63° desafio (Sequencia de fibonacci) #Nao consegui fazer
# n = int(input('Insira um numero : '))
# i = 3
# p_termo = 0
# s_termo = 1
# print('{} | {}'.format(p_termo, s_termo), end=' ')
# while i <= n:
#     t_termo = p_termo + s_termo
#     print('| {}'.format(t_termo), end=' ')
#     #Aqui existe a troca dos termos, fazendo isso o primeiro numero da sequencia soma com o segundo e assim por diante
#     p_termo = s_termo
#     s_termo = t_termo
#     i += 1

#64° desafio (Ler numeros ate o usuario digitar 999, contar quantos numeros foram digitados e a soma entre eles)
# contador = soma = op = 0
# while op != 999: #Flag é um criterio de parada, nesse caso e o 999
#         n = int(input('Insira um numero : '))
#         if n != 999:
#             contador += 1
#             soma += n
#         else:
#             op = n
#             print('{} numeros digitados e a soma deu {}'.format(contador, soma), end=' ')
#             break;

#65° desafio (Ler numeros ate o usuario nao querer mais, mostrar a media entre todos e qual foi o maior e menor valor lido)
# media = 0.0
# soma = 0
# cont = 0
# valores = []
# op = 'S'
# while op != 'N': #while op not 'Ss' -> Outro jeito de fazer caso nao estivesse tratando as letras maiusculas
#     if op != 'S' and op != 'N':
#         op = str(input('Dados invalidos, tente novamente : ')).strip().upper()
#     else:
#         n = int(input('Insira um numero : '))
#         valores.append(n)
#         cont += 1
#         soma += n
#         op = str(input('Quer continuar? S/N : ')).strip().upper()
# media = soma/cont
# ma_x = max(valores)
# mi_n = min(valores)
# print('Menor {} e Maior {}, Media : {}'.format(mi_n, ma_x, media))

#Referente a aula 15
#No python so existe o for e o while, porem nao quer dizer que eu nao possa simular um 'do while' ou um 'repeat'
#no python nao se declara variaveis, so inicializa elas
#cont = 1
#O comando break quebra o loop, sai fora dele
# while cont <= 10:
#     print(cont, '-> ', end='')
#     cont += 1
# print('Acabou')

#PEP - > Proposta de melhoria do python
#Interpolação é intercalação das palavras, ou seja, o que esta nas chaves vao ser trocados pelas variaveis dentro do próprio
#print(f'A soma vale {variavel aqui dentro}')

#66° desafio (Ler infinitamente numeros ate o ususario digitar 999, contar quantos numeros foram digitados e a soma entre eles)
# n = soma = cont = 0
# while True:
#     n = int(input('Digite um valor (999 para parar): '))
#     if n == 999:
#         break;
#     else:
#         cont += 1
#         soma += n

# print(f'A soma dos {cont} valores foi {soma}')

#67° desafio (Tabuada de valores, o criterio de parada é qualquer numero negativo)
# mult = 1
# i = 0
# while True:
#     print(20*'-')
#     n = int(input('Quer ver a tabuada de qual valor? '))
#     if n <= 0:
#         break;
#     else:
#         print(20*'-')
#         for i in range(1, 11):
#             mult = n * i
#             print(f'{n} X {i} = {mult}')
# print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

#68° desafio (Jogar par ou impar com o computador e mostrar o total de vitorias do jogador)
# from random import randint
# aux = soma = 0 #Valor pra guardar o resto por 2 == 0
# print(20*'=')
# print('VAMOS JOGAR PAR OU ÍMPAR')
# while True:
#     print(20*'=')
#     n = int(input('Insira um valor : '))
#     n_pc = randint(0, 11)
#     soma = n + n_pc
#     player = ' ' #Pro while de baixo, é necessario inicializar essa variavel com espaço vazio
#     while player not in 'PI': #Desse jeito eu consigo fazer um loop enquanto for diferente do valor que eu quero pra fazer o jogo
#         player = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
#     if player == 'P': #Condição para caso o jogador ser par
#         if soma % 2 == 0:
#             print(20*'-')
#             print(f'Você jogou {n} e o computador {n_pc}. Total de {soma} deu PAR')
#             print(20*'-')
#             print('Você VENCEU!')
#             print('Vamos jogar novamente...')
#             aux += 1
#         else:
#             print(20*'-')
#             print('Você PERDEU!')
#             print(20*'=')
#             print(f'GAME OVER! Voce venceu {aux} vezes')
#             break;
#     elif player == 'I':
#         if soma % 2 == 1:
#             print(20*'-')
#             print(f'Você jogou {n} e o computador {n_pc}. Total de {soma} deu ÍMPAR')
#             print(20*'-')
#             print('Você VENCEU!')
#             print('Vamos jogar novamente...')
#             aux += 1
#         else:
#             print(20*'-')
#             print('Você PERDEU!')
#             print(20*'=')
#             print(f'GAME OVER! Você venceu {aux} vezes')
#             break;


#69° desafio (Idade e sexo lidos de varias pessoas, cada pessoa deve o programa perguntar se quer continuar ou nao, no final mostrar pessoas maiores de 18, quantos homens foram cadastrados e quantas mulheres com menos de 20 anos)
# anos = quant_f = quant_m = 0
# yes_not = ' '
# sexo = ' ' #Caso eu coloque só '' ele me da erro o programa, por algum acaso é necessario inicializar a variavel com o espaço vazio e '' nao conta como espaço vazio
# while True:
#     idade = int(input('insira a idade : '))
#     while sexo not in 'FM':
#         sexo = str(input('Insira o sexo : [F/M] ')).strip().upper()[0]
#     while yes_not not in 'SN':
#         yes_not = str(input('Quer continuar? [S/N]')).strip().upper()[0]
#     if yes_not == 'S' or yes_not == 'N':
#         if idade >= 18:
#             anos += 1
#         if sexo == 'M':
#             quant_m += 1
#         if sexo == 'F' and idade < 20:
#             quant_f += 1
#     if yes_not == 'N':
#         break;
#     sexo = ' '
#     yes_not = ' '
# print('FIM DO PROGRAMA')
# print(f'Total de pessoas com mais de 18 anos : {anos}')
# print(f'Ao todo temos {quant_m} homens cadastrados')
# print(f'E temos {quant_f} mulheres com menos de 20 anos')

#70° desafio (Ler varios preço de produtos e perguntar se quer continuar, mostrar qual o total gasto na compra, quantos produtos custam mais de 1000 e produto mais barato)
# total = 0.0
# cont = menor = 0
# op = ' '
# produtos = []
# valores = []
# while True:
#     produto = str(input('Insira o nome do produto : ')).strip().upper()
#     valor = float(input('Insira o valor : '))
#     valores.append(valor)
#     produtos.append(produto)
#     op = ' ' #Reinicio a variavel pra dar certo o while
#     while op not in 'SN':
#         op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#     if valor > 1000:
#         cont += 1
#     total += valor
#     produto_barato_indice = valores.index(min(valores)) #Pega o produto mais barato, lembrando que a variavel vai guardar o indice da verificacao do menor valor na lista valores, pegando o indice pode pegar o nome do produto tambem, colocando como indice a varival 
#     if op == 'N':
#         break;

# print(f'O total da compra foi de R${total}')
# print(f'Temos {cont} produtos custando mais de R$1000.00')
# print(f'O produto mais barato foi {produtos[produto_barato_indice]} que custa R${min(valores)}')
#print(f'O total da compra deu {total:2.f}') #Da pra fazer desse jeito a formatação da saida do valor, nesse caso ele vai me apresentar o valor com 2 casas decimais
#print('{:-^40}'.format('FIM DO PROGRAMA')) #O circunflexo vai centralizar minha msg
#71° desafio (simular um caixa eletronico, perguntar qual o valor a ser sacado em inteiro, o programa deve informar quantas cedulas vao ser entregues para o usuario, considerando que o caixa possui cedulas de 50, 20, 10 e 1)

#cedulas
#50, 20, 10 e 1
#Contador de cedulas e a outra variavel vai armazenar o valor e ira dividindo com as celulas disponiveis

#Como nao consegui fazer vou explicar
#O programa ele vai ter uma variavel que vai ser a primeira cedula, dentro do programa, rodando em loop infinito caso nao for apos saber que o valor que
#foi dado é maior que a cedula inicial, no caso 50, e decrementado 50 do total do valor, ou seja o montante inicial maior entao quer dizer que as notas
#de 50 maximas que da pra tirar do montante ja alcançaram seu limite e assim a variavel que controla as notas recebera a proxima nota, no caso 20, E assim
#por diante vai, no final é feito uma verificação caso o montante chegue no zero, pois caso verdadeiro nao é necessario continuar no loop e é 
#colocado um break pra sair do programa

# ced = 50 #Vai receber a primeira cedula pra depois ir recebendo o restante ate o valor chegar a zero
# cont = 0 #Total de cedulas
# valor = int(input('Qual o valor você quer sacar? '))
# total = valor
# while True:
#     if total >= ced:
#         total -= ced #Decrementa do montante
#         cont += 1
#     else:
#         if cont > 0:
#             print(f'Total de {cont} cédulas de R${ced}')
#         if ced == 50:
#             ced = 20
#         elif ced == 20:
#             ced = 10
#         elif ced == 10:
#             ced = 1
#         cont = 0
#         if total == 0:
#             break;