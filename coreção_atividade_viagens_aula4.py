viagens = {
    "Paris": {
        "preco": 5000,
        "vagas": 5
    },
    "Nova York": {
        "preco": 4000,
        "vagas": 3
    },
    "Tokyo": {
        "preco": 6000,
        "vagas": 2
    }
}




# Parte 1: Escolha do Destino
# Peça ao usuário:
# Nome do destino
# Quantidade de pessoas


destino =  input('Destino: ')
quantidade = int(input('Quantida de pessoas: '))






# Parte 2: Cálculo do Valor
# Calcule:
# Valor total da viagem (preço * pessoas)


calculo =  viagens[destino]['preco'] * quantidade
print('Calculo da viagem R$', calculo)




# Parte 3: Regras da Agência (SEM if, SEM loop)


# Aplique:
# Se pessoas > 3 → desconto de 10%
desconto_1 = (quantidade > 3) * calculo * 0.10
print('Desconto de 10%', desconto_1)



# Se valor total > 10000 → desconto extra de 5%
total =  (calculo > 10000 ) * calculo * 0.05
print('desconto de 5%',  calculo - total)


# Se não houver vagas suficientes → taxa de 500 (overbooking)
vagas_s =  (calculo + 500.0) * (viagens[destino]['vagas'] < quantidade ) 
print('Overbooking', vagas_s)



# Se destino não existir → valor vira 0
destino_ex = (input('Digite o destino> ') in viagens  ) * calculo  
print('Valor total R$ ', destino_ex)



