#Estrutura de dados dinâmica
#Podemos alterar dados e tamanhos
#Indexadas por valores numéricos inteiros
#Representadas em Python por colchetes []

#Listas []

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('Lista: ', mochila)

mochila[2] = ('laranja')    #trocar valores da lista
print('Lista: ', mochila)

mochila.append('Ovos') #Acrescentar um novo valor a lista
print('Lista: ', mochila)

mochila.insert(1,'Canivete') #acrescentar um novo valor a lista, em posição específica
print('Lista: ', mochila)

del mochila[1]   #deleta o elemento pelo índice
print ('Lista: ', mochila)
mochila.remove('Ovos') #deleta o elemento pelo valor
print ('Lista: ', mochila)
#########################################################

#mesma referência
x = [5, 7, 9, 11]
y = x
print(x)
print(y)

y[0] = 2  #altera ambas as listas
print(x)
print(y)
##########################################################

#cópia
x = [5, 7, 9, 11]
y = x[:]
print(x)
print(y)

y[0] = 2 #altera somente a lista y
print(x)
print(y)
