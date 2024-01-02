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
# while sexo != 'F' and sexo != 'M':
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
#     if pc == player:
#         print('Parabens voce acertou o numero, foram necessarios {} palpites'.format(palpites))
#         break;
#     palpites += 1

#59° desafio (Criar programa que le 2 valores e ter um menu pra realizar a operacao solicitada, somar, maior, multiplicar, novos numeros, ou sair)
# import os
# from time import sleep
# op = 0
# n1 = int(input('Insira o valor 1° : '))
# n2 = int(input('Insira o valor 2° : '))
# while op != 5:
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
#         break;
    
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
#     fat = fat * i
#     i += 1
    
# print('O fatorial do numero {} é {}'.format(n, fat))

#61° desafio (Fazer uma pa)
# n = int(input('Insira o 1° termo : '))
# r = int(input('Insira a razao : '))
# enesimo = n + (10 - 1) * r
# while enesimo :
#     print('{}'.format(n))
