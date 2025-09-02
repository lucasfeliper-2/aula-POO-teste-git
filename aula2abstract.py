'''from abc import ABC, abstractmethod
class Animal(ABC):  # Herda de ABC, tornando-se abstrata

    @abstractmethod
    def emitirSom(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Cachorro(Animal):

    def emitirSom(self):
        return "Au au!"

    def mover(self):
        return "Correndo com as patas"

class Peixe(Animal):

    def emitirSom(self):
        return "Blublublu"

    def mover(self):
        return "Nadando"
    
c = Cachorro()

print(c.emitirSom())  
# Saída: Au au!

p = Peixe()

print(p.emitirSom()) 
# Saída:  Blublublu'''

'''from abc import ABC, abstractmethod

class Pagamento(ABC):

    @abstractmethod
    def pagar(self, valor):
        pass

class CartaoCredito(Pagamento):

    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} com cartão de crédito.")

class Boleto(Pagamento):

    def pagar(self, valor):
        print(f"Gerando boleto no valor de R${valor:.2f}.")

p = CartaoCredito()
p.pagar(100.0)  # Saída: Pagando R$100.00 com cartão de crédito.

p = Boleto()
p.pagar(150.0)  # Saída: Gerando boleto no valor de R$150.00.'''
'''
from abc import ABC, abstractmethod
class Pessoa(ABC):

    @abstractmethod
    def falar(self):
        pass

    def respirar(self):
        print("Pessoa respirando")  # método concreto

class Brasileiro(Pessoa):

    def falar(self):
        print("Olá!")

class Americano(Pessoa):

    def falar(self):
        print("Hello!")

b = Brasileiro()
a = Americano()
b.falar()  # Saída: Olá!
a.falar()  # Saída: Hello!
b.respirar()  # Saída: Pessoa respirando
a.respirar()  # Saída: Pessoa respirando'''
'''
from abc import ABC, abstractmethod
class Exemplo(ABC):
    
    @staticmethod
    @abstractmethod
    def metodoEstatico():
        pass'''

'''from abc import ABC, abstractmethod

class Cavaleiro(ABC):
    def __init__(self, nome, signo, golpeEspecial):
        self.nome = nome
        self.signo = signo
        self.golpeEspecial = golpeEspecial

    #método concreto
    def apresentar(self):
        print(f"Eu sou {self.nome}, Cavaleiro de {self.signo}!")

    #método abstrato
    @abstractmethod
    def usarGolpeEspecial(self):
        pass

class CavaleiroDeBronze(Cavaleiro):
    def usarGolpeEspecial(self):
        print(f"{self.nome} usa o golpe: {self.golpeEspecial}!")

class CavaleiroDeOuro(Cavaleiro):
    def usarGolpeEspecial(self):
        print(f"{self.nome} invoca o golpe supremo: {self.golpeEspecial}!")

seiya = CavaleiroDeBronze("Seiya", "Pegasus", "Meteoro de Pegasus")
shaka = CavaleiroDeOuro("Shaka", "Virgem", "Tesouro do Céu")

seiya.apresentar()
seiya.usarGolpeEspecial()

shaka.apresentar()
shaka.usarGolpeEspecial()
'''

