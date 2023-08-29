#Se idade é manor que 60, escreva: "Você tem direitos aos benefícios!"
idade = int(input('Qual sua idade?'))
if (idade >= 60):
    print ('Você tem direitos aos benefícios!')

#Se dano é maior do que 10 e escudo é igual a 0, escreva: "Você está morto!"
dano = int(input('Qual foi o dano?'))
escudo = int(input('Qual é seu escudo?'))
if (dano > 10 and escudo == 0):
    print ('Você está morto!')

#Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, escreva: "Você escapou!"
if (norte or sul or leste or oeste):
    print('Você escapou!')