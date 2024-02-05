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
# # Pra nao ficar aparecendo esses colchetes eu poderia criar um for usando o enumerate e verificar o menor e maior valor dentro doo for e mandar imprimir na tela as posições
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

# 80° desafio (Guardar 5 numeros em uma lista e já na posição correta, sem usar o sort, no final mostrar ela ordenada)
# lista = []
# i = 0
# while i < 5:
#     n = int(input('Insira um numero : ')) #Não pode ser apppend pois na volta do loop nao sei qual o valor é o correto para o final da lista
#     #Caso for o primeiro ou ultimo valor entao o append deve ser usado, pois ele adiciona ao final da lista, caso exista um valor ou doi funcionará corretamente
#     if i == 0 or n > lista[len(lista) - 1]: #Se o numero que foi inserido pelo usuário for maior que o ultimo elemento que já esta na lista entao ele é adicionado ao final da lista usando o append tambem
#         lista.append(n)
#         print('Valor adicionado no final da lista')
#     else: #Se nao for o 1° nem o ultimo valor, então está entre os valores digitados 
#         entre = 0 #Guarda o valor que sera inserido na posição especifica entre 2 valores, ele deve começar com 0 pois toda vez terá que verificar toda a lista desde a 1° posição ate a ultima
#         while entre < len(lista):
#             if n <= lista[entre]: #Insere somente uma vez e sai do loop para depois recomeçar e varrer a lista de novo porem com outro valor
#                 lista.insert(entre, n) #Insere na posição 'entre' o numero menor que o valor que esta na posição lista[entre]
#                 print(f'Valor inserido na posição {entre}')
#                 break;
#             entre += 1 #Vai incrementando os valores até chegar no final da lista
#     i += 1
# print(f'Lista ordenada {lista}')

# 81° desafio (Varios numeros digitados, mostrar quantos foram, a lista ordenada de forma decrescente, se o valor 5 esta ou nao na lista)
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
#     print('5 não está na lista')
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
#Tem que lembrar que o programa nao vai empilhar o ')', ele só empilha o parenteses de fechamento caso a expressão esta errada
# pilha = [] #Lista auxiliar pra armazenar os parenteses (A pilha já começa com 0 por causa que ela esta vazia)
# expressao = str(input('Insira a expressão : ')) #Expressão do usuário, que ao ser percorrido pelo for é uma lista praticamente
# print(len(pilha))
# for simbolo in expressao:  
#     if simbolo == '(': # '( )' PILHA - > ['('] -> tamanho é igual a 1
#         pilha.append('(') #Após ser inserido um caractere na pilha como o '(', o tamanho da piha passa a ser 1
#     elif simbolo == ')': 
#         if len(pilha) > 0: #Caso o caractere seja um ')', e a pilha nao esta vazia, é desempilhado o parenteses de abertura que esta contido na pilha
#             pilha.pop() #Retira o '(' da pilha e o tamanho passa a ser 0
#         else:
#             pilha.append(')') #Caso a pilha for menor ou igual a 0, significa que a expressão esta errada, é inserido o ')' para forçar o tamanho da pilha em 1 e na verificação mostrar errada a expressao, pois seu tamanho mudou
#             break;
# # Após todo o 'for', a pilha fica vazia de acordo com o ex "( )"
# if len(pilha) == 0: #A expressao só será valida caso o tamanho seja 0, pois ele desempilha a cada par encontrado
#     print('Expressão Matematica correta!')
# else:
#     print('Expressão matemática errada!')

#Referente a aula 17 Parte 2
# teste = list()
# dados = list()
# # Aqui são adicionados na lista as informações
# dados.append('Jõazin')
# dados.append(13)
# # Aqui são colocadas as informações da lista 'dados' dentro da lista 'teste'
# # teste.append(dados) # É feita a ligação entre as duas listas, porem as duas listas receberão o mesmo valor e as mesmas alterações tambem
# print(teste[0][1]) # Me mostra a idade pois dentro da lista a posição 1 é '13'
# teste.append(dados[:]) # Faz-se uma cópia de todos os elementos de 'dados', para que não haja ligação nenhuma e eu possa mexer nos valores fazendo as devidadas alterações
# dados.clear() # Esse método limpa toda a lista, porem como nao foi feita nenhuma ligação entre as listas, somente a cópia, o que esta em teste permanecerá intacto
# print(teste, dados) 

# galera = []
# pessoas = []

# for c in range(0, 4):
#     pessoas.append(str(input('Insira seu nome: ')).strip())
#     pessoas.append(int(input('Insira sua idade : ')))
#     galera.append(pessoas[:]) # Faz-se uma cópia e joga todas as informações da lista pessoas em galera
#     pessoas.clear() # Limpa os dados de pessoas a cada iteração
# print(galera)
# print(pessoas) # Caso imprima na tela será uma lista vazia. pois a cada iteração eu apago o que está em pessoas, porem como foi feita uma cópia dela a galera, o que esta em galera permanece, já que nao foi feita nenhuma ligação entre elas

# 84° desafio (Nome e peso de várias pessoas, mostrar quantas pessoas foram cadastradas, listagem com as pessoas mais gordas e listagem com as pessoas mais leves)
# pessoas = []
# dados = []
# cont_pessoas = 0
# pessoa_gorda = pessoa_magra = 0
# nome_pessoa_gorda = nome_pessoa_magra = ''
# while True:
#     dados.append(str(input('Insira seu nome : ')).strip())
#     dados.append(float(input('Insira seu peso : ')))
#     if pessoa_gorda < dados[1] or cont_pessoas == 0: # Verificação   para encontrar o maior peso e o respectivo nome
#         pessoa_gorda = dados[1]
#         nome_pessoa_gorda = dados[0]
#     if pessoa_magra > dados[1] or cont_pessoas == 0: # Verificação para encontrar o menor peso e o respectivo nome
#         pessoa_magra = dados[1]
#         nome_pessoa_magra = dados[0]
#     pessoas.append(dados[:]) # Fazendo isso eu estou criando uma ligação entre as listas, deveria ser pessoas.append(dados[:])
#     dados.clear()
#     cont_pessoas += 1 # Quantidade de pessoas
#     op = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
#     while 'S' != op != 'N':
#         op = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
#     if op == 'N':
#         break;
# # Ao invés de um contador de pessoas, de forma simples se coloca o tamanho da lista principal
# # print(f'Ao todo você cadastrou {len(pessoas)} pessoas!')
# print(f'Ao todo você cadastrou {cont_pessoas} pessoas!')
# print(f'O maior peso foi de {pessoa_gorda}Kg.', end=' ')
# print(f'Pertence o maior peso a {nome_pessoa_gorda}',end='')
# for p in pessoas:
#     if p[1] == pessoa_gorda:
#         print(f'{p[0]}', end=' ')
# print(f'\nO menor peso foi de {pessoa_magra}kg.', end=' ') 
# print(f'Pertence a {nome_pessoa_magra} o menor peso!',end=' ')
# for p in pessoas:
#     if p[1] == pessoa_magra:
#         print(f'{p[0]}', end=' ') # Esse trecho já mostra uma lista ao inves de 1 variavel só

# 85° desafio (Sete valores numéricos, cadastrar em uma unica lista, nela existem duas listas, uma de pares e outra de impares, colocar em ordem crescente no final)
# lista_par = []
# lista_impar = []
# par = impar = 0
# lista = [] # Lista principal
# lista.append(lista_par)
# lista.append(lista_impar)
# for i in range(0, 6):
#     num = int(input(f'Insira o {i + 1}° numero : '))
#     if num % 2 == 0:
#         lista_par.append(num)
#     else:
#         lista_impar.append(num)
# lista_par.sort()
# lista_impar.sort()
# print(f'Lista de pares : {lista[0]}')
# print(f'Lista de ímpares : {lista[1]}')

# Esse é o jeito certo do desafio
# lista = [[], []]
# valor = 0
# # Faz a junção do que é par ou impar nas sublistas dentro da lista principal
# for i in range(1, 8):
#     valor = int(input(f'Insira o {i} numero : '))
#     if valor % 2 == 0:
#         lista[0].append(valor)
#     else:
#         lista[1].append(valor)
# # Ordena os valores
# lista[0].sort()
# lista[1].sort()
# print(f'Valores pares são : {lista[0]}')
# print(f'Valores ímpares são : {lista[1]}')

# 86° desafio (Criar matriz de dimensao 3X3 e preencha os valores lidos do teclado, depois mostrar a matriz na formatação correta)
# lista = []
# for i in range(0, 3):
#     for j in range(0, 3):
#         lista.append(int(input(f'Digite um valor para [{i, j}] : ')))

# # Lembrando que vai de 0 a 8, a fórmula nos colchetes é pra mapear os indices i e j para o valor correto, é uma maneira simplificada disso : lista[i][j]
# for i in range(0, 3):
#     for j in range(0, 3):
#         print(f'{lista[i * 3 + j]}', end=' ')
#     print('\n', end='')

# Outro maneira de fazer
# lista = []
# for i in range(0, 3):
#     lin = []
#     for j in range(0, 3):
#         num = int(input(f'Insira um valor {[i, j]} : '))
#         lin.append(num) # A lista de linhas vai dando um append ate chegar no final, que posteriormente essa lista vai ser apagada, mas os valores vao ser armazenados em lista 
#     lista.append(lin) # A lista lin que contem os valores lidos é colocada na lista de nome 'lista', assim tenho uma lista dentro de outra lista, por consequencia, cada mini lista são as linhas da matriz
# for cont_sublista in lista:
#     print(cont_sublista) # Ele vai imprimir cada parte de lin, ou seja cada lista dela colocada em lista, como o \n ja é incluso no print, nao é necessário fazer do jeito anterior apagando espaço vazio

# Mais um jeito de fazer, de acordo com o curso em video
# matriz = [[0,0,0], [0,0,0], [0,0,0]]
# for l in range(0,3):
#     for c in range(0,3):
#         matriz[l][c] = int(input(f'Digite um valor para {[l,c]} : '))
# for l in range(0,3):
#     for c in range(0,3):
#         print(f'[{matriz[l][c]:^5}]', end=' ') # Isso ele vai centralizar caso o usuario digite numeros com muitos digitos
#     print()

# 87° desafio (Mostrar a soma de todos os valores pares digitados, soma dos valores da 3 coluna e o maior valor da segunda linha)
# lista = []
# # [[1,2,3], [4,5,6], [7,8,9]]
# soma = soma_col_3 = soma_lin_2 = 0
# for i in range(0, 3):
#     lin = []
#     for j in range(0, 3):
#         num = int(input(f'Insira um valor {[i, j]} : '))
#         if num % 2 == 0:
#             soma += num
#         if j == 2:
#             soma_col_3 += num
#         if i == 1:
#             soma_lin_2 += num
#         lin.append(num) # Cada numero é adicionado em lin, que servirá posteriormente para imprimir a matriz de um jeito mais fácil
#     lista.append(lin) # A cada iteração os 3 elementos de lin que é uma lista é adicionado na lista principal
# for cont_sublista in lista:
#     print(cont_sublista)
# print(f'A soma dos valores pares : {soma}')
# print(f'A soma dos valores da 3 coluna é : {soma_col_3}')
# print(f'A soma dos valores da 2 linha é : {soma_lin_2}')

# 88° desafio (Jogo da megasena, programa pergunta quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo cadastrando em uma lista composta)
# from random import randint
# from time import sleep
# i = 0
# str = 'MEGA SENA'
# lista = []
# num = int(input('Quantos jogos serao gerados? ')) # numero de jogos
# while i < num:
#     jogo = []
#     for j in range(0, 6):
#         num_gerado = randint(1, 60)
#         jogo.append(num_gerado)
#     lista.append(jogo) # É atribuido a 'lista', lista 'jogo', onde é gerado o 1° jogo
#     i += 1
# print(f'{str:^30}') # Centralizando a string
# for c, cont_sublistas in enumerate(lista):
#     print(f'{c + 1}° Jogo : {cont_sublistas}')
#     sleep(1)
# print('BOA SORTE')

# 89° desafio (Nome e duas notas guardadas em listas, mostrar o boletim da media de cada um, permitir o usuario mostrar as notas de cada aluno individualmente)
# [[nome, [nota1, nota2]], [nome2, [nota1, nota2]]] -> ideia principal
# from time import sleep
# lista = []
# media = 0
# i = 0
# while True:
#     # Preciso esvaziar as listas pois a cada iteração, elas nao devem guardar o valor passado, pois o append coloca no final da lista o valor passado, guardando o que foi colocado antes, informações como notas ou nomes dos alunos serao colocados apenas em uma lista e nao separados individualmente em sublistas
#     alunos = []
#     notas = []
#     alunos.append(str(input('Insira o nome : ')).strip())
#     notas.append(int(input('Insira nota 1 : ')))
#     notas.append(int(input('Insira nota 2 : ')))
#     alunos.append(notas)
#     # Faço a media, nesse caso como sao apenas 2 notas o jeito mais facil que encontrei foi esse, em caso de muitas notas ja seria necessario um loop
#     media = (notas[0] + notas[1])/2
#     alunos.append(media)
#     lista.append(alunos)
#     op = str(input('Deseja continuar: ')).strip().upper()[0]
#     while 'S' != op != 'N':
#         op = str(input('Deseja continuar: ')).strip().upper()[0]
#     if op == 'N':
#         break;

# #               0
# # [[nome, [nota1, nota2], media]]
# #   0           1           2


# # Considerando apenas o 1 nome, pois o nome completo a identação não sairá correta
# #print('N     Nomes      Média')
# print(f'{"No.":<4}{"Nome":^13}{"Média":>6}') # Dá pra fazer desse jeito tambem, mais facil e pratico
# for cont_sublista, alunos in enumerate(lista):
#     print(f'{cont_sublista:<4}{lista[cont_sublista][0]:^13}{lista[cont_sublista][2]:>6}') # Formatado na mão mesmo

# while True:
#     option = int(input('Insira qual nota gostaria de ver (999 interrompe) : '))
#     while option < 0 or option >= len(lista) and option != 999: # Verificação para erros do usuário
#         option = int(input('Insira qual nota gostaria de ver (999 interrompe) : '))
#     if option == 999:
#         break;
#     print(f'Notas de aluno {lista[option][0]} são : {lista[option][1]}')
# print('FINALIZANDO....') 
# sleep(1)
# print('VOLTE SEMPRE!')