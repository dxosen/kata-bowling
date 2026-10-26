class Jogo:
    def __init__(self):
        self._pontuacao = 0  
        self._total_lancamentos = 0  
   
    def lancar(self, pinos): 
    
        if self._total_lancamentos < 20:
            if pinos <= 10:
                self._pontuacao += pinos
                self._total_lancamentos += 1
            
    def pontuacao(self):
        return self._pontuacao
