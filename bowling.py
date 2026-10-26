class Jogo:
    def __init__(self):
        self._pontuacao = 0
        self._jogada_atual = 1 
        self._num_lancamento_na_jogada = 1
        self._bonus_futuros = [0] * 40
        self._indice_lancamento = 0
        self._pinos_primeiro_lancamento = 0
   
    def lancar(self, pinos: int): 
        if pinos > 10:
            return

        if self._jogada_atual > 10:
            multiplicador = self._bonus_futuros[self._indice_lancamento]
            
        else:
            multiplicador = 1 + self._bonus_futuros[self._indice_lancamento]

        self._pontuacao += pinos * multiplicador

        if self._jogada_atual <= 10:
            if self._num_lancamento_na_jogada == 1:
                if pinos == 10:
                    self._bonus_futuros[self._indice_lancamento + 1] += 1
                    self._bonus_futuros[self._indice_lancamento + 2] += 1
                    self._jogada_atual += 1

                else:
                    self._pinos_primeiro_lancamento = pinos
                    self._num_lancamento_na_jogada = 2

            else:
                if self._pinos_primeiro_lancamento + pinos == 10:
                    self._bonus_futuros[self._indice_lancamento + 1] += 1
                
                self._jogada_atual += 1
                self._num_lancamento_na_jogada = 1
        
        self._indice_lancamento += 1
            
    def pontuacao(self):
        return self._pontuacao
