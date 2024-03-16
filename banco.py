from time import sleep
from models.cliente import Cliente
from models.conta import Conta
from utils.menu import menu

contas = []
clientes = []


def application():
    while True:
        print(menu())

        op = int(input("         => "))

        if op == 0:
            print('\t\t Agradecemos à preferência. É um prazer tê-lo conosco!!!')
            print('\t\t Volte Sempre!!!')
            sleep(1)
            break

        elif op == 1:
            criar_conta()
        elif op == 2:
            efetuar_saque()
        elif op == 3:
            efetuar_deposito()
        elif op == 4:
            efetuar_transferencia()
        elif op == 5:
            listar_contas()
        elif op == 6:
            listar_clientes()
        else:
            print('\t\t Operação Inválida. Volte ao Menu e digite uma opção válida.')


def criar_conta():
    print('Informe os dados do Cliente: ')
    nome = input('Nome: ')
    cpf = input('CPF: ')
    data_nascimento = input('Data de Nascimento [dd/mm/aaaa]: ')
    email = input('Email: ')

    cliente = Cliente(nome, cpf, data_nascimento, email)
    conta = Conta(cliente)

    contas.append(conta)
    clientes.append(cliente)

    print('\t\tConta cadastrada com sucesso!!')
    print('\t\tDados da Conta: ')
    print('\t\t******************************')
    print(conta)
    sleep(1.5)


def efetuar_saque():
    if possui_contas:
        numero_conta = int(input('Digite o número da sua conta: '))
        conta = buscar_conta_por_numero(numero_conta)

        if conta:
            valor = float(input("Informe o valor que deseja sacar: R$ "))
            conta.sacar(valor)
        else:
            print(f'Não foram encontradas contas com o número {numero_conta}!!')

    sleep(1.5)


def efetuar_deposito():
    if possui_contas:
        numero_conta = int(input('Digite o número da sua conta: '))
        conta = buscar_conta_por_numero(numero_conta)

        if conta:
            valor = float(input("Informe o valor que deseja depositar: R$ "))
            conta.depositar(valor)
        else:
            print(f'Não foram encontradas contas com o número {numero_conta}!!')

    sleep(1.5)


def efetuar_transferencia():

    if possui_contas():
        numero_conta_org = int(input('Digite o número da sua conta: '))
        conta_org = buscar_conta_por_numero(numero_conta_org)

        if conta_org:
            numero_conta_dest = int(input('Informe o numero da conta de destino da sua transferência: '))
            conta_dest = buscar_conta_por_numero(numero_conta_dest)

            if conta_dest:
                valor = float(input("Informe o valor que deseja transferir: R$ "))
                conta_org.transferir(conta_dest,valor)
            else:
                print(f'\t\t Não encontramos a conta de número {numero_conta_dest}')

        else:
            print(f'\t\t Não encontramos a conta de número {numero_conta_org}')



def listar_contas():

    if possui_contas():
        print('\t\tLista de Contas')
        print('\t\t' + '*' * 30)
        for conta in contas:
            print(conta)
            print('\t\t' + '*' * 30)

    sleep(1.5)


def listar_clientes():

    if possui_clientes:
        print('\t\tLista de Clientes')
        print('\t\t'+'*' * 30)
        for cliente in clientes:
            print(cliente)
            print('\t\t'+'*' * 30)

    sleep(1.5)


def buscar_conta_por_numero(numero_conta):

    if len(contas) > 0:
        for conta in contas:
            if numero_conta == conta.numero:
                return conta

    return None

def possui_contas():
    return True if len(contas) > 0 else print('\t\t Ainda não existem contas cadastradas!!')


def possui_clientes():
    return True if len(clientes) > 0 else print('\t\t Ainda não existem clientes cadastradoas!!!')


if __name__ == '__main__':
    application()
