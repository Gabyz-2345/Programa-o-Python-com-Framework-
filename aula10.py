# # def teste():
# #     print('teste')


# # print('teste2')
# # teste()



# # variáveis global


# a = 'teste 1'
# def x():
#     a = 'teste 2'
#     print(a)
# x()
# print(a)    


# # variáveis locais 


# def y():
#     nome = 'Paulo'
#     idade = 12
#     print(nome, idade)


# y()


# # globais
# nome = 'teste'
# def z():
#     global nome, idade, endereco
    
#     nome = 'Marcos'
#     idade  =  25
#     endereco = 'rua 10'



# # z()


# print(nome)
# # print(idade)
# # print(endereco)


# def x(a=5,b=0,c =5):
#     print(a+b)


# x(10,200)
# x(110,20)
# x() 

# def soma(x,y):
#     return x + y


# def subtrair(x,y):
#     return x - y


# def multiplicar(x,y):
#     return x * y


# def dividir(x,y):
#     try:
#         return x / y
            
#     except ZeroDivisionError as erro:
#         return erro



# def operacoes():


#     op =  input(':>>>')
#     if op == '+':
#        s  =  str(soma(10,50))
#        print(s) 
#        print(type(s))
#     elif op == '-':
#        s  =  str(subtrair(10,50))
#        print(s) 
#        print(type(s))


#     elif op == '*':
#        s  =  str(multiplicar(10,50))
#        print(s) 
#        print(type(s))   
#     elif op == '/':
#        s  =  str(dividir(10,0))
#        print(s) 
#        print(type(s))   
#     else:
#         print('Digite algo válido')           
# operacoes()

# def soma(x,y):
#     return x + y


# def subtrair(x,y):
#     return x - y


# def multiplicar(x,y):
#     return x * y


# def dividir(x,y):
#     try:
#         return x / y
            
#     except ZeroDivisionError as erro:
#         return erro



# def operacoes():


#     op =  input(':>>>')
#     x = int(input('>>>'))
#     y = int(input('>>>'))
#     if op == '+':
#        s  =  str(soma(x,y))
#        print(s) 
#        print(type(s))
#     elif op == '-':
#        s  =  str(subtrair(x,y))
#        print(s) 
#        print(type(s))


#     elif op == '*':
#        s  =  str(multiplicar(x,y))
#        print(s) 
#        print(type(s))   
#     elif op == '/':
#        s  =  str(dividir(x,y))
#        print(s) 
#        print(type(s))   
#     else:
#         print('Digite algo válido')           
# operacoes()

