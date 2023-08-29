#Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa.
#Se a pessoa tiver menos de 3 anos de idade, o ingresso será gratuito, se tiver entre 3
#e 12 anos, o ingresso custará R$ 15, se tiver mais de 12 anos, custará R$ 30.

#Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes o preço
#do ingresso do cinema.

#Encerre o laço usando um break quando o usuário digitar sair.

#Após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos, o total
#de dinheiro arrecadado e a média de idade das pessoas.

print ('Digite "sair" para encerrar o programa"')

total = 0
dinheiro = 0

while True:
    idade = (input('Qual sua idade?'))
    if idade == 'sair':
        print('Encerrando programa...')
        break
    idade = int(idade)
    total += 1
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso

media = dinheiro / total
print('O total de pesssoas é de {}.'.format(total))
print('O total arrecadado é de R$ {}.'.format(dinheiro))
print('A média arrecadada é de R$ {}.'.format(ingresso))