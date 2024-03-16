from models.cliente import Cliente
from models.conta import Conta

cliente_1 = Cliente('José', '125.524.125.65', '19/12/1990', 'jose@gmail.com')
cliente_2 = Cliente('Valci', '125.524.125.65', '03/05/1964', 'valci@gmail.com')
conta_1 = Conta(cliente_1)
conta_2 = Conta(cliente_2)

print(conta_1)
print(cliente_1)

