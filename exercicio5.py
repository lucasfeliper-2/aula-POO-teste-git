'''Implemente uma classe Impressora com o método imprimir(Documento d), que recebe um objeto da classe Documento e 
imprime suas informações na tela. A classe Documento deve conter os atributos título e conteúdo. 
A classe Impressora apenas utiliza o documento, sem manter uma referência permanente a ele, 
caracterizando uma relação de dependência. Desenvolva um programa com um menu interativo no console que permita 
criar vários documentos, visualizar seu conteúdo por meio da impressora e encerrar o programa.'''

'''class impressora:
    def imprimir(self, documento):
        print(f"Título: {documento.titulo}")
        print(f"Conteúdo: {documento.conteudo}")

class documento:
    def _init_(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

def main():
    impressora1 = impressora()
    documentos = []
    
    while True:
        print("\nMenu:")
        print("1. Criar Documento")
        print("2. Imprimir Documento")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            titulo = input("Digite o título do documento: ")
            conteudo = input("Digite o conteúdo do documento: ")
            doc = documento(titulo, conteudo)
            documentos.append(doc)
            print("Documento criado com sucesso!")
        
        elif escolha == '2':
            if not documentos:
                print("Nenhum documento disponível para imprimir.")
                continue
            
            for idx, doc in enumerate(documentos):
                print(f"{idx + 1}. {doc.titulo}")
            
            doc_index = int(input("Escolha o número do documento para imprimir: ")) - 1
            
            if 0 <= doc_index < len(documentos):
                impressora1.imprimir(documentos[doc_index])
            else:
                print("Número inválido.")
        
        elif escolha == '3':
            print("Encerrando o programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if _name_ == "_main_":
    main()
    '''

# código corrigido e melhorado


# Classe Documento
class Documento:
    def _init_(self, titulo: str, conteudo: str):
        # Atributos privados
        self.__titulo = titulo
        self.__conteudo = conteudo

    # Getter para o título
    def get_titulo(self) -> str:
        return self.__titulo

    # Getter para o conteúdo
    def get_conteudo(self) -> str:
        return self.__conteudo


# Classe Impressora
class Impressora:
    def imprimir(self, documento: Documento):
        # Imprime os dados de um documento na tela
        print("\n--- Impressão do Documento ---")
        print(f"Título: {documento.get_titulo()}")
        print(f"Conteúdo: {documento.get_conteudo()}")
        print("------------------------------\n")

# Função principal com menu
def main():
    # Lista que armazenará os documentos criados
    documentos = []

    # Cria uma impressora (objeto único que apenas usa documentos)
    impressora = Impressora()

    # Texto do menu
    MENU = """
    =============================
         Sistema de Impressão
    =============================
    1 - Criar documento
    2 - Listar documentos
    3 - Imprimir documento
    4 - Sair
    """

    # Loop principal
    while True:
        print(MENU)  # Exibe o menu
        opc = input("Escolha uma opção (1-4): ").strip()

        # Opção 1 - Criar documento
        if opc == "1":
            titulo = input("Digite o título do documento: ").strip()
            conteudo = input("Digite o conteúdo do documento: ").strip()

            doc = Documento(titulo, conteudo)  # Cria o documento
            documentos.append(doc)  # Armazena na lista
            print(f"Documento '{titulo}' criado com sucesso!\n")

        # Opção 2 - Listar documentos
        elif opc == "2":
            if not documentos:  # Se a lista estiver vazia
                print("Nenhum documento foi criado ainda.\n")
            else:
                print("\nDocumentos disponíveis:")
                for i, doc in enumerate(documentos):
                    print(f"{i+1}. {doc.get_titulo()}")
                print("")

        # Opção 3 - Imprimir documento
        elif opc == "3":
            if not documentos:
                print("Não há documentos para imprimir.\n")
            else:
                # Mostra os documentos disponíveis
                print("\nEscolha o número do documento para imprimir:")
                for i, doc in enumerate(documentos):
                    print(f"{i+1}. {doc.get_titulo()}")

                try:
                    escolha = int(input("Número do documento: ").strip())
                    # Ajusta o índice (usuário digita a partir de 1)
                    if 1 <= escolha <= len(documentos):
                        impressora.imprimir(documentos[escolha - 1])
                    else:
                        print("Opção inválida!\n")
                except ValueError:
                    print("Entrada inválida! Digite apenas números.\n")

        # Opção 4 - Sair
        elif opc == "4":
            print("Encerrando o programa. Até mais!")
            break

        # Opção inválida
        else:
            print("Opção inválida. Escolha entre 1 e 4.\n")


# Executa o programa somente se for chamado diretamente
if _name_ == "_main_":
    main()