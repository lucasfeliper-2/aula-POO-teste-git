'Criar uma classe utilizando, método construtor OK,atributos de classe OK, atributos estáticos,'
'atributos de instância, métodos de classe e métodos de instância.'

class Estudante:
    #atributos de classe
    escola = 'Técnica'
    ESTADO = 'DF'
    contadorEstudantes = 0

 #método construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Estudante.contadorEstudantes += 1

 #método de instância - modifica atributos da instância
    def atualizaIdade(self, novaIdade=1):
        self.idade += novaIdade


 #métodos de classe - modifica apenas atributos da classe
    @classmethod
    def modificaEscola(cls, novaEscola):
        cls.escola = novaEscola

p1 = Estudante('Ana', 12)
p2 = Estudante('Carlos', 14)

print(f"Quantidade de estudantes: {Estudante.contadorEstudantes}")
print(f"{p1.nome} tem {p1.idade} anos e estuda na escola {p1.escola}, do {p1.ESTADO}.")
print(f"{p2.nome} tem {p2.idade} anos e estuda na escola {p2.escola}. do {p2.ESTADO}.")

p1.atualizaIdade()
print(f"{p1.nome} agora tem {p1.idade} anos.")

p1.modificaEscola('Faculdade')
print(f"{p1.nome} estuda agora na {p1.escola}.")