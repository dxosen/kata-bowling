class Jogo:
    def __init__(self):
        self._pontuacao = 0  
   
    def lancar(self, pinos): 
         if pinos <= 10:
                    self._pontuacao += pinos
    def pontuacao(self):
        
        return self._pontuacao