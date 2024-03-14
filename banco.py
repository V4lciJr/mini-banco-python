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
            print('\t\tAgradecemos à preferência. É um prazer tê-lo conosco!!!')
            print('\t\tVolte Sempre!!!')
            sleep(1)
            break
        else:
            print('\t\tOperação Inválida. Volte ao Menu e digite uma opção válida.')


def criar_conta():
    pass


def efetuar_saque():
    pass


def efetuar_deposito():
    pass


def efetuar_transferencia():
    pass


def listar_contas():
    pass


def listar_clientes():
    pass


def buscar_conta_por_numero():
    pass


if __name__ == '__main__':
    application()