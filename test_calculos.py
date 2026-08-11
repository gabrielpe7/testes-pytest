from calculos import calcular_desconto, calcular_frete, validar_percentual_desconto, calcular_pedido_final
import pytest

def test_calcular_desconto_10_por_cento():
    resultado = calcular_desconto(100, 10)
    assert resultado == 999
    
def test_calcular_desconto_0_por_cento():
    resultado = calcular_desconto(100, 0)
    assert resultado == 100
    
def test_calcular_desconto_100_por_cento():
    resultado = calcular_desconto(100, 100)
    assert resultado == 0
    
@pytest.mark.parametrize("valor, percentual, esperado", [
    (100, 10, 90),
    (200, 50, 100),
    (50, 0, 50),
    (80, 100, 0),
])
def test_calcular_desconto_varios_casos(valor, percentual, esperado):
    resultado = calcular_desconto(valor, percentual)
    assert resultado == esperado
    
@pytest.mark.parametrize("peso, esperado", [
    (0.5, 10.00),
    (1, 10.00),
    (2, 13.00),
    (5, 22.00),
])
def test_calcular_frete_varios_casos(peso, esperado):
    resultado = calcular_frete(peso)
    assert resultado == esperado
    
def test_validar_percentual_valido():
    resultado = validar_percentual_desconto(50)
    assert resultado == True
    
def test_validar_percentual_invalido_recusa():
    with pytest.raises(ValueError):
        validar_percentual_desconto(150)
        
def test_calcular_pedido_final():
    resultado = calcular_pedido_final(valor=100, percentual_desconto=10, peso_kg=2)
    assert resultado == 103.00


def test_calcular_pedido_final_com_desconto_invalido():
    with pytest.raises(ValueError):
        calcular_pedido_final(valor=100, percentual_desconto=200, peso_kg=2)