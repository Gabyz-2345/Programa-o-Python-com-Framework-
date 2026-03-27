
# estruturas de dados
# funções build
# sinais aritméticos
# sinais lógicos
# média


# lógica de programação:

# cadastrar o aluno
# cadastrar as notas do aluno >
# trazer média > nota
# trazer média da sala
# verificar qual a melhor média > média
# verificar qual pior média > todas as médias
# verificar se o aluno passou ou não > médias

dados_escola = {}

nome_1 = input('Diite o nome: ')
nome_2 = input('Diite o nome: ')
nome_3 = input('Diite o nome: ')
nome_4 = input('Diite o nome: ')

dados_escola['alunos'] = []
dados_escola['alunos'].extend([nome_1, nome_2, nome_3, nome_4]) # () ou [] dps do ()

nota_aluno_1 = [float(input('Nota1: ')), float(input('Nota2: ')), float(input('Nota3: '))]
nota_aluno_2 = [float(input('Nota1: ')),float(input('Nota2: ')),float(input('Nota3: '))]
nota_aluno_3 = [float(input('Nota1: ')),float(input('Nota2: ')),float(input('Nota3: '))]
nota_aluno_4 = [float(input('Nota1: ')),float(input('Nota2: ')),float(input('Nota3: '))]

dados_escola['notas'] = []
dados_escola['notas'].extend([nota_aluno_1,nota_aluno_2,nota_aluno_3, nota_aluno_4])


media_aluno_1 =  sum(dados_escola['notas'][0])/len(dados_escola['notas'][0])
media_aluno_2 = sum(dados_escola['notas'][1])/len(dados_escola['notas'][1])
media_aluno_3 =sum(dados_escola['notas'][2])/len(dados_escola['notas'][2])
media_aluno_4 = sum(dados_escola['notas'][3])/len(dados_escola['notas'][3])

print('Média aluno', dados_escola['alunos'].index(nome_1))
print('Média aluno', dados_escola['alunos'].index(nome_2))
print('Média aluno', dados_escola['alunos'].index(nome_3))
print('Média aluno', dados_escola['alunos'].index(nome_4))


dados_escola['media_sala'] = []
dados_escola['media_sala'].extend([media_aluno_1, media_aluno_2, media_aluno_3,  media_aluno_4])
 maior = max(dados_escola['media_sala'])
menor = min(dados_escola['media_sala'])

print('Maior nota', maior)
print('Menor nota', menor)



