'''
 Declarar matriz 3 x 4
'''

matriz = []
for i in range(3):
    matriz.append([0] * 4)

for i in range(3):
    for j in range(4):
        print('[', i, ',', j, '] ', sep = '', end=" ")
    print()

print('')
for j in range(4):
    for i in range(3):
        print('[', i, ',', j, '] ', sep = '', end=" ")
    print()
