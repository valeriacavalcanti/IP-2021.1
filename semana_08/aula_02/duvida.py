qtde_p = int(input())
T = int(input())

matriz = ['']*T

p_removidas = 0

for i in range(qtde_p):
    p1, p2 = input().split()
    p1, p2 = int(p1), int(p2)
    if matriz[p1] != '':
        p_removidas +=1
    else:
        matriz.insert(p1,p2)

if p_removidas > 0 :
    print(f'{False}\n{p_removidas}')
else:
    print(f'{True}\n{p_removidas}')
