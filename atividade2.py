# Peça o valor de um produto e: 
produto = float(input('Digite o valor do produto: '))

# Calcule um desconto de 10%.
valor_desconto = produto * 0.10



# Mostre o valor final. 
print(valor_desconto)
print()

vp = produto - valor_desconto

# Verifique se o valor final é maior que 100.
print(vp > 100) # verifica se 1º numero é maior que 100.

# Verifique se o produto ficou barato (menor que 50).
print(vp < 50) # menor ou igual a 50








# coreção da atividade:





# Peça o valor de um produto e:
produto =  float(input('Digite o valor do produto: '))


# Calcule um desconto de 10%.


desconto = produto * 0.10


# Mostre o valor final.


valor_prod = produto - desconto
print('Valor do produto R$', valor_prod)


# Verifique se o valor final é maior que 100.


print('Verifique se o valor final é maior que 100 - ', valor_prod > 100)


# Verifique se o produto ficou barato (menor que 50).


print('Verifique se o produto ficou barato (menor que 50) - ', valor_prod < 50)