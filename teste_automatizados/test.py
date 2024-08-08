# Importação das bibliotecas
import pandas as pd

# Variavel para armazenar tabela (A tabela nao deve estar aberta no excel, caso contrario havera negacao na hora da abertura)
tabela =  pd.read_excel("TABELA DE VALORES.xlsx")

# Exclui a 1° linha da tabela
tabela = tabela.drop(tabela.columns[0], axis=1)

# Exclui a 1° coluna da tabela (O iloc da-se o intervalo de linha a coluna, no caso 1° linha ate a ultima coluna existente, isso tudo é selecionado)
tabela = tabela.iloc[1:, :]

# Salva as modificações no arquivo original
tabela = tabela.to_excel('TABELA DE VALORES.xlsx', index=False)
print(tabela)