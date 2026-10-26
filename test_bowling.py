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