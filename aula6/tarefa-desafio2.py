# atividade 2

# contexto:
# Uma indústria monitora temperatura (T), umidade (U) e presença de gás inflamável (G, 0 ou 1). //---------------OK
# O nível de risco é dado por:

# Crítico: (T > 40 ou U > 80 Contexto 0) e G == 1 //--------------------EX DE TESTE: T=45 U=60 G=1 //-----------OK

# Alto: (T > 40 ou U > 80) e G == 0 //----------------------EX DE TESTE: T=45 U=60 G=0 //-----------OK

# Médio: (T entre 25 e 40) e (U entre 50 e 80) //-------------------------EX DE TESTE: T=30 U=60 G=0 //---------OK

# Baixo: qualquer outra situação //--------------------------EX DE TESTE: T=20 U=40 G=0 //---------------OK

# Tarefa:
# Receba T (float), U (float), G (0 ou 1). //------------------------OK
# Classifique o risco em "Crítico", "Alto", "Médio" ou "Baixo" sem usar if/elif //--------------OK
# Use apenas dicionários com chaves booleanas e operadores lógico //--------------------OK

# UTILIZE APENAS SINAIS LÓGICOS -  VARIAVEIS  -  LISTAS  -  I/O -  NÃO UTILIZE CONDICIONAIS OU LOOPS //------------------------OK


# sinais lógicos
# variáveis
# input e output


# Lógica de programação:

# receber dados
# verificar condições
# classificar risco


# entrada:



print('--------------------------------------')

T = float(input('Temperatura: '))
U = float(input('Umidade: '))
G = int(input('Gás (0 ou 1): '))


# Condições separadas:

cond_temp = T > 40
cond_umidade = U > 80

cond_perigo = cond_temp or cond_umidade

cond_gas = G == 1
cond_sem_gas = G == 0

# Classificação:

critico = cond_perigo and cond_gas
alto = cond_perigo and cond_sem_gas

cond_temp_media1 = T >= 25
cond_temp_media2 = T <= 40

cond_umidade_media1 = U >= 50
cond_umidade_media2 = U <= 80

cond_temp_media = cond_temp_media1 and cond_temp_media2
cond_umidade_media = cond_umidade_media1 and cond_umidade_media2

medio = cond_temp_media and cond_umidade_media

baixo = (critico == False) and (alto == False) and (medio == False)

# Dicionário:

riscos = {
    critico: 'Crítico',
    alto: 'Alto',
    medio: 'Médio',
    baixo: 'Baixo'
}


# saída: 

resultado = riscos[True]

print('Classificação:', resultado)





