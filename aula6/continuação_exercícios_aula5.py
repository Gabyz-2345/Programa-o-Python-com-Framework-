# -------------------------------------------
print('ATIVIDADE 1') 


idade = int(input('Idade: '))
autorizacao = input('Possui autorização?>>> ')


condicao_idade = idade >= 18
condicao_autorizacao = autorizacao == 'True'


pode_participar = condicao_idade or condicao_autorizacao


msg1 = pode_participar and "Pode participar"
msg2 = (pode_participar == False) and "Não pode participar"


msg = msg1 or msg2


print(msg)




# -------------------------------------------
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




# -------------------------------------------
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




# -------------------------------------------
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




# -------------------------------------------
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




# -------------------------------------------
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




# -------------------------------------------
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




# -------------------------------------------
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




# -------------------------------------------
print('ATIVIDADE 9')

idade = int(input('Idade: '))


condicao_crianca = idade < 12
condicao_adolescente1 = idade >= 12
condicao_adolescente2 = idade <= 17
condicao_adolescente = condicao_adolescente1 and condicao_adolescente2


condicao_adulto = idade >= 18


msg1 = condicao_crianca and "Criança"
msg2 = condicao_adolescente and "Adolescente"
msg3 = condicao_adulto and "Adulto"


msg = msg1 or msg2 or msg3


print(msg)


# -------------------------------------------
print('ATIVIDADE 10')


temp = float(input('Temperatura: '))
umidade = float(input('Umidade: '))


condicao_temp = temp > 35
condicao_umidade = umidade > 70


alerta = condicao_temp or condicao_umidade


msg1 = alerta and "Alerta"
msg2 = (alerta == False) and "Condições normais"


msg = msg1 or msg2


print(msg)

