numeros = []

while (len(numeros) < 6):
    num = int(input())
    if (num % 2 == 0):
        numeros.append(num)

print(numeros)
