# 1 - Desafio com a professora
# 2 - Exercícios
# 1. Classificação de Notas com Menção
# Crie um programa que leia a nota de um aluno (0 a 10) e exiba a menção correspondente:
# "Excelente" se nota >= 9
# "Bom" se nota >= 7 e < 9
# "Regular" se nota >= 5 e < 7
# "Insuficiente" se nota < 5
# 2. Validação de Triângulo
# Leia três lados de um triângulo. Verifique se eles formam um triângulo (cada lado é menor que a soma dos outros dois). Se sim, classifique como:
# "Equilátero" (todos os lados iguais)
# "Isósceles" (dois lados iguais)
# "Escaleno" (todos diferentes)
# 3. Cálculo de IMC com Faixas
# Leia peso (kg) e altura (m). Calcule o IMC e classifique conforme a tabela da OMS:
# "Abaixo do peso" se IMC < 18.5
# "Peso normal" se 18.5 ≤ IMC < 25
# "Sobrepeso" se 25 ≤ IMC < 30
# "Obesidade" se IMC ≥ 30
# 4. Imposto de Renda Simplificado
# Leia o salário bruto mensal e calcule o desconto do INSS (11% sobre o salário, limitado a R$ 1.500,00) e o IRRF conforme tabela:
# Isento se salário bruto ≤ R$ 2.500,00


# 7,5% sobre o que exceder R$ 2.500,00 até R$ 3.500,00


# 15% sobre o que exceder R$ 3.500,00 até R$ 5.000,00


# 27,5% sobre o que exceder R$ 5.000,00

#  Exiba o salário líquido após os descontos.


# 5. Jogo de Pedra, Papel e Tesoura
# Leia duas jogadas ("pedra", "papel" ou "tesoura") e determine o vencedor ou empate. Use condicionais aninhadas.
# 6. Aprovação com Recuperação
# Leia a nota da N1 e N2. Calcule a média ((N1+N2)/2). Se média ≥ 7, aprovado. Se média < 4, reprovado. Caso contrário, o aluno vai para recuperação. Nesse caso, leia a nota da recuperação (NR). A média final é (média + NR)/2. Se média final ≥ 5, aprovado; senão, reprovado.
# 7. Alistamento Militar
# Leia o ano de nascimento, o sexo (M ou F) e se o usuário possui alguma deficiência impeditiva (sim ou não).
# Se sexo for F, exiba "Não obrigatório".
# Se sexo for M, calcule a idade. Se idade < 18, exiba o tempo restante. Se idade = 18, exiba "Aliste-se imediatamente". Se idade > 18 e ≤ 45, exiba "Já passou do prazo". Se idade > 45, exiba "Dispensado por idade".
# Se houver deficiência, altere a mensagem para "Dispensado por condição de saúde" (prioridade sobre outras mensagens).
# 8. Escolha de Plano de Saúde
# Leia a idade do cliente e o tipo de plano ("basico", "standard", "premium"). O valor mensal é calculado como:
# Básico: R$ 100 + (idade * 2)


# Standard: R$ 150 + (idade * 3)


# Premium: R$ 200 + (idade * 5)

#  Se o cliente tiver mais de 60 anos, há um acréscimo de 10% sobre o valor total


# 9. Validação de Data
# Leia um dia (1-31), mês (1-12) e ano (qualquer). Verifique se a data é válida, considerando meses com 30/31 dias e fevereiro (28 ou 29 dias, considerando ano bissexto: divisível por 400 ou (divisível por 4 e não por 100)).
# 10. Simulador de Caixa Eletrônico
# Leia o valor a ser sacado (inteiro, múltiplo de 5, entre 10 e 1000). Calcule a menor quantidade possível de notas de 50, 20, 10 e 5. Exiba a quantidade de cada nota. Caso o valor não esteja dentro das regras, exiba uma mensagem de erro.




# -------------------------------------------
print('ATIVIDADE 1 - Notas')

nota = float(input('Digite a nota: '))

if nota >= 9:
    print('Excelente')
elif nota >= 7:
    print('Bom')
elif nota >= 5:
    print('Regular')
else:
    print('Insuficiente')


# -------------------------------------------
print('ATIVIDADE 2 - Triângulo')

a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print('Equilátero')
    elif a == b or a == c or b == c:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não forma triângulo')


# -------------------------------------------
print('ATIVIDADE 3 - IMC')

peso = float(input('Peso: '))
altura = float(input('Altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso normal')
elif imc < 30:
    print('Sobrepeso')
else:
    print('Obesidade')


# -------------------------------------------
print('ATIVIDADE 4 - Salário')

salario = float(input('Salário bruto: '))

inss = salario * 0.11

if inss > 1500:
    inss = 1500

if salario <= 2500:
    ir = 0
elif salario <= 3500:
    ir = (salario - 2500) * 0.075
elif salario <= 5000:
    ir = (salario - 3500) * 0.15
else:
    ir = (salario - 5000) * 0.275

liquido = salario - inss - ir

print('Salário líquido:', liquido)


# -------------------------------------------
print('ATIVIDADE 5 - Pedra, Papel e Tesoura')

j1 = input('Jogador 1: ')
j2 = input('Jogador 2: ')

if j1 == j2:
    print('Empate')
elif j1 == 'pedra':
    if j2 == 'tesoura':
        print('Jogador 1 venceu')
    else:
        print('Jogador 2 venceu')
elif j1 == 'papel':
    if j2 == 'pedra':
        print('Jogador 1 venceu')
    else:
        print('Jogador 2 venceu')
else:
    if j2 == 'papel':
        print('Jogador 1 venceu')
    else:
        print('Jogador 2 venceu')


# -------------------------------------------
print('ATIVIDADE 6 - Média')

n1 = float(input('N1: '))
n2 = float(input('N2: '))

media = (n1 + n2) / 2

if media >= 7:
    print('Aprovado')
elif media < 4:
    print('Reprovado')
else:
    nr = float(input('Recuperação: '))
    media_final = (media + nr) / 2

    if media_final >= 5:
        print('Aprovado')
    else:
        print('Reprovado')


# -------------------------------------------
print('ATIVIDADE 7 - Alistamento')

ano = int(input('Ano de nascimento: '))
sexo = input('Sexo (M/F): ')
deficiencia = input('Deficiência (sim/nao): ')

idade = 2026 - ano

if deficiencia == 'sim':
    print('Dispensado por condição de saúde')
elif sexo == 'F':
    print('Não obrigatório')
else:
    if idade < 18:
        print('Falta tempo para alistar')
    elif idade == 18:
        print('Aliste-se imediatamente')
    elif idade <= 45:
        print('Já passou do prazo')
    else:
        print('Dispensado por idade')


# -------------------------------------------
print('ATIVIDADE 8 - Plano de saúde')

idade = int(input('Idade: '))
plano = input('Plano: ')

if plano == 'basico':
    valor = 100 + (idade * 2)
elif plano == 'standard':
    valor = 150 + (idade * 3)
else:
    valor = 200 + (idade * 5)

if idade > 60:
    valor = valor + (valor * 0.10)

print('Valor:', valor)


# -------------------------------------------
print('ATIVIDADE 9 - Data')

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

if mes == 2:
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        if dia <= 29:
            print('Data válida')
        else:
            print('Data inválida')
    else:
        if dia <= 28:
            print('Data válida')
        else:
            print('Data inválida')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
        print('Data válida')
    else:
        print('Data inválida')
else:
    if dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')


# -------------------------------------------
print('ATIVIDADE 10 - Caixa eletrônico')

valor = int(input('Valor: '))

if valor >= 10 and valor <= 1000 and valor % 5 == 0:

    n50 = valor // 50
    valor = valor % 50

    n20 = valor // 20
    valor = valor % 20

    n10 = valor // 10
    valor = valor % 10

    n5 = valor // 5

    print('50:', n50)
    print('20:', n20)
    print('10:', n10)
    print('5:', n5)

else:
    print('Valor inválido')




# correção:

