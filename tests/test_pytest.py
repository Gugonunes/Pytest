#def test_meu_primeiro_teste():
#    assert True

from codigo.jogo import brincadeira

"""
O teste é formado por tres etapas (GWT - AAA):
1- Given - Dado
2- When - Quando
3- Then - Então

- Arange
- Act
- Assert
"""

def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    """
        Brincadeira - SUT - System Under Test
    """
    entrada = 1                        #Given
    esperado = 1                       #Given
    resultado = brincadeira(entrada)   #When
    assert resultado == esperado       #Then

    #Versao pequena
    #assert brincadeira(1) == 1

def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    assert brincadeira(2) == 2


def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    assert brincadeira(3) == 'queijo'