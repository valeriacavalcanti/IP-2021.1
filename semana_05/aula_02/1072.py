qtde = int(input())
qtde_in = qtde_out = 0

for i in range(qtde):
    num = int(input())
    if (num >= 10) and (num <= 20):
        qtde_in += 1 # qtde = qtde + 1
    else:
        qtde_out += 1

print(qtde_in, 'in')
print(qtde_out, 'out')
