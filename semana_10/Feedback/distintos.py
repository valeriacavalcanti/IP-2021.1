def distintos(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        if (lista[i] in lista[i + 1 : tamanho]):
            return False
    return True

# Programa Principal

numeros = [1,2,3,4,5,6]

print(distintos(numeros))
