num = input("Número: ")
digitos = True

for s in num:
    if (s < '0') or (s > '9'):
        digitos = False
        break

print(digitos and len(num) > 0)
