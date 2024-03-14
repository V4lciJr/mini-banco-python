from utils.helper import *
from datetime import date


class Cliente:
    id = 100

    def __init__(self, nome, cpf, data_nascimento, email):
        self.__id_cliente = Cliente.id
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__data_cadastro = date.today()
        self.__data_nascimento = str_for_date(data_nascimento)
        Cliente.id += 1

    @property
    def id_cliente(self):
        return self.__id_cliente

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def email(self):
        return self.__email

    @property
    def data_cadastro(self):
        return date_for_str(self.__data_cadastro)

    @property
    def data_nascimento(self):
        return date_for_str(self.__data_nascimento)

    def __str__(self):
        return f'''        ID Cliente - {self.id_cliente}
        Nome: {self.nome}
        CFP: {self.__cpf}
        E-mail: {self.email}
        Data de Cadastro: {date_for_str(self.__data_cadastro)}'''
