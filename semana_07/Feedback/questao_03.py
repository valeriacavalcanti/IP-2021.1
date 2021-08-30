qtde = 0
numeros = [0] * 10

for i in range(10):
    numeros[i] = int(input())

for i in range(9):
    if (numeros[i] > numeros[9]):
        qtde += 1

print(qtde)
