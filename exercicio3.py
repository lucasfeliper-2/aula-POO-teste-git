'''Faça um programa em Python orientado a objetos que receba uma frase dada pelo usuário e a criptografe. 
A criptografia consistirá na troca das vogais da frase por um número correspondente: A – 4, E – 3, I – 1, O – 0, U – 8.'''

'''class Criptografia:
    def _init_(self, frase):
        self.frase = frase

    def criptografar(self):
        tabela_criptografia = str.maketrans('AEIOUaeiou', '4310843108')
        frase_criptografada = self.frase.translate(tabela_criptografia)
        return frase_criptografada
    
# Solicita ao usuário que insira uma frase
frase_usuario = input("Digite uma frase para criptografar: ")

# Cria uma instância da classe Criptografia com a frase do usuário
criptografador = Criptografia(frase_usuario)    
# Chama o método para criptografar a frase e exibe o resultado
frase_criptografada = criptografador.criptografar()
print("Frase criptografada:", frase_criptografada)'''

# Código adicional para melhorar a funcionalidade e usabilidade do programa
'''# Classe para criptografar frases usando substituição de vogais por números
class CriptografadorAvancado:
    """
    Classe que implementa criptografia através da substituição de vogais por números.
    Utiliza a tabela: A=4, E=3, I=1, O=0, U=8
    """
    
    # Método construtor que inicializa o objeto com a frase
    def _init_(self, frase):
        # Armazena a frase original fornecida pelo usuário
        self.frase_original = frase
        
        # Cria tabela de tradução para criptografia (maiúsculas e minúsculas)
        self.tabela_cripto = str.maketrans(
            'AEIOUaeiou',  # Caracteres a serem substituídos
            '4310843108'   # Caracteres substitutos (respectivamente)
        )
        
        # Cria tabela de tradução para descriptografia
        self.tabela_descripto = str.maketrans(
            '43108',       # Números a serem convertidos de volta
            'AEIOU'        # Vogais correspondentes (sempre maiúsculas)
        )

    # Método para criptografar a frase usando a tabela de tradução
    def criptografar(self):
        """
        Criptografa a frase substituindo vogais por números.
        Retorna: Frase criptografada
        """
        # Usa o método translate() com a tabela de criptografia
        return self.frase_original.translate(self.tabela_cripto)

    # Método para descriptografar uma frase criptografada
    def descriptografar(self, frase_criptografada=None):
        """
        Descriptografa uma frase convertendo números de volta para vogais.
        Se nenhuma frase for fornecida, usa a frase atual do objeto.
        Retorna: Frase descriptografada
        """
        # Se não for fornecida frase, usa a frase criptografada atual
        if frase_criptografada is None:
            frase_criptografada = self.criptografar()
        
        # Aplica a tradução reversa para obter a frase original
        return frase_criptografada.translate(self.tabela_descripto)

    # Método para exibir análise completa da criptografia
    def exibir_analise_completa(self):
        """
        Exibe uma análise completa comparando frase original e criptografada
        """
        # Criptografa a frase original
        frase_cripto = self.criptografar()
        
        # Exibe cabeçalho formatado
        print("\n" + "═" * 60)
        print("🔐 ANÁLISE DE CRIPTOGRAFIA")
        print("═" * 60)
        
        # Exibe a frase original
        print(f"📝 Frase original: {self.frase_original}")
        
        # Exibe a frase criptografada
        print(f"🔒 Frase criptografada: {frase_cripto}")
        
        # Exibe a frase descriptografada (para demonstração)
        print(f"🔓 Frase descriptografada: {self.descriptografar(frase_cripto)}")
        
        # Exibe estatísticas
        print(f"📊 Total de caracteres: {len(self.frase_original)}")
        
        # Conta quantas vogais foram substituídas
        vogais = 'AEIOUaeiou'
        vogais_substituidas = sum(1 for char in self.frase_original if char in vogais)
        print(f"🔢 Vogais substituídas: {vogais_substituidas}")
        
        # Exibe a tabela de substituição
        print("\n📋 Tabela de substituição:")
        print("   A → 4 | E → 3 | I → 1 | O → 0 | U → 8")
        print("═" * 60)
        
        # Retorna a frase criptografada para uso posterior
        return frase_cripto

# Função principal do programa
def main():
    """
    Função principal que gerencia o fluxo do programa
    """
    # Solicita ao usuário que digite uma frase
    frase_usuario = input("Digite uma frase para criptografar: ")
    
    # Cria uma instância do criptografador com a frase do usuário
    criptografador = CriptografadorAvancado(frase_usuario)
    
    # Exibe a análise completa da criptografia
    criptografador.exibir_analise_completa()

# Verifica se o script está sendo executado diretamente
if _name_ == "_main_":
    """
    Garante que o código só execute quando o arquivo for rodado diretamente,
    e não quando importado como módulo
    """
    # Chama a função principal
    main()'''