'''
    COMENTÁRIO

    até 200            : 10%
    entre 200,01 - 300 : 20%
    entre 300,01 - 400 : 30%
    acima 400          : 50%
''' 

valor = float(input('Valor: '))

if (valor <= 200):
    print('10%')
else:
    if (valor <= 300):
        print('20%')
    else:
        if (valor <= 400):
            print('30%')
        else:
            print('50%')
