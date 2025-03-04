# FUNÇÃO
def fibonacci(limite):
    # VARIAVEIS
    a, b = 0, 1
    sequencia = [a]

    # CONDICIONAL
    while b <= limite:
        sequencia.append(b)
        a, b = b, a + b

    return sequencia

limite = 100
resultado = fibonacci(limite)
print(resultado)

# O RESULTADO SERÁ [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
