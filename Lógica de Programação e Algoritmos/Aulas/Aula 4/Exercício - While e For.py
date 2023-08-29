#Escreva eum algoritmo em Python que calcule a tabuada de todos os números de 1 até 10, e
#para cada número, vamos calcular a tabuada multiplicando-o pelo intervalo de 1 até 10.

#2 while
tabuada = 1
while tabuada <= 10:
    print ('tabuada do {}.'.format(tabuada))
    i = 1
    while i <= 10:
        print ('{} x {} = {}'.format(tabuada, i, tabuada * i))
        i += 1
    tabuada += 1

#2 for
for tabuada in range(1,11,1):
    print('tabuada do {}'.format(tabuada))
    for i in range (1,11,1):
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))

#while + for
tabuada = 1
while tabuada <= 10:
    print('tabuada do {}:'.format(tabuada))
    for i in range(1,11,1):
        print('{} X {} = {}'.format(tabuaeda, i, tabuada * i))
    tabuada += 1
