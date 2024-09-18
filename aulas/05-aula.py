# No exemplo abaixo temos a variavel teclado, como faço para acessa a letra (C) da palavra teclado?
teclado = 'teclado'
print(teclado[2])#aqui eu acabei de utilizar um indice para acessar a letra (c), lembrando que o indice começa por zero(0).
#por isso, quando acessei o numero 2, na tela saiu a letra c.

#Vamos imaginar que eu queira acessar a letra (a ) do teclado!

print(teclado[4])# pra acessarmos a letra (a) do teclado o nosso indice eh 4.


#Vamos supor que eu esteja a trabalhar com informaçoes muito maior na nossa variavel (teclado), e queremos acessar o ultimo caracter da string.
teclado = 'Angola tem maior numero de casos de programadores'
print(teclado[-1])# Quando nos fizemos isso, o (-1) ele vai ate ao nosso ultimo indice e imprime na tela.

# Vamos supor que eu nao quero contar qual eh o indice e quero chegar na letra (B)
teclado = 'celebracao'
print(teclado.index('b')) # nos podemos fazer isso, para saber qual eh o indice na nossa letra, no caso aqui foi (b), utilizamos o (index, dentro de parenteses com aspas simples ou duplas)

# No exemplo acima, ele pega o valor numerico, do nosso indice, ja no exemplo abaixo ele pega a letra, que esta no nosso indice.

# Se eu quiser imprimir, o que esta dentro, onde esta o index b, usamos o seguinte comando
print(teclado[teclado.index('b')])# Aqui ele vai ir onde esta o index (b) e vai imprimir pra nos na tela

# Acessando Partes de um string

link = 'facebook.com/devaprender'
print(link[0])#Aqui podemos acessar o primeiro caracter da nossa string
print(link[-1])# Aqui vamos acessar o ultimo caracter da nossa string
print(link[0:5])# Aqui podemos passar, parte de uma string, onde ele inicia e onde ele termina
print(link[0:])# Aqui caso voce nao expecifique em qual indice ele deve terminar, ele vai imprimir toda linha
print(link[-5:])#Aqui caso eu queira começar de tras pra frente, eu quero que vai ate ao final, e volte 5 indices.
print(link[5:]) # Aqui da mesma forma, voce pode iniciar, outras posicoes dentro da minha string, e caso eu nao expecifique vai ate ao final
print(link[:-5])# Aqui caso eu nao especifique no inicio ele vai entender que inicie da posicao zero, ate ao quinto caracter e de tras pra frente

# Em alguns casos, eu vou querer ir buscar caracteres que estao sendo repetidos dentro de uma frase duas vezes
frase = 'Clean Code'
print(frase.rindex('C'))# Aqui usamos o (rindex), para nos acessar a ultima ocorrencia do ultimo caracter

