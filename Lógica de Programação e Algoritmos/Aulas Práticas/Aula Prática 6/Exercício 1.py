#Escreva um algoritmo que crie uma tupla com 10 palavras. Encontre dentro dessa tupla as
#vogais de cada palavra. Faça um print na tela com o nome da palavra e suas respectivas vogais.

palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser', 'Zelda', 'Link', 'Ash', 'Pikachu', 'Eevee')

for palavra in palavras:
    print('\nPalavra: {}. Vogais: '.format(palavra.upper()), end = '')  #O upper irá imprimir todas as palavras em maiúscula.
    for letra in palavra:
        if letra.lower() in 'aeiou': #lower irá transformar todas as letras em maiúscula para fazer o teste.
            print(letra.upper(), end =' ') #end serve para não haver quebra de linha no print
