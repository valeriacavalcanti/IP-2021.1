# Exibir menu de opções enquanto usuário não encerrar o programa.
saldo = 1000

print('e - exibir o saldo')
print('s - saque')
print('d - depósito')
print('x - sair')
opcao = input('Informe sua opcao: ')
while (opcao != 'x'):
    if (opcao == 'e'):
        print('Saldo:', saldo)
    elif (opcao == 's'):
        valor = float(input("Valor: "))
        if (valor <= saldo):
            saldo -= valor
            print('Saque realizado com sucesso')
            print('Saldo:', saldo)
        else:
            print('saldo insuficiente')
    elif (opcao == 'd'):
        valor = float(input('Valor do deposito: '))
        saldo += valor
        print('depósito realizado com sucesso!')
        print('Saldo:', saldo)
    else:
        print('opcao invalida')

    print('e - exibir o saldo')
    print('s - saque')
    print('d - depósito')
    print('x - sair')
    opcao = input("Informe sua opcao: ")
