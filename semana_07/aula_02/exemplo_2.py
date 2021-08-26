'''
Escreva um programa para ler vários números. O programa deverá encerrar quando forem informados
06 (seis) números pares. Ao final, exiba todos os números pares lidos.
'''

lista = []
while (len(lista) < 6):
    num = int(input())
    if (num % 2 == 0):
        lista.append(num)

print(lista)
