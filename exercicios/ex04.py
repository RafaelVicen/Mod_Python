#Desafio 1
# Encontre o indice de 'o' dentro da variavel biblioteca
biblioteca = 'Biblioteca'
print(biblioteca.index('o'))

#Desafio 2
# Usando a frase
'Desenvolvimento De Aplicacoes'
#imprima apenas 'De Aplicacoes'
aplicacoes = 'Desenvolvimento De Aplicacoes'
print(aplicacoes[-13:])

#Ou podemos fazer de outra forma que eh

indice_d = aplicacoes.rindex('D') # Aqui encontramos o indice da letra D
indice_s = aplicacoes.rindex("s")# Aqui encontramos o indice da letra s
print(aplicacoes[indice_d:indice_s+1])# Aqui coloquei o mais 1 para que ele acesse o ultimo indice, para pegar a palavra inteira
