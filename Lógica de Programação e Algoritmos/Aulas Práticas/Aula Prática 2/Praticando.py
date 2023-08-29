#Somatório dos 5 primeiros números inteiros e positivos
print (1+2+3+4+5)
#A média entre 23, 19 e 31
print ((23+19+31)/3)
#O número de vezes que 73 cade em 403
print (403//73)
#A sobra quando 403 é dividido por 73
print (403%73)
#2 elevado à 10° potência
print (2**10)
#O valor absoluto da diferença entre 54 e 57
print (abs(54-57))
#O menor valor entre 34,29 e 31
print (min(34, 29, 31))

#Atribuir o valor inteiro 3 à variável a
a = 3
#Atribuir o valor 4 à variável b
b = 4
#Atribuir à variável c o valor da ex´ress]ap a*a + b*b
c = a*a + b*b
print (a, b, c)

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
#ant bat cod
print (s1 + ' ' + s2 + ' ' + s3)
#ant ant ant ant ant ant ant ant ant ant
print (10 *(s1 + ' '))
#ant bat bat cod cod cod
print (s1 + ' ' +  2 *(s2 + ' ') + 3 *(s3 + ' '))
#ant bat ant bat ant bat ant bat ant bat ant abt ant bat
print (7 *(s1 + ' '+ s2 + ' '))
#batbatcod batbatcod batbatcod batbatcod batbatcod
print (5 *((2*(s2) + s3 + ' ')))