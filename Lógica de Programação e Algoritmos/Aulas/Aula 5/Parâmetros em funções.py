# Parâmetros em funções

def realce(s1):
    print('|', '___' * 10, '|')
    print('|', '___' * 10, '|')
    print(s1)
    print('|', '___' * 10, '|')
    print('|', '___' * 10, '|')

realce('              MENU')


def sub2(x, y):
    res = x - y
    print(res)

sub2(5, 7)
sub2(7, 5)
sub2(y=7, x=5)
