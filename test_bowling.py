import pytest
from bowling import Jogo


@pytest.fixture
def jogo():
    return Jogo()

def test_0_pontos(jogo):
    jogo.lancar(0)
    assert jogo.pontuacao() == 0    

def test_9_pontos(jogo):
    jogo.lancar(9)
    assert jogo.pontuacao() == 9

def test_dois_lancamentos(jogo):
    jogo.lancar(3)
    jogo.lancar(6)
    assert jogo.pontuacao() == 9

def test_tres_lancamentos(jogo):
    jogo.lancar(3)
    jogo.lancar(2)
    jogo.lancar(3)
    assert jogo.pontuacao() == 5