#classe pessoa
#atributos: nome, idade
#métodos para diminuir e aumentar a idade

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def diminuiIdade(self, valor=1):
        self.idade -= valor
    def aumentaIdade(self, valor=1):
        self.idade += valor

p1 = Pessoa('João', 30)
p2 = Pessoa('Maria', 25)

print(f'{p1.nome} tem {p1.idade} anos.')
print(f'{p2.nome} tem {p2.idade} anos.')

p1.aumentaIdade(10)
print(p1.nome, 'agora tem', p1.idade, 'anos.')
p2.diminuiIdade(5)
print(p2.nome, 'agora tem', p2.idade, 'anos.')