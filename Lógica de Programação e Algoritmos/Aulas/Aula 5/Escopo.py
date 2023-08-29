def comida():
    print(ovos)

ovos = 12
comida ()

def comida():
    ovos = 12
    bacon()
    print(ovos)

def bacon():
    ovos = 6

comida()

def comida():
    ovos = 'variável local de comida'
    print(ovos)

def bacon():
    ovos = 'variável local de bacon'
    print (ovos)
    comida()
    print(ovos)

ovos = 'variável global'
bacon()
print(ovos)

def comida():
    global ovos
    ovos = 'comida'

ovos = 'global'
comida()
print(ovos)


