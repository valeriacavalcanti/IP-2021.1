from random import randint
import os

# Gerar um conjunto de 6 números aleatórios e distintos, com valores entre n1 e n2 (inclusive).
def novo(n1, n2):
    numeros = []

    while (len(numeros) < 6):
        num = randint(n1, n2)
        if (contido(num, numeros) == False):
            numeros.append(num)

    return numeros

# Verificar se um número está contigo em uma lista.
def contido(n, lista):
    if (n in lista):
        return True
    else:
        return False

# Verificar quantos números da lista 1(l1) estão contidos na lista 2 (l2)
def verificar(l1, l2):
    qtde = 0
    for i in range(len(l1)):
        if (contido(l1[i], l2) == True):
            qtde += 1
    return qtde

# Inserir um número em uma lista, apenas se este número não estiver
# contigo na lista.
def inserir(n, lista):
    if (contido(n, lista) == False):
        lista.append(n)

# trocar os valores de n1 e n2
def trocar(n1, n2):
    n1, n2 = n2, n1

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
