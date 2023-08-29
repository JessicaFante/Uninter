#Condicionais de Múltipla Escolha (ELIF)

#O usuário deverá escolher se quer comprar maças, laranjas ou bananas. Deverá ser apresentado na tela um menu com as
#opções: 1 para maça, 2 para laranja e 3 para banana. Após escolhida a fruta, deve-se digitar quantas unidades se quer
#comprar. O algoritmo deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela.
#Considere que uma maça custa R$2,30, uma laranja R$3,60 e uma banana R$1,85

print ('O que deseja comprar?')
print ('1 - Maça')
print ('2 - Laranja')
print ('3 - Banana')
produto = int(input('Qual sua escolha?'))
quantidade = int(input('Quantas unidades?'))
if (produto == 1):
    pagar = quantidade * 2.3
    print ('Você comprou {} maças. Total à pagar: R${}.'.format(quantidade,pagar))
elif (produto == 2):
    pagar = quantidade * 3.6
    print ('Você comprou {} laranjas. Total à pagar: R${}.'.format(quantidade,pagar))
elif (produto == 3):
    pagar = quantidade * 1.85
    print ('Você comrpou {} bananas. Total à pagar: R${}.'.format(quantidade,pagar))
else:
    print ('Produto inexistente!')
