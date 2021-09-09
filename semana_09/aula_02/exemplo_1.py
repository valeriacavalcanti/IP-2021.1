num = input("Número: ")
qtde = 0

# print(num, type(num), num.isdigit())

for s in num:
    if (s >= '0') and (s <= '9'):
        qtde += 1

if (qtde == len(num)) and (qtde != 0):
    print("sim")
else:
    print("não")
