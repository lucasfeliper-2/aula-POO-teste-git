from livros import Livro
from usuarios import Usuario

# Dados simulados para testes
livros = [
    Livro("George Orwell", "1984"),
    Livro("Harper Lee", "To Kill a Mockingbird"),
    Livro("J.R.R. Tolkien", "The Hobbit"),
    Livro("F. Scott Fitzgerald", "The Great Gatsby")
]

usuarios = [
    Usuario("Alice", "12345"),
    Usuario("Bob", "67890"),
    Usuario("Charlie", "11111")
]

# Funções do menu
def listar_usuarios():
    print("\nUsuários cadastrados:")
    for i, u in enumerate(usuarios):
        print(f"{i + 1}. {u.nome} (Matrícula: {u.getMatricula()})")

def listar_livros():
    print("\nLivros disponíveis:")
    for i, l in enumerate(livros):
        print(f"{i + 1}. {l.get_titulo()} - {l.get_autor()} (ID: {l.getID()})")

def emprestar_livro():
    listar_usuarios()
    try:
        usuario_idx = int(input("\nEscolha o número do usuário: ")) - 1
        usuario = usuarios[usuario_idx]
    except (ValueError, IndexError):
        print("Usuário inválido.")
        return

    listar_livros()
    try:
        livro_idx = int(input("\nEscolha o número do livro: ")) - 1
        livro = livros[livro_idx]
    except (ValueError, IndexError):
        print("Livro inválido.")
        return

    if usuario.emprestar_livro(livro):
        print("Livro emprestado com sucesso!")
    else:
        print("Esse livro já foi emprestado por este usuário.")

def devolver_livro():
    listar_usuarios()
    try:
        usuario_idx = int(input("\nEscolha o número do usuário: ")) - 1
        usuario = usuarios[usuario_idx]
    except (ValueError, IndexError):
        print("Usuário inválido.")
        return

    print("\nLivros emprestados:")
    usuario.listar_emprestimos()
    
    try:
        livro_id = int(input("\nDigite o ID do livro a devolver: "))
    except ValueError:
        print("ID inválido.")
        return

    # Encontrar livro emprestado por ID
    for livro in livros:
        if livro.getID() == livro_id:
            if usuario.devolver_livro(livro):
                print("Livro devolvido com sucesso!")
            else:
                print("Este livro não está emprestado a este usuário.")
            return
    print("Livro não encontrado.")

def listar_emprestimos_por_usuario():
    listar_usuarios()
    try:
        usuario_idx = int(input("\nEscolha o número do usuário: ")) - 1
        usuario = usuarios[usuario_idx]
    except (ValueError, IndexError):
        print("Usuário inválido.")
        return

    print(f"\nLivros emprestados por {usuario.nome}:")
    usuario.listar_emprestimos()

# Loop do menu
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Listar usuários")
        print("2. Listar livros")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Listar livros emprestados por usuário")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_usuarios()
        elif escolha == "2":
            listar_livros()
        elif escolha == "3":
            emprestar_livro()
        elif escolha == "4":
            devolver_livro()
        elif escolha == "5":
            listar_emprestimos_por_usuario()
        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
if __name__ == "__main__":
    menu()