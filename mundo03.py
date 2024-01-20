#Referente a aula 16 (Variaveis compostas : Tuplas, listas e dicionários)
#As tuplas sao imutaveis, nao é possivel fazer a mudança de algum valor armazenado dentro da tupla, ela ficara assim ate o final do programa
#Durante a execução nao tem como mudar a tupla, só se parar trocar os valores e reiniciar o programa

# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita') #Mesmo sem colocar parenteses o python considera como tupla
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
# numeros = ('zero', 'um', 'dois', 'tres', 'quatro',
#            'cinco', 'seis', 'sete', 'oito', 'nove',
#             'dez', 'onze', 'doze', 'treze', 'catorze',
#             'quinze', 'dezesseis', 'dezessete',
#             'dezoito', 'dezenove', 'vinte')

# n = int(input('Insira um numero : '))
# while True:
#     #if 0 <= n <= 20 #Da pra fazer desse jeito tambem a lógica do or pra intervalos de um numero a outro
#     if n < 0 or n > 20:
#         n = int(input('Número fora do intervalo de 0 a 20. Insira um número: '))
#     else:
#         cont = numeros.index(numeros[n])
#         print(f'{numeros[cont].upper()}') #Dá de eu fazer isso pois estou escrevendo uma string, na inicialização não é possível
#         op = str(input('Quer continuar? [S/N]')).strip().upper()[0]
#         if op =='N':
#             break;
#         else:
#             n = int(input('Insira um numero : '))


#73° desafio (Tupla com 20 primeiros colocados da tabela do campeonato brasileiro, mostrar 5 primeiros colocados,
#os ultimos 4 colocados, uma lista com times em ordem alfabética e em que posicao da tabela esta o time da chapecoense)
# times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Red Bull Bragantino',
#           'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo',
#             'Cuibá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
# print(f'Primeiros 5 colocados : {times[0:5]}') #Primeiros 5 times
# print(f'Últimos 4 colocados : {times[20:15:-1]}') #Ultimos 4 colocados
# print(f'Times em ordem alfabética : {sorted(times)}') #Ordem alfabética
# for i, cont in enumerate(times): #É necessário o cont pra ser uma variavel composta pra enumeração do times
#     if 'Chapecoense' in times[i]:
#         print(f'Chapecoense está na posição {i + 1}')

#74° desafio (Gerar cinco numeros aleatorios e colocar em uma tupla, depois mostrar a listagem de numeros, indicando o maior e o menor valor lidos)
# from random import randint
# numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10) #Como uma tupla nao da pra inserir valores, pois sao imutaveis, a nao ser de ela ser deletada, porem consigo em cada posição da tupla, gerar um numero aleatório, é o que o programa realiza nessa linha

# #print(numeros[:]) #Dá pra fazer desse jeito sem repetição nenhuma
# for i, cont in enumerate(numeros):
#     print(f'{numeros[i]}',end=' ')
# # for i in numeros: #Dá pra fazer dess outro jeito, que é mais facil ainda
# #     print(f'{n}', end=' ')
# menor = min(numeros)
# maior = max(numeros) #Max é 'Específico' das tuplas, funciona em outros lugares mas é especifico delas
# print(f'\nMaior {maior} e menor {menor}')

#75° desafio (Ler 4 valores do teclado e guardar na tupla, saber quantas vezes o valor nove apareceu, em que posicao o 3 ta, quais foram os numeros pares)
# num1 = int(input('Digite um numero : '))
# num2 = int(input('Digite outro numero : '))
# num3 = int(input('Digite mais um numero : '))
# num4 = int(input('Digite o último numero : '))
# #Dá pra fazer desse jeito abaixo, sem necessidade de criar varias variaveis
# # num = (int(input('Insira um numero : ')), int(input('Insira um numero : ')),
# #    int(input('Insira um numero : ')), int(input('Insira um numero : ')), )

# valores = (num1, num2, num3, num4)
# cont = valores.count(9)
# print(f'Você digitou os valores : {valores}')
# print(f'Foram {cont} vezes que o 9 apareceu')
# aux2 = 0
# for i in range(len(valores)):
#     if valores[i] % 2 == 0:
#         print(f'Numero par : {valores[i]}')
#     else:
#         if valores[i] == 3:
#             aux = valores.index(valores[i])
#             print(f'Posição do numero 3 é : {aux + 1}')
#         if 3 not in valores[:]: #Por algum acaso, quando coloco alguma lógica como o not, nao posso procurar o numero com algun indice dentro da tupla, ele me da erro quando coloco alguma logica na condição
#             print('\nO 3 Não foi encontrado')
#             break;

#76° desafio (Fazer uma listagem de preço utilizando apenas uma tupla)
# tupla = ('Banana', 10.0, 'Pão', 1.50, 'Refrigerante', 3.50, 'Amoeba', 1.50, 'Caneta', 1.0, 'Celular', 120)
# print(50*'=')
# string = 'TABELA DE PREÇOS'
# print(f'{string:^50}') #Centralizado em 50 espaços
# print(50*'=')
# for i in range(len(tupla)):
#     if i % 2 == 0:
#         print(f'{tupla[i]:.<40}', end='') #Alinhado a esquerda com 40 espaços
#     else:
#         print(f'R$  {tupla[i]:>6.2f}') #essa é uma formatação alinhada a direita em 6 espaços, depois é formatada a saída para float com 2 casas decimais usando 2.f
# print(50*'=')

#77° desafio (Tupla com varias palavras, mostra qual sao as vogais)
# tupla = ('mercado', 'arroz', 'pao', 'agua', 'banana')
# string = ''
# for i in range(len(tupla)):
#     string = tupla[i] #Cada posição da tupla é uma palavra, criei uma variavel pra receber cada palavra dessa
#     print(f'\nAs vogais da palavra {string.upper()} são : ', end=' ')
#     for j in range(len(string)): #De acordo com a palavra dentro da variavel string, varro toda ela e verifico ocorrência de vogais
#         if string[j] == 'a' or string[j] == 'e' or string[j] == 'i' or string[j] == 'o' or string[j] == 'u': #Verificação das vogais
#         #if string[j] in 'aeiou' #A mesma verficação feita de forma simples
#             print(f'{string[j]}', end=' ') #Caso haja mostro na tela
# print('\n')

#Referente a aula 17
# lanche.append('Coisa aqui') #Adiciona o elemento no parâmetro á lista
# lanche.insert(0, 'Outra coisa') #Ele adiciona o parametro na posição 0 e 'empurra' os outros elementos para frente
# del lanche[3] #Elimina o que esta na posição 3
# lanche.pop(3) #normalmente usado pra remover o ultimo elemento, mas é possível passar o indice de quem quer deseja eliminar
# lanche.remove('Coisa aqui') #elimina o elemento e reposiciona a contagem dos indices
# lanche.pop() #Elimina o ultimo elemento sem passar nenhum parâmetro
# #Caso tente remover algum elemento que nao esta na lista, ocorrera um erro na linguagem
# if 'Coisa' in lanche: #verificação se algo esta na lista para remove-lo
# lanche.remove('Coisa')
# #Criação de listas atraves de range
# valores = list(range(4, 11)) #cria uma lista de 4 ate 10 usando o range, podendo eu passar os parametros, posso colocar um 3 elemento que pula de 2 em dois ou 3 em tres
# valores = [8,2,5,4,9,3,0]
# valores.sort() #Vai ordenar os elementos da lista
# valores.sort(reverse=True) #Aqui ocorre a ordenação na ordem reversa da lista
# len(valores) #Retorna o tamanho da lista

#Tupla
# num = (2,7,9,1)
# print(num)
# # num[2] = 3 #Erro pois é uma tupla
# num = [2,7,9,1]
# num[2] = 3 #Aqui não ocorre erro pois a lista é mutavel
# num = [2,5,9,1]
# num.append(4) #Adiciona valores
# num.sort(reverse=True) #Ordena na ordem inversa a lista
# num.append(2, 0) #Insere o 0 na posição 2
# num.pop(2) #Ele remove o que esta no indice 0 da lista
# num.remove(2) #Ele remove o valor passado, caso haja valores iguais, ele remove apenas o primeiro que aparecer com base no parâmetro

#Lista mais bonita
# valores = list()
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for i in range(0, 5):
#     # n = int(input('Insira um valor : '))
#     # valores.append(n)
#     valores.append(int(input('Insira um valor : '))) #Dá pra fazer diretamente desse jeito
# for c, v in enumerate(valores):
#     print(f'Posição {c}, valor é {v}')

# a = [1,2,3,4]
# b = a #Ligação entre listas
#Caso eu coloque algum valor dentro de 'b', a lista 'a' sofrera com a inserção de 'b', pois o python cria uma ligação entre ela

#Pra fazer uma cópia de uma lista para outra e não uma ligação
# a = [1,2,3,4,5]
# b = a[:] #Aqui a leitura seria, 'b' recebe todos os itens de 'a', ou seja todos os valores são jogados em 'b', umma cópia perfeita da lista 'a'
# b[2] = 8 #Aqui sim a lista 'b' ela muda e a lista 'a' continua com os valores iniciais
# # É como as estruturas em C, caso um ponteiro aponte a elas, há mudança na estrutura como um todo, caso nao haja um ponteiro pra apontar para os elementos é criado uma cópia perfeita da estrutura original

#78° desafio (Ler 5 valores numericos, mostrar o maior e menor valor com suas respectivas posições considerando caso haja valores iguais)
# valores = []
# aux = []
# aux2 = []
# cont = 0
# while cont != 5:
#     valores.append(int(input('Insira um valor :  ')))
#     cont += 1
# for i, cont in enumerate(valores):
#     menor = min(valores)
#     maior = max(valores)
#     if menor == valores[i]:
#         aux.append(i)
#     if maior == valores[i]:
#         aux2.append(i)
# print(f'O valor maior da lista é {maior} na respectiva posição : {aux2[:]}')
# print(f'O valor menor da lista é {menor} na respectiva posição : {aux[:]}')

#79° desafio (Digitar varios valores numéricos, caso o numero ja exista la dentro, ele nao será adicionado, exibir os valores unicos digitados em ordem crescente)
# lista = []
# cont = 0
# i = 0
# while True:
#     lista.append(int(input('Insira um número : ')))
#     if i >= 1: #A partir do 2° valor faz a verificação na lista
#         aux = lista[i]
#         for i in range(len(lista) - 1): #Esse for ele vai ate o antipenultimo numero, tipo de 0 a 10, ele iria ate 9, onde esse seria o ultimo numero que eu digitei, subtraindo -1, chego no antipenultimo, assim eu nao vou ate o ultimo numero adicionado, vou ate um a menos que ele, pois caso fosse ao contrario o segundo valor adicionado nunca iria entrar na lista
#             if aux == lista[i]:
#                 print('Valor duplicado')
#                 lista.remove(aux)
#                 break;
#     op = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
#     while 'N' != op != 'S': #loop infinito até o usuario digitar corretamene (Tratamento de erros)
#         op = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
#     if op == 'N':
#         break;
#     i += 1
# lista.sort() #Ordena a lista
# print(f'Você digitou os valores {lista}')
# # print(f'Você digitou os valores {lista.sort()}') #Caso eu mande imprimir desse jeito, me retornara  NONE, isso ocorre devido a impressao, o retorno desse metodo é o NONE, porem ele modifica a lista e a ordena, mas para aparecer na tela tem que fazer isso antes

# 80 desafio (Guardar 5 numeros em uma lista e já na posição correta, sem usar o sort, no final mostrar ela ordenada)
# # lista = []
# # i = 0
# # while i < 5:
# #     lista.append(int(input('Insira um numero : ')))
# #     index_maior = lista.index(max(lista)) #Pega o maior valor e sua respectiva posição dentro da lista
# #     print(index_maior)
# #     for j in range(1, len(lista)):
# #         if lista[j] > lista[i]:
# #             aux = lista[j]
# #             lista[j] = lista[i]
# #             lista[i] = aux
# #     i += 1
# # print(f'\nLista ordenada : {lista}')

# 81 desafio (Varios numeros digitados, mostrar quantos foram, a lista ordenada de forma decrescente, se o valor 5 esta ou nao na lista)
# valores = []
# contagem = 0
# while True:
#     valores.append(int(input('Insira um numero : ')))
#     contagem += 1
#     op = str(input('Quer contiuar ? [S/N] ')).strip().upper()[0]
#     while 'S' != op != 'N':
#         op = str(input('Quer contiuar ? [S/N] ')).strip().upper()[0]
#     if op == 'N':
#         break;
# if 5 in valores:
#     print('5 está na lista')
# else:
#     print('5 não esta na lista')
# valores.sort(reverse=True)
# print(f'Lista ordenada de forma decrescente {valores}')

# 82 desafio (Ler valores, colocar na 2 lista so pares e lista 3 so impares)
# valores = []
# pares = valores[:] #Cópia
# impares = valores[:]
# i = 0
# while True:
#     valores.append(int(input('insira um valor : ')))
#     op = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
#     while 'S' != op != 'N':
#         op = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
#     if op == 'N':
#         break;
#     if valores[i] % 2 == 0:
#         pares.append(valores[i])
#     else:
#         impares.append(valores[i]) 
#     i += 1
# print(f'Lista completa : {valores}')
# print(f'Lista dos Pares : {pares}')
# print(f'Lista dos Ímpares : {impares}')

# 83° desafio (Ler uma expressao e verificar se ela fecha os parenteses corretamente)
exp = [] #expressao do usuario
i = 0
j = 0
del_posi_parentes_abre = 0
del_posi_parentes_fecha = 0
exp.extend(input('Insira a expressão : ')) # O extend separa, ou seja cada elemento dentro é separado em poisiçoes, o append insere o que for dado no final da lista, o extend ele já insere na lista nas posições adequadas e nao no final
for i in range(len(exp)):
    if exp[i] == '(' or exp[i] == ')':
        del_posi_parentes_abre = exp.index(exp[i]) #recebe o indice da abertura de parenteses
        #Tem que achar o fechamento agora, dai deletar o indice que abre e depois o que fecha
        if exp[j] == ')': #Nao ta entrando aqui, tem que achar um jeito de entrar e deletar os elementos de abrir e fechar os parenteses nas suas respectivas condições
            print('asd')
            exp.pop(del_posi_parentes_abre) #Da um pop na abertura
            exp.pop(j) #Da um pop no fechamento
print(exp)

#O index ele pega somente a primeira ocorrencia, a logica ta errada pq toda vez pega somente o 1° parenteses que ta na 0° posição
        