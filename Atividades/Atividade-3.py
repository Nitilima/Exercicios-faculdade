import random

def cadastra_doador(nome:str, doacao:float): #função para o cadastro do doador com os parametros de nome e doação com valores de string e flutuante
    doador = [nome for _ in range(int(doacao // 10))] #variável doador recebendo um laço de repetição
    doadores.extend(doador)
    return

def sorteia_ganhador():
    random.shuffle(doadores) #metodo para embaralhar os nomes que forem inseridos
    print(f'Lista de doadores embaralhada: {doadores}')
    return random.choice(doadores)

opcao = int(input('Cadastrar a pessoa? 0 - não  1 - sim'))

doadores= []
while opcao == 1:
    doador = input('Nome do doador: ')
    valor = float(input('Valor doado: '))

    while len(doador.strip()) == 0 or valor < 10:
        print('O nome é obrigatório e o valor mínimo para doação é de R$ 10')
        doador = input('Nome do doador: ')
        valor = float(input('Valor da doação: '))

    cadastra_doador(doador, valor)

    opcao = int(input('Cadastrar doador? 0 - Não 1 - Sim'))

if len(doadores) > 0:
    print(f'Lista de doadores para sorteio: {doadores}')
    print(f'O vencedor foi: {sorteia_ganhador()}')