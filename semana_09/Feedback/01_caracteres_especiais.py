frase = input('Frase: ')

qtde = 0

for s in frase:
    if (not (s >= 'A') and (s <= 'Z')) and \
            (not (s >= 'a') and (s <= 'z')) and \
            (not (s >= '0') and (s <= '9')):
        qtde += 1

print(qtde)
