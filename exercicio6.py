'''Desenvolva uma classe Departamento com nome e um vetor de objetos Funcionario, 
onde cada funcionário tem nome e salário, permitindo que funcionários existam independentemente do departamento 
para que possam ser adicionados ou removidos livremente (agregação). Implemente métodos no Departamento para adicionar 
funcionários, calcular a média salarial e listar todos os funcionários. Crie um programa com menu interativo 
no console que permita criar departamentos, criar funcionários, adicionar 
funcionários a departamentos, listar funcionários e mostrar a média salarial, além de permitir sair do programa.'''

'''class Departamento:
    def _init_(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def calcular_media_salarial(self):
        if not self.funcionarios:
            return 0
        total_salario = sum(funcionario.salario for funcionario in self.funcionarios)
        return total_salario / len(self.funcionarios)

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f"Nome: {funcionario.nome}, Salário: {funcionario.salario}")

'''

'''from anthropic import Anthropic

client = Anthropic(api_key="SUA_CHAVE_API_AQUI")

resp = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Olá, Claude! Me diga uma curiosidade interessante."}
    ]
)

print(resp.content[0].text)'''