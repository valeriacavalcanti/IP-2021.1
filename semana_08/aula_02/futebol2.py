# dimensões: 5 x 3
qtde = 0
campo = []
for i in range(5):
    campo.append([0] * 3)

# 10 jogadores
while (qtde < 10):
    linha, coluna = input('Posição {}: '.format(qtde + 1)).split()
    linha, coluna = int(linha), int(coluna)

    if (campo[linha][coluna] == 0):
        campo[linha][coluna] = 1
        qtde += 1

# exibir o esquema tático
# defesa
defesa = 0
for i in range(5):
    if (campo[i][0] == 1):
        defesa += 1

# meio campo
meio = 0
for i in range(5):
    if (campo[i][1] == 1):
        meio += 1

# ataque
ataque = 0
for i in range(5):
    if (campo[i][2] == 1):
        ataque += 1

print(defesa, meio, ataque)
