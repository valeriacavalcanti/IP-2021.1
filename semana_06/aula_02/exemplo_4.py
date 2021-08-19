'''
    Ler 4 números.

    Para cada número lido exibir a soma
    de 1 até esse número lido.
'''

for i in range(4):
    num = int(input())
    soma = 0
    for j in range(1, num + 1):
        soma += j
        print("j: {} soma parcial: {}".format(j, soma))
    print(soma)
