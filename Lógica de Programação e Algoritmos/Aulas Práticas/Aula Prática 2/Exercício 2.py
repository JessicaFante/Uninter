#Exercício 2
#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a
#quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por
#dia e R$0,15 por km rodado.

km = int (input('Quantos KM foram percorridos pelo carro alugado?'))
dias = int (input('Por quantos dias o carro foi alugado?'))

preco = 60 * dias + 0.15 * km
print ('Foram percorridos {} km. O carro foi alugado por {} dias.'.format(km, dias))
print ('O valor a ser pago será de R${}.'.format(preco))