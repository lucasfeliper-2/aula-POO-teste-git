'''Elabore um programa em Python orientado a objetos que leia um número 
n (o número de termos de uma progressão aritmética), a1 (o primeiro termo da progressão)
 e r (razão) e escreva todos os termos dessa progressão, bem como a soma dos elementos 
 (Fórmulas da P.A.: an = a1 + r x (n – 1) e  S = n * (a1 + an) / 2).'''
 

'''class ProgressaoAritmetica:
    def _init_(self, n, a1, r):
        self.n = n  # número de termos
        self.a1 = a1  # primeiro termo
        self.r = r  # razão
        self.termos = []  # lista para armazenar os termos da progressão

    def calcular_termos(self):
        for i in range(self.n):
            an = self.a1 + i * self.r  # fórmula do n-ésimo termo
            self.termos.append(an)

    def soma_termos(self):
        if not self.termos:
            self.calcular_termos()
        an = self.termos[-1]  # último termo
        soma = self.n * (self.a1 + an) / 2  # fórmula da soma dos termos
        return soma

    def exibir_progressao(self):
        if not self.termos:
            self.calcular_termos()
        print("Termos da Progressão Aritmética:")
        for termo in self.termos:
            print(termo, end=' ')
        print("\nSoma dos termos:", self.soma_termos())

# Exemplo de uso
n = int(input("Digite o número de termos (n): "))
a1 = int(input("Digite o primeiro termo (a1): "))
r = int(input("Digite a razão (r): "))

progressao = ProgressaoAritmetica(n, a1, r)
progressao.exibir_progressao()  # Saída'''
#### Melhoria do código acima com validações, tipagem, separação de lógica e I/O,
#### e formatação de saída para inteiros e floats.
'''from typing import List, Tuple


class ProgressaoAritmetica:
    """
    Representa uma progressão aritmética (PA).

    Atributos:
        n (int): número de termos (deve ser >= 1)
        a1 (float): primeiro termo
        r (float): razão
        termos (List[float]): lista dos termos gerada por calcular_termos()
    """

    def _init_(self, n: int, a1: float, r: float):
        if not isinstance(n, int):
            raise TypeError("n deve ser um inteiro.")
        if n <= 0:
            raise ValueError("n deve ser >= 1.")
        self.n: int = n
        self.a1: float = float(a1)
        self.r: float = float(r)
        self.termos: List[float] = []

    def calcular_termos(self) -> List[float]:
        """
        Calcula e armazena a lista de termos da PA.
        Usa list comprehension e sobrescreve self.termos (evita duplicações).
        """
        self.termos = [self.a1 + i * self.r for i in range(self.n)]
        return self.termos

    def soma_termos(self) -> float:
        """
        Retorna a soma dos termos da PA usando a fórmula:
            S = n * (a1 + an) / 2
        Garante que os termos estejam calculados antes.
        """
        if not self.termos:
            self.calcular_termos()
        an = self.termos[-1]
        soma = self.n * (self.a1 + an) / 2
        return soma

    def get_progressao(self) -> Tuple[List[float], float]:
        """
        Retorna (termos, soma). Não realiza prints — separação de lógica e I/O.
        """
        if not self.termos:
            self.calcular_termos()
        return self.termos, self.soma_termos()


# -----------------------
# Interface simples (I/O)
# -----------------------
def read_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Erro: digite um inteiro positivo (>= 1).")
                continue
            return value
        except ValueError:
            print("Erro: insira um número inteiro válido.")


def read_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Erro: insira um número válido (ex.: 3, 4.5).")


def format_num(x: float) -> str:
    """
    Formata o número para exibição: se for inteiro, mostra sem ponto decimal.
    """
    if float(x).is_integer():
        return str(int(x))
    return str(x)


if _name_ == "_main_":
    n = read_positive_int("Digite o número de termos (n): ")
    a1 = read_number("Digite o primeiro termo (a1): ")
    r = read_number("Digite a razão (r): ")

    pa = ProgressaoAritmetica(n, a1, r)
    termos, soma = pa.get_progressao()

    # Impressão amigável
    termos_formatados = " ".join(format_num(t) for t in termos)
    print("\nTermos da Progressão Aritmética:")
    print(termos_formatados)
    print("Soma dos termos:", format_num(soma))'''