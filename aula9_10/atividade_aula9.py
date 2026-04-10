# ## **1 - Atividade pratica com a professora**

# ## **2  - Exercícios**



# ### **1. Tabuada Personalizada**

# Peça ao usuário um número inteiro positivo. Use `for` para exibir a tabuada desse número de 1 a 10.

# **Exemplo:**

# `Digite um número: 7` → exibe 7 x 1 = 7, 7 x 2 = 14, ..., 7 x 10 = 70.

# ---




# ### **2. Contagem Regressiva com Pausa**

# Peça um número inteiro positivo. Use `while` para fazer uma contagem regressiva até 0, exibindo cada número. Após o término, exiba `"Fogo!"`.

# ---



# ### **3. Média de Notas com `while`**

# Peça notas até que o usuário digite `-1`. Calcule e exiba a média das notas válidas (0 a 10). Ignore entradas inválidas e use `continue` quando necessário.

# ---



# ### **4. Validação de Senha com Limite de Tentativas**

# Defina uma senha fixa (ex: `"python123"`). Dê ao usuário 3 tentativas usando `while`. Se acertar, exiba `"Acesso liberado"` e encerre. Se errar todas, exiba `"Conta bloqueada"`.]]
            
#------



# ### **5. Números Primos**

# Peça um número inteiro positivo e determine se ele é primo. Use `for` com `range` e `break` para otimizar.

# ---



# ### **6. Sequência de Fibonacci**

# Gere os primeiros N termos da sequência de Fibonacci, onde N é informado pelo usuário. Use `for` ou `while` para iterar.

# ---



# ### **7. Soma de Dígitos**

# Peça um número inteiro positivo e calcule a soma de seus dígitos. Use `while` para extrair os dígitos um a um.

# ---



# ### **8 Menu Interativo**

# Crie um menu que permaneça ativo até que o usuário escolha a opção `"Sair"`. As opções podem ser:

# - `1` – Exibir mensagem "Olá!"
# - `2` – Exibir a data/hora atual (use `import datetime`)
# - `3` – Sair

# Use `while True` e `break` para sair.

# ---




# ### **9 Simulador de Lançamento de Dados**

# Simule 100 lançamentos de um dado de 6 faces. Conte quantas vezes cada face foi sorteada e exiba o resultado. Use `for` e `random.randint(1,6)`. (Importe `random`.)




# ATIVIDADE 1 
#-------------------------------------------
# Peça ao usuário um número inteiro positivo. Use `for` para exibir a tabuada desse número de 1 a 10.

# Usei for para repetir de 1 até 10. em cada repetição eu multiplico o número digitado pelo contador e mostro o resultado

print('-------------------------------------------------')

print('ATIVIDADE 1 - Tabuada Personalizada: ')

numero = int(input('Digite um número:'))

for i in range(1, 11):
    resultado = numero *i 
    print(numero, 'x',i,'=', resultado)



# ATIVIDADE 2
#-----------------------------------------------
# Peça um número inteiro positivo. Use `while` para fazer uma contagem regressiva até 0, exibindo cada número. Após o término, exiba `"Fogo!"`.

# Eu usei um while que começa no número digitado e vai diminuindo até chegar em 0. Depois que termina, aparece "fogo!"

print('-----------------------------------------------------')

print('ATIVIDADE 2 -  Contagem Regressiva com Pausa: ')

n = int(input('Digite um número:'))

contador = n 

while contador >= 0:
    print(contador)
    contador = contador -1

    print('Fogo!')



# ATIVIDADE 3
#-----------------------------------------------
# Peça notas até que o usuário digite `-1`. Calcule e exiba a média das notas válidas (0 a 10). Ignore entradas inválidas e use `continue` quando necessário.

# Fui seguindo a lógica de pedir para o usuário digitar notas até ele digitar -1 para parar. e enquanto isso as notas vão sendo somadas, e no final elas são divididas pela quantidade para encontrar a média

print('---------------------------------------------------')

print('Atividade 3 - Médias de notas com while: ')

soma = 0
quantidade = 0

nota = float(input('Digite a nota (-1 para sair):'))

while nota !=-1:
    soma = soma + nota 
    quantidade = quantidade + 1

    nota = float(input('Digite a nota (-1 para sair):'))

media = soma / quantidade

print('Soma:', soma)
print('Quantidade:', quantidade)
print('Média:', media)


# ATIVIDADE 4
#------------------------------------------------
# Defina uma senha fixa (ex: `"python123"`). Dê ao usuário 3 tentativas usando `while`. Se acertar, exiba `"Acesso liberado"` e encerre. Se errar todas, exiba `"Conta bloqueada"`.]]

# Eu usei um while para dar até 3 tentatvas ao usuário, se acertar o acesso é liberado se errar a conta é bloqueada


print('-------------------------------------------------')

print('ATIVIDADE 4 - Validação de Senha com Limite de Tentativas:')

senha_correta = 'python123'
tentativas = 0

while tentativas < 3:
    senha = input('Digite a senha: ')

    if senha == senha_correta:
        print('Acesso liberado')
        break
    else:
        print('Senha incorreta')

    tentativas = tentativas + 1

if tentativas == 3:
    print('Conta bloqueada')




# ATIVIDADE 5
#--------------------------------------------------
# Peça um número inteiro positivo e determine se ele é primo. Use `for` com `range` e `break` para otimizar.

# Eu utilizei um for para testar se o número é divisível por outros números, se ele não é divisível por nenhum ele é primo, caso contrário não é primo.

print('--------------------------------------------')

print('ATIVIDADE 5 - Números Primos:')

num = int(input('Digite um número: '))

primo = True

for i in range(2, num):
    resto = num % i

    if resto == 0:
        primo = False
        break

if primo == True:
    print('É primo')
else:
    print('Não é primo')



# ATIVIDADE 6
#--------------------------------------------------
# Gere os primeiros N termos da sequência de Fibonacci, onde N é informado pelo usuário. Use `for` ou `while` para iterar.

# Usei duas variáveis para guardar os valores da sequência e fui atualizando elas a cada repetição  usando um contador

print('-----------------------------------------------')

print('ATIVIDADE 6 - Sequência de Fibonacci:')

n = int(input('Quantidade de termos:'))

a = 0
b = 1

contador = 0

while contador < n:

    print('Valor atual:' , a)

    proximo = a + b
    print('Soma dos dois:' , proximo)

    a = b
    b = proximo 

    contador = contador + 1


# ATIVIDADE 7
#---------------------------------------------------
# Peça um número inteiro positivo e calcule a soma de seus dígitos. Use `while` para extrair os dígitos um a um.

# Eu usei um while para pegar cada dígito do número. Após isso eu usei o resto da divisão por 10 para pegar o último número e fui somando, e depois disso eu fui dividindo o número até acabar.

print('--------------------------------------------')

print('ATIVIDADE 7 - Soma de Dígitos:')

num = int(input('Digite um número: '))

soma = 0

while num > 0:
    digito = num % 10
    soma = soma + digito 

    num = num // 10 

print('Resultado da soma:', soma)



# ATIVIDADE 8
#----------------------------------------------------
# Crie um menu que permaneça ativo até que o usuário escolha a opção `"Sair"`. As opções podem ser:

# - `1` – Exibir mensagem "Olá!"
# - `2` – Exibir a data/hora atual (use `import datetime`)
# - `3` – Sair

# Use `while True` e `break` para sair.

print('----------------------------------------------')

print('ATIVIDADE 8 - Menu Interativo')

import datetime

opcao = ''

while opcao != '3':

    print('1 - Olá')
    print('2 - Data e hora')
    print('3 - Sair')

    opcao = input('Escolha: ')

    if opcao == '1':
        print('Olá!')

    elif opcao == '2':
        agora = datetime.datetime.now()
        print('Data e hora:', agora)

    elif opcao == '3':
        print('Encerrando...')

    else:
        print('Opção inválida')




# ATIVIDADE 9
#----------------------------------------------------
# Simule 100 lançamentos de um dado de 6 faces. Conte quantas vezes cada face foi sorteada e exiba o resultado. Use `for` e `random.randint(1,6)`. (Importe `random`.)

print('---------------------------------------------------')

print('ATIVIDADE 9 - Simulador de Lançamento de Dados')


import random

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0

for i in range(100):
    valor = random.randint(1, 6)

    if valor == 1:
        c1 = c1 + 1

    elif valor == 2:
        c2 = c2 + 1

    elif valor == 3:
        c3 = c3 + 1

    elif valor == 4:
        c4 = c4 + 1

    elif valor == 5:
        c5 = c5 + 1

    else:
        c6 = c6 + 1

print('Quantidade de cada número:')
print('1:', c1)
print('2:', c2)
print('3:', c3)
print('4:', c4)
print('5:', c5)
print('6:', c6)
