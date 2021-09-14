numero_lido = False

while (not numero_lido):
    numero_lido = True
    numero = input("Número: ")
    for i in range(len(numero)):
        if (numero[i] not in '0123456789'):
            numero_lido = False
            break

print(numero)
