x = 1
while (x <= 5):
    print (x)
    x = x + 1

x = 0
while (x <= 99):
    print(x)
    x = x + 1

#CONTADOR
#Escreva um algoritmo que imprima na tela somente valores dentro de um intervalo especificado
#pelo usuário e que sejam números pares.

inicial = int(input('Qual valor deseja iniciar a contagem?'))
final = int(input('Qual valor deseja encerrar a contagm?'))
x = inicial
while (x <= final):
    if (x % 2) == 0:
        print (x)
    x = x + 1

#ACUMULADOR
#Escreva um algoritmo que calcule a sua média de notas em determinadas disciplina.
#Vamos assumir que a média final é dada pela média aritmética de cinco notas digitadas.

soma = 0
cont = 1
while (cont <= 5):
    x = float(input('Digite a {}° nota:'.format(cont)))
    soma += x
    cont += 1
media = soma / 5
print('Média final: {}'.format(media))

#VALIDANDO DADOS DE ENTRADA
#Crie um algoritmo que receba um valor do tipo inteiro via teclado. No entando, o programa
#só deve aceitar, obrigatoriamente, valores inteiros e positivos. Qualquer valor nnegativo,
#ou igal a zero, dever ser rejeitado pelo programa e um novo valor deve ser solicitado.

x= int(input('Digite um valor maior que zero: '))
while (x <= 0):
    x = int(input('Digite um valor maior que zero : '))
print('Você digitou {}. Encerrando o programa...'.format(x))