#Recebendo dados do usuario

"""
para receber entrada de dados em python nos usamos o input
na linha baixo o que eu acabei de fazer foi, fazer uma pergunta e inseri uma msg que deve ser solicitada pelo usuario
mas quando nos fazemos uma pergunta e alguem digita algo ele nos retorna essa informacao na tela, nos podemos guardar essa essa informacao em uma variavel como
por exemplo (nome)
Lembrando que o tipo da resposta sera sempre string, por padrao ele converte tudo que eu digitar entre parenteses para string
"""

nome = input('Digite o seu nome: ')
print(nome)
print(type(nome))
