def borda(s1):
    tam = len(s1)
    #Só imprime caso exista algum caractere)
    if tam:
        print ('+','-' * tam, '+')
        print ('|', s1, '|')
        print ('+','-' * tam,'+')

#Programa principal
borda('Olá, mundo!')
borda('Lógica de Programação e Algoritmos')