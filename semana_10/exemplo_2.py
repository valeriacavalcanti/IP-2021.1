'''
    Programa para obter 10 números inteiros. Exibir:
    - Quantidade de números com valor acima da média.
'''

# FUNÇÕES

def somar(pLista):
    total = 0 # escopo local
    for i in range(len(pLista)):
        total += pLista[i]
    return total

def media(pLista):
    return somar(pLista)/len(pLista)

def acima(pLista):
    qtde = 0
    media_lista = media(pLista)
    for i in range(len(pLista)):
        if (pLista[i] > media_lista):
            qtde += 1
    return qtde

# PROGRAMA PRINCIPAL

numeros = []

for i in range(10):
    num = int(input('Número: '))
    numeros.append(num)

# somar os números que estão da lista
soma_lista = somar(numeros)
print(soma_lista)

# calcular a média dos números que estão na lista
print(media(numeros))

# Contar a quantidade de elementos que possuem valor acima
# de um determinado valor (média)
print(acima(numeros))


print(numeros)
