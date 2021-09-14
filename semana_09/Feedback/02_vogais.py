qtde = 0
frase = input("Frase: ")

for i in range(len(frase)):
    if (frase[i] in 'AEIOUaeiou'):
        qtde += 1

print("Vogais", qtde)
