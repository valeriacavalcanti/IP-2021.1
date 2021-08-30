'''
 Declarar matriz 3 x 4
'''

matriz = []
for i in range(3):
    matriz.append([0] * 4)

print(matriz)

matriz[1][0] = 5
matriz[1][1] = 10
matriz[1][2] = 20
matriz[1][3] = 40
print(matriz)

matriz[1][0] = 60
matriz[1][1] = 60
matriz[1][2] = 60
matriz[1][3] = 60
print(matriz)

for i in range(4):
    matriz[0][i] = 80

for i in range(4):
    matriz[1][i] = 80

for i in range(4):
    matriz[2][i] = 80

for i in range(3):
    for j in range(4):
        print(i, j)
        matriz[i][j] = 100

print(matriz)
