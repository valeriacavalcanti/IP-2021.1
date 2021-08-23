'''
    ler 10 números
    exibir a soma dos números lidos
    quantidade de números digitados com valor acima da média
'''
soma = 0
lista = [0] * 10

for i in range(10):
    #valor = int(input())
    lista[i] = int(input())
    #soma += valor # soma = soma + valor
    soma += lista[i]

#print(valor)
print(soma)

media = soma / 10
print(media)
print(lista)

for i in range(10):
    if (media < lista[i]):
        print(i, lista[i])
