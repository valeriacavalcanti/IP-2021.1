# dimensões: 5 x 3
qtde = 0
campo = []
for i in range(5):
    campo.append([0] * 3)

# 10 jogadores
for i in range(10):
    linha, coluna = input('Posição: ').split()
    linha, coluna = int(linha), int(coluna)

    if (campo[linha][coluna] == 0):
        campo[linha][coluna] = 1
        qtde += 1

if (qtde == 10):
    print('Jogo pode começar')
else:
    print('Faltam jogadores no seu esquema')
