# Realizar saque enquanto houver saldo.

saldo = float(input("Saldo: ")) # 100

valor = float(input("Saque: ")) # 10
while (valor <= saldo):
    saldo -= valor # saldo = saldo - valor
    print("Saldo: {:.2f}".format(saldo))
    valor = float(input("Saque: "))

print("Saldo final: {:.2f}".format(saldo))
