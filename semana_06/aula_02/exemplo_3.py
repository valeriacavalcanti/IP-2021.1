'''
    Ler vários números. Encerra quando
    for informado o número menor ou igual ao zero.

    Para cada número lido exibir a soma
    de 1 até esse número lido.
'''

num = int(input())

while(num > 0):
    soma = 0
    for i in range(1, num + 1):
        soma += i
        print("i: {} soma parcial: {}".format(i, soma))
    print(soma)
    num = int(input())
