#Referente a aula 16 (Variaveis compostas : Tuplas, listas e dicionários)
#As tuplas sao imutaveis, nao é possivel fazer a mudança de algum valor armazenado dentro da tupla, ela ficara assim ate o final do programa
#Durante a execução nao tem como mudar a tupla, só se parar trocar os valores e reiniciar o programa

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita') #Mesmo sem colocar parenteses o python considera como tupla
# print(lanche[1])

#for cont in range(0, len(lanche):
#print(f'Eu vou comer {lanche[cont]}')

#Isso abaixo é variavel composta
#for comida in lanche:
# print(f'Eu vou comer {comida}')

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# for pos, comida in enumerate(lanche): #Além do dado ele me dá a posição
#     print(f'Eu vou comer {comida} na posição {pos}') #O pos é um contador normal, como qualquer outro, como comida é uma váriavel composta ela sucessivamente vai trocando o valor conforme o indice que é ela própria vai incrementando, o pos é mais uma variavel comum, basicamente servindo so pra saber a posição mesmo

# print(sorted(lanche)) #Mostra em ordem alfabética
# lanche = sorted(lanche) #como a tupla é imutavel, fazendo isso, eu estaria mudando de tupla para lista, apos isso agora o lanche é lista e nao tupla mais
# print(lanche)

#Concatena as tuplas na tupla c, ou seja, junta elas
# a = (2,5,4)
# b = (5,8,1,2)
# c = a + b
# print(c. index(5, 1)) #Começa na posição um e retorna o indice de 5
# pessoa = ('Gustavo', 39, 'M', 99.88) #Multiplos tipos de variaveis podem ser inicializados na tupla
# del(pessoa) #Como ela é imutavel, existe o del pra deletar TODA A TUPLA, após isso é apagada da memória, assim posterior a esse comando a tupla não existira mais

#72° desafio (Ler numero entre 0 e 20 e mostra-lo por extenso utilizando tuplas)
# numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# n = int(input('Insira um numero : '))
# while True:
#     if n < 0 or n > 20:
#         n = int(input('Número fora do intervalo de 0 a 20. Insira um número: '))
#     else:
#         cont = numeros.index(numeros[n])
#         print(f'{numeros[cont].upper()}') #Dá de eu fazer isso pois estou escrevendo uma string, na inicialização não é possível
#         break;

#73° desafio (Tupla com 20 primeiros colocados da tabela do campeonato brasileiro, mostrar 5 primeiros colocados,
#os ultimos 4 colocados, uma lista com times em ordem alfabética e em que posicao da tabela esta o time da chapecoense)
# times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Red Bull Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuibá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
# print(times[0:5]) #Primeiros 5 times
# print(times[20:15:-1]) #Ultimos 4 colocados
# print(sorted(times)) #Ordem alfabética
# for i, cont in enumerate(times): #É necessário o cont pra ser uma variavel composta pra enumeração do times
#     if 'Chapecoense' in times[i]:
#         print(f'Chapecoense está na posição {i + 1}')

#74° desafio (Gerar cinco numeros aleatorios e colocar em uma tupla, depois mostrar a listagem de numeros, indicando o maior e o menor valor lidos)
# from random import randint
# numeros = randint(0, 6), randint(0, 6), randint(0, 6), randint(0, 6), randint(0, 6)

# for i, cont in enumerate(numeros):
#     print(f'{numeros[i]}',end=' ')
# menor = min(numeros)
# maior = max(numeros)
# print(f'\nMaior {maior} e menor {menor}')

#75° desafio (Ler 4 valores do teclado e guardar na tupla, saber quantas vezes o valor nove apareceu, em que posicao o 3 ta, quais foram os numeros pares)
# # num1 = int(input('Digite um numero : '))
# # num2 = int(input('Digite outro numero : '))
# # num3 = int(input('Digite mais um numero : '))
# # num4 = int(input('Digite o último numero : '))
# # valores = (num1, num2, num3, num4)
# # cont = valores.count(9)
# # print(f'Você digitou os valores : {valores}')
# # print(f'Foram {cont} vezes que o 9 apareceu')
# # aux2 = 0
# # for i in range(len(valores)):
# #     if 3 not in valores[:]:
# #         print('Não foi encontrado')
# #     else:
# #         aux = valores.index(valores[aux2])
# #         print(aux)
# #         break;
# #     aux2 += 1

