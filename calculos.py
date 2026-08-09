def calcular_desconto(valor, percentual):
    desconto = valor * (percentual / 100)
    return valor - desconto

def validar_percentual_desconto(percentual):
    if percentual < 0 or percentual > 100:
        raise ValueError("Percentual de desconto deve estar entre 0 e 100")
    return True

def calcular_frete(peso_kg):
    if peso_kg <= 1:
        return 10.00
    return 10.00 + (peso_kg - 1) * 3.00

def calcular_pedido_final(valor, percentual_desconto, peso_kg):
    validar_percentual_desconto(percentual_desconto)
    
    valor_com_desconto = calcular_desconto(valor, percentual_desconto)
    frete = calcular_frete(peso_kg)
    
    return valor_com_desconto + frete

def calcular_juros(valor, taxa_mensal, meses):
    return valor * (1 + taxa_mensal) ** meses