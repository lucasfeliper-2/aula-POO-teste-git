'''Crie um sistema para gerenciar contas de uma biblioteca. 
Implemente uma classe Livro, com atributos como título, autor e um identificador único (ID), 
sendo que todos devem ser privados. A classe deve conter um construtor para inicializar os dados e métodos públicos para acessar (get) e modificar (set) os atributos, respeitando o encapsulamento. Em seguida, crie uma classe Usuario, com atributos como nome, número de matrícula (privado) e uma lista de livros emprestados. Adicione métodos públicos para realizar empréstimos e devoluções de livros, 
garantindo que a matrícula seja acessada e modificada apenas por métodos da própria classe.
#Criar um menu:
1. listar usuários 
2. listar livros
3. emprestar livro
4. devolver livro
5. Listar livros emprestados por usuário
6. Sair
'''

from livros import Livro
from usuarios import Usuario

# criando alguns livros
livro1 = Livro("George Orwell", "1984")
livro2 = Livro("Harper Lee", "To Kill a Mockingbird")
livro3 = Livro("J.R.R. Tolkien", "The Hobbit")

# criando alguns usuários
usuario1 = Usuario("Alice", "12345")
usuario2 = Usuario("Bob", "67890")

# realizando empréstimos
usuario1.emprestar_livro(livro1)
usuario1.emprestar_livro(livro2)
usuario2.emprestar_livro(livro3)

# listando empréstimos
print(f"Lista de empréstimos de {usuario1.nome}, Matricula: {usuario1.getMatricula()}:")
usuario1.listar_emprestimos()
print(f"\nLista de empréstimos de {usuario2.nome}, Matricula: {usuario2.getMatricula()}:")
usuario2.listar_emprestimos()

# realizando devoluções
usuario1.devolver_livro(livro1)
usuario2.devolver_livro(livro3)

print(f"\nLista de empréstimos de {usuario1.nome}, Matricula: {usuario1.getMatricula()}:")
usuario1.listar_emprestimos()
print(f"\nLista de empréstimos de {usuario2.nome}, Matricula: {usuario2.getMatricula()}:")
usuario2.listar_emprestimos()

