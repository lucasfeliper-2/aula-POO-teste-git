'''Utilizando a estrutura try except escreva os códigos do que se pede:
Criar um código que recebe um CPF digitado pelo usuário e valida se ele tem 11 dígitos numéricos. Tratar erros de entrada como letras, símbolos ou tamanho incorreto.'''

class ValidadorCPF:
    def validar_cpf(self):
        while True:
            cpf = input("Digite um CPF (11 dígitos numéricos. Sem pontos/digito): ")
            try:
                if len(cpf) != 11 or not cpf.isdigit():
                    raise ValueError("CPF deve conter exatamente 11 dígitos numéricos.")
            except ValueError as ve:
                print(f"Erro: {ve}")
            else:
                print(f"CPF válido: {cpf}")
                break

validador_cpf = ValidadorCPF()
validador_cpf.validar_cpf()
