# Contexto
# Uma loja oferece um cupom especial. O cliente ganha o cupom se atender a pelo menos  das seguintes condições:
#  Se for VIP (responde "sim" ou "não")
# Valor da compra acima de R$ 200
# Primeira compra no mês (responder "sim" ou "nao")
# Além disso, o cupom  pode ser aplicado se o cliente tiver  no histórico (número inteiro).Tarefa
# Receba:
# vip (string "sim" ou "nao")
# valor (float)
# primeira_compra (string "sim" ou "nao")
# reclamações (int)
# Determine se o cliente  ("Cupom liberado") ou  ("Sem cupom"),  (SEM IF , SEM LOOP, SEM FUNÇÃO)







# sinais lógicos;
# variáveis;
# input e output.


# Lógica de programação:

# receber dados;
# verificar condições;
# decidir cupom.


# entrada:


vip = input('Cliente VIP? (sim/nao): ')
valor = float(input('Valor da compra: '))
primeira_compra = input('Primeira compra? (sim/nao): ')
reclamacoes = int(input('Quantidade de reclamações: '))


# condições:

cond_vip = vip == 'sim'
cond_valor = valor > 200
cond_primeira = primeira_compra == 'sim'

cond_beneficio = cond_vip or cond_valor or cond_primeira

cond_sem_reclamacao = reclamacoes == 0


# decisão:

pode_cupom = cond_beneficio and cond_sem_reclamacao


# mensagem: (com cupom ou sem cupom)

msg1 = pode_cupom and "Cupom liberado"
msg2 = (pode_cupom == False) and "Sem cupom"

msg = msg1 or msg2


# saída:

print(msg)








