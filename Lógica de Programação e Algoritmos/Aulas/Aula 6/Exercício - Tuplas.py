#Desempacotamento de parâmetros em Funções

#Suponha que você quer realizar o somatório de diversos valores, porém, não sabe quantos valores serão
#somados. Pode ser que sejam somente 2, ou então 10, ou mesmo 100 números.

#Como criar uma função capaz de receber um número tão variável de parâmetros?

#* - desempacotamento

def soma(*num):
    soma = 0
    print ('Tupla: {}'.format(num))
    for i in num:
        soma += i
    return soma

print('Resultado: {}\n.'.format(soma(1,2)))
print('Resultado: {}\n.'.format(soma(1,2,3,4,5,6,7,8,9)))


