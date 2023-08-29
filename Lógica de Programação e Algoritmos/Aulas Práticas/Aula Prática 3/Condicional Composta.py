#Se ano é divisível por 4, escreva: "Pode ser um ano bissexto". Caso contrário, escreva: "Definitivamente não
#é um ano bissexto".
ano = int(input('Em que ano estamos?'))
if (ano % 4 == 0):
    print ('Pode ser um ano bissexto!')
elif (ano % 4 != 0):
    print ('Definitivamente não é um ano bissexto!')


#Se ambas variáveis booleanas cima e baixo forem True, escreva: "Decida-se!", caso contrário, escreva:"Você
#escolheu um caminho!"

print ('Escolha o caminho para seguir:')
print ('1 - Cima')
print ('2 - Baixo')
caminho = input('Qual caminho irá seguir?')
if (caminho == 1 or caminho == 2):
    print ("Decida-se!")
elif (caminho == 1 and caminho == 2):
    print ("Você escolheu um caminho!")
#EXERCICIO IMCOMPLETOOOOOOOOOOOOOOOO!