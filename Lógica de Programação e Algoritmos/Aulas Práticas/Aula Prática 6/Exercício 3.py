#Crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas.
#Armazene os dados em um dicionário com listas.
#Ao encerrar o cadastro, apresente:
    #O total de cadastros efetuados;
    #A média das idades das pessoas;
    #Uma lista de mulheres com menos de 30 anos;
    #Uma lista de homens com idade acima da média;

cadastro = {'Nome': [], 'Sexo': [], 'Ano': []}
total = 0
somaIdades = 0
mulhermenos30 = []
homensacimamedia = []


while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]:')
    if terminar.upper() in 'N':
        print('Encerrando o programa...')
        break
    if terminar.upper() not in 'S':
        print('Digite "S" para SIM e "N" para NÃO.')
        continue
    nome = input('Insira o nome:')
    sexo = input('Insira o sexo [M/F]:')
    ano = int(input('Insira o ano de nascimento:'))
    cadastro['Nome'].append(nome)
    cadastro['Sexo'].append(sexo.upper())
    cadastro['Ano'].append(ano)
    total += 1
    somaIdades += (2023 - ano)

    somaIdades = sum([2023 - ano for ano in cadastro ['Ano']])
    total = len(cadastro['Ano'])
    if total > 0:
        mediaIdades = somaIdades / total

    if sexo.upper() == 'M' and (2023 - ano) > mediaIdades:
        homensacimamedia.append(nome)

    if sexo.upper() == 'F' and (2023 - ano) < 30:
        mulhermenos30.append(nome)

if total > 0:
    mediaIdades = (somaIdades / total)
    print('A média das idades de todas as pessoas é: {}.'.format(mediaIdades))
else:
    print('Nenhum cadastro efetuado')

print(cadastro)
print('O total de cadastros é de {}.'.format(total))
print('A(s) mulher(es) com menos de 30 anos é(são): {}.'.format(mulhermenos30))
print('O(s) homem(ns) com idade acima da média é(são): {}.'.format(homensacimamedia))

