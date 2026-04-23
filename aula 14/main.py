# class Dados:
#     def __init__(self):
#         self.nome = 'Ana' # publicp
#         self._cpf = '123146' # protegido
#         self.__conta = '1213' # privado


#     def display(self):
#         print(self.nome)
#         print(self._cpf)
#         print(self.__conta)


# class Dados2(Dados):
#     def __init__(self):
#         super().__init__()
#         self.x  =  10
        
#     def mostrar(self):
#         print(self._Dados__conta)



# # d = Dados()
# # d.display()
# # print(d._Dados__conta)        
# # print('cpf', d._cpf)


# d2  =  Dados2()
# d2.display()
# d2.mostrar()

### **Exercício 1 – Livro**

# Crie uma classe `Livro` com atributos de instância: `titulo`, `autor`, `ano`, `emprestado` (booleano, padrão `False`). Métodos:

# - `emprestar()` – se disponível, muda `emprestado` para `True`.
# - `devolver()` – muda `emprestado` para `False`.
# - `__str__()` – retorna uma string com as informações.
    
#     Teste com dois livros.



# Exercício 2 – Contador com Atributo de Classe
# Crie uma classe Contador que tenha um atributo de classe total_contadores que conta quantas instâncias foram criadas. Cada vez que um novo objeto é criado, esse contador deve ser incrementado. Adicione um método exibir_total() que exibe o total de contadores criados.

# Exercício 3 – Produto com Desconto
# Classe Produto com atributos privados _nome, _preco, _quantidade. Use propriedades (@property) para acessar esses atributos. Crie um método aplicar_desconto(percentual) que reduz o preço. O preço não pode ficar negativo. Teste criando produtos e aplicando descontos.

# Exercício 4 – Banco com Saldo Privado
# Classe ContaBancaria com atributo privado __saldo. Métodos:
# depositar(valor) – aumenta saldo.


# sacar(valor) – reduz saldo se houver saldo suficiente; senão, exibe mensagem.


# exibir_saldo() – retorna o saldo (use propriedade saldo apenas para leitura).

#  Crie uma conta, realize operações e exiba o saldo.


# Exercício 5 – Aluno com Notas
# Classe Aluno com atributos: nome, matricula e uma lista privada __notas. Métodos:
# adicionar_nota(nota) – adiciona à lista (valida de 0 a 10).


# calcular_media() – retorna a média.


# situacao() – retorna "Aprovado" se média >= 7, "Recuperação" se >= 5, "Reprovado" caso contrário.

#  Teste com um aluno e algumas notas.



# Exercício 6 – Data (validação)
# Crie uma classe Data com atributos dia, mes, ano. No __init__, valide se a data é válida (considere meses com 30/31 dias e ano bissexto para fevereiro). Use propriedades para garantir que alterações futuras também sejam validadas. Adicione um método __str__ que retorna a data no formato dd/mm/aaaa.

# Exercício 7 – Funcionário com Aumento
# Classe Funcionario com atributos: nome, cargo, salario_base (privado). Métodos:
# aumentar_salario(percentual) – aumenta o salário.


# calcular_bonus() – retorna 10% do salário base.


# Propriedade salario para leitura.

#  Teste criando um funcionário, aumente o salário e mostre o novo valor.



# Exercício 8 – Carro com Velocidade (Encapsulamento)
# Classe Carro com atributos marca, modelo e __velocidade (inicial 0). Métodos:
# acelerar(valor) – aumenta velocidade até no máximo 200.


# frear(valor) – reduz velocidade até no mínimo 0.


# Propriedade velocidade para leitura.

#  Teste acelerando e freando.



# Exercício 9 – Estatísticas (Atributos de Classe)
# Classe Estatistica com atributos de classe soma e contagem. Métodos de classe:
# adicionar(valor) – atualiza soma e contagem.


# calcular_media() – retorna a média (ou 0 se nenhum valor adicionado).
# 9
#  Use @classmethod e não crie instâncias. Teste adicionando números e exibindo a média.



# Exercício 10 – Agenda com Contatos (Composição)
# Crie uma classe Contato com atributos nome, telefone, email. Crie uma classe Agenda que possui uma lista privada de contatos. Métodos:
# adicionar_contato(contato) – adiciona à lista.


# listar_contatos() – exibe todos os contatos.


# buscar_contato(nome) – exibe os dados do primeiro contato com aquele nome.

#  Teste adicionando vários contatos e fazendo buscas.


#-------------------------------------------------------------------------
print('---------------------------------------------------')
print('ATIVIDADE 1 - Livro:')


class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.emprestado =  False
    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True 


    def devolver(self):
        self.emprestado = False


    def __str__(self):
        return f'NOME: {self.titulo} AUTOR:{self.autor} ANO:{self.ano}'


livro = Livro('antifragil', 'taleb', 2015)


livro.emprestar()
livro.devolver()


print(livro) 


print('--------------------------------------------------------')

print('ATIVIDADE 2 - Contador com Atributo de Classe:')

class Contador:

    total_contadores = 0

    def __init__(self):
        Contador.total_contadores = Contador.total_contadores + 1

    def exibir_total(self):
        print('Total de contadores:', Contador.total_contadores)


c1 = Contador()
c2 = Contador()
c3 = Contador()

c1.exibir_total()


# Usei um atributo de classe para contar quantos objetos foram criados.

#--------------------------------------------------------------
print('---------------------------------------------------')

print('ATIVIDADE 3 - Produto com Desconto:')

class Produto:

    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @property
    def quantidade(self):
        return self._quantidade

    def aplicar_desconto(self, percentual):
        desconto = self._preco * (percentual / 100)
        self._preco = self._preco - desconto

        if self._preco < 0:
            self._preco = 0


p = Produto('Caneta', 10, 5)

p.aplicar_desconto(20)

print(p.nome, p.preco)

# Usei propriedades para proteger os atributos e método para aplicar desconto.


#-------------------------------------------------------------------------

print('----------------------------------------------------')

print('ATIVIDADE 4 - Banco com Saldo Privado:')

class ContaBancaria:

    def __init__(self):
        self.__saldo = 0

    def depositar(self, valor):
        self.__saldo = self.__saldo + valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo = self.__saldo - valor
        else:
            print('Saldo insuficiente')

    @property
    def saldo(self):
        return self.__saldo


c = ContaBancaria()

c.depositar(500)
c.sacar(200)
c.sacar(1000)

print('Saldo:', c.saldo)


# Usei atributo privado para proteger o saldo.




#----------------------------------------------------------------------
print('--------------------------------------------------------------------')

print('ATIVIDADE 5 - Aluno com Notas:')

class Aluno:

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.__notas = []

    def adicionar_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.__notas.append(nota)

    def calcular_media(self):
        soma = sum(self.__notas)
        return soma / len(self.__notas)

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

print(a.calcular_media())
print(a.situacao())

# Controlei notas privadas e validei valores.




#------------------------------------------------------------------------
print('---------------------------------------------------------')

print('ATIVIDADE 6 - Data - Validação:')

class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return str(self.dia) + '/' + str(self.mes) + '/' + str(self.ano)


d = Data(10, 4, 2026)

print(d)
Explicação:
# Criei uma classe simples com formato de data.




#---------------------------------------------------------------------------------
print('-----------------------------------------------------------------------')

print('ATIVIDADE 7 - Funcioário com Aumento:')

class Funcionario:

    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario

    def aumentar_salario(self, percentual):
        aumento = self.__salario * (percentual / 100)
        self.__salario = self.__salario + aumento

    def calcular_bonus(self):
        return self.__salario * 0.10

    @property
    def salario(self):
        return self.__salario


f = Funcionario('Pedro', 'Analista', 2000)

f.aumentar_salario(10)

print(f.nome, f.salario, f.calcular_bonus())


# Protegi o salário e criei aumento e bônus.




#-------------------------------------------------------------------------------------
print('-------------------------------------------------------------------')

print('ATIVIDADE 8 - Carro com Velocidade:')





#-------------------------------------------------------------------------
print('-------------------------------------------------------------------------')

print('ATIVIDADE 9 - Estátisticas - Atributo de Classe:')





#-----------------------------------------------------------------------------------------
print('-------------------------------------------------------------------------')

print('ATIVIDADE 10 - Agenda com Contatos - Composição:')






#--------------------------------------------------------------------------------
print('------------------------------------------------------------------------')