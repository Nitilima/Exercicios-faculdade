soma = 0
cont = 1
while (cont <= 5):
    x = int(input('Digite o {}º número'.format(cont)))
    soma += x #equivalente: soma = soma + x
    cont += 1 #equivalente: cont = cont + 1
print('Somatório: {}'.format(soma))