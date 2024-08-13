# # Importação das bibliotecas
# import pandas as pd

# # Variavel para armazenar tabela (A tabela nao deve estar aberta no excel, caso contrario havera negacao na hora da abertura)
# tabela =  pd.read_excel("TABELA DE VALORES.xlsx")

# # Exclui a 1° linha da tabela
# tabela = tabela.drop(tabela.columns[0], axis=1)

# # Exclui a 1° coluna da tabela (O iloc da-se o intervalo de linha a coluna, no caso 1° linha ate a ultima coluna existente, isso tudo é selecionado)
# tabela = tabela.iloc[1:, :]

# # Salva as modificações no arquivo original
# tabela = tabela.to_excel('TABELA DE VALORES.xlsx', index=False)
# print(tabela)

#Importação e criação da Tabela
import pandas as pd
tabela = pd.read_excel('PCA_2025_v1.xlsx')
Col_proc_ref = tabela["Proc_Ref"]

#Criacao de uma lista de dicionarios
lista_dicionarios = []

#Percorrer a coluna da tabela
for string in Col_proc_ref:

    #Retorna uma string de acordo com o delimitador passado
    lista = string.split('/')

    #Caso tenha 2 arumentos a lista, ocorreu bem o split
    if len(lista) == 2:

        #Dicionario temporario criado
        referencias = {"id": int(lista[0]), "ano": int(lista[1])}

        #Adição do dicionario referencias dentro da lista de dicionarios
        lista_dicionarios.append(referencias)
        
print(lista_dicionarios)
