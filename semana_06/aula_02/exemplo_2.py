'''
    Ler vários números. Encerrar quando a soma dos
    números informados for maior ou igual a 20.
'''


soma = 0

num = int(input())
while (soma < 20):
    soma += num # soma = soma + num
    num = int(input())

print(num)
print(soma)
