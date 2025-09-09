'''Implemente uma calculadora simples em Python que ofereça um menu para o usuário escolher entre as operações: 
(1) soma, (2) subtração, (3) multiplicação, (4) divisão e (5) sair. 
Para cada operação, o programa deve pedir dois números ao usuário e mostrar o resultado. 
Use blocos try/except para garantir que o programa não quebre caso o usuário digite valores inválidos 
(ex: letras em vez de números) ou tente dividir por zero. 
O programa deve continuar funcionando normalmente após qualquer erro, 
permitindo novas operações até o usuário escolher sair.'''

'''
corrigido pela IA:
class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return a / b

def ler_numero(prompt):
    #Tenta ler um float do usuário; repete até obter ou retorna None se o usuário cancelar.
    while True:
        try:
            texto = input(prompt)
            return float(texto)
        except ValueError:
            print("Erro: por favor, digite um número válido.")
        except (KeyboardInterrupt, EOFError):
            print("\nEntrada cancelada pelo usuário.")
            return None
        
def main():
    calc = Calculadora()
    while True:
            print("Escolha a operação:")
            print("1. Soma")
            print("2. Subtração")
            print("3. Multiplicação")
            print("4. Divisão")
            print("5. Sair")
            
            escolha = input("Digite sua escolha (1/2/3/4/5): ").strip()
            
            if escolha == '5':
                print("Saindo da calculadora.")
                break
            
            if escolha not in {'1', '2', '3', '4'}:
                print("Escolha inválida. Tente novamente.")
                continue
            
            num1 = ler_numero("Digite o primeiro número: ")
            if num1 is None:    #Usuário cancelou
                break 

            num2 = ler_numero("Digite o segundo número: ")
            if num2 is None:    #Usuário cancelou
                break

            try:
                if escolha == '1':
                    resultado = calc.soma(num1, num2)
                    operador = '+'
                elif escolha == '2':
                    resultado = calc.subtracao(num1, num2)
                    operador = '-'
                elif escolha == '3':
                    resultado = calc.multiplicacao(num1, num2)
                    operador = '*'
                else: #escolha == '4':
                     resultado = calc.divisao(num1, num2)
                     operador = '/'
            except ZeroDivisionError:
                    print("Erro: divisão por zero não é permitida.")
                    continue
        
            print(f"{num1} {operador} {num2} = {resultado}")

if __name__ == "__main__":
    main()'''

class Calculadora:
    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        return a / b

calc = Calculadora()
while True:
        print("Escolha a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
            
        escolha = input("Digite sua escolha (1/2/3/4/5): ")
            
        if escolha == '5':
            print("Saindo da calculadora.")
            break
            
        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if escolha == '1':
                    print(f"{num1} + {num2} = {calc.soma(num1, num2)}")
                        
                elif escolha == '2':
                    print(f"{num1} - {num2} = {calc.subtracao(num1, num2)}")
                            
                elif escolha == '3':
                    print(f"{num1} * {num2} = {calc.multiplicacao(num1, num2)}")
                            
                elif escolha == '4':
                    try: 
                        print(f"{num1} / {num2} = {calc.divisao(num1, num2)}")
                    except ZeroDivisionError:
                        print("Erro: Divisão por zero não é permitida.")
                                
            except ValueError:
                print("Erro: Por favor, digite números válidos.")
                                
        else:
            print("Escolha inválida. Tente novamente.")

calc= Calculadora()
