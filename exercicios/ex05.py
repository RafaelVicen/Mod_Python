#Desafio
# Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variavel chamada palavras1
"""
Desafio 2: Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variavel chamada palavras2

"""
# para resolver esse desafio, primeiro temos que lembrar que lista, eh a forma de armazenar varias informacoes em um lugar so.
frase1 = 'Desafio manipulacao de strings'
frase2 = 'jhonatan,rafael,carol,camilla'

#### Solucao ###
# Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variavel chamada palavras1
palavras1 = frase1.split()# aqui, transformamos a frase1 em uma lista de string, com o split recebendo o metodo vazio

#Desafio 2: Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variavel chamada palavras2
palavras2 = frase2.split(',')# aqui estamos a fazer o mesmo processo, so que o split recebeu o metodo com  virgulas ao invez do vazio
#vamos estar separar por virgulas ao inves de espacos vazios.

#Desafio 3: pegue o palavras1 e transforme elas no seguinte string: "Desafio, manipulacao,de,string". Imprima o resultado no console
print(','.join(palavras1))# Aqui com o metodo join eu uni as palavras e separei elas com uma virgula

#Desafio 4: pegue o palavras2 e transforme elas no seguinte string: frase2 = "jhonatan & rafael & carol & camilla". Imprima o resultado no consol
print(' & '.join(palavras2))#Aqui peguei a frase da palavra2 e separei eles por espacos e adicionei um (&) e depois dei espacos.
