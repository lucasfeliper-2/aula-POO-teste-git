'''class Pessoa:
    def __init__(self, nome):
        self.__nome = nome  # atributo "privado"

#Internamente, o Python transforma __nome em:
#_NomeDaClasse__nomeDoAtributo
#_Pessoa__nome

#Isso significa que:
p = Pessoa("Ana")

# Acesso direto falha
print(p.__nome)  # AttributeError

# Mas ainda é acessível por:
print(p._Pessoa__nome)  # Ana'''

'''class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular        # público
        self._banco = "Banco XYZ"     # protegido (convenção)
        self.__saldo = saldo          # privado (name mangling)
    

    def exibir_saldo(self):
        print(f"Saldo: R$ {self.__saldo:.2f}")

conta = Conta("João", 1000)

print(conta.titular)     # OK: público
print(conta._banco)      # OK, mas uso interno por convenção
#print(conta.__saldo)   # ERRO: atributo privado

print(conta._Conta__saldo)  # Acesso por name mangling deve ser evitado

conta.exibir_saldo()        # Modo correto de acessar, via método
'''
'''class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str):
        self.nome = nome              # público
        self._idade = idade           # protegido (por convenção)
        self.__cpf = cpf              # privado (name mangling)

    def cumprimentar(self) -> None:
        print(f"Olá, meu nome é {self.nome}.")

    def _calcular_idade(self) -> int:
        pass

    def __validar_cpf(self) -> str:
        pass'''

#setters significa definir um valor
#getters significa obter um valor
#setters e getters são métodos especiais usados para acessar e modificar atributos privados de uma classe.

class ContaBancaria:
    def __init__(self, titular, saldo_inicial, senha):
        self.titular = titular              # público
        self.__saldo = saldo_inicial        # privado
        self.__senha = senha                # privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
           
    def getSaldo(self):
        return self.__saldo

    def getSenha(self):                
        return self.__senha

    def setSenha(self, novaSenha):      
        self.__senha = novaSenha

conta = ContaBancaria("Ana", 1000, 123)

print(conta.titular)         # Acesso direto (ok)
# print(conta.__saldo)       # ERRO! atributo privado

print(conta.getSaldo())     # Acesso indireto via getter
conta.getSenha()            # Acesso indireto via getter
print(conta.getSenha())     # Acesso indireto via getter
conta.setSenha(456)         # Acesso indireto via setter
print(conta.getSenha())     # Acesso indireto via getter