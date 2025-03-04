

# VETOR
faturamento_mensal = [
    {"estado": "SP", "valor": 67836.43},
    {"estado": "RJ", "valor": 36678.66},
    {"estado": "MG", "valor": 29229.88},
    {"estado": "ES", "valor": 27165.48},
    {"estado": "Outros", "valor": 19849.53}
]

# VARIAVEL LEITURA
total_faturamento = sum(estado["valor"] for estado in faturamento_mensal)
# CONDICIONAL 
for estado in faturamento_mensal:
    percentual = (estado["valor"] / total_faturamento) * 100
    # IMPRESSAO
    print(f"{estado['estado']}: {percentual:.2f}%")

# RESULTADO
# SP: 37.53%
# RJ: 20.29%
# MG: 16.17%
# ES: 15.03%
# Outros: 10.98%

