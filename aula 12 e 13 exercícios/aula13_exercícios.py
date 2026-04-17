
# aula 13 exercícios 

# 1. Classe Livro
# Crie uma classe Livro com:
# Atributos: titulo, autor, ano, disponivel (booleano, padrão True)
# Métodos:
# emprestar(): se disponível, marca como False e exibe "Livro emprestado"; senão, exibe "Indisponível"


# devolver(): marca como True e exibe "Livro devolvido"


# info(): mostra todas as informações do livro

#  Crie dois livros, faça empréstimos e devoluções.



# 2. Classe Funcionário
# Crie uma classe Funcionario com:
# Atributos: nome, cargo, salario_base
# Métodos:
# aumentar_salario(percentual): aumenta o salário com base no percentual


# calcular_bonus(): retorna 10% do salário base


# exibir_dados(): exibe todas as informações

#  Crie um funcionário, aumente o salário e mostre os dados atualizados.


# 3./ Classe Calculadora (estática)
# Crie uma classe `Calculadora` que **não precisa de atributos**. Apenas métodos de classe (use `@classmethod` ou métodos estáticos) para:

# - `somar(a, b)`
# - `subtrair(a, b)`
# - `multiplicar(a, b)`
# - `dividir(a, b)`
    
#     Teste os métodos sem criar objetos (chamando diretamente pela classe).


# 4. Classe Carro com Controle de Velocidade
# Crie uma classe Carro com:
# Atributos: marca, modelo, velocidade (inicial 0)
# Métodos:
# acelerar(valor): aumenta a velocidade (não pode ultrapassar 200 km/h)


# frear(valor): diminui a velocidade (não pode ficar negativa)


# velocidade_atual(): exibe a velocidade

#  Crie um carro, acelere e freie até parar.



# 5. Classe Agenda
# Crie uma classe Agenda que armazena contatos. Cada contato é um objeto da classe Contato (crie-a separada), com nome, telefone e email. A classe Agenda deve ter:
# Atributo: contatos (lista)
# Métodos:
# adicionar_contato(contato): adiciona à lista


# listar_contatos(): exibe todos os contatos


# buscar_contato(nome): exibe os dados do contato (se existir)

#  Crie alguns contatos, adicione-os à agenda e faça buscas.

print('--------------------------------')
# Crie uma classe Livro com:
# Atributos: titulo, autor, ano, disponivel (booleano, padrão True)
# Métodos:
# emprestar(): se disponível, marca como False e exibe "Livro emprestado"; senão, exibe "Indisponível"
# devolver(): marca como True e exibe "Livro devolvido"
# info(): mostra todas as informações do livro
#  Crie dois livros, faça empréstimos e devoluções.


print('ATIVIDADE 1 - Classe Livro')

class Livro:

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print('Livro emprestado')
        else:
            print('Indisponível')

    def devolver(self):
        self.disponivel = True
        print('Livro devolvido')

    def info(self):
        print(self.titulo, self.autor, self.ano, self.disponivel)


l1 = Livro('Livro A', 'Autor X', 2020)

l1.info()
l1.emprestar()
l1.emprestar()
l1.devolver()




print('-----------------------------------------------')
# Crie uma classe Funcionario com:
# Atributos: nome, cargo, salario_base
# Métodos:
# aumentar_salario(percentual): aumenta o salário com base no percentual
# calcular_bonus(): retorna 10% do salário base
# exibir_dados(): exibe todas as informações
#  Crie um funcionário, aumente o salário e mostre os dados atualizados.



print('ATIVIDADE 2 - Classe Funcionário:')

class Funcionario:

    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def aumentar_salario(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario = self.salario + aumento

    def calcular_bonus(self):
        return self.salario * 0.10

    def exibir_dados(self):
        print(self.nome, self.cargo, self.salario)


f = Funcionario('Pedro', 'Analista', 2000)

f.aumentar_salario(10)
print('Bônus:', f.calcular_bonus())
f.exibir_dados()




print('--------------------------------------------')
# Crie uma classe `Calculadora` que **não precisa de atributos**. Apenas métodos de classe (use `@classmethod` ou métodos estáticos) para:
# - `somar(a, b)`
# - `subtrair(a, b)`
# - `multiplicar(a, b)`
# - `dividir(a, b)`
#     Teste os métodos sem criar objetos (chamando diretamente pela classe).

print('ATIVIDADE 3 - Classe Calculadora estática')

class Calculadora:

    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def subtrair(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            return 'Erro'
        return a / b


print(Calculadora.somar(10, 5))




print('------------------------------------------')
# Crie uma classe Carro com:
# Atributos: marca, modelo, velocidade (inicial 0)
# Métodos:
# acelerar(valor): aumenta a velocidade (não pode ultrapassar 200 km/h)
# frear(valor): diminui a velocidade (não pode ficar negativa)
# velocidade_atual(): exibe a velocidade
#  Crie um carro, acelere e freie até parar.




print('ATIVIDADE 4 - Classe Carro com Controle de Velocidade:')

class Carro:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade = self.velocidade + valor
        if self.velocidade > 200:
            self.velocidade = 200

    def frear(self, valor):
        self.velocidade = self.velocidade - valor
        if self.velocidade < 0:
            self.velocidade = 0

    def velocidade_atual(self):
        print('Velocidade:', self.velocidade)


c = Carro('Ford', 'Fiesta')

c.acelerar(50)
c.acelerar(200)
c.frear(30)

c.velocidade_atual()




print('--------------------------------')
# Crie uma classe Agenda que armazena contatos. Cada contato é um objeto da classe Contato (crie-a separada), com nome, telefone e email. A classe Agenda deve ter:
# Atributo: contatos (lista)
# Métodos:
# adicionar_contato(contato): adiciona à lista
# listar_contatos(): exibe todos os contatos
# busar_contato(nome): exibe os dados do contato (se existir)
#  Crie alguns contatos, adicione-os à agenda e faça buscas.

print('ATIVIDADE 5 - Classe Agenda:')


class Contato:

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email


class Agenda:

    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def listar_contatos(self):
        for c in self.contatos:
            print(c.nome, c.telefone, c.email)

    def buscar_contato(self, nome):
        for c in self.contatos:
            if c.nome == nome:
                print(c.nome, c.telefone, c.email)


a = Agenda()










