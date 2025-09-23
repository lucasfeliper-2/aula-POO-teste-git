'''Faça um programa em Python orientado a objetos que, a partir de uma string digitada pelo usuário, imprima:
◦ O número de caracteres da string;
◦ A string com todas suas letras em maiúsculo;
◦ A string com todas suas letras em minúsculo;
◦ O número de vogais da string;
◦ Se a substring “IFB” aparece no texto (ignorando 
maiúsculas/minúsculas).'''

# Define a classe principal que fará a análise de strings
class StringAnalyzer:
    # Método construtor que inicializa o objeto com a string a ser analisada
    def _init_(self, string):
        # Armazena a string fornecida como atributo do objeto
        self.string = string

    # Método para contar o total de caracteres na string
    def count_characters(self):
        # Usa a função len() para retornar o comprimento da string
        return len(self.string)

    # Método para converter toda a string para letras maiúsculas
    def to_uppercase(self):
        # Usa o método upper() para converter caracteres para maiúsculo
        return self.string.upper()

    # Método para converter toda a string para letras minúsculas  
    def to_lowercase(self):
        # Usa o método lower() para converter caracteres para minúsculo
        return self.string.lower()
    
    # Método para contar o número de vogais na string
    def count_vowels(self):
        # Define uma string com todas as vogais (incluindo acentuadas) maiúsculas e minúsculas
        vowels = 'aeiouáéíóúâêîôûàèìòùãõäëïöüAEIOUÁÉÍÓÚÂÊÎÔÛÀÈÌÒÙÃÕÄËÏÖÜ'
        # Usa generator expression para contar vogais: soma 1 para cada caractere que é vogal
        return sum(1 for char in self.string if char in vowels)

    # Método para verificar se a substring "IFB" está presente
    def contains_ifb(self):
        # Converte a string para minúsculas e verifica se "ifb" está contido
        # Isso torna a busca case-insensitive (não diferencia maiúsculas/minúsculas)
        return 'ifb' in self.string.lower()
    
    # Método que exibe toda a análise de forma organizada e formatada
    def show_analysis(self):
        """Exibe análise completa de forma organizada"""
        # Imprime uma linha em branco para separar visualmente
        print("\n" + "="*50)
        # Imprime o título da análise
        print("ANÁLISE DA STRING")
        # Imprime outra linha separadora
        print("="*50)
        # Exibe a string original fornecida pelo usuário
        print(f"Texto original: {self.string}")
        # Chama count_characters() e exibe o número total de caracteres
        print(f"Número de caracteres: {self.count_characters()}")
        # Chama to_uppercase() e exibe a versão em maiúsculas
        print(f"Em maiúsculo: {self.to_uppercase()}")
        # Chama to_lowercase() e exibe a versão em minúsculas
        print(f"Em minúsculo: {self.to_lowercase()}")
        # Chama count_vowels() e exibe o número de vogais encontradas
        print(f"Número de vogais: {self.count_vowels()}")
        # Chama contains_ifb() e exibe se a substring "IFB" foi encontrada
        print(f"Contém 'IFB': {self.contains_ifb()}")
        # Imprime linha final para fechar visualmente a análise
        print("="*50)

# Solicita ao usuário que digite uma string para análise
user_input = input("Digite uma string: ")

# Cria uma instância (objeto) da classe StringAnalyzer com a string do usuário
analyzer = StringAnalyzer(user_input)

# Chama o método show_analysis() para exibir todos os resultados formatados
analyzer.show_analysis()