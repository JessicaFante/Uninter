#Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar:
#adição (+), subtração (-), multiplicação (*) ou divisão (/). Exiba na tela o resultado da operação desejada.

print('CALCULADORA')
print('+ Adição')
print('- Substração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione outra tecla para sair')

operador = input('Qual operação deseja fazer?')
if operador == '+' or operador == '-' or operador == '*' or operador == '/':
    x = int(input('Digite o primeiro valor:'))
    y = int(input('Digite o segundo valor:'))

if (operador == '+'):
    res = x + y
    print('O resultado da soma de {} e {} é: {}.'.format(x,y,res))
elif (operador == '-'):
    res = x - y
    print('O resultado da substração de {} e {} é: {}.'.format(x, y, res))
elif (operador == '*'):
    res = x * y
    print('O resultado da multiplicação de {} e {} é: {}.'.format(x, y, res))
elif (operador == '/'):
    res = x / y
    print('O resultado da divisão de {} e {} é: {}.'.format(x, y, res))
else:
    print('Operação Inválida')

print('Encerrando o programa...')