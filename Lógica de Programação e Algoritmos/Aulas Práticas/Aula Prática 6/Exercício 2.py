#Crie um jogo de pedra, papel ou tesoura (Jokenpô). Você deverá jogar contra o computador.
#Você irá sempre escolher uma das opções: 1- pedra, 2 – papel, 3 – tesoura.
#O computador irá sempre sortear um número de 1 até 3 para jogar.
#Armazene todos os resultados em uma lista e no final apresente o vencedor.
#Encerre o programa ao digitar zero
import random
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x
def vencedor(jogador1,jogador2):
    global empate, vitorias1, vitorias2
    if jogador1 == 1: #Pedra
        if jogador2 == 1: #Pedra
            empate += 1
        elif jogador2 == 2: #Papel
            vitorias2 += 1
        elif jogador2 == 3: #Tesoura
            vitorias1 += 1
    elif jogador1 == 2: #Papel
        if jogador2 == 1: #Pedra
            vitorias1 += 1
        elif jogador2 == 2: #Papel
            empate += 1
        elif jogador2 == 3: #Tesoura
            vitorias2 += 1
    elif jogador1 == 3: #Tesoura
        if jogador2 == 1: #Pedra
            vitorias2 += 1
        elif jogador2 == 2: #Papel
            vitorias1 += 1
        elif jogador2 == 3: #Tesoura
            empate += 1
    resultados = [vitorias1, vitorias2, empate]
    return resultados

#Programa Principal
print('JOKENPO')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

resultados = []
jogadas = []
vitorias1 = 0
vitorias2 = 0
empate = 0

while True:
    jogada1 = valida_int('Escolha sua jogada: ', 0, 3)  #Validação do número inteiro utilizando a função
    if not jogada1: #pode ser também if jogada1 == 0
        print('Encerrando o programa...')
        break #Encerrando o programa
    jogada2 = random.randint(1,3) #importação da biblioteca random, função randint
    jogadas.append([jogada1,jogada2])  #Adiciona um item ao final da lista
    resultados = vencedor(jogada1, jogada2)
    print(vencedor(jogada1, jogada2))

    for jogada in jogadas:
        for dado in jogada:
            print(dado, end=' ')
        print()

print('Número de vítorias do Jogador 1: {}.'.format(resultados[0]))
print('Número de vítorias do Computador: {}.'.format(resultados[1]))
print('Número de empates: {}.'.format(resultados[2]))
