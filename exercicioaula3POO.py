'''Implemente uma calculadora simples em Python que ofereça um menu para o usuário escolher entre as operações: 
(1) soma, (2) subtração, (3) multiplicação, (4) divisão e (5) sair. 
Para cada operação, o programa deve pedir dois números ao usuário e mostrar o resultado. 
Use blocos try/except para garantir que o programa não quebre caso o usuário digite valores inválidos 
(ex: letras em vez de números) ou tente dividir por zero. 
O programa deve continuar funcionando normalmente após qualquer erro, 
permitindo novas operações até o usuário escolher sair.'''

class calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b
    
    calc = calculadora()
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