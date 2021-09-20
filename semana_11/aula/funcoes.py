# Funções

def print_abaixo(st):
    for i in range(len(st)):
        print(st[i])

def print_espaco(st, qtde):
    for s in st:
        print(s, end=" " * qtde)
        #print("{}".format(s), end=" ")
    print()

# Calcular a quantidade de caracteres especiais contidos em uma string.
def especial(st):
    # numero: s >= '0' and s <= '9'
    # letra maiúscula: s >= 'A' and s <= 'Z'
    # letra minúscula: s >= 'a' and a <= 'z'
    qtde = 0
    for s in st:
        if (not (s >= '0' and s <= '9') and
            not (s >= 'A' and s <= 'Z') and
            not(s >= 'a' and s <= 'z')):
            qtde += 1
    return qtde
