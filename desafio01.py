#O desafio é imprimir na tela as boas vindas ao usuario de acordo com o valor digitado
#Todos os arquivos nessa pasta sao referenetes ao 1° modulo do python no curso em video
#Esse é o primeiro video, primeiro desafio
'''nome = input('Qual o seu nome ')
print('Boas vindas', nome , 'prazer em conhecê-lo')'''

#Segundo desafio (Pedido de nascimento do usuario)
'''dia = input('Dia: ')
mes = input('Mes: ')
ano = input('Ano: ')
print('Voce nasceu em', dia, 'de', mes, 'do ano de' , ano)# O + vai concatenar as stirngs, o virgula é um tipo de separador, independente de qual tipo for a variavel
#Um outro jeito de imprimir na tela a mesma coisa porem utilizando '{}' e '.format()', segue abaixo
print('Voce nasceu em {} de {} do ano de {}' .format(dia, mes, ano)) #O format vai seguir a ordem das chaves para impressão'''

#Terceiro desafio (Soma de 2 dois numeros)
#aqui ele fala sobre os tipos primitivos, antes de pedir o numero ao usuario ele formata a string para um tipo int, para que depois seja somado e nao concatenado
num1 = int(input('Insira um numero: '))
num2 = int(input('Insira um numero: '))
soma = num1 + num2
print('A soma é {}'.format(soma))