def ordenar_lista(lista):
    x = 0
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[i] > lista[j]:
                x  = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = x
            # else:
            #     lista[j] = x
            #     lista[j+1] =  lista[j]
            #     x = lista[j+1]
        print(lista)        
ordenar_lista([10,15,61,2,1,35])


# ### **6. Jogo de Adivinhação**


# Crie uma função `jogar()` que sorteia um número entre 1 e 100 e dá dicas ("maior", "menor") até o usuário acertar. Use `random.randint()`. A função deve retornar o número de tentativas. No programa principal, chame a função e exiba quantas tentativas foram necessárias.



import random



def jogar():
    n_a = random.randint(1,10)
    
    
    c = 0
    while c <= 100: 
        escolha  =  int(input('1 à  100 >>> '))
        if escolha  == n_a:
            print('acertou!')
            c = c + 1
            print('Tentativas - ', c )
            break
        elif escolha > n_a:
            print('É menor...')
            c = c + 1
            print('Tentativas - ', c )
        elif escolha < n_a:
            print('É maior... ')        
            c = c + 1
            print('Tentativas - ', c )
        else:
            print('Digite algo válido...')    
jogar()





def analisar_lista(lista):
    
    # menor
    menor  =  min(lista)
    # maior
    maior = max(lista)
    # soma 
    soma  =  sum(lista)
    # media 
    media  =  soma / len(lista)
    
    l =  []


    l.extend([menor, maior, soma, media])


    a,b,c,d = l


    print(a,b,c,d)
       


    return [menor, maior, soma , media]


analise  =  analisar_lista([1,2,3,20,3040,150,0,66,99,10])


print(analise)





estoque  =  []


def adicionar_produto(nome, quantidade):
    estoque.append([{nome:quantidade}])
  
    return estoque 


# print(adicionar_produto('x', 2))


def remover_produto(i):
    estoque.pop(i)
    return estoque
   



def listar_estoque():
    return estoque


def main():
  adicionar_produto('x', '0')
  while True:  
    menu =  int(input('''


                1 - add
                2 - remover
                3 - listar            



                '''))


    if menu == 1:
       prod = input('Nome produto: ')
       q  =  int(input('Quantidade: '))
       print(adicionar_produto(prod, q))


    elif menu == 2:
        print(listar_estoque())
        prod = int(input('Nome produto: '))
        remover_produto(prod)
        
    elif menu == 3:
        print(listar_estoque())





main()

