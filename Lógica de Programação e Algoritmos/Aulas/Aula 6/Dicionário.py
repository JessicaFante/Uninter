#É uma estrutura de dados dinâmica
#Podemos alterar dados e tamanho
#Indexados por chves (palavra-chave)
#Representador em python por chaves {}

#Dicionários {}

game = {'nome':'Super Mario',
        'desenvolvedora':'Nintendo',
        'ano': 1990}

print(game)
print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

#values: obtém somente os dados
#keys: obtém somente as chaves
#items: obtem o par chave:dado

print(game.values())

for i in game.values():
    print(i)

print(game.keys())

for i in game.keys():
    print(i)

print(game.items())

for i,j in game.items():
    print('{} = {}'.format(i, j))

#####################################################################
#Uma lista, pode conter em cada índice, um dicionário

games = []
game1 = {'nome':'Super Mario',
         'videogame':'Super Nintendo',
         'ano': 1990}
game2 = {'nome':'Zelda Ocarina of Time',
         'videogame':'Nintendo 64',
         'ano': 1998}
game3 = {'nome': 'Pokemon Yellow',
         'videogame':'Game Boy',
         'ano': 1992}
games = [game1, game2, game3]
print (games)

game = {}
games = []
for i in range(3):
    game['nome'] = input('Qual o nome do jogo?')
    game['videogame'] = input('Para qual video-game ele foi lançado?')
    game['ano'] = int(input('Qual o ano de lançamento?'))
    game.append(game.copy())
print ('-' * 20)
for e in games:
    for i,j in e.items():
        print('O campo {} tem o valor {}.'.format(i,j))
#######################################################################
#Um dicionário , pode conter várias listas

games = {'nome':['Super Mario', 'Zelda Ocarina of Time', 'Pokemon Yellow'],
         'videogame':['Super Nintendo', 'Nintendo 64', 'Game Boy'],
         'ano':[1990, 1998, 1999]}
print (games)

games = {'nome':[], 'videogame':[], 'ano':[]}
for i in range(3):
    nome = input('Qual o nome do jogo?')
    videogame = input('Para qual video-game foi lançado?')
    ano = int(input('Qual o ano de lançamento?'))
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].append(ano)
print('-' * 20)
print(games)