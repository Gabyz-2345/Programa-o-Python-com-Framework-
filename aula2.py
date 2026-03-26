# 4 tipos de dados primitivos 
# srt, type, float, bool
# textos numeros inteiros reais lógicos 
#'texto', 10, 5.2, true , false 
#'Bom dia' , 2026,1.80, 1   ,0
#'Seu nome: ' ,1, 60.200,
# 'R$'

# ESTRUTURA DE DADOS****

# espaços na memória ram da máquina 
# variar
# variáveis são dados únicos
# interpertador
# meio termo linguagem
# força a identação = organização do código
# OUTPUT - SAÍDA - print ()
# nomear de forma semântica - dar o nome daquilo que ele é para ter uma organização melhor 

# regras para criar variáveis:
#_ ou alguma letra de resto NÃO
# não pode começar por números
# não pode caracteres especiais
# não pode utilizar números (só não pode começar)
# palavra composta snake_case

# linguagem alto nível
# interpretada 
# dinâmica - variáveis

cidade = 'Guarulhos' 
cidade = 'São Paulo'
CIDADE = 'BH'
Cidade = 'rj'

print('Guarulhos')

print(cidade)

print('CADASTRO DE USUÁRIOS:')
nome = 'Gabriely'
idade = 17
email_usuário = 'gabrielyaraujo179@gmail.com'
peso = 80.50
altura = 1.90
endereço = 'Rua 10, Jd X'
graduação = 'ADS'
casado = False

# saída
print('nome')
print('idade')
print('email_usuário')
print('peso')
print('altura')
print('endereço')
print('graduação')
print('casado')

# Entrada

nome_2 = input('digite seu nome:')
print(nome_2)

numero1 = float (input('digite seu peso: '))
numero2=  float (input ('digite sua altura: '))
numero3 = int (input('digite o ano:'))

soma = numero1 + numero2
print(soma)

print(IMC)

peso = float(input('digite seu peso:'))
altura = float(input)





# código da prof:
# 4  tipos
# str      int             float    bool
# textos numeros inteiros reais lógicos
# 'texto',  10 ,  5.2 ,  True , False
# 'Bom dia', 2026,1.80, 1 , 0
# 'Seu nome:',1, 60.200, 
# 'R$'


# ESTRUTURAS DE DADOS ****


# espaços na memória ram da maquina
# variar
# variaveis são dados únicos
# interpertador 
# meio termo linguagem 
# força indentação = organização
# OUTPUT - SAIDA - print()
# nomear de forma semantica  -  boa pratica


# regras para criar variáveis:
# _ ou letra
# não pode começar por números 
# não pode carcateres especiais 
# pode utilizar números(só não pode começar)
# palavra composta snake_case


# linguagem alto nivel
# interpretada
# dinamica - variáveis


print('CADASTRO DE USUÁRIOS:')


nome = 'Lucas Lima'
idade  =  25
email_usuario = 'lucas@gmail.com'
peso = 80.50
altura =  1.90
endereco = 'Rua 10, Jd X'
graduacao = 'ADS'
casado = False 


# SAÍDA
print(nome)
print(idade)
print(email_usuario)
print(endereco)
print(graduacao)
print(peso)
print(altura)
print(casado)

#código da prof:

print('IMC')


peso =  float(input('Digite seu peso: '))
altura  =  float(input('Digite sua altura: '))
imc  =  peso/altura**2
print('IMC', imc)

print(10+200) # soma
print(10-200) # subtração
print(10*200) # multiplicalçi
print(10/200) # divisão
print('modulo', 10%200) #módulo
print(10**2) # potencia
print(10//200.0) # divisão c/ 2 barras

# variáveis  - estrtuturas de dados
# funções - print() input() float() int()
# sinais ariméticos


# sinais lógicos

print('SINAIS DE CALCULO ARITMÉTICO')



print(10+200) # soma
print(10-200) # subtração
print(10*200) # multiplicalçi
print(10/200) # divisão
print('modulo', 10%200) #módulo
print(10**2) # potencia
print(10//200.0) # divisão c/ 2 barras


# variáveis -  estruturas de dados 
# funções  - print() input() float() int()
# sinais aritmétivos 



# sinais lógicos


print(10 == 200) # comparar
print(10 > 200) # verifa se 1º numero é maior
print(10<200) # verifa se 1º numero é menor
print(10>=200) # maior ou iguael
print(10<=200) # menor ou igual
print(10 != 2) # diferente


# atividade: 

# Crie um programa que: Peça ao usuário dois números.
n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))

# mostre
# A soma, subtração, multiplicação e divisão.
print(n1+n2) # soma
print(n1-n2) # subtração
print(n1*n2) # multiplicação
print(n1/n2) # divisão

# Verifique: 

# Se os números são iguais.
print(n1 == n2) # diferente


# Se o primeiro número é maior que o segundo.
print(n1 > n2) # verifica se o 1º numero é maior que o segundo

# Se pelo menos um dos números é maior que 10.
print(n1 > 10) # verifica se o 1º numero é maior que 10