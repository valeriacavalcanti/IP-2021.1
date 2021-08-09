# ler 10 números inteiros
soma = 0

qtde = int(input('Quantidade: '))

for i in range(qtde):
    #print('i =', i)
    n = int(input('Informe {} valor: '.format(i + 1)))
    soma = soma + n
    #print('soma parcial =', soma)

print(soma)
