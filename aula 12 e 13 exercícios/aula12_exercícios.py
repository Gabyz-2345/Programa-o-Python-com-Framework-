# aula 12 exercícios:

# 1- Classe Pessoa // ok
# Crie uma classe Pessoa com os atributos nome e idade. Adicione um método apresentar() que exiba "Olá, meu nome é [nome] e tenho [idade] anos."
#  Crie duas pessoas diferentes e chame o método.
#----------------------------------------------------

# 2.Classe Retângulo // ok
# Crie uma classe Retangulo com os atributos largura e altura. Adicione métodos:
# calcular_area() – retorna a área



# calcular_perimetro() – retorna o perímetro

#  Crie um retângulo com largura 5 e altura 3 e exiba sua área e perímetro.
#----------------------------------------------------



# 3. Classe Conta Bancária // ok 
# Crie uma classe ContaBancaria com:
# Atributos: titular, saldo (inicial 0)
# Métodos:
# depositar(valor): acrescenta ao saldo



# sacar(valor): se houver saldo suficiente, subtrai; senão, exibe "Saldo insuficiente"


# exibir_saldo(): mostra o saldo formatado

#  Crie uma conta, faça depósitos e saques e exiba o saldo.
#----------------------------------------------------


# 4. Classe Produto // ok 
# Crie uma classe Produto com:
# Atributos: nome, preco, quantidade_estoque
# Métodos:
# total_estoque(): retorna preco * quantidade_estoque


# adicionar_estoque(quantidade): aumenta a quantidade


# remover_estoque(quantidade): diminui, mas não permite ficar negativo

#  Crie um produto, altere o estoque e exiba o valor total.
#----------------------------------------------------



# 5. Classe Aluno // ok 
# Crie uma classe Aluno com:
# Atributos: nome, matricula, notas (lista de floats)
# Métodos:
# adicionar_nota(nota): adiciona à lista


# calcular_media(): retorna a média das notas


# situacao(): retorna "Aprovado" se média >= 7, "Recuperação" se >= 5, "Reprovado" caso contrário

#  Crie um aluno, adicione 3 notas e exiba sua situação.
#----------------------------------------------------




print('----------------------------------------')
#  Crie uma classe Pessoa com os atributos nome e idade. Adicione um método apresentar() que exiba "Olá, meu nome é [nome] e tenho [idade] anos." Crie duas pessoas diferentes e chame o método.
print('ATIVIDADE 1 - Classe Pessoa:')

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print('Olá, meu nome é', self.nome, 'e tenho', self.idade, 'anos')


p1 = Pessoa('Ana',18)
p2 = Pessoa('João',20)

p1.apresentar()
p2.apresentar()

# nota para veificar depois: nesse exercício eu criei uma classe com o nome e idade e um método para mostrar os dados.
# teste que deve aparecer: Olá, meu nome é Ana e tenho 18 anos. ou: Olá, meu nome é João e tenho 20 anos.
#----------------------------------------------------------------------------------------------------------------------




print('-------------------------------------')
# Crie uma classe Retangulo com os atributos largura e altura. Adicione métodos:
# calcular_area() – retorna a área


# calcular_perimetro() – retorna o perímetro

#  Crie um retângulo com largura 5 e altura 3 e exiba sua área e perímetro.

print('ATIVIDADE 2 - Classe Retângulo: ')

class Retangulo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        area = self.largura * self.altura 
        return area
    
    def calcular_perimetro(self):
        area = self.largura * self.altura
        return area
    
    def calcular_perimetro(self):
        perimetro = 2 * (self.largura + self.altura)
        return perimetro
    
r = Retangulo(5,3)

print('Área:', r.calcular_area())
print('Perímetro:', r.calcular_perimetro())

# nota para veificar depois: nesse aqui eu usei fórmulas simples de área e perímetro.
# teste que deve aparecer: área: 15 e perímetro: 16
#----------------------------------------------------------------------------------------------------------------------




print('----------------------------------------')
# Crie uma classe ContaBancaria com:
# Atributos: titular, saldo (inicial 0)
# Métodos:
# depositar(valor): acrescenta ao saldo
# sacar(valor): se houver saldo suficiente, subtrai; senão, exibe "Saldo insuficiente"
# exibir_saldo(): mostra o saldo formatado
#  Crie uma conta, faça depósitos e saques e exiba o saldo.

print('ATIVIDADE 3 - Classe Conta Bancária:')

class ContaBancaria:

    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
       self.saldo = self.saldo + valor
       print('Depósito feito!')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            print('Saque realizado com sucesso!')
        else:
            print('Saldo insuficiente')

    def exibir_saldo(self):
        print('Saldo:', self.saldo)

c = ContaBancaria('Carlos')

c.depositar(1000)
c.sacar(200)
c.sacar(900)
c.exibir_saldo()

# nota para veificar depois: nesse eu controlei o saldo cok depósito e saque verificando se tem dinheiro ou não
# teste que deve aparecer: Depósito feito! / Saque realizado com sucesso! / Saldo insuficiente / saldo: 800
#----------------------------------------------------------------------------------------------------------------------






print('----------------------------------------------')
# Crie uma classe Produto com:
# Atributos: nome, preco, quantidade_estoque
# Métodos:
# total_estoque(): retorna preco * quantidade_estoque
# adicionar_estoque(quantidade): aumenta a quantidade
# remover_estoque(quantidade): diminui, mas não permite ficar negativo
#  Crie um produto, altere o estoque e exiba o valor total.

print('ATIVIDADE 4 - Classe Produto:')

class Produto:

    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def total_estoque(self):
        total = self.preco * self.quantidade_estoque
        return total
    
    def adicionar_estoque(self, quantidade):
        self.quantidade_estoque = self.quantidade_estoque + quantidade

    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade_estoque:
            self.quantidade_estoque = self.quantidade_estoque - quantidade 
        else:
            print('Estoque insuficiente')

p = Produto('Caneta:', 2, 10)

p.adicionar_estoque(5)
p.remover_estoque(8)

print('Total em estoque:', p.total_estoque())

# nota para veificar depois: nesse eu controlei a quantidade e calculei o valor total do estoque.
# teste que deve aparecer: Total em estoque: 14
#----------------------------------------------------------------------------------------------------------------------




print('------------------------------------------------')
# Crie uma classe Aluno com:
# Atributos: nome, matricula, notas (lista de floats)
# Métodos:
# adicionar_nota(nota): adiciona à lista
# calcular_media(): retorna a média das notas
# situacao(): retorna "Aprovado" se média >= 7, "Recuperação" se >= 5, "Reprovado" caso contrário
#  Crie um aluno, adicione 3 notas e exiba sua situação.

print('ATIVIDADE 5 - Classe Aluno')

class Aluno:

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        soma = sum(self.notas)
        media = soma / len(self.notas)
        return media

    def situacao(self):
        media = self.calcular_media()

        if media >= 7:
            return 'Aprovado'
        elif media >= 5:
            return 'Recuperação'
        else:
            return 'Reprovado'


a = Aluno('Maria', 123)

a.adicionar_nota(7)
a.adicionar_nota(6)
a.adicionar_nota(8)

print('Média:', a.calcular_media())
print('Situação:', a.situacao())

# nota para veificar depois: nesse eu guardei as notas em uma lista e calculei a média para definir a sitiação.
# teste que deve aparecer: média: 7.0 / situação: Aprovado.
#----------------------------------------------------------------------------------------------------------------------

