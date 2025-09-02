from abc import ABC, abstractmethod

class MinhaInterface(ABC):
    @abstractmethod
    def metodo1(self):
        pass

    @abstractmethod
    def metodo2(self, valor):
        pass

class MinhaClasseConcreta(MinhaInterface):
    def metodo1(self):
        return "Implementação do método 1"

    def metodo2(self, valor):
        return f"Implementação do método 2 com valor: {valor}"
    
# Testando a implementação
obj = MinhaClasseConcreta()
print(obj.metodo1())
#print(obj.metodo2(42))
