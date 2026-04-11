# Aula 10 exercícios

# # 

# ## **Exercícios de Nível Médio**

# ### **1. Calculadora com Funções**

# Crie funções separadas para as quatro operações básicas (`somar`, `subtrair`, `multiplicar`, `dividir`). Em seguida, escreva um programa que leia dois números e a operação desejada (como string) e chame a função correspondente. A divisão deve tratar divisão por zero.



# ### **2. Validador de CPF (simplificado)**

# Crie uma função `validar_cpf(cpf)` que recebe uma string com 11 dígitos e retorna `True` se for válido (use o algoritmo básico de validação de CPF). Em seguida, teste a função com alguns CPFs.




# ### **3. Gerador de Tabuada**

# Escreva uma função `tabuada(numero, inicio=1, fim=10)` que exibe a tabuada do `numero` no intervalo `[inicio, fim]`. Se os argumentos `inicio` e `fim` não forem fornecidos, use 1 e 10.




# ### **4. Contador de Palavras**

# Crie uma função `contar_palavras(texto)` que retorna um dicionário com a contagem de cada palavra no texto (considere palavras separadas por espaços). O programa principal deve ler uma frase e exibir o resultado.





# ### **5. Ordenação Personalizada**

# Implemente uma função `ordenar_lista(lista, crescente=True)` que retorna uma nova lista ordenada. Se `crescente=True`, ordena em ordem crescente; caso contrário, decrescente. Não use `sorted()` ou `list.sort()` (implemente o algoritmo de ordenação de sua escolha, como bolha).





### **6. Jogo de Adivinhação**

# Crie uma função `jogar()` que sorteia um número entre 1 e 100 e dá dicas ("maior", "menor") até o usuário acertar. Use `random.randint()`. A função deve retornar o número de tentativas. No programa principal, chame a função e exiba quantas tentativas foram necessárias.




# ### **7. Conversor de Bases**

# Escreva uma função `converter_base(numero, base_origem, base_destino)` que converte um número entre bases 2, 8, 10 e 16. A entrada `numero` é uma string. A função retorna a string convertida. (Exemplo: `converter_base("1010", 2, 16)` → `"A"`). Use `int()` com base e depois formate.





# ### **8. Sistema de Caixa Eletrônico**

# Crie uma função `sacar(valor)` que retorna um dicionário com a quantidade de notas de 100, 50, 20, 10, 5 e 2 necessárias para o valor. O valor deve ser inteiro e positivo. Caso não seja possível (valor não múltiplo de 2), a função retorna `None`. No programa principal, chame a função e exiba o resultado.



# ### **9. Análise de Lista com Múltiplos Retornos**

# Escreva uma função `analisar_lista(lista)` que retorna quatro valores: o menor valor, o maior valor, a soma e a média. No programa principal, receba uma lista de números do usuário (terminada por -1) e exiba os resultados usando desempacotamento.




# ### **10. Função que Modifica Lista Global**

# Crie uma lista global `estoque = []`. Escreva funções:

# - `adicionar_produto(nome, quantidade)`: adiciona um dicionário `{"nome": nome, "quantidade": quantidade}` à lista global.
# - `remover_produto(nome)`: remove o produto com esse nome (se existir).
# - `listar_estoque()`: exibe todos os produtos.
    
#     Use a palavra-chave `global` para modificar a lista dentro das funções. O programa principal deve apresentar um menu interativo para o usuário.




#------------------------------------------------------
print('---------------------------------------------------')

# Crie funções separadas para as quatro operações básicas (`somar`, `subtrair`, `multiplicar`, `dividir`). Em seguida, escreva um programa que leia dois números e a operação desejada (como string) e chame a função correspondente. A divisão deve tratar divisão por zero.


print('ATIVIDADE 1 - Calculadora com Funções:')

def somar (a,b):
  return a + b 

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
   return a * b

def dividir(a,b):
   if b == 0:
     print('Não pode dividir por zero')
     return 0
     return a/b

n1 = float(input('Número 1:'))
n2 = float(input('Número 2:'))
op = input('Operação (+ - * /):')

if op == '+':
   print(somar(n1, n2))
elif op == '-':
   print(subtrair(n1, n2))
elif op == '*':
    print(multiplicar(n1, n2))
elif op == '/':
   print(dividir(n1, n2))

# Criei uma função para cada operação e usei if para escolher qual executar 

#------------------------------------------




print('----------------------------------------------')

# Crie uma função `validar_cpf(cpf)` que recebe uma string com 11 dígitos e retorna `True` se for válido (use o algoritmo básico de validação de CPF). Em seguida, teste a função com alguns CPFs.

print('ATIVIDADE 2 - Validador de CPF (simplificado):')


def validar_cpf(cpf):

    if len(cpf) != 11:
        return False

    soma = 0
    peso = 10

    for i in range(9):
        soma = soma + int(cpf[i]) * peso
        peso = peso - 1

    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0

    soma = 0
    peso = 11

    for i in range(10):
        soma = soma + int(cpf[i]) * peso
        peso = peso - 1

    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
        return True
    else:
        return False


cpf = input('Digite o CPF: ')
print(validar_cpf(cpf))

# multipliquei os números pelos pesos, calculei os dígitos e comparei com os finais do CPF.

#----------------------------



print('---------------------------------------------------')

# Escreva uma função `tabuada(numero, inicio=1, fim=10)` que exibe a tabuada do `numero` no intervalo `[inicio, fim]`. Se os argumentos `inicio` e `fim` não forem fornecidos, use 1 e 10.


print('ATIVIDADE 3 - Gerador de Tabuada:')

def tabuada(numero, inicio=1, fim=10):
   
   for i in range(inicio, fim + 1):
      print(numero, 'x', i, '=', numero * i)

num = int(input('Número:'))
tabuada(num)

# uma função com valore padrões utilizando for para repetir

#---------------------------------




print('---------------------------------------------------')

# Crie uma função `contar_palavras(texto)` que retorna um dicionário com a contagem de cada palavra no texto (considere palavras separadas por espaços). O programa principal deve ler uma frase e exibir o resultado.


print('ATIVIDADE 4 - Contador de Palavra:')











print('---------------------------------------------------')

# Implemente uma função `ordenar_lista(lista, crescente=True)` que retorna uma nova lista ordenada. Se `crescente=True`, ordena em ordem crescente; caso contrário, decrescente. Não use `sorted()` ou `list.sort()` (implemente o algoritmo de ordenação de sua escolha, como bolha).


print('ATIVIDADE 5 - Ordenação Personalizada:')











print('---------------------------------------------------')

# Crie uma função `jogar()` que sorteia um número entre 1 e 100 e dá dicas ("maior", "menor") até o usuário acertar. Use `random.randint()`. A função deve retornar o número de tentativas. No programa principal, chame a função e exiba quantas tentativas foram necessárias.

print('ATIVIDADE 6 - Jogo de Adivinhação:')









print('---------------------------------------------------')

# Escreva uma função `converter_base(numero, base_origem, base_destino)` que converte um número entre bases 2, 8, 10 e 16. A entrada `numero` é uma string. A função retorna a string convertida. (Exemplo: `converter_base("1010", 2, 16)` → `"A"`). Use `int()` com base e depois formate.


print('ATIVIDADE 7 - Conversor de Bases:')










print('---------------------------------------------------')

# Crie uma função `sacar(valor)` que retorna um dicionário com a quantidade de notas de 100, 50, 20, 10, 5 e 2 necessárias para o valor. O valor deve ser inteiro e positivo. Caso não seja possível (valor não múltiplo de 2), a função retorna `None`. No programa principal, chame a função e exiba o resultado.

print('ATIVIDADE 8 - Sistema de Caixa Eletrônico:')













print('---------------------------------------------------')

# Escreva uma função `analisar_lista(lista)` que retorna quatro valores: o menor valor, o maior valor, a soma e a média. No programa principal, receba uma lista de números do usuário (terminada por -1) e exiba os resultados usando desempacotamento.

print('ATIVIDADE 9 - Análise de Lista com Múltiplos Retornos:')









print('---------------------------------------------------')

# Crie uma lista global `estoque = []`. Escreva funções:

# - `adicionar_produto(nome, quantidade)`: adiciona um dicionário `{"nome": nome, "quantidade": quantidade}` à lista global.
# - `remover_produto(nome)`: remove o produto com esse nome (se existir).
# - `listar_estoque()`: exibe todos os produtos.
    
#     Use a palavra-chave `global` para modificar a lista dentro das funções. O programa principal deve apresentar um menu interativo para o usuário.

print('ATIVIDADE 10 -  Função que Modifica Lista Global:')

estoque = []

def adicionar_produto(nome, quantidade):
   global estoque 
   estoque.append({'nome': nome, 'quantidade': quantidade})

def remover_produto(nome):
   global estoque 
   for p in estoque:
      if p['nome'] == nome:
         estoque.remove(p)

def listar_estoque():
   for p in estoque:
      print(p)

op =""

while op != '3':
   print('1 - Adicionar')
   print('2 - Remover')
   print('3 - Listar')

op = input('Escolha:')

if op == '1':
   n = input('Nome:')
   q = int(input('Quantidade:'))
   adicionar_produto(n,q)

elif op == '2':
   n = input('Nome:')
   remover_produto(n)

elif op == '3':
   listar_estoque()


# Usei uma lista global e funções para manipular os dados.