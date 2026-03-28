# 
# Parte 1: Escolha do Destino > Paris, Nova York, Tokyo/// ok
# Peça ao usuário:
# Nome do destino > Paris, Nova York, Tokyo /// ok
# Quantidade de pessoas /// ok 


# Parte 2: Cálculo do Valor > valor da passagem /// ok
# Calcule:
# Valor total da viagem (preço * pessoas) > pessoas /// ok


# Parte 3: Regras da Agência (SEM if, SEM loop) /// ok

# Aplique:
# Se pessoas > 3 → desconto de 10% /// ok
# Se valor total > 10000 → desconto extra de 5%
# Se não houver vagas suficientes → taxa de 500 (overbooking)
# Se destino não existir → valor vira 0


# ---------------------------------------------------------
# viagens = {
#    "Paris": {
#        "preco": 5000,
#        "vagas": 5
#    },
#    "Nova York": {
#        "preco": 4000,
#        "vagas": 3
#    },
#    "Tokyo": {
#        "preco": 6000,
#        "vagas": 2
#    }


import statistics  
# Atividade parte 1 /ok

viagens = {
"Paris": {
    "preço": 4000,
    "vagas": 5
},
"Nova York": {
    "preço": 4000,
    "vagas": 3
},
"Tokyo": {
    "preço": 6000,
    "vagas": 2
}
}

# Parte 1: entrada de dados/ ok
destino = input('Digite o destino: ')
pessoas = int(input('Quantidade de pessoas: '))

dados_viagem = {}

dados_viagem['destino'] = destino
dados_viagem['pessoas'] = pessoas




# verificar se destino existe/ ok
existe = destino in viagens



# verificar se destino existe / ok
existe = destino in viagens



# pegar preço e vagas (sem if, loop)/// ok
preço = existe * viagens.get(destino, {'preco': 0})['preço']
vagas = existe * viagens.get(destino, {'vagas': 0})['vagas']




# Parte 2: cálculo do valor > valor da passagem/// ok
valor_total = preço * pessoas



print('-------------------------------------------')
print('Valor total: ', valor_total)



# Parte 3: regras (sem if ou loop) // ok
# desconto 10% /// ok
desconto1 = (pessoas > 3) * (valor_total * 0.10)




# desconto extra 5% /// ok
desconto2 = (valor_total > 10000) * (valor_total * 0.05)

# taxa overbooking /// ok
taxa = (pessoas > vagas) * 500

# destino inexistente = valor 0 /// ok 
valor_total = valor_total * existe 

# valor final
valor_final = valor_total - desconto1 - desconto2 + taxa


print('-------------------------------------------')
 
# printar os destinos/ pessoas /// ok
print('Destino:', destino)
print('Pessoas:', pessoas)
print('Desconto 10%:', desconto1)
print('Desconto extra 5%:', desconto2)
print('Taxa:', taxa)
print('Valor final:', valor_final)

