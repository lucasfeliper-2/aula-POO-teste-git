'''Crie um código para demonstrar dependência de Coordenador e Disciplina.
Coordenador tem nome e um Curso.
Disciplina tem nome e uma ementa.
Coordenador deve ser capaz de exibir a ementa, mas sem manter disciplina como atributo.
Crie os objetos, teste os métodos e exiba as informações.'''


class Disciplina:
    def __init__(self, nome, ementa):
        self.nome = nome
        self.ementa = ementa

    def getEmenta(self):
        return self.ementa

    def getNome(self):
        return self.nome

class Coordenador:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso

    def exibir_ementa(self, disciplina):
        print(f"Ementa da disciplina {disciplina.nome}: {disciplina.ementa}")

# Criando objetos
disciplina1 = Disciplina("Matemática", "Estudo dos números, formas e estruturas.")
coordenador1 = Coordenador("Ana Silva", "Engenharia")
# Testando o método
coordenador1.exibir_ementa(disciplina1)

disciplina2 = Disciplina("Física", "Estudo da matéria, energia e suas interações.")
coordenador2 = Coordenador("Carlos Souza", "Ciências Exatas")
# Testando o método
coordenador2.exibir_ementa(disciplina2)
disciplina3 = Disciplina("Química", "Estudo da composição, estrutura e propriedades da matéria.")
coordenador3 = Coordenador("Mariana Lima", "Ciências Naturais")

