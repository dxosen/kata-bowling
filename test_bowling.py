import pytest
from bowling import Jogo


@pytest.fixture
def jogo():
    return Jogo()


def test_0_pontos(jogo):
    jogo.lancar(0)
    jogo.lancar(0)
    assert jogo.pontuacao() == 0    


def test_9_pontos(jogo):
    jogo.lancar(9)
    jogo.lancar(0)
    assert jogo.pontuacao() == 9


def test_dois_lancamentos(jogo):
    jogo.lancar(3)
    jogo.lancar(6)
    assert jogo.pontuacao() == 9


def test_duas_jogadas(jogo):
    # Jogada 1
    jogo.lancar(3)
    jogo.lancar(2)
    
    # Jogada 2 
    jogo.lancar(3)
    jogo.lancar(0) 
    
    assert jogo.pontuacao() == 8

def test_strike(jogo):

    # Jogada 1
    jogo.lancar(10)
    
    # Jogada 2
    jogo.lancar(3)
    jogo.lancar(4)
    
    assert jogo.pontuacao() == 24

def test_um_spare(jogo):
    
    # Jogada 1
    jogo.lancar(5)
    jogo.lancar(5)
    
    # Jogada 2
    jogo.lancar(3)
    jogo.lancar(4)
    
    assert jogo.pontuacao() == 20