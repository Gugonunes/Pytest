from codigo.jogo import brincadeira
from pytest import mark

'''def test_meu_primeiro_teste():
       assert True'''

# pytest --junitxml report_1.xml   -> cria o arquivo com os testes
# pytest -v                        -> versão verbosa do resultado
# pytest -k "goiabada"             -> faz testes com palavra chave
# pytest -s                        -> mostra prints dentro do teste
# pytest -m "goiabada"             -> usa a tag, "not goiabada" faz sem os da tag

"""
O teste é formado por tres etapas (GWT - AAA):
1- Given - Dado
2- When - Quando
3- Then - Então

- Arange
- Act
- Assert
"""
@mark.smoke
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

@mark.smoke
def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    assert brincadeira(3) == 'queijo'

@mark.goiabada
def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
    assert brincadeira(5) == 'goiabada'

@mark.goiabada
def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    assert brincadeira(10) == 'goiabada'

@mark.goiabada
def test_quando_brincadeira_receber_20_entao_deve_retornar_goiabada():
    assert brincadeira(20) == 'goiabada'

@mark.skip(reason='Ainda nao implementei')
def test_quando_brincadeira_receber__1_entao_deve_retornar_None():
    assert brincadeira(-1) == 'goiabada'

@mark.xfail()
def test_xfail():
    assert brincadeira(20) != 'goiabada'

@mark.xfail()
def test_xfail2():
    assert brincadeira(20) == 'goiabada'

import sys
@mark.xfail(sys.platform == 'win32')
def test_xfailwindows():
    assert brincadeira(20) == 'goiabada'

@mark.skipif(reason = "sys.platform == 'win32'")
def test_skipif_windows_skip():
    assert brincadeira(20) == 'goiabada'

@mark.parametrize(
    'entrada',
    [5, 10, 20, 25, 35]
)
def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada):
    assert brincadeira(entrada) == 'goiabada'

@mark.parametrize(
    'entrada',
    [3, 6, 9, 12, 18]
)
def test_brincadeira_deve_retornar_quijo_com_multiplos_de_3(entrada):
    assert brincadeira(entrada) == 'queijo'

@mark.parametrizado
@mark.parametrize(
    'entrada,esperado',
    [(1,1), (2,2), (3, 'queijo'), (4, 4), (5, 'goiabada')]
)
def test_brincadeira_deve_retornar_valor_esperado(entrada, esperado):
    assert brincadeira(entrada) == esperado