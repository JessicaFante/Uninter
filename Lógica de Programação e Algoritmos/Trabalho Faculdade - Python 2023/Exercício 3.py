print('Bem-vindo ao Petshop da Jéssica Beatriz Fante')

# Função responsável em obter o peso do cachorro
def cachorro_peso():
    while True:
        try:
            peso = float(input('Qual o peso do cachorro?'))
            if peso >= 3 and peso < 10:
                return 50
            elif peso >= 10 and peso < 30:
                return 60
            elif peso >= 30 and peso < 50:
                return 70
            elif peso < 3:
                return 40
            else:
                peso >= 50
                print('Não aceitamos cachorros tão grandes.\nPor favor entre com o peso do cachorro novamente.')
        except ValueError:
            print('Você digitou um valor não numérico.\nPor favor entre com o peso do cachorro novamente.')

# Função responsável em obter o tipo de pelo do cachorro
def cachorro_pelo():
    while True:
        try:
            pelo = input('Qual o tipo de pelo do cachorro?(c - Pelo Curto, m - Pelo Médio, l - Pelo Longo)')
            if pelo in ['c', 'm', 'l']:
                if pelo == ('c'):
                    return 1
                elif pelo == ('m'):
                    return 1.5
                elif pelo == ('l'):
                    return 2
            else:
                print('Opção inválida.\nDigite novamente!')
        except:
            print('Opção inválida.\nDigite novamente!')

#Função responsável em obter informação de serviços adicionais
def cachorro_extra():
    extra = 0
    while True:
        try:
            adicional = int(input('Deseja algum serviço adicional? (1 - Corte de Unhas, 2 - Escovar os Dentes, 3 - Limpeza das Orelhas, 0 - Não desejo serviços adicionais)'))
            if adicional == 0:
               return extra
            elif adicional in [1, 2, 3]:
                if adicional == 1:
                    extra += 10
                elif adicional == 2:
                    extra += 12
                elif adicional == 3:
                    extra += 15
            else:
                print('Opção inválida. Escolha 1, 2, 3 ou 0!')
        except:
            print('Opção inválida. Digite um número válido!')


# Função principal, com os valores retornados
def main():
    base = cachorro_peso()
    multiplicador = cachorro_pelo()
    extra = cachorro_extra()

    total = base * multiplicador + extra
    print(f'Total a pagar R$ {total:.2f}.(Peso:{base:.2f} * pelo:{multiplicador} + adicional(is):{extra:.2f}).')

if __name__ == '__main__':
    main()