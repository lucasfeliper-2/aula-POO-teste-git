'''Criar uma classe utilizando, método construtor, atributos de classe, atributos estáticos, 
atributos de instância, métodos de classe e métodos de instância. 
Os atributos devem ser privados e acessados somente via métodos públicos getters e setters'''

conta = ContaBancaria("Ana", 1000, 123)

print(conta.titular)         # Acesso direto (ok)
# print(conta.__saldo)       # ERRO! atributo privado

print(conta.getSaldo())     # Acesso indireto via getter
conta.getSenha()            # Acesso indireto via getter
print(conta.getSenha())     # Acesso indireto via getter
conta.setSenha(456)         # Acesso indireto via setter
print(conta.getSenha())     # Acesso indireto via getter