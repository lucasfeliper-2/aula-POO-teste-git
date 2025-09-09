'''Utilizando a estrutura try except escreva os códigos do que se pede:
Criar um código que sorteia um número entre 1 e N, onde N é fornecido pelo usuário. Tratar erros como entrada não numérica, número negativo ou zero'''

import random
class Sorteio:
    def sortear_numero(self):
        while True:
            try:
                n = int(input("Digite um número inteiro positivo (N): "))
                if n <= 0:
                    raise ValueError("O número deve ser maior que zero.")
                numero_sorteado = random.randint(1, n)
            except ValueError as ve:
                print(f"Erro: {ve}")
            else:
                print(f"Número sorteado entre 1 e {n}: {numero_sorteado}")
                break

sorteio = Sorteio()
sorteio.sortear_numero()
