#Condicional Simples

#Lê dois valores inteiros e compara ambos
x = int(input('Digite um valor inteiro:'))
y = int(input('Digite um segundo valor inteiro:'))
if (x > y):
    print('O primeiro valor é maior que o segundo')

#Condicional Composta

#Par ou Ímpar
x = int(input('Digite um valor inteiro:'))
if (x % 2 == 0):
    print ('O número é par!')
else:
    print ('O número é impar!')

#Expressões Lógicas e Álgebra Booleana

#not
x = True
y = False
print (not x)
print (not y)

#and
x = True
y = False
print (x and y)

#or
x = True
y = False
print (x or y)

x = 10
y = 1
res = not x > y
print (res)

x = 10
y = 1
z = 5.5
res = x > y and z == y
print (res)