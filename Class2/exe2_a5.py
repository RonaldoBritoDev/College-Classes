import math
a = int(input('informe o valor de a:'))
b = int(input('Informe o valor de b:'))

soma = a + b 
diferenca = a - b 
media = (a + b)/2 
distancia = math.fabs(a-b)
maior = (a + b + math.fabs(a-b))/2
menor = (a + b - math.fabs(a-b))/2


print('Soma: ', soma)
print('Diferença ',  diferenca)
print('Media: ', media )
print('Distancia: ', distancia)
print('Maior: ', maior)
print('Menor: ', menor)