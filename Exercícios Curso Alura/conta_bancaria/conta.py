class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto... Localização: {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print(f"O saldo da conta do titular {self.__titular} é de R$ {self.__saldo:.2f}")
    
    def depositar(self, valor):
        self.__saldo += valor
        
    def sacar(self, valor):
        self.__saldo -= valor
        
    def transfere(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        

conta1 = Conta(496256, 'Gabriel Gilberto', 660, 2500)
conta2 = Conta(496854, 'Emmanuel Nicolas', 5500, 10000)

print(conta1._Conta__saldo)
print(conta2._Conta__saldo)
conta2.transfere(10, conta1)
conta1.extrato()
conta2.extrato()