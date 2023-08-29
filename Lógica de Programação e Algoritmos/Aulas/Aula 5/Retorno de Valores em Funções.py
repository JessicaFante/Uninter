def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    return res

retornado = soma3(1,2,3)
print(retornado)

#Forma alternativa simplificada
print(soma3(1,2,3))

retornado1 = soma3(1,2,3)
retornado2 = soma3(1,2)
retornado3 = soma3()
print ('Somatórios: {}, {} e {}.'.format(retornado1,retornado2,retornado3))