# Função Aumenta o valor da moeda
def aumentar(num, aumento=0, show=0):
    total = num + ((aumento/100) * num)
    if show == True:
        return moeda(total)
    else:
        return total

# Função Diminui o valor da moeda
def diminui(num, diminuir=0, show=0):
    total = num - ((diminuir/100) * num)
    if show == True:
        return moeda(num)
    else:
        return total

# Função Dobro
def dobro(num, show=0):
    num = num * 2
    if show == True:
        return moeda(num)
    else:
        return num

# Função Metade
def metade(num, show=0):
    num = num/2
    if show == True:
        return moeda(num)
    else:
        return num

# Função adicional chamada moeda (mostra o valor formatado)
def moeda(num): # Show sera a variavel opcional para mostrar ou nao o valor formatado na tela
    num = str(num)
    num = num.replace('.', ',')
    return num
