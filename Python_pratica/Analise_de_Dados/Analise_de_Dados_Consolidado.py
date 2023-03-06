# Análise de dados conslidado

# Importando as bibliotecas
import pandas as pd

# Carregando dados da planilha consolidado
df = pd.read_excel('report-consolidado.xlsx')

# Visualizando as primeiras linhas do meu dataframe
print(df.head())
# Visualizando as últimas linhas do meu dataframe
print(df.tail())

# Verificando o tipo de dados do dataframe
print(df.info())

print()

# Listando os nomes das colunas
print(df.columns)

print()

for coluna in df.columns:
    print(coluna)

print()

# Verificando a quantidade de linhas e colunas do dataframe
print(df.shape)