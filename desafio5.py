#VARIAVEL
string = "Target Sistemas"

#FUNCAO
def inverter_caracteres(string):
    resultado = ""
    for i in range(len(string) - 1, -1, -1):
        resultado += string[i]
    return resultado

#IMPRESSÃO
print(inverter_caracteres(string))

# O RESULTADO SERÁ sametsiS tegraT