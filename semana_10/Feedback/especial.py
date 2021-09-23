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


# Programa Principal

print(especial("valeria. 123. !!"))
