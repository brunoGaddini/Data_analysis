import os

print(os.getcwd())

os.chdir(r"C:\Users\Bruno\Downloads")
print(os.getcwd())
print(os.listdir())

print([arquivo for arquivo in os.listdir()]) # Comprehension para listar os arquivos em Downloads

print()

lista_arquivos = [arquivo.lower() for arquivo in os.listdir() if os.path.isfile(arquivo )]
print(lista_arquivos)

lista_split_exemplo = '201 - Visão Geral da Ferramenta.mp4'.split(".")[-1] # O objetivo aqui é pegar a extensão do arquivo
print(lista_split_exemplo)

lista_tipos_split = set([tipo.split(".")[-1] for tipo in lista_arquivos]) # A função set remove os elementos repetidos da lista
print(lista_tipos_split)
print(type(lista_tipos_split))
lista_tipos = {tipo.split(".")[-1] for tipo in lista_arquivos} #Agrupamento sem repetição mesma função do que na variável acima lista_tipos_split
print(lista_tipos)

print()

for tipo in lista_tipos:
    print(tipo)

print(print(os.getcwd()))

for tipo in lista_tipos:
    if os.path.exists(tipo): # Condição para evitar erro se determinada pasta já existir
        pass
    else:
        os.mkdir(tipo)

for arquivo in lista_arquivos:
    pasta_destino = arquivo.split(".")[-1]
    de = os.path.join(os.getcwd(), arquivo) # Definindo endereço para criação da pasta arquivo e juntar com o nome da extensão
    para = os.path.join(os.getcwd(), pasta_destino, arquivo)
    if os.path.exists(de):
        os.replace(de, para)