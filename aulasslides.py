'''class Aluno:
    escola = "Escola Estadual"  # atributo da classe (compartilhado)
    def __init__(self, nome, idade):
        self.nome = nome       # atributo de instância (único por objeto)
        self.idade = idade


a1 = Aluno("João", 15)

# Atributos de instância
print(a1.nome)   # João
print(a1.idade)  # 15

# Atributo da classe (forma preferida)
print(Aluno.escola)  # Escola Estadual

# Também pode acessar atributo da classe via instância (não recomendado para modificar)
print(a1.escola)     # Escola Estadual'''

'''class Veiculo:
    TIPO = "Transporte"         # Constante (por convenção, atributo de classe)
    categoria = "Terrestre"     # Atributo de classe
    def __init__(self, modelo):
        self.modelo = modelo    # Atributo de instância

# Criando um objeto
carro = Veiculo("Sedan")

# Criando atributo dinâmico diretamente na instância
carro.ano = 2023  # Atributo dinâmico

# ---- ACESSOS POR OBJETO ----
print("Acesso por objeto:")
print("Instância:", carro.modelo)       # Atributo de instância
print("Classe:", carro.categoria)       # Atributo de classe acessado pela instância
print("Constante:", carro.TIPO)         # Constante acessada pela instância
print("Dinâmico:", carro.ano)           # Atributo criado fora da classe

# ---- ACESSOS POR CLASSE ----
print("\nAcesso por classe:")
#print(Veiculo.modelo)  # ERRO: atributo de instância não existe na classe
print("Classe:", Veiculo.categoria)     # Atributo de classe
print("Constante:", Veiculo.TIPO)       # Constante (por convenção)

# carro.ano não está na classe, então não é acessível por Veiculo
# print(Veiculo.ano)  # ERRO: atributo dinâmico pertence só ao objeto'''

class Calculadora:
    fator_global = 10

    def __init__(self, base):
        self.base = base

    # Método de instância
    def somar_fator(self):
        return self.base + self.__class__.fator_global

    # Método de classe
    @classmethod
    def alterar_fator(cls, novo_fator):
        cls.fator_global = novo_fator

    # Método estático
    @staticmethod
    def multiplicar(a, b):
        return a * b

# Criando um objeto
calc = Calculadora(5)

# 1. Método de instância
print(calc.somar_fator())  # 5 + 10 = 15

# 2. Método de classe
Calculadora.alterar_fator(20)  # mudando o fator_global para 20
print(calc.somar_fator())      # 5 + 20 = 25

# 3. Método estático
print(Calculadora.multiplicar(3, 4))  # 12
print(calc.multiplicar(2, 5))         # 10 (também funciona)
