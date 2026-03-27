# sinais lógicos
# sinais aritméticos
# estruturas de dados
# funções build
# sinais aritmeticos
# sinais lógicos
# média 


# Lógica de programação:


# cadastrar o aluno
# cadastrar as notas do aluno > ok
# trazer média > nota
# trazer a média da sala 
# verificar qual a melhor média > media
# verifica qual a pior média > todas as media
# verificar de o aluno passou ou não >  medias


dados_escola = {}


nome_1 = input('Digite o nome: ')
nome_2 = input('Digite o nome: ')
nome_3 = input('Digite o nome: ')
nome_4 = input('Digite o nome: ')


dados_escola['alunos'] = []
dados_escola['alunos'].extend([nome_1, nome_2, nome_3,nome_4])


nota_aluno_1 = [float(input('Nota1 : ')), float(input('Nota2 : ')), float(input('Nota3 : '))]
nota_aluno_2 = [float(input('Nota1 : ')), float(input('Nota2 : ')), float(input('Nota3 : '))]
nota_aluno_3 = [float(input('Nota1 : ')), float(input('Nota2 : ')), float(input('Nota3 : '))]
nota_aluno_4 = [float(input('Nota1 : ')), float(input('Nota2 : ')), float(input('Nota3 : '))]


dados_escola['notas'] = []
dados_escola['notas'].extend([nota_aluno_1,nota_aluno_2,nota_aluno_3, nota_aluno_4])


print(dados_escola)