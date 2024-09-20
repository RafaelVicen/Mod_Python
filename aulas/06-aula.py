#Havera situacoes que eu terei que separar uma string em varias partes, como em caso se eu quiser separar uma frase em palavras.
# Usamos o

frase = 'Ola, bem-vindo a este treinamento'
print("----------------------------------------------\n")
print(frase.split( ))# Quando uso o metodo split ele por padrao, vai encontrar todos os pacosdentro de uma string e vai separar isso em uma lista.
print(frase.split(',')) #Aqui a todo moment que ele encontrar uma virgula, ele vai separar aquela frase, 'Ola, bem', 'vindo a este treinamento'
print(frase.split('-'))# Aqui ele vai encontrar o caracter de traço (-) e vai separar o  (bem-vindo) ficando 'Ola, bem', 'vindo a este treinamento'

print("----------------------------------------------\n")
nome = 'Flavio, Rafael, Carol, Amanda,Guterres'
print(nome.split())#aqui ele busca os espacos em brancos e separa as informacoes, lembrando que o separador espacos nao eh um separador de virgulas
print(nome.split(','))#aqui ele separa todas as ocorrencias com virgulas


print("----------------------------------------------\n")
hashtags = '#music #guitarra #viola #python #codar'
print(hashtags.split())# aqui ele separa onde encontra os espacos em brancos
print(hashtags.split('#'))# Aqui se eu colocar a hashtag  paramentro, ele separa cada uma delas, em um item diferente
print(hashtags.split('#',3))# Caso eu queria parametizar, para que ele faz a separacao ate um certo ponto e depois pare, eu posso passar um segundo parametro para 
# a nossa funcao split que eh o separador que ele vai estar utilizando, nesse caso a hashtag e quantas ocorrencias ele deve procurar antes de parar, nesse caso foram 3.


print("------------------------------------------\n")
# Como concatenar(combinar) string, por exemplo uma virgula ou ponto ou simplesmente um espaco
hashtags_separados_por_espacos = hashtags.split(' ')# aqui usamos o metodo split para separar as hashtag usando espacos
print(hashtags_separados_por_espacos)# Aqui imprimimos na tela 
print(','.join(hashtags_separados_por_espacos))#aqui imprimimos na tela todos os intem que estavam separados em uma lista, colocou eles em uma string unica e
#separou cada um deles com a virgula
print('.'.join(hashtags_separados_por_espacos))#aqui podemos colocar ponto
print(' '.join(hashtags_separados_por_espacos))# e aqui se nos quiser podems colocar um espaco
print("-------------------------------------------------\n")