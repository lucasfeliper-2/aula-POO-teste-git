'''Crie um programa em Python utilizando orientação a objetos para gerenciar uma lista de produtos de um carrinho 
de compras. 
Implemente uma classe chamada Produto, com atributos privados (__nome, __preco e __quantidade) 
e métodos públicos para acessar e modificar esses valores de forma segura (getters e setters). 
Em seguida, implemente uma classe CarrinhoDeCompras, que mantém uma lista de objetos Produto e possui métodos 
para adicionar um produto ao carrinho, remover um produto pelo nome, calcular o valor total da compra e 
listar os produtos com suas quantidades e preços individuais. 
O programa principal deve permitir que o usuário adicione e remova produtos, visualize o conteúdo do carrinho 
e o total da compra. 
Utilize encapsulamento para proteger os dados dos produtos e boas práticas de organização orientada a objetos.'''


class Produto:
    def _init_(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Preço não pode ser negativo.")

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        if quantidade >= 0:
            self.__quantidade = quantidade
        else:
            print("Quantidade não pode ser negativa.")

    def _str_(self):
        return f"{self._nome}: R${self.preco:.2f} x {self._quantidade}"
    
class CarrinhoDeCompras:
    def _init_(self):
        self.__produtos = []

    def adicionar_produto(self, produto):
        self.__produtos.append(produto)

    def remover_produto(self, nome):
        for produto in self.__produtos:
            if produto.get_nome() == nome:
                self.__produtos.remove(produto)
                return
        print("Produto não encontrado no carrinho.")

    def calcular_total(self):
        total = 0
        for produto in self.__produtos:
            total += produto.get_preco() * produto.get_quantidade()
        return total

    def listar_produtos(self):
        if not self.__produtos:
            print("Carrinho vazio.")
            return
        for produto in self.__produtos:
            print(produto)

# Exemplo de uso
carrinho = CarrinhoDeCompras()

# Adicionando produtos ao carrinho
produto1 = Produto("Maçã", 3.50, 2)
produto2 = Produto("Banana", 2.00, 5)   
carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)

class Produto:
    def _init_(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Preço não pode ser negativo.")

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        if quantidade >= 0:
            self.__quantidade = quantidade
        else:
            print("Quantidade não pode ser negativa.")

    def _str_(self):
        return f"{self._nome}: R${self.preco:.2f} x {self._quantidade}"
    
class CarrinhoDeCompras:
    def _init_(self):
        self.__produtos = []

    def adicionar_produto(self, produto):
        self.__produtos.append(produto)

    def remover_produto(self, nome):
        for produto in self.__produtos:
            if produto.get_nome() == nome:
                self.__produtos.remove(produto)
                return
        print("Produto não encontrado no carrinho.")

    def calcular_total(self):
        total = 0
        for produto in self.__produtos:
            total += produto.get_preco() * produto.get_quantidade()
        return total

    def listar_produtos(self):
        if not self.__produtos:
            print("Carrinho vazio.")
            return
        for produto in self.__produtos:
            print(produto)

# Exemplo de uso
carrinho = CarrinhoDeCompras()

# Adicionando produtos ao carrinho
produto1 = Produto("Maçã", 3.50, 2)
produto2 = Produto("Banana", 2.00, 5)   
carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)

# Listando os produtos no carrinho
print("Produtos no carrinho:")
carrinho.listar_produtos()

# Removendo um produto do carrinho
carrinho.remover_produto("Maçã")

# Listando os produtos atualizados no carrinho
print("\nProdutos no carrinho após remoção:")
carrinho.listar_produtos()

# Calculando e exibindo o total da compra
total_compra = carrinho.calcular_total()
print(f"\nTotal da compra: R${total_compra:.2f}")


# Versão melhorada com validações e funcionalidades adicionais
'''class Produto:
    def _init_(self, nome, preco, quantidade):
        self.__nome = nome
        # Usa os setters para validação já na criação
        self.set_preco(preco)
        self.set_quantidade(quantidade)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome and isinstance(nome, str):
            self.__nome = nome.strip()
        else:
            print("Nome não pode ser vazio.")

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        try:
            preco_float = float(preco)
            if preco_float >= 0:
                self.__preco = round(preco_float, 2)  # Arredonda para 2 casas decimais
            else:
                print("Preço não pode ser negativo.")
                self.__preco = 0.0
        except (ValueError, TypeError):
            print("Erro: Preço deve ser um número válido.")
            self.__preco = 0.0

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        try:
            quantidade_float = float(quantidade)
            if quantidade_float >= 0:
                self.__quantidade = round(quantidade_float, 3)  # Arredonda para 3 casas (gramas)
            else:
                print("Quantidade não pode ser negativa.")
                self.__quantidade = 0.0
        except (ValueError, TypeError):
            print("Erro: Quantidade deve ser um número válido.")
            self.__quantidade = 0.0

    def get_valor_total(self):
        # Calcula o valor total e arredonda para 2 casas decimais
        valor_total = self._preco * self._quantidade
        return round(valor_total, 2)

    def _str_(self):
        # Formata a exibição baseada no tipo de quantidade (inteira ou decimal)
        if self.__quantidade.is_integer():
            quantidade_str = f"{int(self.__quantidade)} un"
            valor_unitario = f"R${self.__preco:.2f}/un"
        else:
            quantidade_str = f"{self.__quantidade:.3f} kg"
            valor_unitario = f"R${self.__preco:.2f}/kg"
        
        return f"{self.__nome} ({valor_unitario}) × {quantidade_str} = R${self.get_valor_total():.2f}"


class CarrinhoDeCompras:
    def _init_(self):
        self.__produtos = []

    def adicionar_produto(self, produto):
        # Verifica se produto já existe (case-insensitive)
        nome_novo = produto.get_nome().lower()
        for prod in self.__produtos:
            if prod.get_nome().lower() == nome_novo:
                # Se existe, aumenta a quantidade (para float também funciona)
                nova_quantidade = prod.get_quantidade() + produto.get_quantidade()
                prod.set_quantidade(nova_quantidade)
                print(f"✓ Quantidade de '{prod.get_nome()}' atualizada para {self._formatar_quantidade(nova_quantidade)}.")
                return True
        
        # Se não existe, adiciona novo produto
        self.__produtos.append(produto)
        print(f"✓ Produto '{produto.get_nome()}' adicionado ao carrinho.")
        return True

    def _formatar_quantidade(self, quantidade):
        """Formata a quantidade para exibição amigável"""
        if quantidade.is_integer():
            return f"{int(quantidade)} un"
        else:
            return f"{quantidade:.3f} kg"

    def remover_produto(self, nome):
        nome = nome.lower()
        for produto in self.__produtos:
            if produto.get_nome().lower() == nome:
                self.__produtos.remove(produto)
                print(f"✓ Produto '{produto.get_nome()}' removido do carrinho.")
                return True
        print("✗ Produto não encontrado no carrinho.")
        return False

    def remover_quantidade_parcial(self, nome, quantidade_remover):
        """Remove apenas uma parte da quantidade do produto"""
        nome = nome.lower()
        for produto in self.__produtos:
            if produto.get_nome().lower() == nome:
                if quantidade_remover >= produto.get_quantidade():
                    # Remove o produto completamente
                    self.__produtos.remove(produto)
                    print(f"✓ Produto '{produto.get_nome()}' removido do carrinho.")
                else:
                    # Remove apenas a quantidade especificada
                    nova_quantidade = produto.get_quantidade() - quantidade_remover
                    produto.set_quantidade(nova_quantidade)
                    print(f"✓ Removido {self._formatar_quantidade(quantidade_remover)} de '{produto.get_nome()}'.")
                return True
        print("✗ Produto não encontrado no carrinho.")
        return False

    def calcular_total(self):
        total = sum(produto.get_valor_total() for produto in self.__produtos)
        return round(total, 2)

    def listar_produtos(self):
        if not self.__produtos:
            print("\n📭 Carrinho vazio.")
            return
        
        print("\n🛒 PRODUTOS NO CARRINHO:")
        print("=" * 65)
        for i, produto in enumerate(self.__produtos, 1):
            print(f"{i}. {produto}")
        print("=" * 65)
        print(f"💰 TOTAL: R${self.calcular_total():.2f}")
        print("=" * 65)

    def esta_vazio(self):
        return len(self.__produtos) == 0

    def get_quantidade_itens(self):
        # Retorna a contagem de produtos distintos
        return len(self.__produtos)

    def get_quantidade_total(self):
        # Retorna a soma de todas as quantidades (para unidade ou peso)
        return sum(produto.get_quantidade() for produto in self.__produtos)

    def limpar_carrinho(self):
        self.__produtos.clear()
        print("✓ Carrinho esvaziado.")


class MenuCarrinho:
    def _init_(self):
        self.carrinho = CarrinhoDeCompras()

    def exibir_menu(self):
        print("\n" + "=" * 60)
        print("🛒 SISTEMA DE CARRINHO DE COMPRAS (UN/PESO)")
        print("=" * 60)
        print("1. 📥 Adicionar produto")
        print("2. 📤 Remover produto completo")
        print("3. 🔻 Remover quantidade parcial")
        print("4. 📋 Listar produtos")
        print("5. 💰 Ver total da compra")
        print("6. 🧹 Limpar carrinho")
        print("7. 🚪 Sair")
        print("=" * 60)

    def _ler_numero(self, mensagem, tipo='float'):
        """Lê e valida números float ou int com tratamento de erro"""
        while True:
            try:
                entrada = input(mensagem).replace(',', '.').strip()
                if not entrada:
                    print("✗ Valor não pode estar vazio. Tente novamente.")
                    continue
                
                if tipo == 'float':
                    valor = float(entrada)
                    if valor < 0:
                        print("✗ Valor não pode ser negativo. Tente novamente.")
                        continue
                    return valor
                else:  # int
                    valor = int(entrada)
                    if valor <= 0:
                        print("✗ Valor deve ser maior que zero. Tente novamente.")
                        continue
                    return valor
                    
            except ValueError:
                print("✗ Valor inválido! Digite um número (ex: 2.50 ou 2,50).")

    def adicionar_produto_menu(self):
        print("\n📥 ADICIONAR PRODUTO")
        
        # Solicita nome do produto
        nome = input("Nome do produto: ").strip()
        if not nome:
            print("✗ Nome do produto não pode estar vazio.")
            return

        # Solicita preço
        preco = self._ler_numero("Preço unitário (R$): ")

        # Solicita quantidade com opção de tipo
        print("\nTipo de quantidade:")
        print("1. Unidades (ex: 5)")
        print("2. Peso (ex: 0.685 kg)")
        
        while True:
            opcao_tipo = input("Escolha o tipo (1-2): ").strip()
            if opcao_tipo == "1":
                quantidade = self._ler_numero("Quantidade (unidades): ", 'float')
                break
            elif opcao_tipo == "2":
                quantidade = self._ler_numero("Quantidade (kg): ", 'float')
                break
            else:
                print("✗ Opção inválida! Escolha 1 ou 2.")

        # Cria e adiciona o produto
        produto = Produto(nome, preco, quantidade)
        self.carrinho.adicionar_produto(produto)

    def remover_produto_completo_menu(self):
        if self.carrinho.esta_vazio():
            print("\n📭 Carrinho vazio! Não há produtos para remover.")
            return

        print("\n📤 REMOVER PRODUTO COMPLETO")
        self.carrinho.listar_produtos()
        
        nome = input("\nDigite o nome do produto a remover: ").strip()
        if not nome:
            print("✗ Nome não pode estar vazio.")
            return

        self.carrinho.remover_produto(nome)

    def remover_quantidade_parcial_menu(self):
        if self.carrinho.esta_vazio():
            print("\n📭 Carrinho vazio! Não há produtos para remover.")
            return

        print("\n🔻 REMOVER QUANTIDADE PARCIAL")
        self.carrinho.listar_produtos()
        
        nome = input("\nDigite o nome do produto: ").strip()
        if not nome:
            print("✗ Nome não pode estar vazio.")
            return

        # Verifica se o produto existe
        produto_encontrado = None
        for produto in self.carrinho.CarrinhoDeCompras_produtos:  # Acesso protegido
            if produto.get_nome().lower() == nome.lower():
                produto_encontrado = produto
                break

        if not produto_encontrado:
            print("✗ Produto não encontrado no carrinho.")
            return

        print(f"\nQuantidade atual: {produto_encontrado.get_quantidade():.3f}")
        quantidade_remover = self._ler_numero("Quantidade a remover: ")

        if quantidade_remover > produto_encontrado.get_quantidade():
            print("✗ Quantidade a remover é maior que a disponível!")
            return

        self.carrinho.remover_quantidade_parcial(nome, quantidade_remover)

    def ver_total_menu(self):
        if self.carrinho.esta_vazio():
            print("\n📭 Carrinho vazio!")
        else:
            total = self.carrinho.calcular_total()
            quantidade_produtos = self.carrinho.get_quantidade_itens()
            quantidade_total = self.carrinho.get_quantidade_total()
            
            print(f"\n💰 RESUMO DA COMPRA:")
            print("-" * 40)
            print(f"Produtos distintos: {quantidade_produtos}")
            print(f"Quantidade total: {quantidade_total:.3f}")
            print(f"Valor total: R$ {total:.2f}")
            print("-" * 40)

    def limpar_carrinho_menu(self):
        if self.carrinho.esta_vazio():
            print("\n📭 Carrinho já está vazio!")
        else:
            confirmacao = input("\n⚠️  Tem certeza que deseja esvaziar o carrinho? (s/n): ").lower()
            if confirmacao == 's' or confirmacao == 'sim':
                self.carrinho.limpar_carrinho()
            else:
                print("Operação cancelada.")

    def executar(self):
        print("🎉 Bem-vindo ao Sistema de Carrinho de Compras!")
        print("💡 Agora com suporte para produtos por unidade e por peso!")
        
        while True:
            self.exibir_menu()
            
            opcao = input("\nEscolha uma opção (1-7): ").strip()
            
            if opcao == "1":
                self.adicionar_produto_menu()
                
            elif opcao == "2":
                self.remover_produto_completo_menu()
                
            elif opcao == "3":
                self.remover_quantidade_parcial_menu()
                
            elif opcao == "4":
                self.carrinho.listar_produtos()
                
            elif opcao == "5":
                self.ver_total_menu()
                
            elif opcao == "6":
                self.limpar_carrinho_menu()
                
            elif opcao == "7":
                if not self.carrinho.esta_vazio():
                    print("\n📋 Resumo final da compra:")
                    self.carrinho.listar_produtos()
                print("\n✅ Obrigado por usar nosso sistema! Até logo! 👋")
                break
                
            else:
                print("✗ Opção inválida! Escolha um número entre 1 e 7.")
            
            # Pausa para visualizar resultados
            if opcao in ["1", "2", "3", "4", "5", "6"]:
                input("\nPressione Enter para continuar...")


# Programa principal
if _name_ == "_main_":
    # Cria e executa o sistema de menu
    sistema = MenuCarrinho()
    sistema.executar()'''


'''
# Definição da classe Produto
class Produto:
    def _init_(self, nome: str, preco: float, quantidade: int = 1):
        # Inicializa os atributos privados como None
        self.__nome = None
        self.__preco = None
        self.__quantidade = None

        # Usa os setters para aplicar validações logo na criação do objeto
        self.set_nome(nome)
        self.set_preco(preco)
        self.set_quantidade(quantidade)

    # Getter para o nome
    def get_nome(self) -> str:
        return self.__nome

    # Getter para o preço
    def get_preco(self) -> float:
        return self.__preco

    # Getter para a quantidade
    def get_quantidade(self) -> int:
        return self.__quantidade

    # Setter para o nome (com validação)
    def set_nome(self, nome: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Nome deve ser uma string não vazia.")  # Garante nome válido
        self.__nome = nome.strip()  # Remove espaços extras

    # Setter para o preço (com validação)
    def set_preco(self, preco: float):
        try:
            preco = float(preco)  # Tenta converter para float
        except (TypeError, ValueError):
            raise ValueError("Preço deve ser um número.")
        if preco < 0:
            raise ValueError("Preço não pode ser negativo.")
        self.__preco = preco

    # Setter para a quantidade (com validação)
    def set_quantidade(self, quantidade: int):
        if not isinstance(quantidade, int):
            # Caso não seja inteiro, tenta converter
            try:
                quantidade = int(quantidade)
            except Exception:
                raise ValueError("Quantidade deve ser um inteiro.")
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        self.__quantidade = quantidade

    # Método para exibir o produto em formato de string
    def _str_(self):
        return f"{self.get_nome()} — R$ {self.get_preco():.2f} x {self.get_quantidade()}"

    # Método que retorna o subtotal (preço * quantidade)
    def subtotal(self) -> float:
        return self.get_preco() * self.get_quantidade()


# Definição da classe CarrinhoDeCompras
class CarrinhoDeCompras:
    def _init_(self):
        # Lista privada que armazenará objetos Produto
        self.__produtos = []

    # Método para adicionar um produto ao carrinho
    def adicionar_produto(self, produto: Produto):
        if not isinstance(produto, Produto):
            raise TypeError("Só é permitido adicionar objetos do tipo Produto.")
        
        # Converte o nome do produto para minúsculo para comparar
        nome = produto.get_nome().lower()
        
        # Verifica se já existe um produto igual no carrinho
        for p in self.__produtos:
            if p.get_nome().lower() == nome:
                # Se já existe, apenas soma a quantidade
                nova_qt = p.get_quantidade() + produto.get_quantidade()
                p.set_quantidade(nova_qt)
                return
        # Caso não exista, adiciona novo produto
        self.__produtos.append(produto)

    # Método para remover um produto pelo nome
    def remover_produto_por_nome(self, nome: str) -> bool:
        if not isinstance(nome, str) or nome.strip() == "":
            return False
        alvo = nome.strip().lower()
        
        # Procura o produto pelo nome
        for i, p in enumerate(self.__produtos):
            if p.get_nome().lower() == alvo:
                del self.__produtos[i]  # Remove da lista
                return True
        return False  # Se não encontrou, retorna False

    # Método para calcular o total da compra
    def calcular_total(self) -> float:
        total = 0.0
        for p in self.__produtos:
            total += p.subtotal()  # Soma os subtotais dos produtos
        return total

    # Método que retorna a lista de produtos
    def listar_produtos(self) -> list:
        return list(self.__produtos)  # Retorna uma cópia da lista

    # Método que verifica se o carrinho está vazio
    def esta_vazio(self) -> bool:
        return len(self.__produtos) == 0


# Função principal com menu interativo
def main():
    # Cria um objeto carrinho
    carrinho = CarrinhoDeCompras()

    # Menu de opções para o usu'''ário
    '''MENU = '''
'''
    ============================
      Carrinho de Compras - Menu
    ============================
    1 - Adicionar produto
    2 - Remover produto por nome
    3 - Listar produtos
    4 - Mostrar total da compra
    5 - Sair
    # Loop infinito até o usuário escolher sair
    while True:
        print(MENU)  # Mostra o menu
        opc = input("Escolha uma opção (1-5): ").strip()  # Recebe a opção escolhida

        # Opção 1 - Adicionar produto
        if opc == "1":
            try:
                nome = input("Nome do produto: ").strip()
                preco_str = input("Preço unitário (ex: 12.50): ").strip()
                qt_str = input("Quantidade (inteiro, padrão 1): ").strip() or "1"

                preco = float(preco_str)  # Converte preço
                quantidade = int(qt_str)  # Converte quantidade

                prod = Produto(nome, preco, quantidade)  # Cria objeto Produto
                carrinho.adicionar_produto(prod)  # Adiciona ao carrinho
                print(f"Produto '{prod.get_nome()}' adicionado/atualizado com sucesso.\n")
            except Exception as e:
                print(f"Erro ao adicionar produto: {e}\n")

        # Opção 2 - Remover produto
        elif opc == "2":
            nome = input("Nome do produto a remover: ").strip()
            if carrinho.remover_produto_por_nome(nome):
                print(f"Produto '{nome}' removido do carrinho.\n")
            else:
                print(f"Produto '{nome}' não encontrado no carrinho.\n")

        # Opção 3 - Listar produtos
        elif opc == "3":
            if carrinho.esta_vazio():
                print("O carrinho está vazio.\n")
            else:
                print("Produtos no carrinho:")
                for p in carrinho.listar_produtos():
                    print(f" - {p} (subtotal: R$ {p.subtotal():.2f})")
                print("")  # Linha em branco para separar

        # Opção 4 - Mostrar total
        elif opc == "4":
            total = carrinho.calcular_total()
            print(f"Total da compra: R$ {total:.2f}\n")

        # Opção 5 - Sair
        elif opc == "5":
            print("Encerrando. Obrigado!")
            break

        # Opção inválida
        else:
            print("Opção inválida. Escolha entre 1 e 5.\n")


# Executa o programa apenas se for o arquivo principal
if _name_ == "_main_":
    main()'''
