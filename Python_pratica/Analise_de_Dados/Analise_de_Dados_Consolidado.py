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
# Acessando colunas individualmente
print(df['Segmento'])

# >> Alterando o nome das colunas
colunas = ['Segmento', 'País', 'Produto', 'Qtde de Unidades Vendidas',
       'Preço Unitário', 'Valor Total', 'Desconto', 'Valor Total c/ Desconto',
       'Custo Total', 'Lucro', 'Data', 'Mês', 'Ano']

print()

# >>> Mudando o nome das colunas para letras minusculas
for nome in range(len(colunas)):
    colunas[nome] = colunas[nome].lower()
    #print(colunas)

print(colunas)

print()

colunas_final = ['segmento', 'país', 'produto', 'unidades vendidas', 'preço unitário', 'valor total', 'desconto', 'valor total c/ desconto', 'custo total', 'lucro', 'data', 'mês', 'ano']
df.columns = colunas_final
print(df.columns)