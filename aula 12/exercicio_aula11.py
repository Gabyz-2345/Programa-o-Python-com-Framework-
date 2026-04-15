# aula 11 

# Exemplos práticos
# 1. Escrever em um arquivo (modo 'w')/// ok
# # Abre o arquivo para escrita (cria/substitui)/// ok
# arquivo = open("dados.txt", "w")/// ok
# arquivo.write("Linha 1\\n")/// ok
# arquivo.write("Linha 2\\n")/// ok
# arquivo.close()/// ok

# 2. Adicionar ao final (modo 'a')/// ok
# arquivo = open("dados.txt", "a")/// ok
# arquivo.write("Linha 3\\n")/// ok
# arquivo.close()/// ok

# 3. Ler todo o conteúdo ´a´/// ok
# arquivo = open("dados.txt", "r")/// ok
# conteudo = arquivo.read()///ok
# print(conteudo)///ok
# arquivo.close()/// ok

# 4. Ler linha por linha com readline
# arquivo = open("dados.txt", "r") linha = arquivo.readline() while linha: print(linha.strip()) # strip remove a quebra de linha linha = arquivo.readline() arquivo.close()

# 5. Ler todas as linhas com readlines()
# arquivo = open("dados.txt", "r")
# linhas = arquivo.readlines()
# for l in linhas:
#     print(l.strip())
# arquivo.close()

# 6. Usando with
# # O arquivo é fechado automaticamente ao sair do bloco
# with open("dados.txt", "r") as arquivo:
#     for linha in arquivo:
#         print(linha.strip())

#        print(linha.strip())

# Atividades com a professora

# Exercicicios de fixação
# Criar e escrever

#  Crie um programa que peça ao usuário um nome e uma idade, e grave essas informações em um arquivo chamado cadastro.txt, uma pessoa por linha no formato "nome,idade". O programa deve permitir adicionar várias pessoas até que o usuário digite "sair".


# Ler e exibir

#  Escreva um programa que leia o arquivo cadastro.txt criado no exercício anterior e exiba na tela cada pessoa no formato "Nome: [nome], Idade: [idade]".


# Contar linhas

#  Crie uma função contar_linhas(nome_arquivo) que retorna o número de linhas do arquivo. Teste com o arquivo cadastro.txt.


# Procurar palavra

#  Peça ao usuário uma palavra e um nome de arquivo. Conte quantas vezes essa palavra aparece no arquivo (ignorando maiúsculas/minúsculas). Exiba o resultado.


# Copiar arquivo

#  Peça ao usuário o nome de um arquivo de origem e um arquivo de destino. Copie o conteúdo do arquivo de origem para o destino, mantendo as linhas.




#-----------------------------------------------
print('----------------------------------')

print('ATIVIDADE 1 - Criar e escrever ')

print('CADASTRO')

arquivo = open('cadastro.txt', 'a')

nome = input('Digite o nome (ou sair): ')

while nome != 'sair':

    idade = input('Digite a idade: ')

    linha = nome + ',' + idade + '\n'
    arquivo.write(linha)

    nome = input('Digite o nome (ou sair): ')

arquivo.close()



print('------------------------------------')

#--------------------------------------------

print('ATIVIDADE 2 - Ler e exibir ')


arquivo = open('cadastro.txt', 'r')

linha = arquivo.readline()

while linha:

    dados = linha.strip().split(',')

    nome = dados[0]
    idade = dados[1]

    print('Nome:', nome, '| Idade:', idade)

    linha = arquivo.readline()

arquivo.close()




print('------------------------------------')

#--------------------------------------------

print('ATIVIDADE 3 -  Contar linhas')


def contar_linhas(nome_arquivo):

    arquivo = open(nome_arquivo, 'r')

    linhas = arquivo.readlines()

    arquivo.close()

    return len(linhas)


print(contar_linhas('cadastro.txt'))





print('------------------------------------')

#--------------------------------------------

print('ATIVIDADE 4 - ler linha por linha com readline')

arquivo_nome = input('Arquivo: ')
palavra = input('Palavra: ')

arquivo = open(arquivo_nome, 'r')

conteudo = arquivo.read().lower()
palavra = palavra.lower()

quantidade = conteudo.count(palavra)

print('Quantidade:', quantidade)

arquivo.close()

print('ATIVIDADE 5 -  Copiar arquivo ')


origem = input('Arquivo origem: ')
destino = input('Arquivo destino: ')

arq1 = open(origem, 'r')
arq2 = open(destino, 'w')

linha = arq1.readline()

while linha:

    arq2.write(linha)

    linha = arq1.readline()

arq1.close()
arq2.close()

print('Arquivo copiado')

print('--------------------------------')

#--------------------------------------





