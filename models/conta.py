from utils.helper import format_float_for_str
from utils.exceptions import ValueMenorZero


class Conta:
    codigo = 1001

    def __init__(self, cliente):
        self.__numero = Conta.codigo
        self.__cliente = cliente
        self.__saldo = 0
        self.__limite = 200
        self.__saldo_total = self.__calcula_saldo_total
        Conta.codigo += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        self.saldo = value

    @property
    def limite(self):
        return self.__limite

    @property
    def saldo_total(self):
        return self.__saldo_total

    @property
    def __calcula_saldo_total(self):
        return self.saldo + self.limite

    def __str__(self):
        return f'Número da Conta: {self.numero}\n' \
               f'Cliente: {self.cliente.nome}\n' \
               f'Saldo Total:{format_float_for_str(self.saldo_total)}'

    def depositar(self, valor):
        if valor > 0:
            self.saldo = valor
        else:
            raise ValueMenorZero

    def sacar(self, valor):
        pass

    def transferir(self, conta_destino, valor):
        pass
