class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.__matricula = matricula
        self.__emprestimos = list ()

    def getMatricula(self):
        return self.__matricula
    def setMatricula(self, nova_matricula):
        self.__matricula = nova_matricula

    def emprestar_livro(self, livro):
        if not livro in self.__emprestimos:
            self.__emprestimos.append(livro)
            return True
        else:
            return False
    
    def devolver_livro(self, livro):
        if livro in self.__emprestimos:
            self.__emprestimos.remove(livro)
            return True
        else:
            return False
    def listar_emprestimos(self):
        if self.__emprestimos:
            for livro in self.__emprestimos:
                print(f"Título: {livro.get_titulo()}, Autor: {livro.get_autor()}, ID: {livro.getID()}")
        else:
            print("Nenhum livro emprestado.")

        