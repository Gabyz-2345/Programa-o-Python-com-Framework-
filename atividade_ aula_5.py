# NÃO UTILIZE IF ELSE, LOOPS, FUNÇÕES, APENAS I/O, VARIÁVEIS, LISTAS, TUPLAS SINAIS LÓGICOS E ARITMÉTICOS

# 1. Verificação de maioridade e permissão
# Enunciado:
# Crie um programa que leia a idade do usuário e se ele possui autorização dos pais (responda True ou False).
# O usuário pode participar da atividade se tiver 18 anos ou mais ou tiver autorização dos pais.
# Use and / or para verificar e exiba "Pode participar" ou "Não pode participar".

# Exemplo:

# idade  = int(input('Idade: '))
# autorizacao = input('Possui autorização?>>>  ')
# pode  =  idade >= 18 and autorizacao == 'Pode'
# msg =  pode and "pode" or "não pode"
# print(msg)


# 2. Classificação de peso ideal
# Enunciado:
# Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC (peso / altura**2).
# Uma pessoa está com peso normal se o IMC estiver entre 18.5 e 24.9 (inclusive).
# Use operadores lógicos para verificar se o IMC está nessa faixa e exiba "Peso normal" ou "Fora da faixa".




# 3. Acesso ao sistema
# Enunciado:
# Leia o nome de usuário e a senha. O acesso é permitido apenas se o usuário for "admin" e a senha for "1234".
# Use and para verificar as duas condições e exiba "Acesso liberado" ou "Acesso negado".



# 4. Compra com desconto
# Enunciado:
# Leia o valor da compra e se o cliente é VIP (True ou False).
# O cliente ganha 10% de desconto se o valor for maior que R$ 100 ou ele for VIP.
# Exiba o valor final com desconto (se aplicável) ou o valor original.




# 5. Elegibilidade para doação de sangue
# Enunciado:
# Leia a idade e o peso.
# Para doar sangue, a pessoa deve ter entre 16 e 69 anos (inclusive) e pesar pelo menos 50 kg.
# Use and para verificar ambos os critérios e informe se a pessoa pode doar.




# 6. Validação de horário de funcionamento
# Enunciado:
# Uma loja funciona de segunda a sexta, das 9h às 18h.
# Leia o dia da semana (1=segunda, 7=domingo) e a hora (0 a 23).
# Determine se a loja está aberta.
# Dica: use and para combinar dia útil com horário, e or se quiser tratar sábado/domingo como fechado.



# 7. Aprovação em duas disciplinas
# Enunciado:
# Leia as notas de Matemática e Português.
# O aluno é aprovado se ambas as notas forem maiores ou iguais a 6.
# Use and para verificar e exiba "Aprovado" ou "Reprovado".



# 8. Identificação de ano bissexto
# Enunciado:
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400.
# Leia um ano e use and e or para determinar se ele é bissexto.
# Exiba "Ano bissexto" ou "Ano não bissexto".



# 9. Faixa etária
# Enunciado:
# Leia a idade e classifique:

# "Criança" se idade < 12

# "Adolescente" se 12 ≤ idade ≤ 17

# "Adulto" se idade ≥ 18
# Use and e or para definir os intervalos e exiba a classificação.



# 10. Sistema de alerta de temperatura e umidade
# Enunciado:
# Leia a temperatura (°C) e a umidade (%).
# Dispare um alerta se temperatura > 35 ou umidade > 70.
# Caso contrário, exiba "Condições normais".
# Use or para combinar as condições.


# atividade


print('-------------------------------------------')

print('ATIVIDADE 1')


idade = int(input('Idade: '))
autorizacao = input('Possui autorização? ')


condicao_idade = idade >= 18
condicao_autorizacao = autorizacao == 'True'


pode_participar = condicao_idade or condicao_autorizacao


msg1 = pode_participar and "Pode participar"
msg2 = (pode_participar == False) and "Não pode participar"


msg = msg1 or msg2


print(msg)

print('-----------------------------------------')

print('ATIVIDADE 2')


peso = float(input('Peso: '))
altura = float(input('Altura: '))


imc = peso / (altura ** 2)


condicao1 = imc >= 18.5
condicao2 = imc <= 24.9


peso_normal = condicao1 and condicao2


msg1 = peso_normal and "Peso normal"
msg2 = (peso_normal == False) and "Fora da faixa"


msg = msg1 or msg2


print(msg)

print('----------------------------------------')

print('ATIVIDADE 3')

usuario = input('Usuário: ')
senha = input('Senha: ')


condicao_user = usuario == 'admin'
condicao_senha = senha == '1234'


acesso = condicao_user and condicao_senha


msg1 = acesso and "Acesso liberado"
msg2 = (acesso == False) and "Acesso negado"


msg = msg1 or msg2


print(msg)


print('----------------------------------------')

print('ATIVIDADE 4')

valor = float(input('Valor da compra: '))
vip = input('É VIP? (True/False): ')


condicao_valor = valor > 100
condicao_vip = vip == 'True'


tem_desconto = condicao_valor or condicao_vip


valor_desconto = valor * 0.10
valor_final = valor - (tem_desconto * valor_desconto)


msg1 = tem_desconto and "Desconto aplicado"
msg2 = (tem_desconto == False) and "Sem desconto"


msg = msg1 or msg2


print(msg)
print('Valor final:', valor_final)


print('-------------------------------------')

print('ATIVIDADE 5')

idade = int(input('Idade: '))
peso = float(input('Peso: '))


condicao1 = idade >= 16
condicao2 = idade <= 69
condicao3 = peso >= 50


pode_doar = condicao1 and condicao2 and condicao3


msg1 = pode_doar and "Pode doar"
msg2 = (pode_doar == False) and "Não pode doar"


msg = msg1 or msg2


print(msg)


print('------------------------------')

print('ATIVIDADE 6')

dia = int(input('Dia (1 a 7): '))
hora = int(input('Hora: '))


condicao_dia1 = dia >= 1
condicao_dia2 = dia <= 5
condicao_hora1 = hora >= 9
condicao_hora2 = hora <= 18


dia_util = condicao_dia1 and condicao_dia2
horario = condicao_hora1 and condicao_hora2


loja_aberta = dia_util and horario


msg1 = loja_aberta and "Loja aberta"
msg2 = (loja_aberta == False) and "Loja fechada"


msg = msg1 or msg2


print(msg)


print('---------------------------------------')

print('ATIVIDADE 7')

nota1 = float(input('Matemática: '))
nota2 = float(input('Português: '))


condicao1 = nota1 >= 6
condicao2 = nota2 >= 6


aprovado = condicao1 and condicao2


msg1 = aprovado and "Aprovado"
msg2 = (aprovado == False) and "Reprovado"


msg = msg1 or msg2


print(msg)

print('--------------------------------------')

print('ATIVIDADE 8')

ano = int(input('Ano: '))


condicao1 = ano % 4 == 0
condicao2 = ano % 100 != 0
condicao3 = ano % 400 == 0


parte1 = condicao1 and condicao2
bissexto = parte1 or condicao3


msg1 = bissexto and "Ano bissexto"
msg2 = (bissexto == False) and "Ano não bissexto"


msg = msg1 or msg2


print(msg)



