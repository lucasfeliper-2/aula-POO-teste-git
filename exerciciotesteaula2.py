'''Criar uma classe utilizando, método construtor, atributos de classe, atributos estáticos, 
atributos de instância, métodos de classe e métodos de instância. 
Os atributos devem ser privados e acessados somente via métodos públicos getters e setters'''

class ContaBancaria:
    def __init__(self, titular, saldo, senha):

        
        '''self.titular = titular          # Atributo público
        self.__saldo = saldo            # Atributo privado
        self.__senha = senha            # Atributo privado

    def getSaldo(self):                # Método getter para saldo
        return self.__saldo

    def getSenha(self):                # Método getter para senha
        return self.__senha

    def setSenha(self, nova_senha):    # Método setter para senha
        self.__senha = nova_senha'''


conta = ContaBancaria("Ana", 1000, 123)

print(conta.titular)         # Acesso direto (ok)
# print(conta.__saldo)       # ERRO! atributo privado

print(conta.getSaldo())     # Acesso indireto via getter
conta.getSenha()            # Acesso indireto via getter
print(conta.getSenha())     # Acesso indireto via getter
conta.setSenha(456)         # Acesso indireto via setter
print(conta.getSenha())     # Acesso indireto via getter