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
print('-------------------------------------------------')

print('ATIVIDADE 1 - Tabuada Personalizada: ')

numero = int(input('Digite um número:'))

for i in range(1, 11):
    resultado = numero *i 
    print(numero, 'x',i,'=', resultado)



# ATIVIDADE 2
#-----------------------------------------------
# Peça um número inteiro positivo. Use `while` para fazer uma contagem regressiva até 0, exibindo cada número. Após o término, exiba `"Fogo!"`.

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

print('-------------------------------------------------')

print('ATIVIDADE 4 - Validação de Senha com Limite de Tentativas:')








# ATIVIDADE 5
#--------------------------------------------------
print('--------------------------------------------')

print('ATIVIDADE 5 - Números Primos:')







# ATIVIDADE 6
#--------------------------------------------------
print('-----------------------------------------------')

print('ATIVIDADE 6 - Sequência de Fibonacci:')




# ATIVIDADE 7
#---------------------------------------------------
print('--------------------------------------------')

print('ATIVIDADE 7 - Soma de Dígitos:')





# ATIVIDADE 8
#----------------------------------------------------
print('----------------------------------------------')

print('ATIVIDADE 8 - Menu Interativo')





# ATIVIDADE 9
#----------------------------------------------------
# Simule 100 lançamentos de um dado de 6 faces. Conte quantas vezes cada face foi sorteada e exiba o resultado. Use `for` e `random.randint(1,6)`. (Importe `random`.)

print('---------------------------------------------------')

print('ATIVIDADE 9 - Simulador de Lançamento de Dados')
