'''Crie código que demonstre uma hierarquia de classes relacionada a animais. O programa deve conter:
Uma classe base chamada Animal, que possui:
 Um atributo nome.
Um método chamado falar() que imprime uma mensagem genérica indicando que o animal está fazendo um som.
Uma classe derivada chamada Cachorro, que herda de Animal e possui:
Um atributo adicional raca.
O método __init__() deve utilizar super() para chamar o construtor da classe Animal.
Um método  falar()  sobrescreve o da classe base, utilizando super()  para reaproveitar a mensagem genérica e adicionar uma mensagem específica de cachorro.
Crie uma instância da classe Cachorro e exiba o resultado
'''

class Operacoes:
    def somar(self, a, b):
        if isinstance(a, int) and isinstance(b, int):  # Ambos inteiros
            return a + b
        elif isinstance(a, str) and isinstance(b, str):  # Ambos strings
            return a + " " + b
        else:
            return "Operação invalida: os argumentos devem ser ambos inteiros ou ambos strings."

op = Operacoes()

print(op.somar(3, 4))             # 7
print(op.somar("Olá", "Mundo"))   # "Olá Mundo"
print(op.somar(3, "Mundo"))       # Operação inválida...