# BIBLIOTECA
import json

# FUNCAO LEITURA JSON
def ler_dados(caminho):
    try:
        with open(caminho, 'r') as arquivo:
            dados = json.load(arquivo)
            print(f"Dados carregados: {dados}") 
            print(f"Tipo dos dados: {type(dados)}")
            return dados
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao ler o arquivo {caminho}: {e}")
        return None

# FUNCAO MENOR VALOR
def menor_valor():
    caminho = 'json_desafio3.json'
    dados = ler_dados(caminho)
    if dados and "faturamento_diario" in dados:
        lista = dados["faturamento_diario"]
        return min(dado["valor"] for dado in lista if dado["valor"] > 0)
    print("Erro: Estrutura JSON inválida")
    return None

# FUNCAO MAIOR VALOR
def maior_valor():
    caminho = 'json_desafio3.json'
    dados = ler_dados(caminho)
    if dados and "faturamento_diario" in dados:
        lista = dados["faturamento_diario"]
        return max(dado["valor"] for dado in lista if dado["valor"] > 0)
    print("Erro: Estrutura JSON inválida")
    return None

# CONDICIONAL
if __name__ == "__main__":
    resultado_menor = menor_valor()
    resultado_maior = maior_valor()
    if resultado_menor is not None:
        print(f"Menor valor: {resultado_menor}")
        if resultado_maior is not None:
            print(f"Maior valor: {resultado_maior}")

# O RESULTADO SERÁ
# Menor valor: 373.7838
# Maior valor: 48924.2448        