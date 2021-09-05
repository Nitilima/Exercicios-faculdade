tabela = [] #uma tabela vazia para ir inserindo os valores

while True:
    continuar = int(input('Digite 0 - sair 1 - continuar'))
    if (continuar == 0):
        break

    codigo = int(input('Digite o codigo do produto'))
    estoque = int(input('Digite o codigo do estoque'))
    minimo = int(input('Digite o codigo do minimo'))

    dicionario = {'codigo': codigo, 'estoque': estoque, 'minimo': minimo}

    print()
    tabela.append(dicionario)
tabela = sorted(tabela, key = lambda dicionario: dicionario['codigo'])
print(tabela)