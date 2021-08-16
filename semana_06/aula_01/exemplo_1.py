# valores não negativos
# quantidade acima de 10 ??

qtde = 0
num = int(input("Valor: "))

while (num >= 0):
    if (num > 10):
        qtde += 1 # qtde = qtde + 1
    num = int(input("Valor: "))

# D

print('saiu', qtde)
