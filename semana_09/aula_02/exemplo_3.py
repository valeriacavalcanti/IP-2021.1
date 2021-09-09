num = input("Número: ")
qtde = 0

for s in num:
    if (s in '0123456789'):
        qtde += 1

if (qtde == len(num)) and (qtde != 0):
    print("sim")
else:
    print("não")
