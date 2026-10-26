import pytest
from bowling import Jogo


@pytest.fixture
def jogo():
    return Jogo()

def test_0_pontos(jogo):
    
    for _ in range(2):
        jogo.lancar(0)
    assert jogo.pontuacao() == 0