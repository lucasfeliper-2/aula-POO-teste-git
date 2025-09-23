'''2 - Desenvolva um programa em Python utilizando orientação a objetos para simular o funcionamento de um
carrinho de compras.'''
'''Crie uma classe chamada Produto, com atributos privados __nome, __preco __descrição e __quantidade'''#Ok, 
'''e, implemente métodos públicos para acessar e modificar esses dados de forma segura (getters e setters)'''#OK.
'''Em seguida, implemente a classe CarrinhoDeCompras, que armazena uma lista de objetos Produto e oferece
Funcionalidades para adicionar produtos, remover produtos pelo nome, calcular o valor total da compra e
exibir os itens do carrinho com suas respectivas informações'''#OK.
'''O programa principal deve apresentar um menu interativo no console, permitindo ao usuário realizar
operações como incluir e excluir produtos, visualizar o conteúdo do carrinho e consultar o total da compra'''#OK.
'''Utilize boas práticas de encapsulamento e organização orientada a objetos para garantir a integridade dos
dados'''#OK

# Definição da classe Produto
class Produto:
    def __init__(self, nome: str, preco: float, descricao: str, quantidade: int = 1):
        # Inicializa os atributos privados como None
        self.__nome = None
        self.__preco = None
        self.__quantidade = None
        self.__descricao = None

        # Usa os setters para aplicar as validações na criação do objeto
        self.set_nome(nome)
        self.set_preco(preco)
        self.set_quantidade(quantidade)
        self.set_descricao(descricao)

    # Getter para o nome
    def get_nome(self) -> str:
        return self.__nome

    # Getter para o preço
    def get_preco(self) -> float:
        return self.__preco

    # Getter para a quantidade
    def get_quantidade(self) -> int:
        return self.__quantidade

    # Getter para a descricao
    def get_descricao(self) -> str:
        return self.__descricao

    # Setter para o nome (com validação)
    def set_nome(self, nome: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Nome deve ser uma string não vazia.")
        self.__nome = nome.strip()

    # Setter para o preço (com validação)
    def set_preco(self, preco: float):
        try:
            preco = float(preco)
        except (TypeError, ValueError):
            raise ValueError("Preço deve ser um número.")
        if preco < 0:
            raise ValueError("Preço não pode ser negativo.")
        self.__preco = preco

    # Setter para a quantidade (com validação)
    def set_quantidade(self, quantidade: int):
        if not isinstance(quantidade, int):
            try:
                quantidade = int(quantidade)
            except Exception:
                raise ValueError("Quantidade deve ser um inteiro.")
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        self.__quantidade = quantidade

    # Setter para a descricao (com validação)
    def set_descricao(self, descricao: str):
        if not isinstance(descricao, str) or descricao.strip() == "":
            raise ValueError("Descrição deve ser uma string não vazia.")
        self.__descricao = descricao.strip()

    # Método para exibir o produto em formato de string
    def __str__(self):
        return f"{self.get_nome()} — {self.get_descricao()} — R$ {self.get_preco():.2f} x {self.get_quantidade()}"

    # Método que retorna o subtotal (preço * quantidade)
    def subtotal(self) -> float:
        return self.get_preco() * self.get_quantidade()


# Definição da classe CarrinhoDeCompras
class CarrinhoDeCompras:
    def __init__(self):
        # Lista privada que armazenará objetos Produto
        self.__produtos = []

    # Método para adicionar um produto ao carrinho
    def adicionar_produto(self, produto: Produto):
        if not isinstance(produto, Produto):
            raise TypeError("Só é permitido adicionar objetos do tipo Produto.")

        nome = produto.get_nome().lower()

        for p in self.__produtos:
            if p.get_nome().lower() == nome:
                nova_qt = p.get_quantidade() + produto.get_quantidade()
                p.set_quantidade(nova_qt)
                return
        self.__produtos.append(produto)

    # Método para remover um produto pelo nome
    def remover_produto_por_nome(self, nome: str) -> bool:
        if not isinstance(nome, str) or nome.strip() == "":
            return False
        alvo = nome.strip().lower()

        for i, p in enumerate(self.__produtos):
            if p.get_nome().lower() == alvo:
                del self.__produtos[i]
                return True
        return False

    # Método para calcular o total da compra
    def calcular_total(self) -> float:
        total = 0.0
        for p in self.__produtos:
            total += p.subtotal()
        return total

    # Método que retorna a lista de produtos
    def listar_produtos(self) -> list:
        return list(self.__produtos)

    # Método que verifica se o carrinho está vazio
    def esta_vazio(self) -> bool:
        return len(self.__produtos) == 0


# Função principal com menu interativo
def main():
    carrinho = CarrinhoDeCompras()

    MENU = '''
            ============================
            Carrinho de Compras - Menu
            ============================
            1 - Adicionar produto
            2 - Remover produto por nome
            3 - Listar produtos
            4 - Mostrar total da compra
            5 - Sair
        '''
    while True:
        print(MENU)
        opc = input("Escolha uma opção (1-5): ").strip()

        if opc == "1":
            try:
                nome = input("Nome do produto: ").strip()
                preco_str = input("Preço unitário (ex: 12.50): ").strip()
                qt_str = input("Quantidade (inteiro, padrão 1): ").strip() or "1"
                descricao = input("Descrição (ex: Banana prata): ").strip()

                preco = float(preco_str)
                quantidade = int(qt_str)

                # NOTE: aqui passamos descricao antes da quantidade
                prod = Produto(nome, preco, descricao, quantidade)
                carrinho.adicionar_produto(prod)
                print(f"Produto '{prod.get_nome()}' adicionado/atualizado com sucesso.\n")
            except Exception as e:
                print(f"Erro ao adicionar produto: {e}\n")

        elif opc == "2":
            nome = input("Nome do produto a remover: ").strip()
            if carrinho.remover_produto_por_nome(nome):
                print(f"Produto '{nome}' removido do carrinho.\n")
            else:
                print(f"Produto '{nome}' não encontrado no carrinho.\n")

        elif opc == "3":
            if carrinho.esta_vazio():
                print("O carrinho está vazio.\n")
            else:
                print("Produtos no carrinho:")
                for p in carrinho.listar_produtos():
                    print(f" - {p} (subtotal: R$ {p.subtotal():.2f})")
                print("")

        elif opc == "4":
            total = carrinho.calcular_total()
            print(f"Total da compra: R$ {total:.2f}\n")

        elif opc == "5":
            print("Encerrando. Obrigado!")
            break

        else:
            print("Opção inválida. Escolha entre 1 e 5.\n")


# Executa o programa apenas se for o arquivo principal
if __name__ == "__main__":
    main()
