a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)

'''
A seguir, 
se B for maior do que C e 
se D for maior do que A, e 
se soma de C com D for maior que a soma de A e B e 
se C e D, ambos, forem positivos e 
se a variável A for par 

escrever a mensagem "Valores aceitos", 
senão escrever "Valores nao aceitos".
'''

if (b > c) and (d > a) and (c + d > a + b) and (c > 0) and (d > 0) and (a % 2 == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
