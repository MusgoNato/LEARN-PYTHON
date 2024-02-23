# Função Aumenta o valor da moeda
def aumentar(num, aumento=0):
    total = num + ((aumento/100) * num)
    return total

# Função Diminui o valor da moeda
def diminui(num, diminuir=0):
    total = num - ((diminuir/100) * num)
    return total

# Função Dobro
def dobro(num):
    return num * 2

# Função Metade
def metade(num):
    return num/2
