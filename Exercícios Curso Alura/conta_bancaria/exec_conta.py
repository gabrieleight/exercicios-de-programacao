from conta import Conta

conta1 = Conta(496256, 'Gabriel Gilberto', 660, 2500)
conta2 = Conta(496854, 'Emmanuel Nicolas', 5500, 10000)

print(conta1._Conta__saldo)
print(conta2._Conta__saldo)
conta2.transfere(10, conta1)
conta1.extrato()
conta2.extrato()