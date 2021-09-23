# Fonte:
# https://brasilescola.uol.com.br/o-que-e/matematica/o-que-e-numero-primo.htm

def primo(n):
    qtde = 0
    for i in range(1, n + 1):
        if (n % i == 0):
            qtde += 1
    if ((n > 1) and (qtde <= 2)):
        return True
    else:
        return False

# Programa Principal

print(primo(12))
print(primo(11))
