v1 = int (input('informe o valor 1:'))
v2 = int (input('informe o valor 2:'))
v3 = int (input('informe o valor 3:'))

maior = v1
if v2 > maior : maior = v2
if v3 > maior : maior = v3


menor = v1
if v2 < menor : menor = v2
if v3 < menor : menor = v3

meio = v1+v2+v3 -menor - maior

print('Ordem crescente:',menor, meio, maior)
print('Ordem decrecente:',maior, meio, menor)