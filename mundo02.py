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
