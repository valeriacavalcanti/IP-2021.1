def menor(lista):
    valor_menor = lista[0]
    for i in range(1, len(lista)):
        if (lista[i] < valor_menor):
            valor_menor = lista[i]

    return valor_menor


# Programa Principal

numeros = [4, 1, 8, 5, 23, 0, 200]
print(menor(numeros))
