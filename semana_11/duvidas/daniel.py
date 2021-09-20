def par(n):
    if (n % 2 == 0):
        return True
    else:
        return False

def voto_obrigatorio(n):
    if (n >= 18) and (n <= 70):
        return True
    else:
        return False

def multiplo(n1, n2):
    if (n1 % n2 == 0):
        return True
    else:
        return False


# Programa Principal

idade = int(input("Digite a idade: "))

# verificar se a idade digitada é "par"
print(par(idade))

if (par(idade) == True):
    print(idade, 'é par')
else:
    print(idade, 'não é par')

# verificar se o voto obrigatório (idade)
print(voto_obrigatorio(idade))

num1 = int(input("Informe um valor: "))
num2 = int(input("Informe outro valor: "))

print(multiplo(num1, num2))
print(multiplo(100, 10))
print(multiplo(100, 15))
