'''Utilizando a estrutura try except escreva os códigos do que se pede:
Crie um código que solicite ao usuário que digite um valor inteiro, trate o erro caso um valor diferente seja digitado'''

class ValorInteiro:
    def solicitar_inteiro(self):
        while True:
            try:
                valor = int(input("Digite um valor inteiro: "))
                print(f"Você digitou o valor inteiro: {valor}")
                break
            except ValueError:
                print("Erro: Por favor, digite um valor inteiro válido.")

valor_inteiro = ValorInteiro()
valor_inteiro.solicitar_inteiro()