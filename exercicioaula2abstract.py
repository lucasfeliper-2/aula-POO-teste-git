#Você foi contratado para desenvolver um sistema para gerenciar informações e estatísticas dos clubes participantes da Copa do Mundo de Clubes da FIFA. 
#Para isso, implemente uma classe abstrata chamada ClubeParticipante com os atributos nome, pais, confederacao, ranking_fifa, gols_marcados e vitorias, 
#incluindo um método concreto exibir_dados() para mostrar os dados do clube, e 
#métodos abstratos calcular_desempenho() — que deve calcular um índice baseado na fórmula específica da confederação 
#(para clubes da UEFA: desempenho = vitórias × 3 + gols marcados × 0,5; para clubes da CBF: desempenho = vitórias × 3 + gols marcados × 0,7) — 
#e gerar_relatorio_tecnico(), que deve exibir as informações básicas do clube junto com o desempenho calculado. 
#Crie duas subclasses concretas, ClubeUEFA e ClubeCBF, que implementem esses métodos de acordo com as regras definidas, 
#e teste a aplicação criando instâncias de cada tipo, demonstrando o uso de abstração, herança, e polimorfismo em Python.'''

from abc import ABC, abstractmethod
class ClubeParticipante(ABC):
    def __init__(self, nome, pais, confederacao, ranking_fifa, gols_marcados, vitorias):
        self.nome = nome
        self.pais = pais
        self.confederacao = confederacao
        self.ranking_fifa = ranking_fifa
        self.gols_marcados = gols_marcados
        self.vitorias = vitorias

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"País: {self.pais}")
        print(f"Confederação: {self.confederacao}")
        print(f"Ranking FIFA: {self.ranking_fifa}")
        print(f"Gols Marcados: {self.gols_marcados}")
        print(f"Vitórias: {self.vitorias}")

    @abstractmethod
    def calcular_desempenho(self):
        pass

    @abstractmethod
    def gerar_relatorio_tecnico(self):
        pass

class ClubeUEFA(ClubeParticipante):
    def calcular_desempenho(self):
        return self.vitorias * 3 + self.gols_marcados * 0.5

    def gerar_relatorio_tecnico(self):
        desempenho = self.calcular_desempenho()
        self.exibir_dados()
        print(f"Desempenho (UEFA): {desempenho}")

class ClubeCBF(ClubeParticipante):
    def calcular_desempenho(self):
        return self.vitorias * 3 + self.gols_marcados * 0.7

    def gerar_relatorio_tecnico(self):
        desempenho = self.calcular_desempenho()
        self.exibir_dados()
        print(f"Desempenho (CBF): {desempenho}")

# Testando a aplicação
clube_uefa = ClubeUEFA("Real Madrid", "Espanha", "UEFA", 2, 85, 30)
clube_CBF = ClubeCBF("Cruzeiro", "Brasil", "CBF", 1, 90, 35)
clube_CBF2 = ClubeCBF("Alt mineiro", "Brasil", "CBF", 'fora do ranking fifa', 0, 0)

clube_uefa.gerar_relatorio_tecnico()
print("\n")
clube_CBF.gerar_relatorio_tecnico()
print("\n")
clube_CBF2.gerar_relatorio_tecnico()
print("\n")