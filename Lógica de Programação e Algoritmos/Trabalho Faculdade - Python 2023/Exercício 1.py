print ('Bem-vindo a Loja da Jéssica Beatriz Fante')

# Solicita os valores do usuário
valor = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade de produtos: "))

# Calcula o valor total sem desconto
valor_total = valor * quantidade

# Calcula o valor com desconto
if quantidade >= 200 and quantidade < 1000:
    desconto = 0.05
    valor_desconto = valor_total * desconto
elif quantidade >= 1000 and quantidade < 2000:
    desconto = 0.10
    valor_desconto = valor_total * desconto
elif quantidade >= 2000:
    desconto = 0.15
    valor_desconto = valor_total * desconto
else:
    quantidade <= 200
    valor_desconto = valor_total

# Exibe os resultados
print(f"Valor total SEM desconto: R$ {valor_total:.2f}")
print(f"Valor total COM desconto: R$ {valor_total - valor_desconto:.2f}")
print(f"Seu desconto foi de R$ {valor_desconto:.2f}")
