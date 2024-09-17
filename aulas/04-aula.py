nome_curso = ' Edicao de video '

print(nome_curso.upper())#Transforma toda string em sua versao maiuscula
print(nome_curso.lower())# transforma toda string em sua versao minuscula
print(nome_curso.strip())# Remove todo espaco em branco da brase
print(nome_curso.lstrip())# conhecido como left strip ele remove todo espaco da esquerda
print(nome_curso.rstrip()) # Conhecido como rigth strip, ele remove todo espaco vazio da direita
print(nome_curso.find('cao')) # O metodo find, encontra uma infromacao dentro da string, no exemplo acima ele diz que a letra c
# esta no indice 4, o python ele indexa cada valor numerico dentro de uma string, comecando pelo indice 0. e nos encontramos 
#o indice da palavra cao no indice 4.
print(nome_curso.replace('video','musica'))# O metodo replace ele subistitui a primeira palavra que voce passar pela segunda palavra
#nos temos a frase edicao de video, ele muda de video para musica.
print('https://sc.olx.com.br/?o=90&q=relogio'.replace('relogio', 'carro'))# o metodo replace ele eh util quando estamos navegando num site, e querenis que ele
# a cada moment navegue por categoria diferente, no nosso link.

