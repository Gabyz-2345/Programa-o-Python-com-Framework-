# loop finito
import random
import time
from itertools import chain


# # loop finito
# # z = random.randint(1,10)
# l = [1,2,3]

# for i in l:
#     l.append(i)
#     print(l)

# lista  = [1,2,3,4,5,6]
# for x in lista:
#     print(x)

# for  z in list(range(1,11)):
#     print(z)

# x  =  [x for x in range(1,12) if x % 2 == 0]
# print(x)


#  ---------------------------------------
# enquanto 

# x  =  10 > 2

# while x:
#     print('teste')


# c  = 0
# while c <= 10:
#     print(c)
#     c  =  c  + 1
#     time.sleep(2)

# print('isso esta fora')

# percorriveis  = iterar 

# lista
# tuplas 
# 'texto'
# conjuntos = {1,2,3}
# dic  =  {'a':10, 'b':150}

# # dict compressions  dicionarios 
# dicionario =  {x: x ** 2 for x in range(10)}
# print(dicionario)

# # set compressions conjuntos 
# range(10)
# range(1,10)
# range(1,10,2)

# se =  {x for x in range(11)}

# print(se)


# lista = [x for x in range(1,7)]
# print(lista)

# x = []
# for i in range(1,7):
#     x.append(i)
# print(x)    

# crie um form e digite o nome de 3  pessoas

# ln = []

# for i in range(10):
#     nome = input('nome: ')
#     ln.append(nome)
# print(ln)    



# pergunta =  input('Digite sim ou não')
# while pergunta  == 'sim':
#     print('comprar')
#     pergunta = input('Deseja continuar? >>>')
# else:
#     print('obrigada volte sempre')    


# break 


# lista  =  [1,2,3]
# x = int(input('>>>'))
# while x in lista:
#     print(x)
#     if x  % 2 == 0:
#         break
#     x = int(input('>>>'))

# lista  =  [1,2,3]
# x = int(input('>>>'))
# while x in lista:
#     print(x)
#     if x  % 2 == 0:
#         continue
#     x = int(input('>>>'))


# encadeamento

# l1 = [1,2,3]
# l2 = [1,2,3]
# l3 = [1,2,3]

# for x in chain(l1,l2,l3):
#     print(x)

# l = [x for x in chain(l1,l2,l3)]
# print(l)

# l1 = [1,2,3]
# l2 = [1,2,3]
# l3 = [1,2,3]

# for i, valor in enumerate(l1, start=1):
#     print(f'{i}, {valor}')


