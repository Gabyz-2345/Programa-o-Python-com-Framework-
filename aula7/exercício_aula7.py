1
# Trate o TypeError -  Qual expressão deve ser gerada para ele aparecer? //// OK 

2
# Trate o ValueError -  Crie em python o erro //// OK



3
# Exercício: Dada uma lista, solicite ao usuário um índice e imprima o  //// OK
# elemento correspondente,
# lidando com exceções caso o índice fornecido esteja fora dos limites da lista.

4
# Peça ao usuário para inserir um número inteiro, tente convertê-lo 
# para um número real,
# lidando com exceções caso a entrada não seja um número ou não 
# seja possível converter para real.

5
# Exercício: Peça ao usuário para inserir dois números afaça a divisão do primeiro  
# pelo segundo, lidando com exceções caso o segundo número 
# seja zero.



# try:
#    tente fazer isso 
# except:
#    isso não funcionar mostre 
# else:
#    erro não identificado ou sem erros
# finally:
#    sempre carrega   

# qualidade do código 
# trazer organização
# otimizar o tratamento de erros

# var =  10
# x =  100

# indentação  = organização do código





# exemplo:

try:
 
    
    print(10 + 10)
    l = [1,2,3,5]
    y  = l[5]
    print(y)
    
except NameError as erro:
    print(erro)
except ValueError as erro:
    print(erro)

except IndexError as erro:   
    print(erro)     
    
else:
    print('ocorreu um não identificado ou não houve erro')
   
finally:
    print('fim  decarregamento...')
   



# lista =  [1,2,3]

# print(lista[0]/0)



# tratamento de erros 
# try / except / else / finally


print('-------------------------------------------------')

print('ATIVIDADE 1 - TypeError')

try:
    valor1 = 10
    valor2 = '10'

    resultado = valor1 + valor2

    print(resultado)

except TypeError as erro:
    print('Erro identificado:')
    print(erro)

else:
    print('Operação realizada sem erro')

finally: 
   print ('fim do processo\n')


   #----------------------------------------

   print('------------------------------------------------')

print('ATIVIDADE 2 - ValueError')


try:
    texto = "abc"
    numero = int(texto)
    print(numero)

except ValueError as erro:
    print('Erro identificado:')
    print(erro) 

else:
    print('conversão realizada sem erro')

finally:
    print('fim do processo\n')


    #-------------------------------------------- 

print('-------------------------------------------')

print('ATIVIDADE 3 - Lista e Índice')

lista = [10, 20 , 30]

try:
    entrada = input('Digite o índice:')
    indice = int(entrada)

    elemento = lista[indice]

 
    print('Elemento encontrado.')
    print(elemento) 


except ValueError as erro:
     print('Erro de valor:')
     print(erro)


except IndexError as erro:
    print('Erro de índice:')
    print(erro)


else:
    print('Acesso realizado com sucesso')


finally:
    print('fim do processo\n')    


#-----------------------------------------------------


print('----------------------------------------')

print('ATIVIDADE 4 - Converter número')

try: 
    entrada = input('Digite um núemrro:')

    numero_convertido = float(entrada)

    print('Número convertido:')
    print(numero_convertido)

except ValueError as erro: 
    print ('Erro de conversão:')
    print(erro)

finally:
    print('fim do processo\n')


#------------------------------------------------

print('------------------------------------------')

print('ATIVIDADE 5 - Divisão')


try:
    entrada1 = input('Digite o primeiro número:')
    entrada2 = input('Digite o segundo número:')

    numero1 = float(entrada1)
    numero2 = float(entrada2)

    resultado_divisao = numero1 / numero2

    print('Resultado da divisão:')
    print(resultado_divisao)


except ValueError as erro:
    print('Erro de valor:')
    print(erro)

except ZeroDivisionError as erro:
    print('Erro de divisão por zero:')
    print(erro)


else:
    print('Divisão realizada com sucesso')

finally:
    print('fim do processo\n')