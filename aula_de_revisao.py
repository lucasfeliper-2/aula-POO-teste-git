'''Crie código que demonstre uma hierarquia de classes relacionada a animais. 
O programa deve conter:
Uma classe base chamada Animal, que possui:
 Um atributo nome.
Um método chamado falar() que imprime uma mensagem genérica indicando que o animal
está fazendo um som.
Uma classe derivada chamada Cachorro, que herda de Animal e possui:
Um atributo adicional raca.
O método __init__() deve utilizar super() para chamar o construtor da classe Animal.
Um método  falar()  sobrescreve o da classe base, utilizando super()  
para reaproveitar a mensagem genérica e adicionar uma mensagem específica de cachorro.
Crie uma instância da classe Cachorro e exiba o resultado.'''

'''class Animal:
    def __init__(self, nome, olhos):
        self.nome = nome
        self.olhos = olhos

    def falar(self):
        print(f"{self.nome} está latindo 'iuuuuuuuuu'.")

class Cachorro(Animal):
    def __init__ (self, nome, raca, olhos):
        #puxa o init da classe mãe Animal
        super().__init__(nome, olhos)
        self.raca = raca

    def falar(self):
        super().falar() #chama o método falar da classe mãe
        print(f"{self.nome} é um cachorro da raça {self.raca}.")

cachorro1 = Cachorro("Rambo", "pincher", 2)
cachorro1.falar()
print(f"O cachorro {cachorro1.nome} têm os {cachorro1.olhos} olhos pretos.")
'''
'''
Crie código que demonstre uma hierarquia de classes relacionada a veículos. O programa deve conter:
Uma classe base Veiculo, que possui:
 Um atributo marca.
Um método chamado descricao() que imprime uma mensagem genérica indicando a marca do veículo.
Uma classe derivada chamada Carro, que herda de Veiculo e possui:
Um atributo adicional modelo.
O método __init__() deve utilizar super() para chamar o construtor da classe Veiculo.
Um método  descricao()  sobrescreve o da classe base, utilizando super()  
para reaproveitar a mensagem genérica e adicionar uma mensagem específica com o atributo modelo.
Crie uma instância da classe e exiba o resultado'''

class Veiculo:
    def __init__ (self,marca):
        self.marca = marca

    def descricao(self):
        print(f"Este veículo é da marca {self.marca}.")

class Carro(Veiculo):
    #he
    def __init__ (self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

    def descricao(self):
        super().descricao()
        print(f"Este carro é um modelo {self.modelo}.")

carro1 = Carro("Chevrolet", "Onix")
carro1.descricao()




