from time import sleep
from models.cliente import Cliente
from models.conta import Conta
from utils.menu import menu
from os import system

contas = []
clientes = []


def application():
    while True:
        system('cls')
        op = menu()

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
        elif op == 7:
            pesquisar_conta()
        elif op == 8:
            pesquisar_cliente()
        elif op == 9:
            imprimir_extrato()
        else:
            print('\t\t Operação Inválida. Volte ao Menu e digite uma opção válida.')
        sleep(2)


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

    print('\t\t Conta cadastrada com sucesso!!')
    print('\t\t Dados da Conta: ')
    print('\t\t ' + '*' * 40)
    print(conta)
    sleep(2)


def efetuar_saque():
    if possui_contas():
        tipo_operacao = 'sacar'
        numero_conta = int(input('Digite o número da sua conta: '))
        conta = buscar_conta_por_numero(numero_conta)

        if valida_conta(conta, numero_conta, efetuar_saque):
            valor = ler_valor(tipo_operacao)
            eh_menor, valor = saldo_insuficiente(valor, conta.saldo_total, tipo_operacao)
            if eh_menor:
                conta.sacar(valor, 'Saque de R$')



def efetuar_deposito():
    if possui_contas():
        tipo_operacao = 'depositar'
        numero_conta = int(input('Digite o número da sua conta: '))
        conta = buscar_conta_por_numero(numero_conta)

        if valida_conta(conta, numero_conta, efetuar_deposito):
            valor = ler_valor(tipo_operacao)
            valida_valor, valor = valor_maior_q_zero(valor, tipo_operacao)
            if valida_valor:
                conta.depositar(valor, 'Depósito de R$')


def efetuar_transferencia():
    tipo_operacao = 'transferir'
    if possui_contas():
        conta_orig, numero_conta_orig = ler_conta('Digite o número da sua conta: ')

        if valida_conta(conta_orig, numero_conta_orig, efetuar_transferencia):
            conta_dest, numero_conta_dest = ler_conta('Digite a conta para a qual deseja transferir: ')
            if valida_conta(conta_dest, numero_conta_dest, ler_conta):
                valor = ler_valor(tipo_operacao)
                eh_menor, valor = saldo_insuficiente(valor, conta_orig.saldo_total, tipo_operacao)
                if eh_menor:
                    conta_orig.transferir(conta_dest, valor)

def listar_contas():

    if possui_contas():
        print('\t\t Lista de Contas')
        print('\t\t ' + '*' * 40)
        for conta in contas:
            print(conta)
            print('\t\t ' + '*' * 40)


def listar_clientes():

    if possui_clientes():
        print('\t\t Lista de Clientes')
        print('\t\t '+'*' * 40)
        for cliente in clientes:
            print(cliente)
            print('\t\t '+'*' * 40)


def pesquisar_conta():
    if possui_contas():
        numero_conta = int(input('Digite o número da conta que deseja pesquisar: '))
        conta = buscar_conta_por_numero(numero_conta)

        if conta:
            print(conta)
            sleep(2)
        else:
            print(f'Não foram encontradas contas com o número {numero_conta}. Verifique o número da conta!!')
            pesquisar_conta()


def pesquisar_cliente():
    if possui_clientes():
        numero_cliente = int(input('Digite o ID do cliente que deseja pesquisar: '))
        cliente = buscar_cliente_por_numero(numero_cliente)

        if cliente:
            print(cliente)
            sleep(2)
        else:
            print(f'Não encontramos cliente(s) com o número {numero_cliente}. Verifique o ID do cliente!!')
            pesquisar_cliente()


def imprimir_extrato():
    if possui_contas():
        numero_conta = int(input('Digite o número da conta que deseja verificar o extrato: '))
        conta = buscar_conta_por_numero(numero_conta)

        if conta:
            conta.exibir_extrato()
            sleep(2)
        else:
            print(f'Não foram encontradas contas com o número {numero_conta}. Verifique o número da conta!!')
            imprimir_extrato()

def buscar_conta_por_numero(numero_conta):

    for conta in contas:
        if numero_conta == conta.numero:
            return conta
    return None


def buscar_cliente_por_numero(id_cliente):

    for cliente in clientes:
        if id_cliente == cliente.id_cliente:
            return cliente
    return None


def valor_maior_q_zero(valor, tipo_operacao):
    if valor <= 0:
        print('\t\t Valor inválido!! Por favor digite um valor maior que 0, para efetuar sua operação!!')
        valor = ler_valor(tipo_operacao)
        return valor_maior_q_zero(valor, tipo_operacao)
    else:
        return True, valor


def saldo_insuficiente(valor, saldo_total, tipo_operacao):
    valida_valor, valor = valor_maior_q_zero(valor, tipo_operacao)

    if valida_valor:
        if valor > saldo_total:
            print(f'\t\t Você não possui saldo suficiente para saque!!\n\t\t Saldo Total: R$ {saldo_total: .2f}!!')
            valor = ler_valor(tipo_operacao)
            return saldo_insuficiente(valor, saldo_total, tipo_operacao)
        else:
            return True, valor

def valida_conta(conta, numero_conta, funcao_banco):
    if conta:
        return True
    else:
        print(f'Não foram encontradas contas com o número {numero_conta}. Verifique o número da conta!!')
        funcao_banco()

def ler_conta(msg='Digite a conta para a qual deseja transferir: '):
    numero_conta = int(input(msg))
    conta = buscar_conta_por_numero(numero_conta)

    return conta, numero_conta
def ler_valor(tipo_operacao):
    valor = float(input(f"Informe o valor que deseja {tipo_operacao}: R$ "))
    return valor


def possui_contas():
    return True if len(contas) > 0 else print('\t\t Ainda não possuem contas cadastradas!!')


def possui_clientes():
    return True if len(clientes) > 0 else print('\t\t Ainda não possuem clientes cadastrados!!')


if __name__ == '__main__':
    application()
