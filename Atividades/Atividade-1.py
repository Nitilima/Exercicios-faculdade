while True:
    dados = int(input('Inserir dados? 0 - não 1 - sim: '))
    if dados != 1:
        break
    nome = input('Nome do aluno: ')
    nota = float(input('Digite a sua nota: '))

    if nota <= 2.9:
        conceito = 'E'
    elif nota <= 4.9:
        conceito = 'D'
    elif nota <= 6.9:
        conceito = 'C'
    elif nota <= 8.9:
        conceito = 'B'
    elif nota <= 10:
        conceito = 'A'
    else:
        print('Nota inválida')
        break

    print(f'A aluna {nome} tirou a nota {nota} e se enquadra no conceito {conceito}.')
