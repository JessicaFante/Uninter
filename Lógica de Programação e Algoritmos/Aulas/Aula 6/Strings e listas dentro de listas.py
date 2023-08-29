#Strings dentro de listas

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']

#Indexação dupla - Acessar individualmente para caractere de um índice quando esse for uma string

print(mochila[0][0])
print(mochila[0][1])
print(mochila[0][2])
print(mochila[0][3])
print(mochila[0][4])
print(mochila[0][5])
print(mochila[0][6])

#O primeiro índice é referente a cada item da lista, o segundo índice é referente a cada caractere da string.
#Assim podemos acessar não só cada dado dentro da lista, mas também cada caractere das strings de um índice.

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[2][0])
print(mochila[2][1])

for item in mochila:
    for letra in item:
        print(letra, end=' ')
    print()

#Listas dentro de listas

mochila = [['Cebola', 0.39], ['Tomate', 0.49], ['Maça', 0.89]]
print(mochila)
print(mochila[0])
print(mochila[0][0])
print(mochila[0][0][0])
print(mochila[0][1])
###########################################################

item = []
mercado = []

for i in range(3):
    item.append(input('Digite o nome do item:'))
    item.append(int(input('Digite a quantidade:')))
    item.append(float(input('Digite o valor:')))
    mercado.append(item[:])
    item.clear()
print(mercado)

########################################################
mercado = []

for i in range(3):
    nome = input('Digite o nome do item:')
    qtd = int(input('Digite a quantidade:'))
    valor = float(input('Digite o valor:'))
    mercado.append([nome, qtd, valor])
print(mercado)

##########################################################