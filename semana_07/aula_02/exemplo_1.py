idades = [0] * 6

for i in range(6): # 0 1 2 3 4 5
    idades[i] = int(input(f"Idade {i + 1}: "))
    # idades[i] = int(input("Idade {}: ".format(i)))
    # print(idades)

print(idades)

for i in range(6):
    print(idades[i])

for i in range(5, -1, -1):
    print(i, idades[i])
