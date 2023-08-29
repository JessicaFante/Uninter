#Escreva uma função que calcule o fatorial de um número recebido como parâmetro e
#retorne o seu resultado.

#Faça uma validação dos dados por meio de uma outra função, permitindo que somente valores
#positivos sejam aceitos.

#Crie o help da sua função (exercício da apostila – aula 5)

def validaint(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial(num):
    """
    Calcula o fatorial
    :param num:
    :return:
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num+1, 1):
        fat *= i #fat = fat * i
        return fat


x = validaint('Digite um valor para calcular a fatorial:', 0, 99999)
print('{}! = {}.'.format(x, fatorial(x)))
help(fatorial)

###NÃO ESTÁ CALCULANDO FATORIAL CORRETAMENTE