# Mostre:

# Saldo atual
# Lista de transações

# Peça:
# Valor da operação (positivo depósito, negativo saque)

# Calcule:
# Novo saldo

# Peça:
# Valor da operação (positivo depósito, negativo saque)
# Calcule:
# Novo saldo


# Parte 3: Regras do Banco
# aplique regras usando apenas lógica:

# Se saldo final < 0 - cobrar taxa de 20
# Se depósito > 500 - bônus de 10
# Se saque maior que saldo - taxa extra de 15


# Sem if // ok

#-------------------------------------------------------------------------------------------------------


# sinais lógicos
# sinais aritméticos
# estruturas de dados
# funções build


# Lógica de programação:

# escolher cliente
# mostrar saldo
# mostrar transações
# fazer operações
# calcular novo saldo
# aplicar regras





print('---------------------------------')
banco = {
    "Joao": {
        "saldo": 1500,
        "transacoes": [200, -100, 50]
    },
    "Maria": {
        "saldo": 800,
        "transacoes": [-200, -50, 300]
    },
    "Carlos": {
        "saldo": 1200,
        "transacoes": [500, -300, -100]
    }
}




dados_banco = {}


# escolher cliente
nome = input('Digite o nome do cliente: ')

dados_banco['cliente'] = nome


# verificar se existe
existe = nome in banco


# pegar saldo e transações (sem if)
saldo = existe * banco.get(nome, {'saldo': 0})['saldo']
transacoes = existe * banco.get(nome, {'transacoes': []})['transacoes']


print('-------------------------------------------')

print('Saldo atual:', saldo)
print('Transações:', transacoes)


# primeira operação
op1 = float(input('Digite valor (positivo depósito, negativo saque): '))

novo_saldo_1 = saldo + op1


# regras (SEM IF)

taxa_negativo_1 = (novo_saldo_1 < 0) * 20
bonus_1 = (op1 > 500) * 10
taxa_saque_1 = (op1 < 0) * ((-op1) > saldo) * 15


saldo_final_1 = novo_saldo_1 - taxa_negativo_1 + bonus_1 - taxa_saque_1


print('-------------------------------------------')

print('Saldo após operação 1:', saldo_final_1)


# segunda operação
op2 = float(input('Digite valor (positivo depósito, negativo saque): '))

novo_saldo_2 = saldo_final_1 + op2


# regras (SEM IF)

taxa_negativo_2 = (novo_saldo_2 < 0) * 20
bonus_2 = (op2 > 500) * 10
taxa_saque_2 = (op2 < 0) * ((-op2) > saldo_final_1) * 15


saldo_final_2 = novo_saldo_2 - taxa_negativo_2 + bonus_2 - taxa_saque_2


print('-------------------------------------------')

print('Saldo final:', saldo_final_2)


dados_banco['saldo_final'] = saldo_final_2


print('-------------------------------------------')
print(dados_banco)




# teste 

# Nome: Joao
# Operação 1: -2000
# Operação 2: 600





