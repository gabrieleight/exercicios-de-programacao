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
        
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, novo_limite):
        self.__limite == novo_limite
        
"""  # Exemplo:    
class Cliente:
    def __init__(self, nome):
        self.__nome = nome
    
    # Retorna o nome como método get_nome:    
    @property
    def nome(self):
        return self.__nome.title()
    
    # Muda o nome como método set_nome:
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome    

"""
