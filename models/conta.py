from utils.helper import format_float_for_str, date_for_str
from datetime import date


class Conta:
    codigo = 1001
    limite = 200

    def __init__(self, cliente):
        self.__numero = Conta.codigo
        self.__cliente = cliente
        self.__saldo = 0
        self.__limite = Conta.limite
        self.__saldo_total = self.__calcula_saldo_total
        self.__extrato = ''
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
    def _saldo(self, valor):
        self.__saldo = valor

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def _limite(self, valor):
        self.__limite = valor

    @property
    def saldo_total(self):
        return self.__saldo_total

    @saldo_total.setter
    def _saldo_total(self, valor):
        self.__saldo_total = valor

    @property
    def extrato(self):
        return self.__extrato

    @extrato.setter
    def _extrato(self, msg):
        self.__extrato = msg

    @property
    def __calcula_saldo_total(self):
        return self.saldo + self.limite

    def __str__(self):
        return f'''         Número da Conta: {self.numero}
         Cliente:                   {self.cliente.nome}
         Saldo:                     {format_float_for_str(self.saldo)}
         Limite de Cheque Especial: {format_float_for_str(self.limite)}
         Saldo Total:               {format_float_for_str(self.saldo_total)}'''

    def depositar(self, valor):

        self._saldo += valor
        self._saldo_total = self.__calcula_saldo_total
        if self.saldo <= 0 and self.limite < Conta.limite and valor <= Conta.limite:
            self.limite += valor
        self._extrato += f'\t\t => Depósito    R$ {valor:.2f}    {date_for_str(date.today())}\n'
        print(f'Valor de R$ {valor:.2f} depositados com sucesso!!')
        print(f'Saldo Atual R$ {self.saldo_total:.2f}')


    def sacar(self, valor, msg):

        if valor <= self.saldo:
            self._saldo -= valor
            self._saldo_total = self.__calcula_saldo_total
        else:
            resto = self.saldo - valor
            if self.limite >= resto:
                self._limite += resto
                self._saldo = resto
                self._saldo_total = self.__calcula_saldo_total
            else:
                print(f'\t\t Saque não efetuado!! Valor maior que o limite de cheque especial.\n\t\t Limite: R$ {self.limite:.2f}.')

        self._extrato += f'\t\t => Saque      -R$ {valor:.2f}    {date_for_str(date.today())}\n'
        print(f'{msg} {valor:.2f} efetuado com sucesso!!')
        print(f'Saldo Atual R$ {self.saldo_total:.2f}')

    def transferir(self, conta_destino, valor):
        self.sacar(valor, 'Transferência de R$')
        conta_destino.depositar(valor)
    def exibir_extrato(self):
        print('\t\t ************** Extrato *****************')
        print('\t\t -  Operação   | Valor R$   | Data  -')
        print('\t\t Não foram realizadas movimentações!!' if not self.extrato else self.extrato)
        print('\n\t\t ' + '*' * 40)
        print(f'\t\t Saldo:                    {format_float_for_str(self.saldo)}')
        print(f'\t\t Limite Cheque Especial:   {format_float_for_str(self.limite)}')
        print(f'\n\t\t Saldo Total:              {format_float_for_str(self.saldo_total)}')
        print('\t\t ' + '*' * 40)


