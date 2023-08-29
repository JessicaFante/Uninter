#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
#Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para
#comércios.

kWh = float(input('Quantos kWh?'))
tipo = input('Qual o tipo de instalação?(R, I ou C)')

if (tipo == 'R'):
    if  kWh <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif (tipo == 'I'):
    if kWh <= 5000:
        preco =0.55
    else:
        preco = 0.6
elif (tipo == 'C'):
    if kWh <= 1000:
        preco = 0.55
    else:
        preco = 0.6
else:
    print('A instalação é inválida!')

print('Total a pagar: R$ {}.'.format(kWh * preco))