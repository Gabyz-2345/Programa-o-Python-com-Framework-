# instruções:

# Atividade aula 8

# Exemplo prático
# idade = int(input("Digite sua idade: "))
# if idade < 12:
#     print("Criança")
# elif idade < 18:
#     print("Adolescente")
# else:
#     print("Adulto")



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




# # 3. Cálculo de IMC com Faixas
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


#--------------------------------------------
 
print('----------------------------------------------')

print('ATIVIDADE 1 - Classificação de Notas com Menção')

nota = float(input('Digite a nota:'))

if nota >=9:
    print('Excelente')
elif: nota >= 7:
    print('Regular')