from utils.helper import format_float_for_str


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
    def _saldo(self, valor):
        self.__saldo = valor

    @property
    def limite(self):
        return self.__limite

    @property
    def saldo_total(self):
        return self.__saldo_total

    @saldo_total.setter
    def _saldo_total(self, valor):
        self.__saldo_total = valor

    @property
    def __calcula_saldo_total(self):
        return self.saldo + self.limite

    def __str__(self):
        return f'''        Número da Conta: {self.numero}
        Cliente:                   {self.cliente.nome}
        Saldo:                     {format_float_for_str(self.saldo)}
        Limite de Cheque Especial: {format_float_for_str(self.limite)}
        Saldo Total:               {format_float_for_str(self.saldo_total)}'''

    def depositar(self, valor):
        if self.__valor_maior_q_zero(valor):
            self._saldo += valor
            self._saldo_total = self.__calcula_saldo_total
            print(f'Valor de R$ {valor:.2f} depositados com sucesso!!')
            print(f'Saldo Atual R$ {self.saldo_total:.2f}')


    def sacar(self, valor):
        pass

    def transferir(self, conta_destino, valor):
        pass

    def __valor_maior_q_zero(self, valor):
        return True if valor > 0 else print('\t\t Valor inválido!! Por favor digite um valor maior que 0, para efetuar sua operação!!')