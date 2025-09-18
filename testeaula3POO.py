'''from abc import ABC, abstractmethod

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
#print(obj.metodo2(42))'''

'''try:
    x = int(input("Digite um número: "))
    resultado = 10 / x
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Não é possível dividir por zero!")'''
'''
try:
    x = int(input("Digite um número: "))
    resultado = 10 / x
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Operação finalizada.")'''

'''try:
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    print(f"Resultado: {a / b}")
except ValueError:
    print("Erro: Você deve digitar apenas números.")
except ZeroDivisionError:
    print("Erro: Não pode dividir por zero.")'''

'''
try:
    arquivo = open("inexistente.txt")
except Exception as erro:
    print(f"Ocorreu um erro: {erro}")'''
'''
entrada = int(input("Entrada: "))

if entrada < 0:
  raise Exception("Valor negativo!")
else:
  print("Continua....")
'''

'''def registrar_nota(nome_aluno, nota):
    if nota < 0 or nota > 10:
        raise ValueError(f"A nota de {nome_aluno} está fora do intervalo permitido (0 a 10).")
    print(f"Nota {nota} registrada com sucesso para o aluno {nome_aluno}.")

try:
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno (0 a 10): "))
   
    registrar_nota(nome, nota)

except ValueError as erro:
    print("Erro:", erro)

print("Programa continua...")
'''
'''class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def ver_saldo(self):
        print(f"\nSaldo atual de {self.titular}: R${self.saldo:.2f}")

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.") #dentro da função, interrompe apenas a função
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise Exception("Saldo insuficiente para saque.")
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

class SistemaBancario:
    def __init__(self):
        self.nome = input("Digite o nome do titular da conta: ")
        self.conta = ContaBancaria(self.nome, saldo_inicial=1000.0)

    def exibir_menu(self):
        while True:
            print(f"Olá : {self.nome}")
            try:
                print("\n--- Menu Bancário ---")
                print("1. Ver saldo")
                print("2. Depositar")
                print("3. Sacar")
                print("4. Sair")
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    self.conta.ver_saldo()
                elif opcao == 2:
                    valor = float(input("Digite o valor para depósito: "))
                    self.conta.depositar(valor)
                elif opcao == 3:
                    valor = float(input("Digite o valor para saque: "))
                    self.conta.sacar(valor)
                elif opcao == 4:
                    print("Saindo do sistema. Até logo!")
                    break
                else:
                  print("Opção inválida. Escolha entre 1 e 4.")

            except Exception as erro:
                print(f"\nOcorreu um erro: {erro}")
            #raise TypeError("Tipo errado, esperava um inteiro!") # interrompe o programa todo

sistema = SistemaBancario()
sistema.exibir_menu()'''

'''class NotaInvalidaError(Exception):
    pass

def cadastrar_nota(nota):
    if nota < 0 or nota > 10:
        raise NotaInvalidaError("A nota deve estar entre 0 e 10.")
    print("Nota registrada com sucesso!")

try:
    cadastrar_nota(5)
except NotaInvalidaError as e:
    print(f"Erro: {e}")
    # Exceções personalizadas'''


class LimiteEmprestimosError(Exception):
    """Erro lançado quando o usuário ultrapassa o limite de empréstimos."""
    pass

class LivroIndisponivelError(Exception):
    """Erro lançado quando o livro já está emprestado."""
    pass

# Classe Livro
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False

# Classe Usuario
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) >= 3:
            raise LimiteEmprestimosError(f"{self.nome} já possui 3 livros emprestados.")
        if livro.emprestado:
            raise LivroIndisponivelError(f"O livro '{livro.titulo}' já está emprestado.")

       
        livro.emprestado = True
        self.livros_emprestados.append(livro)
        print(f"{self.nome} emprestou o livro '{livro.titulo}' com sucesso.")

# Simulação
try:
    livro1 = Livro("O Alienista")
    livro2 = Livro("O Alquimista")
    livro3 = Livro("A Revolução dos Bichos")
    livro4 = Livro("O Homen Invisível")

    usuario = Usuario("Ana")

    usuario.emprestar_livro(livro1)
    usuario.emprestar_livro(livro2)
    #usuario.emprestar_livro(livro2) # Deve lançar exceção
    usuario.emprestar_livro(livro3)
    #usuario.emprestar_livro(livro4)  # Deve lançar exceção

except LimiteEmprestimosError as e:
    print("Erro de limite:", e)

except LivroIndisponivelError as e:
    print("Erro de disponibilidade:", e)