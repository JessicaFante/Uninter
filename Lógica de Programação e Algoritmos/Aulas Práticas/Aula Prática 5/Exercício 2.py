#Suponha que você é um colecionar de jogosde videogame. Escreva um algoritmo
#que permita cadastrar esses jogos informando o nome e a qual videogame ele pertence.

#Para isso, crie um menu de opções contendo: cadastrar novo item, listar tudo que foi
#cadastrado e sair.

#Para resolver esse exercício, crie pelo menos uma função para cada item do menu.

#Além disso, armazene todos os dados em um arquivo de texto que deve ser salvo em disco
#e manter os dados cadastrados.

def validaInt(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print ('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso.'.format(nomeArquivo))
def cadastrarJogo(nomeArquivo, nomeJogo,nomeVideoGame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{}; {}.\n'.format(nomeJogo,nomeVideoGame))
    finally:
        a.close()
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print ('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print ('1 - Cadastrar novo item')
    print ('2 - Listar os cadastros')
    print ('3 - Sair')
    op = validaInt('Escolha a opção desejada:', 1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecionada...\n')
        nomeJogo = input('Nome do jogo:')
        nomeVideoGame = input('Nome do video game:')
        cadastrarJogo(arquivo,nomeJogo,nomeVideoGame)
    elif op == 2:
        print('Opção de listar selecionada...\n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break
