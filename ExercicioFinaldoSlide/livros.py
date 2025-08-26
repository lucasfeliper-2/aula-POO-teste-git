
'''Crie um sistema para gerenciar contas de uma biblioteca. Implemente uma classe Livro, com atributos como título, 
autor e um identificador único (ID), sendo que todos devem ser privados. A classe deve conter um construtor para inicializar os dados e métodos públicos para acessar (get) e modificar (set) os atributos, respeitando o encapsulamento. Em seguida, crie uma classe Usuario, com atributos como nome, número de matrícula (privado) e uma lista de livros emprestados. 
Adicione métodos públicos para realizar empréstimos e devoluções de livros, garantindo que a matrícula seja acessada e modificada apenas por métodos da própria classe.'''

from random import randint
class Livro:
    def __init__(self, autor, titulo):
        self.__autor = autor
        self.__titulo = titulo
        self.__id = randint(1, 100)

    def get_autor(self):
        return self.__autor
    def set_autor(self, novo_autor):
        self.__autor = novo_autor
    def get_titulo(self):
        return self.__titulo    
    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo
    def getID(self):
        return self.__id
    

    