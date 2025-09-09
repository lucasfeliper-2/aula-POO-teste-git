'''Utilizando a estrutura try except escreva os códigos do que se pede:
Crie um código para dividir dois números informados pelo usuário, tratando erros de entrada e divisão por zero'''

class Divisao:
    def dividir(self):
        while True:
            try:
                num1 = float(input("Digite o primeiro número (dividendo): "))
                num2 = float(input("Digite o segundo número (divisor): "))
                resultado = num1 / num2
            except ValueError:
                print("Erro: Por favor, digite números válidos.")
            except ZeroDivisionError:
                print("Erro: Divisão por zero não é permitida.")
            else:
                print(f"O resultado de {num1} dividido por {num2} é {resultado}")
                break

divisao = Divisao()
divisao.dividir()
