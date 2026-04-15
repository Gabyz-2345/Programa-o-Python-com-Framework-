def contar():


    nome =  input('Nome do arquivo: ')
    palavra  =  input('palavra: ')


    c  =  0
    linhas  = open(nome, 'r')


    for linha in linhas:
        # print(linha)
        linha = linha.lower()
        c  =  c + linha.count(palavra.lower())
    linhas.close()
    print(c) 


contar()       
        