class Jogo:
    def __init__(self):
        self._pontuacao = 0  
        self._jogada_atual = 1  
        self._num_lancamento_na_jogada = 1  
        self._pinos_primeiro_lancamento = 0  
        self._bonus_spare_pendente = False  
        self._bonus_strike_restantes = 0  
   
    def lancar(self, pinos): 
        if self._jogada_atual > 10 and not self._bonus_spare_pendente and self._bonus_strike_restantes == 0:
            return

        if pinos > 10:
            return

        if self._bonus_spare_pendente:
            self._pontuacao += pinos
            self._bonus_spare_pendente = False

        if self._bonus_strike_restantes > 0:
            self._pontuacao += pinos
            self._bonus_strike_restantes -= 1
            if self._bonus_strike_restantes == 2: 
                self._pontuacao += pinos

        if self._jogada_atual <= 10:
            self._pontuacao += pinos

            if self._num_lancamento_na_jogada == 1:
                if pinos == 10:  
                    self._bonus_strike_restantes += 2
                    self._jogada_atual += 1
                else:
                    self._pinos_primeiro_lancamento = pinos
                    self._num_lancamento_na_jogada = 2
            else:
                if self._pinos_primeiro_lancamento + pinos == 10:
                    self._bonus_spare_pendente = True
                
                self._jogada_atual += 1
                self._num_lancamento_na_jogada = 1
            
    def pontuacao(self):
        return self._pontuacao
