'''
    Ler vários números. Encerra qdo for
    digitado o valor zero.

    Ao final, exibe a quantidade de números
    digitados diferentes de zero.

    Contar valores diferentes de zero.
'''

qtde = 0
num = int(input())
while (num != 0):
    qtde += 1 # qtde = qtde + 1
    num = int(input())

print(num)
print(qtde)
