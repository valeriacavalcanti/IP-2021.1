# ler 10 valores, exibir a média dos números lidos

soma = 0
media = 0

for i in range(1, 11):
    num = int(input('Informe o {} valor: '.format(i)))
    #soma = soma + num
    soma += num 

media = soma / 10

print('Media = {:.2f}'.format(media))
