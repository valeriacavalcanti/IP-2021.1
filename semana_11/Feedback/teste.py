from funcoes import novo
from funcoes import contido
from funcoes import verificar
from funcoes import trocar
from funcoes import inserir
from funcoes import limpar

# from funcoes import novo, contido, verificar, trocar, inserir, limpar

# import funcoes as f

print(novo(1, 6))

print(contido(2, [1, 2, 3, 4]))
print(contido(6, [1, 2, 3, 4]))

print(verificar([1,2,3,4], [3,4,5,6,9,10]))
print(verificar([1,2,3,4], [1,2,3,4]))
print(verificar([1,2,3,4], [5,6,7,8,9,10]))

num1 = 10
num2 = 20
print(num1, num2)
trocar(num1, num2)
print(num1, num2)

numeros = [1,2,3,4]
inserir(5, numeros)
print(numeros)

inserir(5, numeros)
print(numeros)

input('Aperte <enter> para continuar ...')
limpar()
print('limpou a tela !')
