# # Função Aumenta o valor da moeda
# def aumentar(num, aumento=0):
#     total = num + ((aumento/100) * num)
#     return total

# # Função Diminui o valor da moeda
# def diminui(num, diminuir=0):
#     total = num - ((diminuir/100) * num)
#     return total

# # Função Dobro
# def dobro(num):
#     return num * 2

# # Função Metade
# def metade(num):
#     return num/2

# # Função adicional chamada moeda (mostra o valor formatado)
# def moeda(num):
#     num = str(num)
#     num = num.replace('.', ',')
#     return num

# # # Outro jeito de fazer a mesma função, porem com um retorno formatado
# # def moeda(num=0, aux='R$'): # Caso nao haja valor adicionado pelo usuario, o valor padrao ja e declarado no inicio
# #     return f'{num}{aux:2.f}'.replace(',''.') # Como é uma string formatada o retorno, é possivel chamar o metodo replace sem precisar criar uma string em si.
#                                                 # a cada . que aparece na string formatada que retorna, esta é trocada por uma virgula, em todos os pontos que aparecerem, caso deseje somente uma vez, é necessario especificar 1 no 3º parametro de replace
# # Com essa função ja nao e necessario no programa principal colocar antes das chamadas o caractere 'R$', pois a função faz isso.
