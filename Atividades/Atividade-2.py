nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
ru = input('Digite os ultimos dois numeros do seu RU: ')

def geraemail(nome:str, sobrenome:str, ru:int):
    if len(nome) > 0 and len(sobrenome) >0 and len(ru) > 0:
        email = nome[0] + sobrenome + ru + '@algoritmos.com.br.'
    return 'Sra '+nome+' '+sobrenome+', seu email é: '+email

print(f'Olá, {nome} {sobrenome}! O seu novo e-mail é {geraemail(nome, sobrenome, ru)}')


