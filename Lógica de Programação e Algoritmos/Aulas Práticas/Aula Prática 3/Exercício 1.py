#Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário.
#Verifique se os valores formam um triângulo e classifique como:
#A - Equilátero (três lados iguais), B - Isósceles (Dois lados iguais), 3 - Escaleno (Três lados diferentes)

#Lembre-se de que, para formar um triângulo, nenhum dos lados pode ser igual a zero, e umn lado não pode ser maior do
#que a soma dos outros dois

a = int(input('Digite o primeiro lado do triângulo:'))
b = int(input('Digite o segundo lado do triângulo:'))
c = int(input('Digite o terceiro lado do triângulo:'))

if (a > 0) and (b > 0) and (c > 0):
 if (a + b > c) and (a + c > b) and (b + c > a):
     if (a != b) and (b != c) and (c != a):
          print('Este é um triângulo escaleno!')
     else:
         if (a == b) and (b == c) and ( c == a):
                print('Este é um triângulo equilátero!')
         else:
                print('Este é um triângulo isósceles!')
 else:
        print ('Ao menos um dos valores indicados não servem para formar um triângulo.')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo.')