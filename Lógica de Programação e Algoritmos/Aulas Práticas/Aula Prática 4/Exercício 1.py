#Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário
#qual operação ele deseja realizar:adição (+), subtração (-), multiplicação (*),
#divisão (/) e sair. Exiba na tela o resultado da operação desejada.

#Repita até que a opção saída seja escolhida.

print('CALCULADORA')
print('+ Adição')
print('- Substração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione outra tecla para sair')

while True:
    operador = input('Qual operação deseja fazer?')
    if operador == '+' or operador == '-' or operador == '*' or operador == '/':
        x = float(input('Digite o primeiro valor:'))
        y = float(input('Digite o segundo valor:'))
    if (operador == '+'):
      res = x + y
      print('O resultado da soma de {} e {} é: {}.'.format(x,y,res))
      continue
    elif (operador == '-'):
      res = x - y
      print('O resultado da substração de {} e {} é: {}.'.format(x, y, res))
      continue
    elif (operador == '*'):
     res = x * y
     print('O resultado da multiplicação de {} e {} é: {}.'.format(x, y, res))
     continue
    elif (operador == '/'):
     res = x / y
     print('O resultado da divisão de {} e {} é: {}.'.format(x, y, res))
     continue
    elif (operador == 's'):
        break
    else:
     print('Operação Inválida')

print('Encerrando o programa...')



