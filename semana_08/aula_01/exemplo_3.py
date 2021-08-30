'''
 Declarar matriz 3 x 4
'''

matriz = []
for i in range(3):
    matriz.append([0] * 4)

print(matriz)

print("Vamos inserir o número 10!")
linha = int(input("Linha: "))
coluna = int(input("Coluna: "))

matriz[linha][coluna] = 10

print(matriz)
