'''
#veículo
marca = 'GM'
rodas = 4
cor = 'branco'
ano = "2000"

veiculo1 = {'marca': 'GM', 'rodas': 4, 'cor': 'branco', 'ano': 2000}
veiculo2 = {'marca': 'Fiat', 'rodas': 4, 'cor': 'branco', 'ano': 2000}

print(veiculo1)
print(veiculo2)

'''
'''
def criaVeiculo(marca, rodas, cor, ano):
    veiculo = {'marca': marca, 'rodas': rodas, 'cor': cor, 'ano': ano}
    return veiculo

veiculo1 = criaVeiculo('GM', 4, 'branco', 2000)
veiculo2 = criaVeiculo('Fiat', 4, 'preto', 2000)

print(veiculo1)
print(veiculo2)
'''

'''
def aumentaAno(veiculo1, ano):
    veiculo1['ano'] += ano

    aumentaAno(veiculo1, 5)
    print(veiculo1) 

def dimuneAno(veiculo1, ano):
    veiculo1['ano'] -= ano

    dimuneAno(veiculo1, 10)
    print(veiculo1)
'''
# variáveis = atributos
# ações = métodos
# classe = moldes do objeto
# métodos = executa ações

"""class Veiculo():
    pass # classe vazia"""
#instanciando um objeto do tipo veiculo
"""
v1 = Veiculo()
v2 = Veiculo()

print(v1) # <class '__main__.Veiculo'>
print(v2) # <class '__main__.Veiculo'>"""

'''class Veiculo():
    # metodo construtor
    def __init__(self, marca, rodas, cor, ano):
        self.marca = marca
        self.rodas = rodas
        self.cor = cor
        self.ano = ano
        self.ligado = False
        
v1 = Veiculo('GM', 4, 'branco', 2000)
print(v1.marca, v1.rodas, v1.cor, v1.ano)
v2 = Veiculo('Fiat', 4, 'preto', 2000)
print(v2.marca, v2.rodas, v2.cor, v2.ano)'''

'''class Veiculo():
  def __init__(self,marca,rodas,cor,ano):
    self.marca = marca
    self.rodas = rodas
    self.cor = cor
    self.ano = ano
    self.ligado = False

  def ligar(self):
    self.ligado = True
    print('Ligado')
  
  def aumentaAno(self, sobeAno): 
    self.ano += sobeAno

  def dimuneAno(self, desceAno):
    self.ano -= desceAno

v1 = Veiculo('Fiat', 4, 'Vermelho', 2000)

print(v1.ligado)
v1.ligar()
print(v1.ligado)

print(v1.ano)
v1.aumentaAno(5)
print(v1.ano)

v1.dimuneAno(5)
print(v1.ano)'''


'''
Criar método para desligar o veiculo.

Criar novos atributos OK.

Criar métodos que modifiquem esses atributos.

Instanciar objetos e testar os atributos e métodos.
'''
class Veiculo():
  # metodo construtor
  def __init__(self,marca,rodas,cor,ano, velocidade, combustivel, tipo_combustivel):
    # atributos
    self.marca = marca
    self.rodas = rodas
    self.cor = cor
    self.ano = ano
    self.ligado = False
    #===============================
    # novos atributos
    self.velocidade = velocidade
    self.combustivel = combustivel # nivel de combustível (0 a 100)
    self.tipo_combustivel = tipo_combustivel # tipo de combustível (Gasolina, Etanol, Diesel)

  # métodos
  def ligar(self):
    self.ligado = True
    print('Ligado')

  # metodo para desligar o veiculo "novo"
  def desligar(self):
    self.ligado = False
    print('Desligado')
    #incluir uma condição para verificar se o veículo está ligado antes de desligar
    
  
  def aumentaAno(self, sobeAno): 
    self.ano += sobeAno

  def dimuneAno(self, desceAno):
    self.ano -= desceAno
  #métodos novos
  def acelerar(self, aumento):
    if self.ligado and self.combustivel > 0:
      self.velocidade += aumento
      self.combustivel -= aumento * 0.1 # cada aumento consome combustível
      print(f'Acelerando para {self.velocidade} km/h')
    else:
      print('O veículo está desligado. Ligue-o primeiro ou abasteça.')
  def frear(self, reducao):
    if self.ligado and self.velocidade > 0:
      self.velocidade -= reducao
      if self.velocidade < 0:
        self.velocidade = 0
      print(f'Freando para {self.velocidade} km/h')
    else:
      print('O veículo está desligado ou já está parado.')

# Instanciando objetos
v1 = Veiculo('Fiat', 4, 'Vermelho', 2000, 0, 100, 'Gasolina')  # combustível em % (100 = tanque cheio)
v2 = Veiculo('GM', 4, 'Branco', 2005, 0, 80, 'Etanol')
v3 = Veiculo('Ford', 4, 'Preto', 2010, 0, 60, 'Diesel')

# Testando os atributos e métodos

print(v1.marca, v1.rodas, v1.cor, v1.ano, v1.ligado, v1.velocidade, v1.tipo_combustivel)
v1.ligar()
v1.acelerar(50)
v1.frear(20)
v1.desligar()
'''print(v2.marca, v2.rodas, v2.cor, v2.ano, v2.ligado, v2.velocidade, v2.tipo_combustivel)
v2.ligar()
v2.acelerar(30)
v2.frear(10)
v2.desligar()
print(v3.marca, v3.rodas, v3.cor, v3.ano, v3.ligado, v3.velocidade, v3.tipo_combustivel)
v3.ligar()
v3.acelerar(70)
v3.frear(30)
v3.desligar()'''


'''class Veiculo():
    # método construtor
    def __init__(self, marca, rodas, cor, ano, velocidade, combustivel, tipo_combustivel):
        # atributos
        self.marca = marca
        self.rodas = rodas
        self.cor = cor
        self.ano = ano
        self.ligado = False
        # novos atributos
        self.velocidade = velocidade
        self.combustivel = combustivel  # nível de combustível (0 a 100)
        self.tipo_combustivel = tipo_combustivel  # tipo de combustível (Gasolina, Etanol, Diesel)

    # métodos
    def ligar(self):
        self.ligado = True
        print('Veículo ligado')

    # método para desligar o veículo
    def desligar(self):
        self.ligado = False
        print('Veículo desligado')
  
    def aumentaAno(self, sobeAno): 
        self.ano += sobeAno

    def dimuneAno(self, desceAno):
        self.ano -= desceAno

    # métodos novos
    def acelerar(self, aumento):
        if self.ligado:
            if self.combustivel > 0:
                self.velocidade += aumento
                combustivel_usado = aumento * 0.1  # Consome 0.1 de combustível a cada 1 km/h de aceleração
                if self.combustivel - combustivel_usado < 0:
                    print(f'Combustível insuficiente! O veículo não pode acelerar mais.')
                    self.velocidade -= aumento  # Reseta a velocidade
                    self.combustivel = 0
                else:
                    self.combustivel -= combustivel_usado
                    print(f'Acelerando para {self.velocidade} km/h. Combustível restante: {self.combustivel}%')
            else:
                print('Combustível esgotado! Não é possível acelerar.')
        else:
            print('O veículo está desligado. Ligue-o primeiro.')

    def frear(self, reducao):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= reducao
            if self.velocidade < 0:
                self.velocidade = 0
            print(f'Velocidade reduzida para {self.velocidade} km/h')
        else:
            print('O veículo está desligado ou já está parado.')

# Instanciando objetos
v1 = Veiculo('Fiat', 4, 'Vermelho', 2000, 0, 100, 'Gasolina')  # combustível em % (100 = tanque cheio)
v2 = Veiculo('GM', 4, 'Branco', 2005, 0, 80, 'Etanol')
v3 = Veiculo('Ford', 4, 'Preto', 2010, 0, 60, 'Diesel')

# Testando os atributos e métodos
print(f'{v1.marca} | Combustível inicial: {v1.combustivel}%')
v1.ligar()
v1.acelerar(50)
v1.frear(20)
v1.desligar()

print(f'{v2.marca} | Combustível inicial: {v2.combustivel}%')
v2.ligar()
v2.acelerar(30)
v2.frear(10)
v2.desligar()

print(f'{v3.marca} | Combustível inicial: {v3.combustivel}%')
v3.ligar()
v3.acelerar(70)
v3.frear(30)
v3.desligar()
'''