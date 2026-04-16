import random 

# PEDRA PAPEL E TESOURA COM POO
# JOGADOR CLASS

class Jogador:
    def escolher(self):
        escolha = input('Escolha Pedra, papel ou Tesoura') 
        return escolha.lower()
    
class Maquina:
        def escolher_maqui(self):
            escolha = ['pedra', 'papel','tesoura']
            return random.choice(escolha)
        
class Jogo:
    def verifica_vitoria(self, jogador, maquina):
          
          if jogador == maquina:
               return 'EMPATE'
          elif jogador == 'pedra' and maquina == 'tesoura':
               return 'você ganhou'
          elif jogador == 'papel' and maquina  == 'pedra':
               return 'você ganhou'
          elif jogador == 'tesoura' and maquina  == 'papel':
               return 'você ganhou'
          else:
               return 'maquina venceu...'
    
    def jogar(self):
              
        jogador = Jogador() # jogador
        maquina = Maquina() # maquina 

        escolher_jogador = jogador.escolher() # atrib. à variável método da escolha
        escolher_maquina = maquina.escolher_maqui() #''

        print('jogador escolheu', escolher_jogador)
        print('maquina escolheu', escolher_maquina)

        resultado =  self.verifica_vitoria(escolher_jogador, escolher_maquina)
        print('RESULTADO -> ', resultado)
                    


jogo = Jogo()
jogo.jogar()