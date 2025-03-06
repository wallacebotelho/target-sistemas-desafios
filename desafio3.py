# BIBLIOTECA
import json

# FUNCAO LEITURA JSON
def ler_dados(caminho):
    try:
        with open(caminho, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao ler o arquivo {caminho}: {e}")
        return None

# FUNCAO MENOR VALOR
def menor_valor(dados):
    valores = [dado["valor"] for dado in dados if dado["valor"] > 0]
    return min(valores) if valores else None

# FUNCAO MAIOR VALOR
def maior_valor(dados):
    valores = [dado["valor"] for dado in dados if dado["valor"] > 0]
    return max(valores) if valores else None

# FUNCAO DIAS ACIMA DA MEDIA
def dias_acima_media(dados):
    valores = [dado["valor"] for dado in dados if dado["valor"] > 0]
    if not valores:
        return None
    media = sum(valores) / len(valores)
    dias_superiores = len([v for v in valores if v > media])
    return dias_superiores, media

# CONDICIONAL
if __name__ == "__main__":
    caminho = 'json_desafio3.json'
    dados = ler_dados(caminho)
    
    if dados:
        resultado_menor = menor_valor(dados)
        resultado_maior = maior_valor(dados)
        resultado_dias, media = dias_acima_media(dados) if dados else (None, None)

        if resultado_menor is not None:
            print(f"Menor valor: {resultado_menor}")
        if resultado_maior is not None:
            print(f"Maior valor: {resultado_maior}")
        if resultado_dias is not None:
            print(f"Média mensal: {media:.2f}")
            print(f"Número de dias acima da média: {resultado_dias}")
    else:
        print("Não foi possível processar os dados")