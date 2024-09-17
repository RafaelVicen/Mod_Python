#Strings Dinamicos

nome = 'rafael'
email = 'rafael@gmail.com'

"""
Ola Rafael, acabou de cadastrar o teu email, verifique se esta correto rafael@gmail.com
"""
#para criar uma string dinamica eu uso o (f) que eh uma string formatado e entre aspas eu meto a frase que quero enviar.
#para colocar dinamicamente usamos chaves, dentro das chaves colocamos a variavel que vai subistituir no moment que eu passar na linha
print(f'ola {nome}, verifique se o email esta correto: {email}')