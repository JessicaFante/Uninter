#Escreva um algoritmo que realize um login em um sistema. O usuário deve informar seu nome e senha.

while True:
    nome = input('Qual seu usuário?')
    if (nome != 'User'):
        continue
    senha = input('Qual a sua senha?')
    if (senha == '12345'):
        break
print ('Acesso concedido')
