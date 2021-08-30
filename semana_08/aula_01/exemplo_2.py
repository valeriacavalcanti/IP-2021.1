'''
 Declarar matriz 3 x 4
'''

matriz = []
for i in range(3):
    matriz.append([0] * 4)

for i in range(3):
    for j in range(4):
        matriz[i][j] = int(input("Elemento {} {}: ".format(i, j)))

print(matriz)
