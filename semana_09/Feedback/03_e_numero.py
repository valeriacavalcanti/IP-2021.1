frase = input("Frase: ")
eh_numero = True

for i in range(len(frase)):
    if (frase[i] not in '0123456789'):
        eh_numero = False
        break

if ((eh_numero == True) and (len(frase) > 0)):
    print('Sim')
else:
    print('Não')
