"""
Tipos de numeros que podem ser usados no python

Quando estivermos a trabalhar com valores numericos, calculos, informacoes do tipo, eh importante que nos saibamos trabalhar com 
numeros, e os numeros dentro de python sao utilizados da seguinte forma:
1- Numeros inteiros, quer dizer que o numero nao tem valor decimal
2- Numeros decimais, que eh onde adiciono um valor depois do ponto.

Para nos descobrir qual eh o valor do numero que estamos a trabalhar basta usarmos o type
"""
a = 20
b = 20.5

print(type(a))
print(type(b))

"""
Quais sao as operacoes matematicas que nos podemos fazer dentro do python?

"""
print(10 + 6)
print(10 - 6)
print(10 * 6)
print(10 / 6)
print(10 // 6)# divisao de inteiro
print(10 % 6)# Modulus
print(10 ** 6)# exponenciais

# Atalho para atribuicao mais rapida
"""
vamos imaginar que vc passou 10 pra variavel a, e depois queres somar a + 5 , a maneira mais rapida eh usar o operador
mais igual (+=) que vai literalmente fazer isso aqui (a = a + 5) so que de uma forma mais rapida e esse mesmo operador (+=)
pode ser usado em todas as operacoes matematicas.
"""
a = 10
a = a + 5
a += 5
# o mesmo que esta em cima, eh o mesmo que esta em baixo
b = 20
b = b - 2
b += 2

#operacoes matematicas comuns que nos podemos fazer em numeros
"""
E nos podemos usar as funcoes ja existentes dentro do python, por exemplo se eu quiser arrendodar um valor (5.7)
caso eu queira arrendodar um valor eu usa a funcao (round e entre parenteses passo o valor que eu quero arrendodar)
mas se eu quiser arrendodar com o valor inteiro mais proximo ainda, por exemplo 2.2 que vai ser 3
primeiro tenho que importar a biblioteca math, e quando importo a biblioteca math
e printo na tela, math.ciel, o nosso resultado esperado sera 3.
"""
import math
print(round(5.7))
print(math.ceil(2.2))