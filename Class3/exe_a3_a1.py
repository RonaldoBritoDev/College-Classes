
altura = float (input('Informe a altura: '))
genero = int (input('informe o genero:1 para homem 2 para mulher:'))


if genero ==1 : peso = 72.7 * altura -58
if genero ==2 : peso = 62.1 * altura - 44.7
if genero != 1 and genero != 2 : 
    print('voce precisa selecionar 1 ou 2')
    peso = 0
print("seu peso ideal é", peso)