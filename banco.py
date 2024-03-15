from time import sleep
from models.cliente import Cliente
from models.conta import Conta
from utils.menu import menu

contas = []
clientes = []
conta_atual = None


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
    global conta_atual
    conta_atual = conta

    contas.append(conta)
    clientes.append(cliente)

    print('Conta cadastrada com sucesso!!')
    print('Dadoa da Conta: ')
    print('******************************')
    print(conta)
    sleep(1)


def efetuar_saque():
    if possui_contas(contas):
        valor = float(input("Informe o valor que deseja sacar: R$ "))
    sleep(1)


def efetuar_deposito():
    if possui_contas(contas):
        valor = float(input("Informe o valor que deseja depositar: R$ "))
    sleep(1)


def efetuar_transferencia():
    pass


def listar_contas():
    pass


def listar_clientes():
    pass


def buscar_conta_por_numero():
    pass


def possui_contas(lista_contas):
    return True if len(lista_contas) > 0 else print('\t\t Ainda não existem contas cadastradas!!')


def possui_clientes(lista_clientes):
    return True if len(lista_clientes) > 0 else print('\t\t Ainda não existem clientes cadastradoas!!!')



if __name__ == '__main__':
    application()
